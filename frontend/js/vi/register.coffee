$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

class RegisterView extends marionette.LayoutView
  template: require './templates/register'

module.exports = RegisterView
