$(document).ready(function () {
  "use strict";

  PageScroll();

  // Loading Box (Preloader)
  function handlePreloader() {
    if ($(".preloader").length > 0) {
      $(".preloader").delay(200).fadeOut(500);
    }
  }

  handlePreloader();

  // $('.minus').click(function () {
  //     var $input = $(this).parent().find('input');
  //     var count = parseInt($input.val()) - 1;
  //     count = count < 1 ? 1 : count;
  //     $input.val(count);
  //     $input.change();
  //     return false;
  // });
  // $('.plus').click(function () {
  //     var $input = $(this).parent().find('input');
  //     $input.val(parseInt($input.val()) + 1);
  //     $input.change();
  //     return false;
  // });

  // OWL SLIDER
  $(".category-slider").owlCarousel({
    loop: true,
    margin: 4,
    nav: true,
    autoplay: false,
    dots: false,
    navText: [
      '<i class="feather-arrow-left-circle"></i>',
      '<i class="feather-arrow-right-circle"></i>',
    ],
    autoWidth: true,
  });

  $(".slider-banner").owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    autoplay: false,
    dots: true,
    navText: [
      '<i class="feather-chevron-left"></i>',
      '<i class="feather-chevron-right"></i>',
    ],
    items: 1,
  });
  $(".product-banner").owlCarousel({
    loop: false,
    margin: 0,
    nav: true,
    autoplay: false,
    dots: true,
    navText: [
      '<i class="feather-chevron-left"></i>',
      '<i class="feather-chevron-right"></i>',
    ],
    items: 1,
  });
  $(".slider-banner-2").owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    autoplay: false,
    dots: false,
    navText: [
      '<i class="feather-chevron-left"></i>',
      '<i class="feather-chevron-right"></i>',
    ],
    autoWidth: true,
  });

  $(".slider-banner-3").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: false,
    dots: true,
    navText: [
      '<i class="feather-chevron-left"></i>',
      '<i class="feather-chevron-right"></i>',
    ],
    items: 3,
    center: true,
  });

  $(".banner-slider-3").owlCarousel({
    loop: true,
    margin: 0,
    nav: true,
    autoplay: false,
    dots: false,
    navText: [
      '<i class="feather-arrow-left-circle"></i>',
      '<i class="feather-arrow-right-circle"></i>',
    ],
    items: 3,
    responsive: {
      0: {
        items: 1,
        nav: true,
      },
      749: {
        items: 3,
        nav: true,
      },
    },
  });

  $(".banner-slider-4").owlCarousel({
    loop: false,
    margin: 0,
    nav: true,
    autoplay: false,
    dots: false,
    navText: [
      '<i class="feather-arrow-left-circle"></i>',
      '<i class="feather-arrow-right-circle"></i>',
    ],
    items: 4,
    responsive: {
      0: {
        items: 1,
        nav: true,
      },
      350: {
        items: 2,
        nav: true,
      },
      500: {
        items: 3,
        nav: true,
      },
      749: {
        items: 4,
        nav: true,
      },
      991: {
        items: 6,
        nav: true,
      },
    },
  });
  // partnyor
  $(document).ready(function () {
    $(".customer-logos").slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1000,
      arrows: false,
      dots: false,
      pauseOnHover: false,
      responsive: [
        { breakpoint: 768, settings: { slidesToShow: 3 } },
        { breakpoint: 520, settings: { slidesToShow: 2 } },
      ],
    });
  });

  $(".banner-slider-5").owlCarousel({
    loop: true,
    margin: 0,
    nav: true,
    autoplay: false,
    dots: false,
    navText: [
      '<i class="feather-arrow-left-circle"></i>',
      '<i class="feather-arrow-right-circle"></i>',
    ],
    items: 5,
    responsive: {
      0: {
        items: 2,
        nav: true,
      },
      749: {
        items: 4,
        nav: true,
      },
      1023: {
        items: 5,
        nav: true,
      },
    },
  });

  $(".nav-item-toggle").on({
    mouseenter: function () {
      $(this).children().addClass("show");
    },
    mouseleave: function () {
      $(this).children().removeClass("show");
    },
  });

  $(".toggle-nav").on("click", function () {
    $(".navigation,.main-content,.nav-header").toggleClass("menu-active");
    return false;
  });

  $(".wishlist-btn").on("click", function () {
    $(this).find("i").toggleClass("active");
    return false;
  });

  $(".category-card").on("click", function () {
    $(".category-card").removeClass("active");
    $(this).addClass("active");
    return false;
  });

  // navigation slide menu mobile
  $(".nav-menu").on("click", function () {
    $(this).toggleClass("active");
    $(".navigation").toggleClass("nav-active");
  });
  $(".close-nav").on("click", function () {
    $(".navigation").removeClass("nav-active");
    return false;
  });
  $(".nav-link").on("click", function () {
    $(".nav-link").removeClass("active");
    $(this).addClass("active");
  });

  $('input[name="color-radio"]').on("change", function () {
    if (this.checked) {
      $("body").removeClass(
        "color-theme-teal color-theme-cadetblue color-theme-pink color-theme-deepblue color-theme-blue color-theme-red color-theme-black color-theme-gray color-theme-orange color-theme-yellow color-theme-green color-theme-white color-theme-brown color-theme-darkgreen color-theme-deeppink color-theme-darkorchid"
      );
      $("body").addClass("color-theme-" + $(this).val());
    }
  });

  $("#checkout").on("click", function () {
    $(".cart-box").fadeOut(0);
    $(".checkout-box").fadeIn();
  });
  $("#payment").on("click", function () {
    $(".checkout-box").fadeOut(0);
    $(".payment-box").fadeIn();
  });

  $(window).on("load", function () {
    $("#modalSubscribe").modal("show");
  });
});

