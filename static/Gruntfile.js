module.exports = function (grunt) {

  var revision = grunt.option('revision') || '12345';
  var staticRoot = grunt.option('staticRoot');
  var srcDir = grunt.option('srcDir');

  var lessFiles = {};
  lessFiles[staticRoot + 'css/style-' + revision + ".css"] = 'less/style.less';
  var processhtmlFiles = {};
  processhtmlFiles[srcDir + 'templates/base.html'] = [srcDir + 'vortaro/app/templates/base.html'];

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    requirejs: {
      compile: {
        options: {
          baseUrl: "./",
          name: "bower_components/almond/almond",
//          name: "bower_components/requirejs/require",
          include: [
            'js/config/require.js',
            'js/app',
            'json',
            'hbs'
          ],
          mainConfigFile: './js/config/require.js',
          out: staticRoot + "js/app-" + revision + ".js",
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
          {expand: true, cwd: srcDir+'static', src: ['fonts/**'], dest: staticRoot }
        ]
      }
    },
    less: {
      production: {
        files: lessFiles
      }
    },
    processhtml: {
      options: {
        data: {
          revision: revision
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
  grunt.loadNpmTasks('grunt-processhtml');
  grunt.registerTask('default', [
    'requirejs', 'processhtml', 'less', 'copy'
  ]);

};