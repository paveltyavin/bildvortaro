$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
word = require './word'

class Layout extends marionette.LayoutView
  el: 'body'
  regions:
    word_list_region: '.word_list_region'
#  events:
#    'submit .search-form': 'onSearchFormSubmit'

#  onSearchFormSubmit: (event)=>
#    event.preventDefault()
#    @word_collection.fetch(data: data)

  initialize: =>
    @word_collection = new word.WordCollection
    @word_list_view = new word.WordListView
      collection: @word_collection
    @word_list_region.show(@word_list_view)

    data = {}
    parameters = _.object _.compact _.map location.search.slice(1).split('&'), (item) ->
      if item
        item.split('=')
    if parameters.search
      data.search = parameters.search
    @word_collection.fetch(data: data)

module.exports = ->
  new Layout()