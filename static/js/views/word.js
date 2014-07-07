define([
  'js/models/word', 'js/reqres', 'hbs!templates/add-word', 'hbs!templates/word-block', 'hbs!templates/plus-block',
  'jquery', 'marionette', 'underscore', 'backbone.modelbinder', 'sortable', 'js/config/csrf', 'jquery.ui.widget',
  'jquery.fileupload', 'jquery.fileupload-process', 'jquery.fileupload-image', 'js/config/select2', 'jquery.finger'
], function (wordModels, reqres, addWordTemplate, wordTemplate, plusTemplate, $, Marionette, _, ModelBinder, Sortable) {

  var hasTouch = reqres.request('hasTouch');

  var WordView = Marionette.ItemView.extend({
    className: 'word-block',
    template: wordTemplate,
    model: wordModels.Word,
    onShow: function () {
      this.me = reqres.request('me');
      if (this.me) {
        this.checkMe();
      }
    },
    checkMe: function () {
      var _this = this;
      if (this.model.get('user_created') == this.me.get('id')) {
        _this.$el.addClass('my');
      }
      if ((this.model.get('user_created') == this.me.get('id')) || (this.me.get('is_staff'))) {
        if (hasTouch) {
          _this.$('.word-image-container').on('flick', function (ev) {
            if (ev.orientation === 'horizontal') {
              _this.trigger('word:edit');
            }
          });
        } else {
          _this.$('.word-image-container').on('dblclick', function () {
            _this.trigger('word:edit');
          });
        }
      }
    }
  });

  var WordsView = Marionette.CollectionView.extend({
    className: 'words',
    itemView: WordView,
    comparator: 'order',
    onShow: function () {
      var filter = reqres.request('getFilter');
      var me = reqres.request('me');
      if (me.get('is_staff')){
        this.listenTo(filter, 'change', this.initSortable);
        this.initSortable();
      }
    },
    initSortable: function () {
      var filter = reqres.request('getFilter');
      var category_id = filter.get('category');
      var wordClass = filter.get('wordClass');
      var _this = this;
      if (category_id && !wordClass) {
        if (!_this.sort) {
          var element = _this.$el[0];
          if (element.children.length > 1) {
            _this.sort = new Sortable(element, {
              draggable: ".word-block",
              onUpdate: function () {
                var orders = {};
                _this.$el.children().each(function(index, el){
                  $.data(el, 'order', index);
                });
                _this.children.each(function (v) {
                  var order = v.$el.data('order');
                  v.model.set('order', order);
                  orders[v.model.id] = order;
                });
                $.ajax({
                  type:'post',
                  data:orders,
                  dataType:'json',
                  url:'/api/orders'
                });
              }
            });
          }
        }
      } else if (_this.sort) {
        _this.sort.destroy();
        delete _this.sort;
      }
    }
  });


  var WordPlusView = Marionette.ItemView.extend({
    template: plusTemplate,
    events: {
      'click a': 'click'
    },
    click: function (ev) {
      ev.preventDefault();
      this.trigger('click');
    }
  });

  var categoriesConverter = function (direction, value, attributeName, model, els) {
    var $elem = $(els[0]), result;
    if (direction === 'ModelToView') {
      result = value;
      if ($elem.data("select2") !== undefined) {
        $elem.select2('val', value);
      } else {
        $elem.val(value);
      }
    }
    if (direction === 'ViewToModel') {
      if ($elem.data("select2") !== undefined) {
        result = $elem.select2('val');
      } else {
        result = $elem.val();
      }
    }
    return result;
  };

  var AddWordView = Marionette.ItemView.extend({
    title: 'Nova vorto',
    template: addWordTemplate,
    modelBinder: new ModelBinder(),
    ui: {
      fileupload: '.fileupload',
      image: '.word-image',
      submit: '.word-add-submit',
      name: '.word-name',
      categories: "input.word-categories",
      wordClass: '.word-class',
      'delete': '.word-delete'
    },
    events: {
      'click @ui.submit': 'submit'
    },

    modelBindings: {
      categories: {
        selector: 'input.word-categories',
        converter: categoriesConverter
      },
      word_class: ".word-class",
      name: ".word-name",
      show_top: '.show-top'
    },

    fileuploadInit: function () {
      var _this = this;
      var url = '/api/word';
      var type = 'POST';
      if (this.model.has('id')) {
        url += '/' + _this.model.get('id');
        type = 'PUT';
      }
      this.ui.fileupload.fileupload({
        url: url,
        type: type,
        dataType: 'json',
        autoUpload: false,
        singleFileUploads: true,
        acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i,
        maxFileSize: 5000000, // 5 MB
        disableImageResize: /Android(?!.*Chrome)|Opera/.test(window.navigator.userAgent),
        previewMaxWidth: 150,
        previewMaxHeight: 150
      }).on('fileuploadprocessalways',function (e, data) {
        var file = data.files[0];
        if (file)
          _this.ui.image.html(file.preview);
      }).on('fileuploadadd',function (e, data) {
        _this.fileuploadData = data;
      }).on('fileuploaddone', function (e, data) {
        _this.model.set(data.response().result);
        _this.model.trigger('sync');
        _this.trigger('word:save', _this);
      });

      if (this.model.get('image')) {
        _this.ui.fileupload.trigger('fileuploadadd');
      }

    },

    categoryInit: function () {
      var _this = this;
      this.ui.categories.eo();
      this.ui.categories.select2({
        multiple: true,
        maximumSelectionSize: 5,
        initSelection: function (element, callback) {
          var category_ids = element.select2('val');
          var data = [];
          for (var i = 0; i < category_ids.length; i++) {
            var category_id = parseInt(category_ids[i]);
            var category = _this.options.categoryCollection.findWhere({id: category_id});
            if (category) {
              data.push({id: category.get('id'), text: category.get('name')})
            }
          }
          callback(data);
        },
        query: function (query) {
          var data = {results: []};
          _(_this.options.categoryCollection.search(query.term)).each(function (category) {
            data.results.push({id: category.get('id'), text: category.get('name')});
          });
          query.callback(data);
        }
      });
    },
    deleteInit: function () {
      var _this = this;
      if (this.model.has('id')) {
        _this.ui.delete.removeClass('hide').on('click', function () {
          if (confirm('Forviŝi ?')) {
            _this.model.destroy();
            _this.close();
          }
        })
      }
    },
    onShow: function () {
      this.modelBinder.bind(this.model, this.el, this.modelBindings);
      this.categoryInit();
      this.fileuploadInit();
      this.deleteInit();
    },
    submit: function (ev) {
      ev.preventDefault();
      var _this = this;
      var data = _this.fileuploadData;
      if (data) {
        data.formData = this.model.toJSON();
        data.submit().complete(function () {
          _this.close();
        });
      } else if (this.model.has('id')) {
        _this.model.save(null, {
          success: function () {
            _this.close();
          }
        })
      }
    },
    serializeData: function () {
      return {
        cid: this.cid,
        word: this.model.toJSON()
      }
    },
    initialize: function (options) {
      if (!this.model) {
        this.model = new wordModels.Word();
        if (this.options.category) {
          this.model.set('categories', [this.options.category]);
        }
      }
    }
  });

  var EditWordView = AddWordView.extend({
    title: 'Redaktu Vorto'
  });

  return {
    AddWordView: AddWordView,
    EditWordView: EditWordView,
    WordPlusView: WordPlusView,
    WordView: WordView,
    WordsView: WordsView
  };
});