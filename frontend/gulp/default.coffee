gulp = require 'gulp'
is_prod = process.env.PRODUCTION

task_browserify = require './browserify'
task_watch = require './watch'

gulp.task 'default', [
  'revision'
  'copy'
  'less'
  'browserify:vendor'
], ->
  if is_prod
    task_browserify.b_app_prod()
  else
    task_watch.watch()