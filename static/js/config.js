require.config({
  baseUrl: '/static',
  paths: {
    'appear': 'bower_components/appear/jquery.appear',
    'backbone': 'bower_components/backbone/backbone',
    'backbone.paginator': 'bower_components/backbone.paginator/dist/backbone.paginator',
    'backbone.dualstorage': 'bower_components/Backbone.dualStorage/backbone.dualstorage.amd',
    'hbs': 'bower_components/hbs/hbs',
    'jquery': 'bower_components/jquery/dist/jquery',
    'json': 'bower_components/requirejs-json/json',
    'marionette': 'bower_components/marionette/lib/backbone.marionette',
    'require': 'bower_components/r.js/require',
    'spin': 'bower_components/spinjs/spin',
    'underscore': 'bower_components/underscore/underscore'
  },
  shim: {
    'backbone': {exports: 'Backbone', deps: ['jquery', 'underscore']},
    'backbone.paginator': ['backbone'],
    'marionette': {exports: 'Marionette', deps: ['jquery', 'underscore', 'backbone']},
    'underscore': {exports: '_'}
  },
  hbs: {
    disableI18n: true,
    helperPathCallback: function (name) {
      return 'templates/helpers/' + name;
    }
  },
  waitSeconds: 15
});