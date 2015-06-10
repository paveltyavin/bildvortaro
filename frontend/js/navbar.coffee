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
    'click .vi': 'onViClick'
    'click .register': 'onViClick'
    'submit .search-form': 'onSearchFormSubmit'

  onSearchFormSubmit: (event)=>
    event.preventDefault()
    search = @$('.search-input').val()

    if search
      backbone.history.navigate 's/' + search, trigger: true

  onViClick: (event) =>
    event.preventDefault()
    backbone.history.navigate 'vi', trigger: true

  onHomeClick: (event)=>
    event.preventDefault()
    backbone.history.navigate '', trigger: true

  onAddClick: (event)=>
    event.preventDefault()
    user_current = data.reqres.request 'user_current'

    if user_current.id is null
      backbone.history.navigate 'vi', trigger: true
    else
      backbone.history.navigate 'aldoni', trigger: true

  onRender: =>
    router = data.reqres.request 'router'
    router.on "route", (route, params) ->
      console.log "Different Page: " + route
      @$('.search-input').val()

module.exports = Navbar