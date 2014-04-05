define(['jquery'], function ($) {
  require('json!/api/csrf', function (token) {
    var ajaxCSRF = {
      csrfSafeMethod: function (method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      },
      init: function () {
        var _this = this;
        $.ajaxSetup({
          crossDomain: false,
          beforeSend: function (xhr, settings) {
            if (!_this.csrfSafeMethod(settings.type)) {
              xhr.setRequestHeader("X-CSRFToken", token);
            }
          }
        });
      }
    };
    ajaxCSRF.init()
  });
});
