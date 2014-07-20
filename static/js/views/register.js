define([
  'hbs!templates/register', 'hbs!templates/about', 'hbs!templates/plus-block', 'jquery', 'backbone', 'marionette'
], function (registerTemplate, aboutTemplate, plusTemplate, $, Backbone, Marionette) {

  var RegisterView = Marionette.ItemView.extend({
    template: registerTemplate,
    title: 'Registrado'
  });

  var AboutView = Marionette.ItemView.extend({
    template: aboutTemplate,
    title: 'Pri'
  });

  var RegisterPlusView = Marionette.ItemView.extend({
    template: plusTemplate,
    events:{
      'click a':'click'
    },
    click:function(ev){
      ev.preventDefault();
      this.trigger('click');
    }
  });

  return {
    RegisterView: RegisterView,
    RegisterPlusView:RegisterPlusView,
    AboutView: AboutView,
  }
});