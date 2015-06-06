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


class CategoryEditListView extends marionette.CompositeView
  childView: CategoryItemView
  childViewContainer: '.childViewContainer'
  template: require './templates/category_edit_list'
  onRender: =>
    @$('.new_category').select2
      placeholder: "search"
      minimumInputLength: -1
      ajax:
        url: '/api/category/'
        data: (term, page)=>
          return search: term
        results: (results, page) =>
          for result in results
            result.text = result.name
          return  results: results
        cache: true
    .on "select2-selecting", (e) =>
      category_id = e.val
      $.ajax
        url: '/api/word/' + @collection.word_id + '/category/'
        data:
          category_id: category_id
        method: 'post'
      .done =>
        @collection.fetch()


module.exports =
  CategoryListView: CategoryListView
  CategoryEditListView: CategoryEditListView
  CategoryCollection: CategoryCollection