define([
  'js/models/word', 'hbs!templates/plusWords', 'hbs!templates/word-block', 'jquery', 'marionette', 'js/config/csrf'
], function (wordModels, plusWordsTemplate, wordTemplate, $, Marionette) {

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

  var AddWordsView = Marionette.ItemView.extend({
    template: plusWordsTemplate,
    ui: {
      'fileupload': '.fileupload'
    },
    events: {
      'fileuploadsend @ui.fileupload': 'fileuploadSend'
    },
    fileuploadSend: function () {
      this.trigger('words:added');
    },
    onRender: function () {
      this.ui.fileupload.fileupload({
        url: '/api/word/add',
        dataType: 'json'
      });
    },
    initialize: function (options) {
      this.collection = options.collection;
    }
  });

  return {
    AddWordsView: AddWordsView,
    WordView: WordView,
    WordsView: WordsView
  };
});