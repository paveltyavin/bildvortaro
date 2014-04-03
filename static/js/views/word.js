define([
  'js/models/word', 'hbs!templates/add-word', 'hbs!templates/word-block', 'hbs!templates/plus-block', 'jquery',
  'marionette', 'underscore', 'js/config/csrf', 'jquery.ui.widget', 'jquery.fileupload', 'jquery.fileupload-process',
  'jquery.fileupload-image', 'select2-amd'
], function (wordModels, addWordTemplate, wordTemplate, plusTemplate, $, Marionette, _) {

  var WordView = Marionette.ItemView.extend({
    className: 'word-block',
    template: wordTemplate,
    model: wordModels.Word
  });

  var WordsView = Marionette.CollectionView.extend({
    className: 'words',
    itemView: WordView,
    initialize: function () {
      this.listenTo(this.collection, 'reset', this.render);
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
      }).on('fileuploaddone',function (e, data) {
        _this.trigger('word:uploaded', data.response().result);
      }).click();

      this.ui.category.select2({
        minimumInputLength: 2,
        placeholder: '...',
        initSelection: function ($el, callback) {
          if ($el.val()) {
            $.ajax('/api/category/' + $el.val()).done(function (data) {
              data.text = data.name;
              callback(data);
            });
          }
        },
        ajax: {
          url: '/api/category',
          results: function (data) {
            debugger
            return {results: _.map(data, function (obj) {
              obj.text = obj.name;
              return obj;
            })};
          }
        }
      });
    },
    submit: function () {
      var _this = this;
      var data = _this.fileuploadData;
      if (data) {
        data.formData = {
          name: _this.ui.name.val(),
          word_class: _this.ui.wordClass.val(),
          category: _this.ui.category.val()
        };
        data.submit();
      }
    }
  });

  return {
    WordPlusView: WordPlusView,
    AddWordView: AddWordView,
    WordView: WordView,
    WordsView: WordsView
  };
});