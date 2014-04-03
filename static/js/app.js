define([
  'js/views/word', 'js/views/category', 'js/views/register',

  'js/models/word', 'js/models/category', 'js/models/user',

  'js/regions/modal',

  'json!/../api/auth',

  'jquery', 'backbone', 'marionette',

  'backbone.dualstorage', 'bootstrap', 'js/config/eo'
], function (wordViews, categoryViews, registerViews, wordModels, categoryModels, userModels, ModalRegion,
  isAuthenticated, $, Backbone, Marionette) {

  var Filter = Backbone.Model.extend({
    defaults: {
      search: '',
      category: undefined,
      wordClass: undefined
    }
  });

  var AppView = Marionette.Layout.extend({
    regions: {
      mainRegion: '.main-region',
      categoriesRegion: '.categories-region',
      modalRegion: ModalRegion.ModalRegion,
      plusRegion: '.plus-region'
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
      wordClasses: '.word-classes-region',
      nextButton: '.next-button'
    },
    initialize: function () {
      this.initData();
      this.initViews();
      this.bindUIElements();
      this.initUI();
    },
    initUI: function () {
      var _this = this;
      this.ui.search.eo();
      this.ui.search.on('keyup', function () {
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

      $(window).scroll(function () {
        _this.checkScroll();
      });
    },
    initData: function () {

      var _this = this;
      this.is_authenticated = isAuthenticated;
      this.categoryCollection = new categoryModels.CategoryCollection();
      this.fullCollection = new wordModels.WordCollection();
      this.sliceCollection = new wordModels.WordCollection();
      this.filterCollection = new wordModels.WordCollection();
      this.filter = new Filter();
      this.filter.on('change', this.doFilter, this);
      this.fullCollection.on('sync', this.doFilter, this);

      this.fullCollection.fetch();
      this.categoryCollection.fetch();
      if (this.is_authenticated) {
        this.me = new userModels.Me();
        this.me.fetch();
      }
    },

    initViews: function () {
      var _this = this;
      var categoriesView = new categoryViews.CategoriesView({
        collection: _this.categoryCollection
      });
      this.categoriesRegion.show(categoriesView);
      this.listenTo(categoriesView, 'category:select', function (category) {
        _this.filter.set('category', category.get('id'));
      });
      this.listenTo(categoriesView, 'category:empty', function () {
        _this.filter.set('category', null);
      });


      this.mainRegion.show(new wordViews.WordsView({
        collection: _this.sliceCollection
      }));


      if (!_this.is_authenticated) {
        var registerPlusView = new registerViews.RegisterPlusView();
        _this.plusRegion.show(registerPlusView);
        _this.listenTo(registerPlusView, 'click', function () {
          _this.modalRegion.show(new registerViews.RegisterView());
        });
      } else {
        var wordPlusView = new wordViews.WordPlusView();
        _this.plusRegion.show(wordPlusView);
        _this.listenTo(wordPlusView, 'click', function () {
          var addWordView = new wordViews.AddWordView({categoryCollection: _this.categoryCollection});
          _this.listenTo(addWordView, 'word:uploaded', function (word) {
            _this.fullCollection.add(word, {at: 0});
            _this.doFilter()
          });
          _this.modalRegion.show(addWordView);
        });
      }
    },

    getSlice: function () {
      var slice = this.filterCollection.slice(0 + this.page * this.perPage, (1 + this.page ) * this.perPage);
      return slice;
    },
    doFilter: function () {
      var filter = this.filter;
      this.page = 0;
      var newArray = [];
      var newCollection = this.fullCollection.search(filter.get('search'));

      var whereParams = {};
      if (filter.get('wordClass'))
        whereParams.word_class = filter.get('wordClass');

      if (filter.get('category'))
        whereParams.category = filter.get('category');

      if (Object.keys(whereParams).length !== 0) {
        newArray = newCollection.where(whereParams);
      } else {
        newArray = newCollection.toArray();
//        newArray = _.shuffle(newArray);
      }
      this.filterCollection.reset(newArray);
      this.sliceCollection.reset(this.getSlice());
      this.endScroll = false;
    },
    checkScroll: function () {
      if (this.blockScroll) return;
      var _this = this;
      setTimeout(function () {
        _this.blockScroll = false;
      }, 500);
      var top = this.$el.height();
      top -= $(window).scrollTop();
      top -= $(window).height();
      if (top < 100)
        this.doScroll();
      this.blockScroll = true;
    },
    doScroll: function () {
      this.page += 1;
      var slice = this.getSlice();
      if (slice.length > 0) {
        this.sliceCollection.add(slice);
      } else {
        this.blockScroll = true;
      }
    }
  });

  var appView = new AppView();
  return appView;

});