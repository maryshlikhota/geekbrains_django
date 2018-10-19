$(function(){

    // scroll
    $('a[href^="#"]').click(function(event){
        var element = $(this).attr("href");
        var destination = $(element).offset().top;
        event.preventDefault();

        $('body, html').animate({
           scrollTop: destination
        }, 1200);
        return false;
    });

    // Show link up
    function showLinkUp() {
        var footerMarginSize = $('footer').innerHeight() - $('footer').height();
        if ($(document).height() - footerMarginSize > $(window).height()) {
            $('.js-link-up').show();
        } else {
            $('.js-link-up').hide();
        }
    }
    
    $(document).ready(function () {
        showLinkUp();
    });

    $(window).resize(function () {
        showLinkUp();
    });

    /* A simple and scalable hamburger menu using css transitions. */
    var isActive = false;

    $('.js-menu').on('click', function () {
        if (isActive) {
            $(this).removeClass('active');
            $('body').removeClass('menu-open');
        } else {
            $(this).addClass('active');
            $('body').addClass('menu-open');
        }

        isActive = !isActive;
    });

    window.onscroll = function () { myFunction() };
    var header = document.getElementById("myHeader");
    var sticky = header.offsetTop;

    function myFunction() {
        if (window.pageYOffset > sticky) {
            header.classList.add("sticky");
        } else {
            header.classList.remove("sticky");
        }
    }

});

