gulp = require 'gulp'

gulp.task 'copy', ->
  gulp.src './copy/**'
  .pipe gulp.dest "./public/"