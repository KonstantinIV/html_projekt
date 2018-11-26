function myFunction() {
    document.getElementById("graf").style.transition = "1s";
    document.getElementById("graf").style.visibility = "visible";
    document.getElementById("graf").style.display = "block";
    document.getElementById("graf").style.webkitTransition = 'opacity 1s';

    var element = document.getElementById("graf");


    element.scrollIntoView({block:"center"}); // center
    document.getElementById("graf").style.opacity = "1";

}