marionette = require 'backbone.marionette'
WordLayout = require './word/layout'
HomeLayout = require './home/layout'
AddLayout = require './add/layout'
ViLayout = require './vi/layout'
RegisterView = require './vi/register'

data = require './data'

class Controller extends marionette.Controller
  home: =>
    app = data.reqres.request 'app'
    app.main_region.show(new HomeLayout())

  word: (word_slug) =>
    view = new WordLayout
      slug: word_slug
    app = data.reqres.request 'app'
    app.main_region.show(view)

  search: (search) =>
    view = new HomeLayout
      search: search
    app = data.reqres.request 'app'
    app.main_region.show(view)

  add: =>
    app = data.reqres.request 'app'
    app.main_region.show(new AddLayout())

  vi: =>
    app = data.reqres.request 'app'
    user_current = data.reqres.request 'user_current'
    if user_current.id is null
      app.main_region.show(new RegisterView())
    else
      app.main_region.show(new ViLayout())

module.exports = Controller


