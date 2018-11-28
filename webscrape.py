from bs4 import BeautifulSoup as soup
import requests
import re
import matplotlib.pyplot as plt
import numpy as np
import lxml.html
import sys


#vastavalt            x             y                z
def tulpdiagram(sinu_koondhinne, kursuse_keskmine,  kursuse_nimed ):
    # Valikulised võib ära kustutada, ei mõjuta koodi tööd
    plt.xlabel('Kursused', fontsize=12) # x telje nimetus
    plt.ylabel('Protsent', fontsize=12) # y telje nimetus
    plt.title('Hinded') # Diagrammi pealkiri


    # Oluline, enne kustutamist konsulteerida Konstantinniga
    index = np.arange(len(kursuse_nimed)) # indeks ehk järjendi_suurus --> [0,1]
    plt.bar(index - 0.05, sinu_koondhinne,0.10, label='Sinu koondhinne') # SINU keskmise väärtus vastvalt indeksile
    plt.bar(index + 0.05, kursuse_keskmine,0.10, label="Kursuse keskmine") # KURSUSE keskmise väärtus vastvalt indeksile
    plt.xticks(index, kursuse_nimed, fontsize=12) # nimi vastvalt indeksile
    #plt.ylim([0,100]) # protsendi skaala, self explanatory
    plt.legend(loc='best') # Näitab legendi
    plt.gca().yaxis.grid(linestyle='dotted') # Näitab Y axis abistavaid jooni statistika jälgimiseks
    plt.savefig("graafik.png")
    print("Valmis")



#näidis väärtused
#tulpdiagram([30,40,50,80],[50,60,50,70],["prog","arhit","sisse","mate pilt"])

################################################################################
# Funktsioon, mis võtab argumendiks kursuse id ja annab välja kursuse protsendid ning kursuse nime
def get_hinded(nimi, url, id):
    produkt = [] # (kursuse nimi, sinu tulemus %, kursuse keskmine %)
    raw_hinded = c.get("https://moodle.ut.ee/grade/report/user/index.php?id="+id)
    hinded_soup = soup(raw_hinded.content, "html.parser")

    lõpphinde_container = hinded_soup.findAll("tr")[-1]
    
    #Proovin leida kursuse protsenti
    if lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-percentage"}) != None: #Kui on olemas protsent
        sinu_protsent = lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-percentage"}).text
        kursuse_protsent = lõpphinde_container.find("td", {"class":"level1 levelodd oddd1 baggt b2b itemcenter column-average"}).text
        
        if ")" in kursuse_protsent:
            kursuse_protsent = kursuse_protsent.split("(")[-1][:len(kursuse_protsent)+1]
        elif "%" not  in kursuse_protsent:
            max_punktid = float(lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-range"}).text[2:])
            kursuse_protsent = str(round((float(kursuse_protsent)/max_punktid )*100)) + " %"
        produkt.append([sinu_protsent, kursuse_protsent, nimi])

    else: #Kui protsenti pole kirjas
        punktide_var1 = lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-grade"})
        punktide_var2 = lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter gradefail column-grade"})
        if punktide_var1 != None or punktide_var2 != None:
            try:
                if punktide_var1 == None:
                    punktid = float(punktide_var2.text)
                else:
                    punktid = float(punktide_var1.text)

                max_punktid = float(lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-range"}).text[2:])
                kursuse_keskmine = float(lõpphinde_container.find("td",{"class":"level1 levelodd oddd1 baggt b2b itemcenter column-average"}).text)
                sinu_protsent = (punktid/max_punktid)*100
                kursuse_protsent = (kursuse_keskmine/max_punktid)*100

            except:
                sinu_protsent, kursuse_protsent = "0","0"
                produkt.append([sinu_protsent, kursuse_protsent, nimi])
        else:
            sinu_protsent, kursuse_protsent = "0","0"
            produkt.append([sinu_protsent, kursuse_protsent, nimi])
    
    if nimi == "Programmeerimine (LTAT.03.001)": #Pagana proge ainel on erinevas kohas jooksvad punktid
        hinded = hinded_soup.findAll("tr")[-2]
        punktid = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-grade"}).text)
        max_punktid = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-range"}).text[2:])
        kursuse_keskmine = float(hinded.find("td",{"class":"level2 leveleven item b1b itemcenter column-average"}).text)
        sinu_protsent = str(round((punktid/max_punktid)*100)) + " %"
        kursuse_protsent = str(round((kursuse_keskmine/max_punktid)*100)) + " %"
        del produkt[-1]
        produkt.append([sinu_protsent, kursuse_protsent, nimi])
    
    return produkt

################################################################################

with requests.Session() as c: #Funktsiooni kutsed peaksid kõik toimuma selle sessiooni jooksul#
    url = "https://moodle.ut.ee/login/index.php"
    USERNAME = sys.argv[1]   ## Kasutajanime ja parooli võtab käsirealt
    PASSWORD = sys.argv[2]
    login_page = c.get(url)
    lxml_login_page = lxml.html.fromstring(login_page.content)
    LOGINTOKEN = lxml_login_page.xpath('//input[@name="logintoken"]/@value')[0]
    #print("This logintoken",LOGINTOKEN)

    
    login_data = dict(username= USERNAME, password = PASSWORD, logintoken=LOGINTOKEN)
    c.post(url, data=login_data)
    raw_page = c.get("https://moodle.ut.ee/my/")

    raw_soup = soup(raw_page.content, "html.parser") #Muudab puhta html-i supi objektiks
    #print(raw_soup)
    container = raw_soup.findAll("div", {"class":"box coursebox"})
    kõik_vajalik = []

    for div in container:
        new = div.findAll("a")
        for a in new:
            if a.get('title') == None or a.get('title') == "Foorum" or a.get('title') == "Ülesanne":
                pass
            else:
                kursuse_nimi = a.get('title')
                kursuse_url = a.get('href')
                kursuse_id = kursuse_url[kursuse_url.find("=")+1:]
                #print(kursuse_nimi, kursuse_url, kursuse_id)
                kõik_vajalik.append(get_hinded(kursuse_nimi, kursuse_url, kursuse_id))
                
    
    # Joonestamise eelne järjendite korrastamine
    kõik_sinu_protsendid = list(map(lambda y: round(float(re.sub(r"[% ()]", "", y))),list(map(lambda x: x[0][0], kõik_vajalik))))
    kõik_kursused = list(map(lambda x: re.sub("[\(\[].*?[\)\]]", "",x[0][2]), kõik_vajalik))
    for i in range(len(kõik_kursused)):
        kõik_kursused[i] = "".join(list(map(lambda x: x[0].upper(),kõik_kursused[i][:-1].split(" "))))
    kõik_kursuste_protsendid = list(map(lambda y: round(float(re.sub(r"[% ()]", "", y))),list(map(lambda x: x[0][1], kõik_vajalik))))
    
################################################################################
#Matplotlibi programmilõik
#tulpdiagram(sinu_koondhinne, kursuse_keskmine,  kursuse_nimed ):
tulpdiagram(kõik_sinu_protsendid, kõik_kursuste_protsendid, kõik_kursused)