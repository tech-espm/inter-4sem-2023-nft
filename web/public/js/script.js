window.onload = function() {
    //create a timeout function to delay the loading of the page by 0.5 second

    var url = window.location.href;
    var activePage = url;
    var a = document.getElementsByClassName("extra-color");
    for (var i = 0; i < a.length; i++) {
    if (a[i].href == activePage) {
        a[i].classList.add("first");
    }
    else{
        a[i].classList.remove("first");
        a[i].classList.add("white");
    }
}

    
}