$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'

class Layout extends marionette.LayoutView
  template : require './templates/layout'
  initialize: =>
    null

module.exports = Layout
