$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

class Word extends backbone.Model
  url: '/api/word/'

class Layout extends marionette.LayoutView
  template: require './templates/layout'
  events:
    'submit form': 'onFormSubmit'

  onFormSubmit: (event)=>
    event.preventDefault()
    name = @$('#name').val()
    if name
      word = new Word(name: name)
      word.save().done =>
        url = 'vorto/' + word.get 'slug'
        backbone.history.navigate url, trigger: true

module.exports = Layout
