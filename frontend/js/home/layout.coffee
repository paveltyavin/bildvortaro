$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
word = require './word'
data = require './../data'
ModelBinder = require 'ModelBinder'

class Layout extends marionette.LayoutView
  className: 'home_layout'
  template: require './templates/layout'
  regions:
    word_list_region: '.word_list_region'

  onRender: =>
    @word_collection = new word.WordCollection
    @word_list_view = new word.WordListView
      collection: @word_collection
      search: @search
    @word_list_region.show(@word_list_view)
    @word_list_view.loadMore()

  initialize: (options)=>
    @search = @options.search || null


module.exports = Layout