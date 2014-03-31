require.config({
  baseUrl: '/static',
  paths: {
    'backbone': 'bower_components/backbone/backbone',
    'backbone.paginator': 'bower_components/backbone.paginator/dist/backbone.paginator',
    'backbone.dualstorage': 'bower_components/Backbone.dualStorage/backbone.dualstorage.amd',
    'bootstrap.dropdown': 'bower_components/bootstrap/js/dropdown',
    'bootstrap': 'bower_components/bootstrap/dist/js/bootstrap',
    'css': 'bower_components/require-css/css',
    'hbs': 'bower_components/hbs/hbs',
    'jquery': 'bower_components/jquery/dist/jquery',
    'jquery.fileupload': 'bower_components/jquery-file-upload/js/jquery.fileupload',
    'jquery.ui.widget':'bower_components/jquery-file-upload/js/vendor/jquery.ui.widget',
    'json': 'bower_components/requirejs-json/json',
    'marionette': 'bower_components/marionette/lib/core/amd/backbone.marionette',
    'requireLib': 'bower_components/r.js/require',
    'backbone.wreqr': 'bower_components/backbone.wreqr/lib/amd/backbone.wreqr',
    'backbone.babysitter': 'bower_components/backbone.babysitter/lib/amd/backbone.babysitter',
    'spin': 'bower_components/spinjs/spin',
    'text': 'bower_components/requirejs-text/text',
    'underscore': 'bower_components/underscore/underscore'
  },
  shim: {
    'backbone': {exports: 'Backbone', deps: ['jquery', 'underscore']},
    'backbone.paginator': ['backbone'],
    'bootstrap.dropdown': ['jquery'],
    'bootstrap': ['jquery'],
    'jquery': {
      exports:'$'
    },
    'jquery.fileupload':['css!bower_components/jquery-file-upload/css/jquery.fileupload'],
    'marionette': {exports: 'Marionette', deps: ['jquery', 'underscore', 'backbone']},
    'underscore': {exports: '_'}
  },
  hbs: {
    disableI18n: true,
    helperPathCallback: function (name) {
      return 'templates/helpers/' + name;
    }
  },
  waitSeconds: 15,
  deps:['js/config/csrf']
});