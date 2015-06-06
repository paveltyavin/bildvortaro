$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
ModelBinder = require 'ModelBinder'

data = require 'data'
category = require './category'

require 'jquery-ui'
require 'blueimp-file-upload'

class Word extends backbone.Model
  url: =>
    if @id
      return '/api/word/' + @id + '/'
    else
      return '/api/word/' + @slug + '/'
  initialize: (options)=>
    @slug = options.slug


class WordDetailView extends marionette.ItemView
  template: require './templates/detail'
  onRender: =>
    @$('.edit').on 'click', =>
      data.vent.trigger('word:edit')


class WordImageView extends marionette.ItemView
  template: require './templates/image'


class WordImageEditView extends marionette.ItemView
  template: require './templates/image_edit'

  initialize: =>
    @listenTo @model, 'sync', @render

  onRender: =>
    @$('#image_upload').fileupload
      url: '/api/word/' + @model.id + '/image/'
      dataType: 'json'
      done: (e, data) =>
        @model.fetch()


class WordDetailEditView extends marionette.ItemView
  template: require './templates/detail_edit'
  bindings:
    name: '[name=name]'
    description: '[name=description]'

  initialize: =>
    @binder = new ModelBinder

  onRender: =>
    @$('.word_form').on 'submit', (event)=>
      event.preventDefault()
      data.vent.trigger('word:save')

    @binder.bind @model, @$el, @bindings


class Layout extends marionette.LayoutView
  regions:
    detail_region: '.detail_region'
    image_region: '.image_region'
    category_list_region: '.category_list_region'
    word_list_region: '.word_list_region'
  template: require './templates/layout'

  initialize: (options)=>
    @word = new Word
      slug: options.slug

  onRender: =>
    @word.fetch().done =>
      @detail_region.show(new WordDetailView({model: @word}))
      @image_region.show(new WordImageView({model: @word}))

      @category_collection = new category.CategoryCollection
        word_id: @word.id
      @category_list_region.show(new category.CategoryListView({collection: @category_collection}))
      @category_collection.fetch()

    @listenTo data.vent, 'word:edit', =>
      @detail_region.show(new WordDetailEditView({model: @word}))
      @image_region.show(new WordImageEditView({model: @word}))
      @category_list_region.show(new category.CategoryEditListView({collection: @category_collection}))


    @listenTo data.vent, 'word:save', =>
      changed_name = @word.changed.name or false

      @word.save().then =>
        @detail_region.show(new WordDetailView({model: @word}))
        @image_region.show(new WordImageView({model: @word}))
        @category_list_region.show(new category.CategoryListView({collection: @category_collection}))

        if changed_name
          backbone.history.navigate 'vorto/' + @word.get('slug')


module.exports = Layout