$ = require 'jquery'
if window
  window.jQuery = $

require './utils/settings'
Raven = require 'raven-js'

Raven.config('http://9e438d06fcf7402588e4c6b2dc853f8c@sentry.tyavin.name/4').install()

modules =
  home: require './home/init'
  word: require './word/init'

module_name = $('body').data('module_name')
module_func = modules[module_name]

try
  $ module_func
catch e
  Raven.captureException(e)


