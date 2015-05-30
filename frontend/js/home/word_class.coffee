$ = require 'jquery'
marionette = require 'backbone.marionette'
backbone = require 'backbone'

class WordClass extends backbone.Model

class WordClassCollection extends backbone.Collection
  model: WordClass
  url: 'api/word_class/'

class WordClassItemView extends marionette.ItemView
  template: require './templates/word_class_item'
  className: 'word_class-block'

class WordClassListView extends marionette.CollectionView
  childView: WordClassItemView

module.exports =
  WordClassItemView: WordClassItemView
  WordClassListView: WordClassListView
  WordClassCollection: WordClassCollection
  WordClass: WordClass
