define([
  'hbs!templates/category',
  'js/models/word',
  'jquery',
  'backbone',
  'marionette'
], function (categoryTemplate, wordModels, $, Backbone, Marionette) {


  var CategoryView = Marionette.ItemView.extend({
    template: categoryTemplate,
    model: wordModels.Category,
    tagName: 'a',
    className: 'category-block',
    events: {
      click: 'onClick',
      dblclick: 'onDblclick'
    },
    onClick: function () {
      this.trigger('click');
    },
    onDblclick: function(){
      this.trigger('dblclick');
    },
    select: function () {
      this.$el.addClass('active');
    },
    deselect: function () {
      this.$el.removeClass('active');
    },
    isSelected: function () {
      return this.$el.hasClass('active');
    }
  });

  var CategoriesView = Marionette.CollectionView.extend({
    className: 'categories',
    itemView: CategoryView,
    initialize: function () {
      this.listenTo(this, 'itemview:click', this.onClick);
      this.listenTo(this, 'itemview:dblclick', this.onDblClick);
    },
    onDblClick: function(itemView){
      this.trigger('category:edit', itemView.model);
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