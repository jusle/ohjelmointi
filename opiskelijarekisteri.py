def lisaa_opiskelija(opiskelijat, opiskelija):
    opiskelijat[opiskelija] = []

def lisaa_suoritus(opiskelijat, opiskelija, suoritus):
    kurssi, arvosana = suoritus
    if 1 <= arvosana <= 5:
        for i in range(len(opiskelijat[opiskelija])):
            if opiskelijat[opiskelija][i][0] == kurssi:
                if arvosana > opiskelijat[opiskelija][i][1]:
                    opiskelijat[opiskelija][i] = suoritus
                break
        else:
            opiskelijat[opiskelija].append(suoritus)

def tulosta(opiskelijat, opiskelija):
    if opiskelija in opiskelijat:
        if opiskelijat[opiskelija] == []:
            print(f"{opiskelija}: ")
            print(" ei suorituksia")
        else:
            arvosanat = []
            print(f"{opiskelija}:")
            print(f" suorituksia {len(opiskelijat[opiskelija])} kurssilta:")
            for suoritus in opiskelijat[opiskelija]:
                print(f"  {suoritus[0]} {suoritus[1]}")
                arvosanat.append(suoritus[1])
            keskiarvo = sum(arvosanat) / len(arvosanat)
            print(" keskiarvo", keskiarvo) # Tähän arvosanat-listaan sofistikoituneempi ratkaisu?
    else:
        print(f"ei löytynyt ketään nimellä {opiskelija}")

def kooste(opiskelijat):
    paras_opiskelija = None
    paras_keskiarvo = 0

    for opiskelija, suoritukset in opiskelijat.items():
        keskiarvo = sum(s[1] for s in suoritukset) / len(suoritukset)
        if keskiarvo > paras_keskiarvo:
            paras_keskiarvo = keskiarvo
            paras_opiskelija = opiskelija

    print(f"opiskelijoita {len(opiskelijat)}")
    print(f"eniten suorituksia {len(opiskelijat[max(opiskelijat)])} {max(opiskelijat)}")
    print(f"paras keskiarvo {paras_keskiarvo} {paras_opiskelija}")

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 4))
    lisaa_suoritus(opiskelijat, "Pekka", ("Joo", 0))
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 4))
    lisaa_opiskelija(opiskelijat, "Minna")
    tulosta(opiskelijat, "Pekka")
    tulosta(opiskelijat, "Liisa")
    tulosta(opiskelijat, "Jukka")
    tulosta(opiskelijat, "Minna")
    kooste(opiskelijat)
