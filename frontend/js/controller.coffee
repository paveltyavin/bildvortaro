marionette = require 'backbone.marionette'
WordLayout = require './word/layout'
HomeLayout = require './home/layout'
AddLayout = require './add/layout'

data = require './data'

class Controller extends marionette.Controller
  home: =>
    $('.search-input').val('')

    view = new HomeLayout()
    app = data.reqres.request 'app'
    app.main_region.show(view)

  word: (word_slug) =>
    view = new WordLayout
      slug: word_slug
    app = data.reqres.request 'app'
    app.main_region.show(view)

  search: (search) =>
    $('.search-input').val(search)
    view = new HomeLayout
      search: search
    app = data.reqres.request 'app'
    app.main_region.show(view)

  add: =>
    view = new AddLayout()
    app = data.reqres.request 'app'
    app.main_region.show(view)

module.exports = Controller


