$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
backbone = require 'backbone'
ModelBinder = require 'ModelBinder'
data = require 'data'

class Layout extends marionette.LayoutView
  template: require './templates/layout'
  events:
    'click .save': 'onSave'

  initialize: =>
    @binder = new ModelBinder

  onRender: =>
    user_current = data.reqres.request 'user_current'
    @binder.bind user_current, @$el,
      first_name: '#first_name'
      last_name: '#last_name'

  onSave: =>
    user_current = data.reqres.request 'user_current'
    user_current.save().then =>
      @$('.ok').removeClass('hide')
      setTimeout =>
        @$('.ok').addClass 'hide'
      , 500


module.exports = Layout
