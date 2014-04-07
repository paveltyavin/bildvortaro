define([
  'jquery', 'backbone', 'marionette'
], function ($, Backbone, Marionette) {

  var WordClass = Backbone.Model.extend({

  });

  var WordClassCollection = Backbone.Collection.extend({
    model: WordClass
  });

  var wordClassCollection = new WordClassCollection([
    {
      value: 'S',
      name:'substantivoj'
    },
    {
      value: 'A',
      name:'adjektivoj'
    },
    {
      value: 'V',
      name:'verboj'
    },
    {
      value: 'N',
      name:'numeraloj'
    }
  ]);

  var WordClassView = Marionette.ItemView.extend({
    model: WordClass,
    template: function(obj){
      return obj.name;
    },
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
    },
    isSelected: function () {
      return this.$el.hasClass('active');
    }
  });

  var WordClassesView = Marionette.CollectionView.extend({
    className: 'word-class list-group',
    itemView: WordClassView,
    initialize: function (options) {
      this.collection = wordClassCollection;
      this.listenTo(this, 'itemview:click', this.onClick)
    },
    onClick: function (itemView) {
      if (itemView.isSelected()) {
        itemView.deselect();
        this.trigger('wordClass:empty');
      } else {
        this.children.each(function (v) {
          v.deselect();
        });
        itemView.select();
        this.trigger('wordClass:select', itemView.model);
      }
    }
  });
  return {
    WordClassesView: WordClassesView
  }
});