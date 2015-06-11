$ = require 'jquery'
_ = require 'underscore'
marionette = require 'backbone.marionette'
backbone = require 'backbone'


class Word extends backbone.Model


class WordCollection extends backbone.Collection
  model: Word
  url: '/api/word/'
  parse: (response) ->
    @count = response.count
    return response.results


class WordItemView extends marionette.ItemView
  template: require './templates/word_item'
  className: 'word-block'
  onRender: =>
    @$el.on 'click', (event)=>
      event.preventDefault()
      backbone.history.navigate 'vorto/' + @model.get('slug'), trigger: true


class WordListView extends marionette.CollectionView
  page: 0
  loading: false
  finish: false
  childView: WordItemView
  $d: $(document)
  $w: $(window)

  loadMore: =>
    @loading = true
    new_collection = new WordCollection
    new_collection.fetch
      data:
        page: @page + 1
        search: @search
    .done =>
      @page += 1
      @loading = false
      @collection.add new_collection.models
      if @collection.models.length >= new_collection.count
        @finish = true


  onScroll: =>
    dh = @$d.height()
    wh = @$w.height()
    st = @$w.scrollTop()
    d = dh - wh - st - @fh
    if d < 0 and !@loading and !@finish
      @loadMore()


  onBeforeDestroy: =>
    @$w.off "scroll", @onScroll

  onRender: =>
    @$w.on "scroll", @onScroll
    @fh = $('.footer').height()

  initialize: (options)=>
    @search = options.search || null


module.exports =
  WordItemView: WordItemView
  WordListView: WordListView
  WordCollection: WordCollection
  Word: Word
