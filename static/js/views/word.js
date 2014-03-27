define([
  'js/models/word',
  'hbs!templates/word-block',
  'jquery',
  'marionette'
], function (wordModels, wordTemplate, $, Marionette) {

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

  return {
    WordView: WordView,
    WordsView: WordsView
  };
});