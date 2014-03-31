define(['jquery', 'json!/../api/csrf'], function ($, token) {
  var ajaxCSRF = {
    csrfSafeMethod: function(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    },
    init: function() {
      var _this = this;
      $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
          if (!_this.csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", token);
          }
        }
      });
    }
  };
  ajaxCSRF.init()

});
