define([
  'hbs!templates/word-block',

  'backbone.dualstorage'
], function (wordTemplate) {
  var Word = Backbone.Model.extend({
    urlRoot: '/api/word/'
  });
  var WordCollection = Backbone.Collection.extend({
    model: Word,
    url: '/api/word'
  });

  var WordView = Marionette.ItemView.extend({
    className:'word-block',
    template: wordTemplate,
    model: Word
  })

  var WordsView = Marionette.CollectionView.extend({
    className:'words',
    itemView: WordView,
    initialize: function () {
      this.listenTo(this.collection, 'reset', this.render);
    },
    onRender: function () {
      console.log(this.collection.length);
    }
  });

  var AppView = Marionette.Layout.extend({
    regions: {
      mainRegion: '.main-region'
    },
    el: 'body',
    initialize: function () {
      var wordCollection = new WordCollection();
      var wordsView = new WordsView({
        collection: wordCollection
      });
      this.mainRegion.show(wordsView);
      wordCollection.fetch({
        success: function () {
          wordCollection.trigger('reset')
        }
      });
    }
  });
  var appView = new AppView();
  window.appView = appView;

});