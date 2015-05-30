$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'

class Layout extends marionette.LayoutView
  el: 'body'

module.exports = ->
  new Layout()