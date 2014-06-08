module.exports = function (grunt) {

  var revision = grunt.option('revision') || '12345';
  var staticRoot = grunt.option('staticRoot');
  var srcDir = grunt.option('srcDir');

  var cssFiles = {};
  cssFiles[staticRoot + 'css/style-' + revision + ".css"] = [
    srcDir + 'css/from-less.css', srcDir + 'bower_components/jquery-file-upload/css/jquery.fileupload.css',
    srcDir + 'bower_components/select2-amd/select2',
    srcDir + 'bower_components/select2-bootstrap-css/select2-bootstrap.css'
  ];

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
        files: {
          'css/from-less.css':'less/style.less'
        }
      }
    },
    cssmin: {
      minify: {
        files: cssFiles
      }
    },
    clean: {
      options: {
        force: true
      },
      js: [
        staticRoot + "js/"
      ],
      css: [
        staticRoot + "css/"
      ]
    },
    processhtml: {
      options: {
        data: {
          revision: revision
        }
      },
      dist: {
        files: {
          'templates/base.html':'vortaro/app/templates/base.html'
        }
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