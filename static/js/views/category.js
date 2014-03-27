define([
  'hbs!templates/category',
  'js/models/category',
  'jquery',
  'backbone',
  'marionette',

  'backbone.dualstorage'
], function (categoryTemplate, categoryModels, $, Backbone, Marionette) {


  var CategoryView = Marionette.ItemView.extend({
    template: categoryTemplate,
    model: categoryModels.Category,
    tagName: 'a',
    className: 'list-group-item',
    events: {
      click: 'onClick'
    },
    onClick: function () {
      this.trigger('click');
    },
    select: function () {
      this.$el.addClass('active');
    },
    deselect: function () {
      this.$el.removeClass('active');
    }
  });

  var CategoriesView = Marionette.CollectionView.extend({
    className: 'categories',
    itemView: CategoryView,
    initialize: function () {
      this.listenTo(this, 'itemview:click', this.onClick)
    },
    onClick: function (itemView) {
      this.children.each(function (v) {
        v.deselect();
      });
      this.trigger('category:select', itemView.model);
      itemView.select();
    }
  });

  return {
    CategoriesView: CategoriesView
  }
});