define(['js/reqres', 'marionette'], function (reqres, Marionette) {
  window.addEventListener('load', function (e) {
    window.applicationCache.addEventListener('updateready', function (e) {
      if (window.applicationCache.status == window.applicationCache.UPDATEREADY) {
        window.applicationCache.swapCache();
        window.location.reload();
      }
    }, false);

  }, false);

  var ua = navigator.userAgent;
  var isChrome = /chrome/i.exec(ua), isAndroid = /android/i.exec(ua), hasTouch = 'ontouchstart' in window &&
    !(isChrome && !isAndroid);
  reqres.setHandler('hasTouch', function () {
    return hasTouch;
  });

  var Application = new Marionette.Application();
  Application.addInitializer(function () {
    require(['js/app']);
  });
  Application.start();
});