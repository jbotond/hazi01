def primteszt():
    szam = input()
    szam = int(szam)
    oszt = 1
    while oszt <= szam:
        if szam==1:
            return "NEM"
        if szam % oszt == 0:
            if oszt == 1 :
                oszt=oszt+1
                continue
            elif oszt==szam:
                return "IGEN"
            else:
                return "NEM"
        else:
            oszt=oszt+1
            continue

if __name__ == "__main__":
    print(primteszt())