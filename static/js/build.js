({
  baseUrl: "./../",
  name: "js/app",
  mainConfigFile: 'config/require.js',
  out: "app-build.js",
  stubModules: ['css'],
  fileExclusionRegExp: /api/,
  optimizeAllPluginResources: true,
  preserveLicenseComments: false,
  inlineText: false,
  findNestedDependencies: false,
  optimize: "uglify",
  logLevel: 0
})