gulp = require 'gulp'
fs = require 'fs'
moment = require 'moment'

gulp.task 'revision', ->
  try
    fs.mkdirSync('./public/')
  catch e
    if e.code != 'EEXIST'
      throw e;
  try
    fs.mkdirSync('./public/templates/')
  catch e
    if e.code != 'EEXIST'
      throw e;
  fs.writeFile('./public/templates/revision.txt', moment().format('llll'));