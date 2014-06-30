define([
  'hbs!templates/category',
  'js/reqres',
  'js/models/word',
  'jquery',
  'backbone',
  'marionette'
], function (categoryTemplate, reqres, wordModels, $, Backbone, Marionette) {


  var CategoryView = Marionette.ItemView.extend({
    template: categoryTemplate,
    model: wordModels.Category,
    tagName: 'a',
    className: 'category-block',
    events: {
      click: 'onClick'
    },
    onRender: function () {
      var _this = this;
      this.me = reqres.request('me');
      if (this.me) {
        _this.checkMe();
      }
    },
    onClick: function () {
      this.trigger('click');
    },
    select: function () {
      this.$el.addClass('active');
    },
    deselect: function () {
      this.$el.removeClass('active');
    },
    isSelected: function () {
      return this.$el.hasClass('active');
    },
    checkMe: function () {
      var _this = this;
      if ((this.model.get('user_created') == this.me.get('id')) || (this.me.get('is_staff'))) {
        _this.$el.on('dblclick', function () {
          _this.trigger('category:edit');
        });
      }
    }
  });

  var CategoriesView = Marionette.CollectionView.extend({
    className: 'categories',
    itemView: CategoryView,
    initialize: function (options) {
      this.listenTo(this, 'itemview:click', this.onClick);
    },
    onClick: function (itemView) {
      if (itemView.isSelected()) {
        itemView.deselect();
        this.trigger('category:empty');
      } else {
        this.children.each(function (v) {
          v.deselect();
        });
        itemView.select();
        this.trigger('category:select', itemView.model);
      }
    }
  });

  return {
    CategoriesView: CategoriesView
  }
});