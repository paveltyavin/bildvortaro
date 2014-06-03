module.exports = function (grunt) {

  var revision = grunt.option('revision');
  var staticDir = grunt.option('staticDir');
  var buildDir = grunt.option('buildDir');
  var srcDir = grunt.option('srcDir');

  var productionLessFiles = {};
  productionLessFiles[staticDir + "/css/style.css"] = 'less/style.less';
  var developmentLessFiles = {};
  developmentLessFiles["static/css/style.css"] = 'less/style.less';

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    requirejs: {
      compile: {
        options: {
          baseUrl: "./static/",
          name: "bower_components/almond/almond",
          include: [
            'js/config/require.js',
            'js/app'
          ],
          mainConfigFile: './static/js/config/require.js',
          out: staticDir + "/js/app.js",
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
          {expand: true, cwd: 'static', src: ['fonts/**'], dest: staticDir}
        ]
      }
    },
    less: {
      production: {
        files: productionLessFiles
      },
      development: {
        files: developmentLessFiles
      }
    },
    processhtml: {
      options: {
      },
      dist: {
        files: {
          '<%= buildDir %>/templates/base.html': ['vortaro/app/templates/base.html']
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-requirejs');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-processhtml');
  grunt.registerTask('default', ['copy', 'requirejs', 'less']);

};