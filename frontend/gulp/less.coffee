gulp = require 'gulp'
less = require 'gulp-less'
util = require "gulp-util"
size = require "gulp-size"
combiner = require('stream-combiner2')

livereload = require 'gulp-livereload'
is_prod = process.env.PRODUCTION

gulp.task 'less', ->
  combined = combiner.obj([
    gulp.src './less/styles.less'
    less()
    size()
    gulp.dest './dist/css'
    livereload()
  ])

  if !is_prod
    combined.on('error', console.error.bind(console));
  return combined