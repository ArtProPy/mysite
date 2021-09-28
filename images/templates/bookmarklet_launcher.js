(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    } else {
        document.body.appendChild(
        document.createElement('script')
        ).src='http://3c2b-79-104-0-182.ngrok.io/static/js/bookmarklet.js?r=' +
        Math.floor(Math.random()*99999999999999999999);
    }
})();