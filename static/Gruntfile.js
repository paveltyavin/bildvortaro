module.exports = function (grunt) {

  var revision = grunt.option('revision') || '12345';
  var staticRoot = grunt.option('staticRoot');
  var srcDir = grunt.option('srcDir');

  var lessFiles = {};
  lessFiles[staticRoot + 'css/from-less.css'] = 'less/style.less';
  var processhtmlFiles = {};
  processhtmlFiles[srcDir + 'templates/base.html'] = [srcDir + 'vortaro/app/templates/base.html'];

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
          optimize: "none",
          logLevel: 0
        }
      }

    },
    copy: {
      main: {
        files: [
          {expand: true, cwd: srcDir + 'static', src: ['fonts/**'], dest: staticRoot }
        ]
      }
    },
    less: {
      production: {
        files: lessFiles
      }
    },
    cssmin: {
      minify: {
        expand: true,
        cwd: srcDir + 'static/',
        src: [
          'css/from-less.css'
        ],
        dest: 'css/style-' + revision + ".css"
      }
    },
    clean: [
      staticRoot+"css/",
      staticRoot+"js/"
    ],
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
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-processhtml');
  grunt.registerTask('default', [
    'clean','requirejs', 'processhtml', 'less', 'cssmin', 'copy'
  ]);

};