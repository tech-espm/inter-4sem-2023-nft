window.onload = function() {
    var url = window.location.href;
    var activePage = url;
    console.log(url)
    if (url == 'http://localhost:3000/top'){
        const rodape = document.getElementsByClassName("rodape")[0];
        rodape.style.marginTop = "25px";
    }
    if (url == 'http://localhost:3000/'){
        const rodape = document.getElementsByClassName("rodape")[0];
        rodape.style.marginTop = "-25px";
    }
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