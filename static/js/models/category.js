define([
  'hbs!templates/category',

  'jquery',
  'backbone',
  'marionette',

  'backbone.dualstorage'
], function (categoryTemplate, $, Backbone, Marionette) {

  var Category = Backbone.Model.extend({
    urlRoot: '/api/caterory/'
  });
  var CategoryCollection = Backbone.Collection.extend({
//    local: function() { return true; },
    model: Category,
    url: '/api/category',
    comparator: 'order'
  });

  return {
    Category: Category,
    CategoryCollection: CategoryCollection
  }
});