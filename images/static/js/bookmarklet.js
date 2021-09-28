(function(){
    var jquery_version = '3.3.1';
    var site_url = 'http://3c2b-79-104-0-182.ngrok.io';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg){
        var css = jQuery('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)
        });
        jQuery('head').append(css);

        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';
        jQuery('body').append(box_html);
        jQuery('#bookmarklet #close').click(function(){
            jQuery('#bookmarklet').remove();
        });
        console.log(1);
        jQuery.each(jQuery('img[src$="jpg"]'), function(index, image) {
            console.log(jQuery(image).height() >= min_height);
            if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height){
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append(
                '<a href="#"><img src="'+image_url +'" /></a>'
                );
                console.log(2);
            }
        });
        console.log(3);
        jQuery('#bookmarklet .images a').click(function(e){
            selected_image = jQuery(this).children('img').attr('src');
            // Скрываем букмарклет.
            jQuery('#bookmarklet').hide();
            // Открываем новое окно с формой сохранения изображения.
            window.open(site_url +'images/create/?url='
                        + encodeURIComponent(selected_image)
                        + '&title=' + encodeURIComponent(jQuery('title').text()),
                        '_blank');
        });
    };

    if (typeof window.jQuery != 'undefined') {
        console.log(typeof window.jQuery);
        bookmarklet();
    } else {
        var conflict = typeof window.$ != 'undefined';
        var script = document.createElement('script');
        script.src = '//ajax.googleapis.com/ajax/libs/jquery/' + jquery_version + '/jquery.min.js';
        document.head.appendChild(script);
        var attempts = 15;
        (function(){
            if (typeof window.jQuery == 'undefined'){
                if (--attempts>0) {
                    console.log(attempts);
                    window.setTimeout(arguments.callee, 250)
                } else {
                    alert('An error occurred while loading jQuerry')
                }
            } else {
                bookmarklet();
            }
        })();
    }
})();