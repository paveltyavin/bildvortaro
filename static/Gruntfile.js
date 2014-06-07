module.exports = function (grunt) {

  var revision = grunt.option('revision') || '12345';
  var staticRoot = grunt.option('staticRoot');
  var srcDir = grunt.option('srcDir');

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    requirejs: {
      compile: {
        options: {
          baseUrl: "./",
          name: "bower_components/almond/almond",
          include: [
            'js/config/require.js',
            'js/app'
          ],
          mainConfigFile: './js/config/require.js',
          out: staticRoot + "js/app.js",
          optimizeAllPluginResources: true,
          preserveLicenseComments: true,
          inlineText: false,
          findNestedDependencies: false,
          optimize: "none",
          logLevel: 0
        }
      }

    },
    copy: {
      main: {
        files: [
          {expand: true, cwd: 'static', src: ['fonts/**'], dest: staticRoot}
        ]
      }
    },
    less: {
      production: {
        files: {
          "css/style.css": 'less/style.less'
        }
      }
    },
    processhtml: {
      options: {
      },
      dist: {
        files: {
          '<%= srcDir %>templates/base.html': ['vortaro/app/templates/base.html']
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-requirejs');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-processhtml');
  grunt.registerTask('default', [
    'requirejs'
  ]);

};