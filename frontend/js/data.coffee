wreqr = require 'backbone.wreqr'
$ = require 'jquery'
backbone = require 'backbone'
_ = require 'underscore'
moment = require 'moment'

class Filter extends backbone.Model
  defaults:
    page: 1

reqres = new wreqr.RequestResponse()
vent = new wreqr.EventAggregator()

module.exports =
  reqres: reqres
  vent: vent
  filter: new Filter
