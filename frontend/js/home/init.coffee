$ = require 'jquery'
marionette = require 'backbone.marionette'
word = require './word'

class Layout extends marionette.LayoutView
  el: 'body'
  regions:
    word_list_region: '.word_list_region'
  initialize: =>
    word_collection = new word.WordCollection
    word_list_view = new word.WordListView
      collection: word_collection
    @word_list_region.show(word_list_view)

    word_collection.fetch()

module.exports = ->
  new Layout()