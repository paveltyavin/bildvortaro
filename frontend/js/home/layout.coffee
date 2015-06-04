$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
word = require './word'
category = require './category'
data = require './../data'
ModelBinder = require 'ModelBinder'

class Layout extends marionette.LayoutView
  template: require './templates/layout'
  regions:
    word_list_region: '.word_list_region'
    category_list_region: '.category_list_region'

  onFilterChange: =>
    filter = data.filter
    url = '/?' + $.param filter.toJSON()
    backbone.history.navigate url
    @word_collection.fetch data: filter.toJSON()

  onRender: =>
    filter = data.filter
    @listenTo filter, 'change', @onFilterChange

    @word_collection = new word.WordCollection
    @word_list_view = new word.WordListView
      collection: @word_collection
    @word_list_region.show(@word_list_view)

    @category_collection = new category.CategoryCollection
    @category_list_view = new category.CategoryListView
      collection: @category_collection
    @category_list_region.show(@category_list_view)
    @category_collection.fetch()

    filter_data = _.object _.compact _.map location.search.slice(1).split('&'), (item) ->
      if item
        item.split('=')
    if _.isEmpty filter_data
      @word_collection.fetch()
    else
      filter.set filter_data

module.exports = Layout