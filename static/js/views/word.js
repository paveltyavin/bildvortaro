define([
  'js/models/word', 'hbs!templates/add-word', 'hbs!templates/word-block', 'hbs!templates/plus-block', 'jquery',
  'marionette', 'js/config/csrf', 'jquery.ui.widget', 'jquery.fileupload-image' , 'canvas-to-blob', 'jquery.fileupload', 'jquery.fileupload-process',
  'jquery.fileupload-image'
  ], function (wordModels, addWordTemplate, wordTemplate, plusTemplate, $, Marionette) {

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
    template: addWordTemplate,
    ui: {
      'fileupload': '.fileupload',
      'image': '.word-image'
    },
    onRender: function () {
      var _this = this;
      this.ui.fileupload.fileupload({
        url: '/api/word/add',
        dataType: 'json',
        autoUpload: false,
        singleFileUploads: true,
        acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i,
        maxFileSize: 5000000, // 5 MB
        disableImageResize: /Android(?!.*Chrome)|Opera/.test(window.navigator.userAgent),
        previewMaxWidth: 100,
        previewMaxHeight: 100,
        previewCrop: true,
        done: function (e, data) {
          _this.trigger('word:uploaded', data.response().result);
        },
        add: function (e, data) {
          debugger
          data.context = $('<div/>');
          _this.triggerMethod('image:add', data)
        },
        processalways: function (e, data) {
          debugger
        }
      }).on('fileuploadprocessalways', function (e, data) {
        debugger
      });
    },
    onImageAdd: function (data) {
      var file = data.files[0];
      var node = $('<p/>').append($('<span/>').text(file.name));
      this.ui.image.html(node);

    },
    onImageProcesslways: function (data) {
      var file = data.files[0];
      debugger
    },
    initialize: function (options) {
      this.collection = options.collection;
    }
  });

  return {
    WordPlusView: WordPlusView,
    AddWordView: AddWordView,
    WordView: WordView,
    WordsView: WordsView
  };
});