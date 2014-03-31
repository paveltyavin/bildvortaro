define([
  'hbs!templates/register', 'hbs!templates/plusRegister', 'jquery', 'backbone', 'marionette'
], function (registerTemplate, plusRegisterTemplate, $, Backbone, Marionette) {

  var RegisterView = Marionette.ItemView.extend({
    template: registerTemplate,
    initialize:function(){
      this.title = 'Registrado';
    }
  });

  var RegisterPlusView = Marionette.ItemView.extend({
    template: plusRegisterTemplate,
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