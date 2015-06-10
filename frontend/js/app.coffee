$ = require 'jquery'
if window
  window.jQuery = $

require './utils/settings'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
Raven = require 'raven-js'
Controller = require './controller'
Navbar = require './navbar'
data = require './data'

Raven.config('http://9e438d06fcf7402588e4c6b2dc853f8c@sentry.tyavin.name/4').install()

class App extends marionette.Application
  el: 'body'
  regions:
    main_region: '.main_region'

class AppRouter extends marionette.AppRouter
  appRoutes:
    "": "home"
    "vorto/:vorto": "word"
    "aldoni": "add"
    "s/:search": "search"
    "vi": "vi"

app = new App()
data.reqres.setHandler 'app', ->
  app

app.on 'start', ->
  navbar = new Navbar
  controller = new Controller
  router = new AppRouter
    controller: controller
  data.reqres.setHandler 'router', ->
    app
  backbone.history.start(pushState: true)


class UserCurrent extends backbone.Model
  url: '/api/user/current/'


loadInitialData = ->
  d = $.Deferred()
  user_current = new UserCurrent
  user_current.fetch().then ->
    data.reqres.setHandler 'user_current', ->
      user_current
    d.resolve()
  return d

try
  loadInitialData().then =>
    app.start()
catch e
  Raven.captureException(e)

