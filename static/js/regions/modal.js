define([
  'jquery', 'backbone', 'marionette', 'bootstrap'
], function ($, Backbone, Marionette) {

  var ModalRegion = Marionette.Region.extend({
    el: ".modal-region",

    constructor: function () {
      Marionette.Region.prototype.constructor.apply(this, arguments);
      this.on("show", this.showModal, this);
    },

    getEl: function (selector) {
      var $el = $(selector);
      $el.on("hidden", this.close);
      return $el;
    },
    open: function (view) {
      this.$el.find('.modal-body').empty().html(view.el);
      if (view.title) {
        this.$el.find('.modal-header').show();
        this.$el.find('.modal-title').empty().html(view.title);
      } else {
        this.$el.find('.modal-header').hide();
      }
    },
    showModal: function (view) {
      view.on("close", this.hideModal, this);
      this.$el.modal('show');
    },

    hideModal: function () {
      this.$el.modal('hide');
    }
  });
  return {
    ModalRegion: ModalRegion
  }
});