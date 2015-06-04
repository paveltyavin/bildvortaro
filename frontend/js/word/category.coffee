$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
ModelBinder = require 'ModelBinder'

data = require 'data'

class Category extends backbone.Model
  url: =>
    return '/api/wordcategory/' + @id + '/'

class CategoryCollection extends backbone.Collection
  model: Category

  url: =>
    return '/api/word/' + @word_id + '/category/'

  initialize: (options)=>
    @word_id = options.word_id


class CategoryItemView extends marionette.ItemView
  template: require './templates/category_item'
  onRender: =>
    @$el.on 'click', =>
      slug = @model.get('category').slug
      backbone.history.navigate '/vorto/' + slug, trigger: true

class CategoryListView extends marionette.CollectionView
  childView: CategoryItemView

module.exports =
  CategoryListView: CategoryListView
  CategoryCollection: CategoryCollection