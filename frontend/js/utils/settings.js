require('./csrf');

$ = require('jquery');
require('select2');

$.fn.select2.locales['ru'] = {
  formatNoMatches: function () {
    return "Совпадений не найдено";
  },
  formatInputTooShort: function (input, min) {
    return "Пожалуйста, введите еще хотя бы" + character(min - input.length);
  },
  formatInputTooLong: function (input, max) {
    return "Пожалуйста, введите на" + character(input.length - max) + " меньше";
  },
  formatSelectionTooBig: function (limit) {
    return "Вы можете выбрать не более " + limit + " элемент" + (limit % 10 == 1 && limit % 100 != 11 ? "а" : "ов");
  },
  formatLoadMore: function (pageNumber) {
    return "Загрузка данных…";
  },
  formatSearching: function () {
    return "Поиск…";
  }
};

$.extend($.fn.select2.defaults, $.fn.select2.locales['ru']);

function character(n) {
  return " " + n + " символ" +
    (n % 10 < 5 && n % 10 > 0 && (n % 100 < 5 || n % 100 > 20) ? n % 10 > 1 ? "a" : "" : "ов");
}


var Handlebars = require("hbsfy/runtime");
Handlebars.registerHelper("debug", function (optionalValue) {
  console.log("Current Context");
  console.log("====================");
  console.log(this);

  if (optionalValue) {
    console.log("Value");
    console.log("====================");
    console.log(optionalValue);
  }
});

Handlebars.registerHelper('times', function (n, block) {
  var accum = '';
  for (var i = 0; i < n; ++i)
    accum += block.fn(i);
  return accum;
});