$ = require 'jquery'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

class Word extends backbone.Model

class WordCollection extends backbone.Collection
  model: Word
  url: 'api/word/'
  parse: (response) ->
    return response.results

class WordItemView extends marionette.ItemView
  template: require './templates/word_item'
  className: 'word-block'

class WordListView extends marionette.CollectionView
  childView: WordItemView

module.exports =
  WordItemView: WordItemView
  WordListView: WordListView
  WordCollection: WordCollection
  Word: Word
