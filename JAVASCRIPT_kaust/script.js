function myFunction() {
    var element = document.getElementById("graf");

    //var txtFile = "/home/leesikas01/m/maier/public_html/32/dist/login_details.txt";
    

    document.getElementById("graf").style.transition = "1s";
    document.getElementById("graf").style.visibility = "visible";
    document.getElementById("graf").style.display = "block";
    document.getElementById("graf").style.webkitTransition = 'opacity 1s';



    element.scrollIntoView({block:"center"}); // center
    element.style.opacity = "1";

}