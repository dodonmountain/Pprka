window.onload=function(){
    const userEmail = document.getElementById('#userEmail')
    const isRememberEmail = document.getElementById('#remeberEmail')
    isRememberEmail.addEventListener("click", function (e) {
        console.log(e)
    })
}


function setCookie(cookie_name, value, days) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + days);

    var cookie_value = escape(value) + ((days == null) ? '' : ';    expires=' + exdate.toUTCString());
    document.cookie = cookie_name + '=' + cookie_value;
}


function getCookie(cookie_name) {
    var x, y;
    var val = document.cookie.split(';');
    for (var i = 0; i < val.length; i++) {
        x = val[i].substr(0, val[i].indexOf('=')); // substr(시작인덱스, 끝 인덱스)
        y = val[i].substr(val[i].indexOf('=') + 1);
        x = x.replace(/^\s+|\s+$/g, ''); // strip()
        if (x == cookie_name) {
            return unescape(y); // unescape로 디코딩 후 값 리턴
        }
    }
}