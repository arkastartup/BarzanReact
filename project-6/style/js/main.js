$(document).ready(function() {
    function menuscroll() {
        let navMenu = $('.nav-menu')
        if ($(window).scrollTop() > 38) {
            navMenu.addClass('is-scrolling');
        }
        else {
            navMenu.removeClass('is-scrolling');
        }
    }

    menuscroll();


    $(window).on('scroll' , menuscroll);


    let sideNav = $('#navbar');

    sideNav.on('show.bs.collapse' , function() {
        $(this).parents('.nav-menu').addClass('menu-is-open');
    })

    sideNav.on('hide.bs.collapse' , function() {
        $(this).parents('.nav-menu').removeClass('menu-is-open');
    })

    $('#navbar .navbar-nav a').on('click' , function(e) {
        let target = $(this.hash); //hash ==> #home
        if (target.length) {
            e.preventDefault();
            $('html,body').animate ({
                scrollTop : target.offset().top
            } , 1000)
        }
    })

    let comments = $('.comments');
    if (comments.length && $.fn.owlCarousel) {
        comments.owlCarousel({
            rtl : true ,
            nav : true ,
            items : 1 ,
            docts : false ,
            navText : ['<i class="fas fa-chevron-right h4"></i>' , '<i class="fas fa-chevron-left h4"></i>'] ,

        });
    }

    let gallery = $('.image-gallery');
    if (gallery.length && $.fn.owlCarousel) {
        gallery.owlCarousel({
            rtl : true ,
            nav : false ,
            items : 3 ,
            docts : true ,
            center : true ,
            autoplay : true ,
            autoplayTimeout : 5000 ,
            stagePadding : 0,
            loop : true ,
            responsive : {
                0 : {
                    items : 1
                },
                768 : {
                    items : 3
                }
            }
        });
    }
})