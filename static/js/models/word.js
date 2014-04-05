define([
  'jquery',
  'backbone'

//  'backbone.dualstorage'
], function ($, Backbone) {

  var Word = Backbone.Model.extend({
    urlRoot: '/api/word/'
  });
  var WordCollection = Backbone.Collection.extend({
//    local: function() { return true; },
    model: Word,
    url: '/api/word',
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
    Word: Word,
    WordCollection: WordCollection
  };
});