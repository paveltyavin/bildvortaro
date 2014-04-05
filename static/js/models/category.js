define([
  'hbs!templates/category',

  'jquery', 'backbone', 'marionette'

//  'backbone.dualstorage'
], function (categoryTemplate, $, Backbone, Marionette) {

  var Category = Backbone.Model.extend({
    urlRoot: '/api/caterory/'
  });
  var CategoryCollection = Backbone.Collection.extend({
//    local: function() { return true; },
    model: Category,
    url: '/api/category',
    comparator: 'order',
    search: function (letters) {
      if (letters == "") return this;
      var pattern = new RegExp(letters, "gi");
      return _(this.filter(function (data) {
        return pattern.test(data.get("name"));
      }));
    }
  });

  return {
    Category: Category,
    CategoryCollection: CategoryCollection
  }
});