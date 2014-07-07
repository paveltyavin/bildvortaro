define([
  'hbs!templates/category', 'js/reqres', 'js/models/word', 'jquery', 'backbone', 'marionette', 'sortable'
], function (categoryTemplate, reqres, wordModels, $, Backbone, Marionette, Sortable) {


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
    onRender: function () {
      var filter = reqres.request('getFilter');
      var category_id = filter.get('category');
      if (category_id) {
        this.children.each(function (v) {
          if (v.model.id === category_id) {
            v.select();
          }
        });
      }
    },
    onShow: function () {
      this.listenTo(this, 'itemview:click', this.onClick);
//      var filter = reqres.request('getFilter');
//      this.listenTo(filter, 'change', this.initSortable);
//      this.initSortable();
    },
    initSortable: function () {
      var filter = reqres.request('getFilter');
      var category_id = filter.get('category');
      var wordClass = filter.get('wordClass');
      if (category_id && !wordClass) {
        if (!this.Sortable){
          var element = $(".words")[0];

          if (element.children.length>1){
            debugger
            this.Sortable = new Sortable(element);
          }
        }
      } else if (this.Sortable) {
        this.Sortable.destroy();
      }
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