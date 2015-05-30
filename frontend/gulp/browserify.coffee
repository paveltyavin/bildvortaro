gulp = require 'gulp'
util = require "gulp-util"
size = require "gulp-size"
_ = require "underscore"

require 'coffeeify'

browserify = require 'browserify'
livereload = require 'gulp-livereload'
uglify = require 'gulp-uglify'
buffer = require 'vinyl-buffer'
source = require 'vinyl-source-stream'
watchify = require 'watchify'
fromArgs = require 'watchify/bin/args'

is_prod = process.env.PRODUCTION

EXTERNALS = [
  { require: "backbone", expose: 'backbone' }
  { require: "backbone.marionette", expose: 'backbone.marionette' }
  { require: "backbone.wreqr", expose: 'backbone.wreqr' }
  { require: "bootstrap", expose: 'bootstrap' }
  { require: "spin.js", expose: 'spin.js' }
  { require: "handlebars", expose: 'handlebars' }
  { require: "hbsfy", expose: 'hbsfy' }
  { require: "hbsfy/runtime", expose: 'hbsfy/runtime' }
  { require: "select2", expose: 'select2' }
  { require: "underscore", expose: 'underscore' }
  { require: "jquery", expose: 'jquery' }
  { require: "moment", expose: 'moment' }
  { require: "moment/locale/ru", expose: 'moment/locale/ru' }
  {
    require: "./js/utils/raven.js"
    expose: 'raven-js'
  }
  {
    require: "./js/utils/tracekit.js"
    expose: 'tracekit'
  }
]

w_app = browserify
  entries: './js/app.coffee'
  extensions: ['.coffee', '.hbs']
  cache: {}
  packageCache: {}
  fullPaths: true

watchify(w_app)

EXTERNALS.forEach (external) ->
  w_app.external external.expose

b_app_dev = ->
  w_app.bundle()
  .on "error", (error) ->
    util.log "browserify:app error", error.message
    util.beep()
    @emit 'end'
  .pipe source 'app.js'
  .pipe buffer()
  .pipe gulp.dest './public/js/'
  .pipe livereload()

gulp.task 'browserify:app:dev', b_app_dev

w_app.on 'update', ->
  b_app_dev()

w_app.on 'time', (time) ->
  util.log "browserify:app:dev ", time, 'ms'

b_app = browserify
  entries: './js/app.coffee'
  extensions: ['.coffee', '.hbs']
EXTERNALS.forEach (external) ->
  b_app.external external.expose

b_app_prod = ->
  b_app.bundle()
  .pipe source 'app.js'
  .pipe buffer()
  .pipe gulp.dest './public/js/'

gulp.task 'browserify:app:prod', b_app_prod

b_vendor = browserify()
EXTERNALS.forEach (external) ->
  b_vendor.require external.require, expose: external.expose

gulp.task 'browserify:vendor', ->
  b_vendor.bundle()
  .on "error", (error) ->
    if is_prod
      throw error.message
    else
      util.log "browserify:vendor error", error.message
      util.beep()
      @emit 'end'
  .pipe source 'vendor.js'
  .pipe buffer()
  .pipe uglify()
  .pipe size()
  .pipe gulp.dest('./public/js/')

module.exports =
  b_app_dev: b_app_dev
  b_app_prod: b_app_prod
