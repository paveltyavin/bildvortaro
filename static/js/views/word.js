define([
  'js/models/word', 'hbs!templates/add-word', 'hbs!templates/word-block', 'hbs!templates/plus-block', 'jquery',
  'marionette', 'underscore', 'backbone.modelbinder', 'js/config/csrf', 'jquery.ui.widget', 'jquery.fileupload',
  'jquery.fileupload-process', 'jquery.fileupload-image', 'select2-amd', 'js/config/select2'
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
    addEditButton: function () {
      var _this = this;
      var editButton = '<div class="word-edit-container"><div class="fa fa-edit word-edit"></div></div>';
      this.$('.word-image-container').append(editButton);
      this.$('.word-edit').on('click', function () {
        _this.trigger('word:edit');
      });
    },
    checkMe: function () {
      var _this = this;
      if ((this.model.get('user_created') == this.me.get('id')) || (this.me.get('is_staff'))) {
        this.addEditButton();
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
      'wordClass': '.word-class'
    },
    events: {
      'click @ui.submit': 'submit'
    },

    modelBindings: {
      category: ".word-category",
      word_class: ".word-class",
      name: ".word-name"
    },
    onRender: function () {
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

      this.ui.category.eo().select2({
        placeholder: '...',
        query: function (query) {
          var data = {results: []};
          _this.categoryCollection.search(query.term).each(function (category) {
            data.results.push({id: category.get('id'), text: category.get('name')});
          });
          query.callback(data);
        }
      });

      this.modelBinder.bind(this.model, this.el, this.modelBindings);
      if (this.model.get('image')) {
        _this.ui.fileupload.trigger('fileuploadadd');
      }
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
      this.categoryCollection = options.categoryCollection;
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