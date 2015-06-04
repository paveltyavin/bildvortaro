$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

data = require './data'

class Navbar extends marionette.LayoutView
  el: 'nav'
  events:
    'click .vortaro-logo': 'onHomeClick'
    'click .add_word': 'onAddClick'
    'submit .search-form': 'onSearchFormSubmit'

  onSearchFormSubmit: (event)=>
    event.preventDefault()

    data.filter.set search: @$('search-input').val()

  onHomeClick: (event)=>
    event.preventDefault()
    backbone.history.navigate '', trigger: true

  onAddClick: (event)=>
    event.preventDefault()
    backbone.history.navigate 'aldoni', trigger: true

module.exports = Navbar