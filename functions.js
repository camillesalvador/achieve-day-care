$(document).ready(function() {
  $('.menu-icon').on('click', function() {
    $('.menu-nav').toggleClass('menu-active');
    $('body').toggleClass('fixed-top');
    $('.menu-nav').fadeIn();
  });
});
