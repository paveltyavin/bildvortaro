define(['jquery', 'select2'], function ($) {
  $.fn.modal.Constructor.prototype.enforceFocus = function () {
  };
  $.extend($.fn.select2.defaults, {
    formatNoMatches: function () {
      return "koencidoj ne estas trovitaj";
    },
    formatInputTooShort: function (input, min) {
      var n = min - input.length;
      return "bonvolu enigi ankoraŭ " + n + " more simbolo" + (n == 1 ? "" : "j") +'n';
    },
    formatInputTooLong: function (input, max) {
      var n = input.length - max;
      return "bonvolu forigi " + n + " simbolo" + (n == 1 ? "" : "j") + 'n';
    },
    formatSelectionTooBig: function (limit) {
      return "vi rajtas elekti nur " + limit + " elemento" + (limit == 1 ? "" : "j")+ 'n';
    },
    formatLoadMore: function (pageNumber) {
      return "estas ŝargataj aliaj rezultoj...";
    },
    formatSearching: function () {
      return "pasas serĉado...";
    }
  });
});