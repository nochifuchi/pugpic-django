// スマホヘッダーメニュー
$(function() {
  const menuBtn = $('.nav-trigger a');
  const nav = $('.sp-header-menu');
  const app = $('#app');

  const openNav = () => {
    menuBtn.addClass('active');
    nav.addClass('active');
  };

  const closeNav = () => {
    menuBtn.removeClass('active');
    nav.removeClass('active');
  };

  menuBtn.click(function() {
    if (menuBtn.hasClass('active') && nav.hasClass('active')) {
      closeNav()
    } else {
      openNav();
    }
    return false;
  });

  //グローバルナビ以外をクリックしたらナビを閉じる
  app.click(function() {
    if (menuBtn.hasClass('active') && nav.hasClass('active')) {
      closeNav();
    }
  });

});