module.exports = function (grunt) {

  var revision = grunt.option('revision') || '12345';
  var staticRoot = grunt.option('staticRoot') || 'build/';
  var srcDir = grunt.option('srcDir');

  var processhtmlFiles = {};
  processhtmlFiles[srcDir + 'templates/base.html'] = srcDir + 'vortaro/app/templates/base.html';
  processhtmlFiles[staticRoot + 'cache.manifest'] = srcDir + 'static/cache.manifest';

  var cssminFiles = {};

  cssminFiles[staticRoot + 'css/style-' + revision + '.css'] = [
    'bower_components/jquery-file-upload/css/jquery.fileupload.css', 'bower_components/select2/select2.css',
    'css/from-less.css'];

  var now = new Date;
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    requirejs: {
      compile: {
        options: {
          baseUrl: "./",
          name: "bower_components/almond/almond",
          include: [
            'js/config/require.js', 'js/app'
          ],
          mainConfigFile: './js/config/require.js',
          out: staticRoot + "js/app-" + revision + ".js",
          optimizeAllPluginResources: true,
          preserveLicenseComments: true,
          inlineText: false,
          findNestedDependencies: false,
          logLevel: 0
        }
      }

    },
    copy: {
      main: {
        files: [
          {expand: true, cwd: srcDir + 'static', src: ['svg/**'], dest: staticRoot },
          {expand: true, cwd: srcDir + 'static/bower_components/select2/', src: ['*.png', '*.gif'], dest: staticRoot +
            'css/' }
        ]
      }
    },
    less: {
      production: {
        files: {
          'css/from-less.css': 'less/style.less'
        }
      }
    },
    cssmin: {
      minify: {
        files: cssminFiles
      }
    },
    clean: {
      options: {
        force: true
      },
      js: [
        staticRoot + "js/**"
      ], css: [
        staticRoot + "css/**"
      ], templates: [
        srcDir + 'templates/'
      ]
    },
    processhtml: {
      options: {
        data: {
          revision: revision,
          modified: now.getFullYear() + '-' + (now.getMonth() + 1) + '-' + now.getDate(),
          now: now
        }
      },
      dist: {
        files: processhtmlFiles
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-requirejs');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-processhtml');
  grunt.registerTask('default', [
    'clean', 'requirejs', 'processhtml', 'less', 'cssmin', 'copy'
  ]);

};