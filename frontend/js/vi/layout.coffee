$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

class Layout extends marionette.LayoutView
  template: require './templates/layout'

module.exports = Layout
