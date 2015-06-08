$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
ModelBinder = require 'ModelBinder'

data = require 'data'

class Relation extends backbone.Model
  url: =>
    return '/api/relation/' + @id + '/'


class RelationCollection extends backbone.Collection
  model: Relation

  url: =>
    return '/api/word/' + @word_id + '/relation/'

  initialize: (options)=>
    @word_id = options.word_id


class RelationItemView extends marionette.ItemView
  template: require './templates/relation_item'
  className: 'word-block'
  onRender: =>
    @$el.on 'click', (event) =>
      event.preventDefault()
      slug = @model.get('slug')
      backbone.history.navigate '/vorto/' + slug, trigger: true


class RelationEditItemView extends  marionette.ItemView
  template: require './templates/relation_edit_item'
  className: 'word-block'
  events:
    'click .remove': 'onClickRemove'
  onRender: =>
    @$el.on 'click', (event) =>
      event.preventDefault()
  onClickRemove: =>
    $.ajax
      url: '/api/word/' + @options.word_id + '/relation/'
      method: 'delete'
      data:
        word_id: @model.id
      success: =>
        null
        @destroy()


class RelationListView extends marionette.CollectionView
  childView: RelationItemView


class RelationEditListView extends marionette.CollectionView
  childView: RelationEditItemView
  childViewOptions: =>
    return {word_id: @collection.word_id}
  onRender: =>
    $('<div>').addClass('relation_new word-block').prependTo(@$el).select2
      placeholder: "aldoni vorto"
      minimumInputLength: -1
      ajax:
        url: '/api/word/'
        data: (term, page)=>
          return search: term
        results: (response, page) =>
          results = response.results
          for result in results
            result.text = result.name
          return  results: results
        cache: true
    .on "select2-selecting", (e) =>
      word_id = e.val
      $.ajax
        url: '/api/word/' + @collection.word_id + '/relation/'
        method: 'post'
        data:
          word_id: word_id
      .done =>
        @collection.fetch()


module.exports =
  RelationListView: RelationListView
  RelationEditListView: RelationEditListView
  RelationCollection: RelationCollection