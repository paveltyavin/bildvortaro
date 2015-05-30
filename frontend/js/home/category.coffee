$ = require 'jquery'
marionette = require 'backbone.marionette'
backbone = require 'backbone'
data = require './../data'
ModelBinder = require 'ModelBinder'

class Category extends backbone.Model

class CategoryCollection extends backbone.Collection
  model: Category
  url: 'api/category/'

class CategoryItemView extends marionette.ItemView
  template: require './templates/category_item'
  className: 'category-block'

  onRender: =>
    filter = data.reqres.request 'filter'
    filter.on 'change:category', =>
      category = filter.get 'category'
      if @model.get('slug') is category
        @$el.addClass 'active'
      else
        @$el.removeClass 'active'

    if filter.get('category') is @model.get('slug')
      @$el.addClass('active')

    @$el.on 'click', =>
      old_category = filter.get 'category'
      new_category = @model.get('slug')
      if new_category isnt old_category
        filter.set 'category', new_category
      else
        filter.unset 'category'

class CategoryListView extends marionette.CollectionView
  childView: CategoryItemView

module.exports =
  CategoryItemView: CategoryItemView
  CategoryListView: CategoryListView
  CategoryCollection: CategoryCollection
  Category: Category
