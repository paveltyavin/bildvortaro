$ = require 'jquery'
_ = require 'underscore'
backbone = require 'backbone'
marionette = require 'backbone.marionette'
ModelBinder = require 'ModelBinder'

data = require 'data'

class Word extends backbone.Model
  url: =>
    if @id
      return '/api/word/' + @id + '/'
    else
      return '/api/word/' + @slug + '/'
  initialize: (options)=>
    @slug = options.slug


class WordView extends marionette.ItemView
  template: require './templates/item'
  onRender: =>
    @$('.edit').on 'click', =>
      data.vent.trigger('word:edit')

class WordEditView extends marionette.ItemView
  template: require './templates/edit'
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
    word_region: '.word_region'
  template: require './templates/layout'
  initialize: (options)=>
    @word = new Word
      slug: options.slug
  onRender: =>
    @word.fetch().done =>
      view = new WordView
        model: @word
      @word_region.show(view)

    @listenTo data.vent, 'word:edit', =>
      view = new WordEditView
        model: @word
      @word_region.show(view)


    @listenTo data.vent, 'word:save', =>
      changed_name = @word.changed.name or false

      @word.save().then =>
        view = new WordView
          model: @word
        @word_region.show(view)

        if changed_name
          backbone.history.navigate 'vorto/' + @word.get('slug')


module.exports = Layout