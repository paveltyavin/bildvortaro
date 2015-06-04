gulp = require 'gulp'

gulp.task 'copy', ->
  gulp.src './public/**'
  .pipe gulp.dest "./dist/"