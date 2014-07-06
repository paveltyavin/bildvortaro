define([
  'jquery', 'backbone',
  'backbone.dualstorage'
], function ($, Backbone) {

  var Word = Backbone.Model.extend({
    urlRoot: '/api/word/',
    defaults:{
      word_class:'S'
    }
  });
  var WordCollection = Backbone.Collection.extend({
    remote: true,
    model: Word,
    url: '/api/word',
    comparator: 'order',
    // search возвращает массив моделей
    search: function (letters) {
      if (letters == "") return this.toArray();
      var pattern = new RegExp(letters, "gi");
      return this.filter(function (data) {
        return pattern.test(data.get("name"));
      });
    }
  });

  var Category = Word.extend({
    url: function () {
      var base = getValue(this, 'urlRoot') || getValue(this.collection, 'url') || urlError();
      if (this.isNew()) return base;
      return base + (base.charAt(base.length - 1) == '/' ? '' : '/') + encodeURIComponent(this.id) + '?show_top=1';
    }

  });

  var CategoryCollection = WordCollection.extend({
    model: Category
  });

  return {
    Word: Word,
    WordCollection: WordCollection,
    Category: Category,
    CategoryCollection: CategoryCollection
  };
});