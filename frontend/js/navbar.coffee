$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

data = require 'data'

class Navbar extends marionette.LayoutView
  el: 'nav'
  events:
    'click .vortaro-logo': 'onHomeClick'
    'click .add_word': 'onAddClick'
    'submit .search-form': 'onSearchFormSubmit'

  onSearchFormSubmit: (event)=>
    event.preventDefault()
    search = @$('.search-input').val()

    if search
      app = data.reqres.request 'app'
      cv = app.main_region.currentView
      if cv.word_list_view
        data.filter.set search: search
      else
        backbone.history.navigate '?search=' + search, trigger: true

  onHomeClick: (event)=>
    event.preventDefault()
    backbone.history.navigate '', trigger: true

  onAddClick: (event)=>
    event.preventDefault()
    backbone.history.navigate 'aldoni', trigger: true

module.exports = Navbar