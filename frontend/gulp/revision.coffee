gulp = require 'gulp'
fs = require 'fs'
moment = require 'moment'

gulp.task 'revision', ->
  try
    fs.mkdirSync('./dist/')
  catch e
    if e.code != 'EEXIST'
      throw e;
  try
    fs.mkdirSync('./dist/templates/')
  catch e
    if e.code != 'EEXIST'
      throw e;
  fs.writeFile('./dist/templates/revision.txt', moment().format('llll'));