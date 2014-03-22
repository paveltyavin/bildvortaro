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
      perPage: 20,
      search: '',
      category: undefined,
      wordClass: undefined
    }
  });

  var AppView = Marionette.Layout.extend({
    regions: {
      mainRegion: '.main-region'
    },
    el: 'body',
    ui: {
      search: 'input.search-input',
      perPage: '.per-page',
      wordClasses: '.word-classes',
      categories: '.categories'
    },
    initialize: function () {
      this.initData();
      this.bindUIElements();
      this.initUI();
    },
    initUI: function () {
      var _this = this;
      this.ui.search.on('keyup', function (ev) {
        var search = this.value;
        _this.filter.set('search', search);
        _this.filter.set('category', undefined);
        _this.filter.set('wordClass', undefined);
      });
      this.ui.perPage.find('.btn').on('click', function (ev) {
        var perPage = $(this).text();
        $(this).siblings().removeClass('active');
        $(this).addClass('active');
        _this.filter.set('perPage', perPage);
      });

      this.filter.on('change:wordClass', function () {
        _this.ui.wordClasses.find('a').removeClass('active')
        _this.ui.wordClasses.find('a[data-word-class="' + _this.filter.get('wordClass') + '"]').addClass('active');
      });
      this.ui.wordClasses.find('a').on('click', function (ev) {
        ev.preventDefault();
        var wordClass = undefined;
        if (!$(this).hasClass('active'))
          wordClass = $(this).data('word-class');
        _this.filter.set('wordClass', wordClass);
      });


      this.filter.on('change:category', function () {
        _this.ui.categories.find('a').removeClass('active')
        _this.ui.categories.find('a[data-category-id="' + _this.filter.get('category') + '"]').addClass('active');
      });
      this.ui.categories.find('a').on('click', function (ev) {
        ev.preventDefault();
        var category = undefined;
        if (!$(this).hasClass('active'))
          category = $(this).data('category-id');
        _this.filter.set('category', category);
      });
    },
    initData: function () {

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

      var whereParams = {};
      if (filter.get('wordClass'))
        whereParams.word_class = filter.get('wordClass');

      if (filter.get('category'))
        whereParams.category = filter.get('category');

      if (Object.keys(whereParams).length !== 0)
        newCollection = newCollection.where(whereParams);

      var slice = newCollection.slice(
        0 + filter.get('page') * filter.get('perPage'),
        (1 + filter.get('page')) * filter.get('perPage')
      );

      this.filterCollection.reset(slice);
    }
  });

  var appView = new AppView();
  window.appView = appView;

});