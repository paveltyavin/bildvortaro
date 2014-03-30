define([
  'js/views/word', 'js/views/category', 'js/views/register',

  'js/models/word', 'js/models/category', 'js/models/user',

  'js/regions/modal',

  'jquery', 'backbone', 'marionette',

  'backbone.dualstorage', 'bootstrap'
], function (wordViews, categoryViews, registerView, wordModels, categoryModels, userModels, ModalRegion, $, Backbone, Marionette) {

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
      plusRegion:'.plus-region'
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
      this.ui.search.on('keyup', function () {
        $(this).val(function (i, v) {
          v = v.replace(/c[xX]/, 'ĉ');
          v = v.replace(/C[xX]/, 'Ĉ');

          v = v.replace(/j[xX]/, 'ĵ');
          v = v.replace(/J[xX]/, 'Ĵ');

          v = v.replace(/u[xX]/, 'ŭ');
          v = v.replace(/U[xX]/, 'Ŭ');

          v = v.replace(/g[xX]/, 'ĝ');
          v = v.replace(/G[xX]/, 'Ĝ');

          v = v.replace(/s[xX]/, 'ŝ');
          v = v.replace(/S[xX]/, 'Ŝ');

          v = v.replace(/h[xX]/, 'ĥ');
          v = v.replace(/H[xX]/, 'Ĥ');
          return v;
        });
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
      this.is_authenticated = $('meta[name="is_authenticated"]').attr('content') == 'True';
      this.me = new userModels.Me();
      this.categoryCollection = new categoryModels.CategoryCollection();
      this.fullCollection = new wordModels.WordCollection();
      this.sliceCollection = new wordModels.WordCollection();
      this.filterCollection = new wordModels.WordCollection();
      this.filter = new Filter();
      this.filter.on('change', this.doFilter, this);
      this.fullCollection.on('sync', this.doFilter, this);

      this.mainRegion.show(new wordViews.WordsView({
        collection: _this.sliceCollection
      }));

      this.fullCollection.fetch();
      this.categoryCollection.fetch();
      if (this.is_authenticated)
        this.me.fetch();

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

      if (!_this.is_authenticated) {
        var registerPlusView = new registerView.RegisterPlusView();
        _this.plusRegion.show(registerPlusView);
        _this.listenTo(registerPlusView, 'click', function () {
          _this.modalRegion.show(new registerView.RegisterView());
        });
      } else {
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
        newArray = _.shuffle(newCollection.toArray());
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