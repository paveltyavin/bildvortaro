define([
  'js/models/word', 'hbs!templates/add-word', 'hbs!templates/word-block', 'hbs!templates/plus-block', 'jquery',
  'marionette', 'underscore', 'backbone.modelbinder', 'js/config/csrf', 'jquery.ui.widget', 'jquery.fileupload',
  'jquery.fileupload-process', 'jquery.fileupload-image', 'js/config/select2'
], function (wordModels, addWordTemplate, wordTemplate, plusTemplate, $, Marionette, _, ModelBinder) {

  var WordView = Marionette.ItemView.extend({
    className: 'word-block',
    template: wordTemplate,
    model: wordModels.Word,
    initialize: function (options) {
      var _this = this;
      this.me = options.me;
      if (this.me) {
        this.listenTo(this.me, 'sync', _this.checkMe);
      }
    },
    onRender: function () {
      if (this.me)
        this.checkMe();
    },
    checkMe: function () {
      var _this = this;
      if ((this.model.get('user_created') == this.me.get('id')) || (this.me.get('is_staff'))) {
        _this.$('.word-image-container').on('dblclick', function () {
          _this.trigger('word:edit');
        });
      }
    }
  });

  var WordsView = Marionette.CollectionView.extend({
    className: 'words',
    itemView: WordView,
    initialize: function (options) {
      this.me = options.me;
    },
    itemViewOptions: function (model, index) {
      return {
        me: this.me
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

  var AddWordView = Marionette.ItemView.extend({
    title: 'Nova vorto',
    template: addWordTemplate,
    modelBinder: new ModelBinder(),
    ui: {
      'fileupload': '.fileupload',
      'image': '.word-image',
      'submit': '.word-add-submit',
      'name': '.word-name',
      'category': '.word-category',
      'wordClass': '.word-class',
      'delete': '.word-delete'
    },
    events: {
      'click @ui.submit': 'submit'
    },

    modelBindings: {
      category: ".word-category",
      word_class: ".word-class",
      name: ".word-name"
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
      this.ui.category.eo().select2({
        multiple:true,
        minimumInputLength:1,
//        maximumSelectionSize:1,
        placeholder: '...',
        initSelection: function (element, callback) {
          var category_id = _this.model.get('category');
          var category = _this.options.categoryCollection.findWhere({id: category_id});
          callback({id: category.get('id'), text: category.get('name')});
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
          if (confirm('Delete ?')) {
            _this.model.destroy();
            _this.close();
          }
        })
      }
    },

    onRender: function () {
      var _this = this;

      this.modelBinder.bind(this.model, this.el, this.modelBindings);
      this.fileuploadInit();
      this.categoryInit();
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