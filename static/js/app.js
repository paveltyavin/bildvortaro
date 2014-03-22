define([
  'hbs!templates/word-block',
  'backbone.dualstorage'
], function (wordTemplate) {
  var Word = Backbone.Model.extend({
    urlRoot: '/api/word/'
  });
  var WordCollection = Backbone.Collection.extend({
    model: Word,
    url: '/api/word',
    search: function (letters) {
      if (letters == "") return this;
      var pattern = new RegExp(letters, "gi");
      return _(this.filter(function (data) {
        return pattern.test(data.get("name"));
      }));
    }
  });

  var WordView = Marionette.ItemView.extend({
    className: 'word-block',
    template: wordTemplate,
    model: Word
  });

  var WordsView = Marionette.CollectionView.extend({
    className: 'words',
    itemView: WordView,
    initialize: function () {
      this.listenTo(this.collection, 'reset', this.render);
    }
  });

  var Filter = Backbone.Model.extend({
    defaults: {
      page: 0,
      perPage: 400,
      search: '',
      category: '',
      wordClass: ''
    }
  });

  var AppView = Marionette.Layout.extend({
    regions: {
      mainRegion: '.main-region'
    },
    el: 'body',
    initialize: function () {
      var _this = this;
      this.wordCollection = new WordCollection();
      this.filterCollection = new WordCollection();
      this.wordCollection.on('sync', _this.filterWordCollection, this);
      this.filter = new Filter();
      this.filter.on('change', this.filterWordCollection, this);

      this.mainRegion.show(new WordsView({
        collection: _this.filterCollection
      }));

      this.wordCollection.fetch();

    },
    filterWordCollection: function () {
      var filter = this.filter;
      var newCollection = this.wordCollection.search(filter.get('search'));
      newCollection = newCollection.slice(
        0 + filter.get('page') * filter.get('perPage'),
        (1 + filter.get('page')) * filter.get('perPage')
      );
      this.filterCollection.reset(newCollection);
    }
  });

  var appView = new AppView();
  window.appView = appView;

});