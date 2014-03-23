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
      search: '',
      category: undefined,
      wordClass: undefined
    }
  });


  var AppView = Marionette.Layout.extend({
    regions: {
      mainRegion: '.main-region'
    },
    page: 0,
    perPage: (function () {
      var w = $(window).width();
      if (w > 1200)
        return 5 * 3;
      if (w > 992)
        return 4 * 3;
      if (w > 768)
        return 3 * 3;
      if (w > 480)
        return 2 * 3;
      return 3;
    })(),
    endScroll: false,
    el: 'body',
    ui: {
      search: 'input.search-input',
      wordClasses: '.word-classes',
      categories: '.categories',
      nextButton: '.next-button'
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

      this.filter.on('change:wordClass', function () {
        _this.ui.wordClasses.find('a').removeClass('active');
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
        _this.ui.categories.find('a').removeClass('active');
        _this.ui.categories.find('a[data-category-id="' + _this.filter.get('category') + '"]').addClass('active');
      });
      this.ui.categories.find('a').on('click', function (ev) {
        ev.preventDefault();
        var category = undefined;
        if (!$(this).hasClass('active'))
          category = $(this).data('category-id');
        _this.filter.set('category', category);
      });

      setInterval(function () {
        _this.checkScroll(_this)
      }, 100);
    },
    initData: function () {

      var _this = this;
      this.fullCollection = new WordCollection();
      this.sliceCollection = new WordCollection();
      this.filterCollection = new WordCollection();
      this.filter = new Filter();
      this.filter.on('change', this.doFilter, this);
      this.fullCollection.on('sync', this.doFilter, this)

      this.mainRegion.show(new WordsView({
        collection: _this.sliceCollection
      }));

      this.fullCollection.fetch();

    },
    getSlice: function () {
      var slice = this.filterCollection.slice(
        0 + this.page * this.perPage,
        (1 + this.page ) * this.perPage
      );
      slice = _.shuffle(slice);
      return slice;
    },
    doFilter: function () {
      var filter = this.filter;
      this.page = 0;
      var newCollection = this.fullCollection.search(filter.get('search'));

      var whereParams = {};
      if (filter.get('wordClass'))
        whereParams.word_class = filter.get('wordClass');

      if (filter.get('category'))
        whereParams.category = filter.get('category');

      if (Object.keys(whereParams).length !== 0)
        newCollection = newCollection.where(whereParams);

      if (newCollection.toArray !== undefined)
        newCollection = newCollection.toArray()
      this.filterCollection.reset(newCollection);
      this.sliceCollection.reset(this.getSlice());
      this.endScroll = false;
    },
    checkScroll: function () {
      if (!this.endScroll) {
        var top = this.$el.height();
        top -= $(window).scrollTop();
        top -= $(window).height();
        if (top < 100)
          this.doScroll();
      }
    },
    doScroll: function () {
      this.page += 1;
      var slice = this.getSlice();
      if (slice.length > 0) {
        this.sliceCollection.add(slice);
      } else {
        this.endScroll = true;
      }
    }
  });

  var appView = new AppView();
  window.appView = appView;

});