define([
  'js/views/word', 'js/views/category', 'js/views/register', 'js/views/word-class',

  'js/models/word', 'js/models/category', 'js/models/user',

  'js/regions/modal',

  'jquery', 'backbone', 'marionette',

  'bootstrap', 'js/config/eo'
//  'backbone.dualstorage',
], function (wordViews, categoryViews, registerViews, wordClassViews, wordModels, categoryModels, userModels,
  ModalRegion, $, Backbone, Marionette) {
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
      plusRegion: '.plus-region',
      wordClassesRegion: '.word-classes-region'
    },
    page: 0,
    columns: function () {
      var w = $(window).width();
      if (w > 1200)
        return 5;
      if (w > 992)
        return 4;
      if (w > 768)
        return 3;
      if (w > 480)
        return 2;
      return 1;
    },
    perPage: function () {
      return this.columns() * 3;
    },
    endScroll: false,
    el: 'body',
    ui: {
      search: 'input.search-input',
      wordClasses: '.word-classes-region',
      nextButton: '.next-button'
    },
    initialize: function () {
      var _this = this;
      $.ajax('/api/auth').success(function(is_authenticated){
        _this.is_authenticated = is_authenticated;
        _this.initData();
        _this.initViews();
        _this.bindUIElements();
        _this.initUI();
      });
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

      $(window).scroll(function () {
        _this.checkScroll();
      });
    },

    getCategoryCollection: function () {
      this.categoryCollection.reset(this.filterCollection.where({show_top: true}))
    },
    initData: function () {
      this.categoryCollection = new wordModels.WordCollection();
      this.fullCollection = new wordModels.WordCollection();
      this.sliceCollection = new wordModels.WordCollection();
      this.filterCollection = new wordModels.WordCollection();
      this.filter = new Filter();
      this.filter.on('change', this.doFilter, this);
      this.fullCollection.on('sync', this.doFilter, this);
      this.fullCollection.on('sync', this.getCategoryCollection, this);

      this.fullCollection.fetch();
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

//      var wordClassesView = new wordClassViews.WordClassesView();
//      this.wordClassesRegion.show(wordClassesView);
//      this.listenTo(wordClassesView, 'wordClass:select', function (wordClass) {
//        _this.filter.set('wordClass', wordClass.get('value'));
//      });
//      this.listenTo(wordClassesView, 'wordClass:empty', function () {
//        _this.filter.set('wordClass', null);
//      });

      var wordsView = new wordViews.WordsView({
        collection: _this.sliceCollection,
        me: _this.me
      });

      this.mainRegion.show(wordsView);

      this.listenTo(wordsView, 'itemview:word:edit', function (view) {
        var editWordView = new wordViews.EditWordView({
          model: view.model,
          categoryCollection: _this.categoryCollection
        });
        _this.modalRegion.show(editWordView);
      });


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
          _this.listenTo(addWordView, 'word:save', function (view) {
            _this.fullCollection.add(view.model, {at: 0});
            _this.doFilter();
            _this.getCategoryCollection();
          });
          _this.modalRegion.show(addWordView);
        });
      }
    },

    getSlice: function () {
      var slice = this.filterCollection.slice((0 + this.page) * this.perPage(), (1 + this.page ) * this.perPage());
      return slice;
    },
    doFilter: function () {
      var filter = this.filter;
      this.page = 0;
      var newArray = this.fullCollection.search(filter.get('search'));
      var whereParams = {};
      if (filter.get('wordClass'))
        whereParams.word_class = filter.get('wordClass');
      if (filter.get('category'))
        whereParams.category = filter.get('category');
      // Todo: сделать поиск по категории

      if (Object.keys(whereParams).length !== 0) {
        newArray = _(newArray).filter(whereParams);
      } else {
        newArray = _.shuffle(newArray);
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
      top -= 150; // ширина одного ряда
      top -= 50; // ширина футера
      if (top < 0)
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

  return new AppView()

});