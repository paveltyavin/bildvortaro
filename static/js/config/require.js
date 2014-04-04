require.config({
  baseUrl: '/static',
  paths: {
    'backbone': 'bower_components/backbone/backbone',
    'backbone.modelbinder': 'bower_components/backbone.modelbinder/backbone.ModelBinder',
    'backbone.paginator': 'bower_components/backbone.paginator/dist/backbone.paginator',
    'backbone.dualstorage': 'bower_components/Backbone.dualStorage/backbone.dualstorage.amd',
    'bootstrap.dropdown': 'bower_components/bootstrap/js/dropdown',
    'bootstrap': 'bower_components/bootstrap/dist/js/bootstrap',
    'canvas-to-blob': 'bower_components/blueimp-canvas-to-blob/js/canvas-to-blob',
    'css': 'bower_components/require-css/css',
    'hbs': 'bower_components/hbs/hbs',
    'jquery': 'bower_components/jquery/dist/jquery',
    'jquery.fileupload': 'bower_components/jquery-file-upload/js/jquery.fileupload',
    'jquery.fileupload-image': 'bower_components/jquery-file-upload/js/jquery.fileupload-image',
    'jquery.fileupload-process': 'bower_components/jquery-file-upload/js/jquery.fileupload-process',
    'jquery.ui.widget': 'bower_components/jquery-file-upload/js/vendor/jquery.ui.widget',
    'json': 'bower_components/requirejs-json/json',
    'load-image': 'bower_components/blueimp-load-image/js/load-image',
    'load-image-meta': 'bower_components/blueimp-load-image/js/load-image-meta',
    'load-image-exif': 'bower_components/blueimp-load-image/js/load-image-exif',
    'load-image-ios': 'bower_components/blueimp-load-image/js/load-image-ios',
    'marionette': 'bower_components/marionette/lib/core/amd/backbone.marionette',
    'requireLib': 'bower_components/r.js/require',
    'backbone.wreqr': 'bower_components/backbone.wreqr/lib/amd/backbone.wreqr',
    'backbone.babysitter': 'bower_components/backbone.babysitter/lib/amd/backbone.babysitter',
    'select2-amd': 'bower_components/select2-amd/select2',
    'spin': 'bower_components/spinjs/spin',
    'text': 'bower_components/requirejs-text/text',
    'underscore': 'bower_components/underscore/underscore'
  },
  shim: {
    'jquery.fileupload': ['css!bower_components/jquery-file-upload/css/jquery.fileupload'],
    'select2-amd': [
      'css!bower_components/select2-amd/select2',
      'css!bower_components/select2-bootstrap-css/select2-bootstrap'
    ]
  },
  hbs: {
    disableI18n: true,
    helperPathCallback: function (name) {
      return 'templates/helpers/' + name;
    }
  },
  waitSeconds: 15
});