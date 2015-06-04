gulp = require 'gulp'
livereload = require 'gulp-livereload'

task_browserify = require './browserify'

watch = ->
  livereload.listen(quiet:true)

  gulp.watch './public/**/*', ['copy']
  gulp.watch './less/**/*.less', ['less']
  gulp.watch './package.json', ['browserify:vendor']
  task_browserify.b_app_dev()

gulp.task 'watch', watch

module.exports =
  watch: watch