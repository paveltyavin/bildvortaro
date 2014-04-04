define([
  'js/models/word', 'hbs!templates/add-word', 'hbs!templates/word-block', 'hbs!templates/plus-block', 'jquery',
  'marionette', 'underscore', 'js/config/csrf', 'jquery.ui.widget', 'jquery.fileupload', 'jquery.fileupload-process',
  'jquery.fileupload-image', 'select2-amd', 'js/config/select2'
], function (wordModels, addWordTemplate, wordTemplate, plusTemplate, $, Marionette, _) {

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
      var editButton = [
        '<div class="word-edit-container">', '<div class="fa fa-edit word-edit">', '</div>', '</div>'
      ].join('');
      this.$('.word-image-container').append(editButton);
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
    onRender: function () {
      var _this = this;
      this.ui.fileupload.fileupload({
        url: '/api/word',
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
        _this.trigger('word:uploaded', data.response().result);
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
    },
    submit: function (ev) {
      ev.preventDefault();
      var _this = this;
      var data = _this.fileuploadData;
      if (data) {
        data.formData = {
          name: _this.ui.name.val(),
          word_class: _this.ui.wordClass.val(),
          category: _this.ui.category.val()
        };
        data.submit().complete(function () {
          _this.close();
        });
      }
    },
    serializeData: function () {
      return {
        id: this.cid
      }
    },
    initialize: function (options) {
      this.categoryCollection = options.categoryCollection;
    }
  });

  return {
    WordPlusView: WordPlusView,
    AddWordView: AddWordView,
    WordView: WordView,
    WordsView: WordsView
  };
});