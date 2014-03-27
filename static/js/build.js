({
  baseUrl: "./../",
  name: "js/app",
  mainConfigFile: 'config.js',
  out: "app-build.js",
  paths: {
    'requireLib': 'bower_components/r.js/require'
  },
  include: ['requireLib']
})