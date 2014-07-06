require.config({
  baseUrl: '/static',
  map: {
    '*': {
      'hbs': 'bower_components/hbs/hbs'
    }
  },
  paths: {
    'backbone': 'bower_components/backbone/backbone',
    'backbone.modelbinder': 'bower_components/backbone.modelbinder/Backbone.ModelBinder',
    'backbone.paginator': 'bower_components/backbone.paginator/dist/backbone.paginator',
    'backbone.dualstorage': 'bower_components/Backbone.dualStorage/backbone.dualstorage.amd',
    'bootstrap': 'bower_components/bootstrap/dist/js/bootstrap',
    'bootstrap.dropdown': 'bower_components/bootstrap/js/dropdown',
    'bootstrap.modal': 'bower_components/bootstrap/js/modal',
    'canvas-to-blob': 'bower_components/blueimp-canvas-to-blob/js/canvas-to-blob',
    'hbs': 'bower_components/hbs/hbs',
    'jquery': 'bower_components/jquery/dist/jquery',
    'jquery.finger': 'bower_components/jquery.finger/dist/jquery.finger',
    'jquery-mousewheel': 'bower_components/jquery-mousewheel/jquery.mousewheel',
    'jquery.fileupload': 'bower_components/jquery-file-upload/js/jquery.fileupload',
    'jquery.fileupload-image': 'bower_components/jquery-file-upload/js/jquery.fileupload-image',
    'jquery.fileupload-process': 'bower_components/jquery-file-upload/js/jquery.fileupload-process',
    'jquery.ui.widget': 'bower_components/jquery-file-upload/js/vendor/jquery.ui.widget',
    'load-image': 'bower_components/blueimp-load-image/js/load-image',
    'load-image-meta': 'bower_components/blueimp-load-image/js/load-image-meta',
    'load-image-exif': 'bower_components/blueimp-load-image/js/load-image-exif',
    'load-image-ios': 'bower_components/blueimp-load-image/js/load-image-ios',
    'marionette': 'bower_components/marionette/lib/core/amd/backbone.marionette',
    'requireLib': 'bower_components/r.js/require',
    'backbone.wreqr': 'bower_components/backbone.wreqr/lib/amd/backbone.wreqr',
    'backbone.babysitter': 'bower_components/backbone.babysitter/lib/amd/backbone.babysitter',
    'select2-amd': 'bower_components/select2-amd/select2',
    'select2': 'bower_components/select2/select2',
    'sortable': 'bower_components/Sortable/Sortable',
    'spin': 'bower_components/spinjs/spin',
    'text': 'bower_components/requirejs-text/text',
    'underscore': 'bower_components/underscore/underscore'
  },
  shim: {
    'select2': ['jquery'],
    'bootstrap.modal': {
      deps: ["jquery"],
      exports: "$.fn.modal"
    }
  },
  hbs: {
    disableI18n: true,
    helperPathCallback: function (name) {
      return 'templates/helpers/' + name;
    }
  },
  waitSeconds: 15
});