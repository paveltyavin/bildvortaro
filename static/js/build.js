({
  baseUrl: "./../",
  name: "js/app",
  mainConfigFile: 'config/require.js',
  out: "app-build.js",
  include: ['requireLib'],
  stubModules: ['json', 'text', 'css', 'hbs'],
  fileExclusionRegExp: /api/,
  optimizeAllPluginResources: true,
  preserveLicenseComments: false,
  inlineText: false,
  findNestedDependencies: false,
  optimize: "uglify",
  logLevel: 0
})