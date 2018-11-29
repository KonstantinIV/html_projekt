<<<<<<< HEAD
function runPython() {
    WshShell = new ActiveXObject("WScript.Shell");
    WshShell.Run("\\\\https://kodu.ut.ee\\~hainluud\\dist\\webscrape.exe",1,true);
    }
=======
function myFunction() {
    document.getElementById("graf").style.transition = "1s";
    document.getElementById("graf").style.visibility = "visible";
    document.getElementById("graf").style.display = "block";
    document.getElementById("graf").style.webkitTransition = 'opacity 1s';

    var element = document.getElementById("graf");


    element.scrollIntoView({block:"center"}); // center
    document.getElementById("graf").style.opacity = "1";

}
>>>>>>> e43e33b5e0c04cea3bdc6afa3086f0999a786035
