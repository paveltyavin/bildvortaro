define([
  'jquery',
  'backbone'
], function ($, Backbone) {

  var User = Backbone.Model.extend({
    urlRoot: '/api/user/'
  });
  var Me = User.extend({
    url:'/api/user/me'
  });
  var UserCollection = Backbone.Collection.extend({
    model: User,
    url: '/api/user'
  });

  return {
    Me:Me,
    User: User,
    UserCollection: UserCollection
  };
});