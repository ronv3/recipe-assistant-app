#tere
#vana
#kere

def loe_toidud_failist(failinimi):
    t_fail = open(failinimi, encoding = "utf-8")
    toidud = []
    for rida in t_fail:
        if rida != '':
            rida = rida.strip().split()
            toidud.append(rida)
    td = {}
    for toit in toidud:
        aine, kogus = toit[0].split(",")
        td[aine] = int(kogus)
    return td

def loe_retsept(failinimi):
    r_fail = open(failinimi, encoding = "utf-8")
    t_ained = []
    for rida in r_fail:
        rida = rida.strip().split()
        if rida == ["-"]:
            break
        t_ained.append(rida)
    recnim = t_ained[0]
    del t_ained[0]
    td = {}
    for toit in t_ained:
        aine, kogus = toit[0].split(",")
        td[aine] = int(kogus)
    return td, recnim

def võrdle(d1, d2):
    võimalikud_retseptid = []
    ained = d2[0]
    recc = ''.join(d2[1])
    if all(aine in d1 and d1[aine] >= arv for aine, arv in ained.items()):
        võimalikud_retseptid.append(recc)
        return võimalikud_retseptid
    else:
        return 0
    
def lisa_retsepti_andmebaasi(a):
    sfn = input("Sisesta uue faili nimi: (r_roa_nimi.txt formaadis): ")
    recf = open(sfn, 'w', encoding = 'utf-8')
    nimi = input("Sisesta roa nimi: ")
    recf.write(f'{nimi}\n')
    tained = input("Sisesta järjest toiduaineid (nt. Kartul,300 Kurk,200): ")
    tained = tained.split()
    for aine in tained:
        recf.write(f'{aine}\n')
    recf.write('-\n')
    reccept = input("Kopeeri või kirjuta valmistamisjuhend siia: ")
    recf.write(reccept)
    recf.close()
    ab = open("retsepti_andmebaas.txt", 'a', encoding = 'utf-8')
    ab.write(f'{sfn}\n')
    ab.close()
    print("Retsept edukalt andmebaasi lisatud!")
    
def retseptiloendur():
    alltoit = loe_toidud_failist("toit.txt")
    v_rec = []
    k_rec = []
    ab = open("retsepti_andmebaas.txt", 'r', encoding = 'utf-8')
    for rida in ab:
        rida = rida.strip()
        k_rec.append(rida)
    for rec in k_rec:
        d2 = loe_retsept(rec)
        a = võrdle(alltoit, d2)
        if a != 0:
            v_rec.append(a)
    print("Saad nende toiduainetega valmistada järgnevaid roogasid: ")
    for x in v_rec:
        print(''.join(x))
    end = ("...ja ongi kõik.")
    return end

def toiduaine_muutja():
    nk = loe_toidud_failist("toit.txt")
    dicti = {}
    dicti2 = {}
    s1 = input("Kas soovid toiduaineid lisada(+) või eemaldada(-)? ")
    if s1 == '+':
        l1 = input("Lisa toiduained. (Aine,Kaal formaadis): ")
        l1 = l1.split()
        dicti = {nimi.split(',')[0]: int(nimi.split(',')[1]) for nimi in l1}
        for aine, kogus in dicti.items():
            if aine in nk:
                nk[aine] += dicti[aine]
            else:
                nk[aine] = kogus
        lis = list(nk.items())
        unk = [f'{x},{y}' for x, y in lis]
        tf = open('toit.txt', 'w', encoding = 'utf-8')
        for toiduaine in unk:
            tf.write(f'{toiduaine}\n')
        tf.close()
        return "Toiduainete nimekiri uuendatud!"
    elif s1 == '-':
        l2 = input("Eemalda toiduaineid. (Aine,Kaal formaadis)\nKui toiduainet on veel alles, kuid vähem, sisesta, kui palju kadus.\nKui toiduaine on täiesti otsas, pane väärtuseks 0\n")
        l2 = l2.split()
        dicti2 = {nimi.split(',')[0]: int(nimi.split(',')[1]) for nimi in l2}
        for aine2, kogus2 in dicti2.items():
            if dicti2[aine2] != 0:
                nk[aine2] -= dicti2[aine2]
            else:
                del nk[aine2]
        lis2 = list(nk.items())
        unk2 = [f'{m},{n}' for m, n in lis2]
        tf = open('toit.txt', 'w', encoding = 'utf-8')
        for toiduaine in unk2:
            tf.write(f'{toiduaine}\n')
        tf.close()
        return "Toiduainete nimekiri uuendatud!"