function PageScroll() {
  $(".scroll-tiger").on("click", function (e) {
    var $anchor = $(this);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: $($anchor.attr("href")).offset().top - 0,
        },
        1500,
        "easeInOutExpo"
      );
    $(".overlay-section").removeClass("active");
    e.preventDefault();
  });
}

// Partnyor slider


// dropdown
(function ($bs) {
  const CLASS_NAME = 'has-child-dropdown-show';
  $bs.Dropdown.prototype.toggle = function (_orginal) {
    return function () {
      document.querySelectorAll('.' + CLASS_NAME).forEach(function (e) {
        e.classList.remove(CLASS_NAME);
      });
      let dd = this._element.closest('.dropdown').parentNode.closest('.dropdown');
      for (; dd && dd !== document; dd = dd.parentNode.closest('.dropdown')) {
        dd.classList.add(CLASS_NAME);
      }
      return _orginal.call(this);
    }
  }($bs.Dropdown.prototype.toggle);
  document.querySelectorAll('.dropdown').forEach(function (dd) {
    dd.addEventListener('hide.bs.dropdown', function (e) {
      if (this.classList.contains(CLASS_NAME)) {
        this.classList.remove(CLASS_NAME);
        e.preventDefault();
      }
      if (e.clickEvent && e.clickEvent.composedPath().some(el => el.classList && el.classList.contains('dropdown-toggle'))) {
        e.preventDefault();
      }
      e.stopPropagation();
    });
  });
  function getDropdown(element) {
    return $bs.Dropdown.getInstance(element) || new $bs.Dropdown(element);
  }
  document.querySelectorAll('.dropdown-hover, .dropdown-hover-all .dropdown').forEach(function (dd) {
    dd.addEventListener('mouseenter', function (e) {
      let toggle = e.target.querySelector(':scope>[data-bs-toggle="dropdown"]');
      if (!toggle.classList.contains('show')) {
        getDropdown(toggle).toggle();
      }
    });
    dd.addEventListener('mouseleave', function (e) {
      let toggle = e.target.querySelector(':scope>[data-bs-toggle="dropdown"]');
      if (toggle.classList.contains('show')) {
        getDropdown(toggle).toggle();
      }
    });
  });
})(bootstrap);

