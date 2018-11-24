function runPython() {
    WshShell = new ActiveXObject("WScript.Shell");
    WshShell.Run("\\\\https://kodu.ut.ee\\~hainluud\\dist\\webscrape.exe",1,true);
    }