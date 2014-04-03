define(['jquery'], function($){
  $.fn.eo = function () {
    this.keyup(function () {
      $(this).val(function (i, v) {
        v = v.replace(/c[xX]/, 'ĉ');
        v = v.replace(/C[xX]/, 'Ĉ');

        v = v.replace(/j[xX]/, 'ĵ');
        v = v.replace(/J[xX]/, 'Ĵ');

        v = v.replace(/u[xX]/, 'ŭ');
        v = v.replace(/U[xX]/, 'Ŭ');

        v = v.replace(/g[xX]/, 'ĝ');
        v = v.replace(/G[xX]/, 'Ĝ');

        v = v.replace(/s[xX]/, 'ŝ');
        v = v.replace(/S[xX]/, 'Ŝ');

        v = v.replace(/h[xX]/, 'ĥ');
        v = v.replace(/H[xX]/, 'Ĥ');
        return v;
      });
    });
  };
});