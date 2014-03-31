define([
  'hbs!templates/register', 'hbs!templates/plus', 'jquery', 'backbone', 'marionette'
], function (registerTemplate, plusTemplate, $, Backbone, Marionette) {

  var RegisterView = Marionette.ItemView.extend({
    template: registerTemplate,
    initialize:function(){
      this.title = 'Registrado';
    }
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
    RegisterPlusView:RegisterPlusView
  }
});