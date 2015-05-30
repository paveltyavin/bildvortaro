wreqr = require 'backbone.wreqr'
$ = require 'jquery'
backbone = require 'backbone'
_ = require 'underscore'
moment = require 'moment'

reqres = new wreqr.RequestResponse()
vent = new wreqr.EventAggregator()

module.exports =
  reqres: reqres
  vent: vent
