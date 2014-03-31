define([
  'js/models/word',
  'hbs!templates/addWords', 'hbs!templates/word-block', 'hbs!templates/plus',
  'jquery', 'marionette'
], function (wordModels, addWordsTemplate, wordTemplate, plusTemplate, $, Marionette) {

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
    template: wordTemplate
  });

  var AddWordsView = Marionette.CompositeView.extend({
    template: addWordsTemplate,
    itemView: AddWordView
  });

  return {
    AddWordsView: AddWordsView,
    AddWordView: AddWordView,
    WordView: WordView,
    WordsView: WordsView,
    WordPlusView: WordPlusView
  };
});