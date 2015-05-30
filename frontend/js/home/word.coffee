$ = require 'jquery'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

class Word extends backbone.Model

class WordCollection extends backbone.Collection
  model: Word
  url: 'api/word/'

class WordItemView extends marionette.ItemView
  template: require './templates/word_item'

class WordListView extends marionette.CollectionView
  childView: WordItemView

module.exports =
  WordItemView: WordItemView
  WordListView: WordListView
  WordCollection: WordCollection
  Word: Word
