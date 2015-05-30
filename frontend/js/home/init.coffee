$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
word = require './word'
category = require './category'
data = require './../data'
ModelBinder = require 'ModelBinder'

class Filter extends backbone.Model
  defaults:
    page: 1

class Layout extends marionette.LayoutView
  el: 'body'
  regions:
    word_list_region: '.word_list_region'
    category_list_region: '.category_list_region'

  events:
    'submit .search-form': 'onSearchFormSubmit'

  onFilterChange: =>
    if window.history
      url = '/?' + $.param @filter.toJSON()
      window.history.pushState {}, document.title, url
    @word_collection.fetch data: @filter.toJSON()


  onSearchFormSubmit: (event)=>
    event.preventDefault()

  initialize: =>
    @filter = new Filter
    @filter.on 'change', @onFilterChange
    data.reqres.setHandler 'filter', => @filter

    @word_collection = new word.WordCollection
    @word_list_view = new word.WordListView
      collection: @word_collection
    @word_list_region.show(@word_list_view)
    @word_collection.fetch()

    @category_collection = new category.CategoryCollection
    @category_list_view = new category.CategoryListView
      collection: @category_collection
    @category_list_region.show(@category_list_view)
    @category_collection.fetch()

    @binder = new ModelBinder
    @binder.bind @filter, @$el, search: '.search-input'

    filter_data = _.object _.compact _.map location.search.slice(1).split('&'), (item) ->
      if item
        item.split('=')
    @filter.set filter_data

module.exports = ->
  new Layout()