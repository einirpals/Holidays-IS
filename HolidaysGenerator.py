import datetime

# https://blog.georgekosmidis.net/c-calculating-orthodox-and-catholic-easter.html
def GetCatholicEaster(year):
    month = 3

    a = year % 19 + 1
    b = year / 100 + 1
    c = (3 * b) / 4 - 12
    d = (8 * b + 5) / 25 - 5
    e = (5 * year) / 4 - c - 10

    f = (11 * a + 20 + d - c) % 30
    if (f == 24):
        f += 1
    if ((f == 25) and (a > 11)):
        f += 1

    g = 44 - f
    if (g < 21):
        g = g + 30

    day = (g + 7) - ((e + g) % 7)
    if (day > 31):
        day = day - 31
        month = 4
    
    return datetime.datetime(int(year), int(month), int(day))

def GetFirstDayByRange(year, month, firstDayOfRange, firstWeekDay):
    date = datetime.datetime(year, month, firstDayOfRange)
    current_weekday = date.weekday() # Monday is 0 and Sunday is 6.
    days_to_add = (firstWeekDay - current_weekday + 7) % 7
    date += datetime.timedelta(days = days_to_add)

    return date

# Sjómannadagurinn er fyrsti sunnudagurinn í júní ár hvert.
# Monday is 0 and Sunday is 6.
# Nema ef hvítasunnu ber upp á þann dag, þá er hann næsti sunnudagur þar á eftir.
def GetSjomannadagurinn(Hvitasunnudagur):
    year = Hvitasunnudagur.year
    Sjomannadagurinn = GetFirstDayByRange(year, 6, 1, 6)

    if(Hvitasunnudagur == Sjomannadagurinn):
        Sjomannadagurinn += datetime.timedelta(days = 7)

    return Sjomannadagurinn

# Þorri
# Hann hefst á föstudegi í 13. viku vetrar, sem nú er á bilinu 19. til 25. janúar.
# Monday is 0 and Sunday is 6. Friday is 4.
def GetÞorri(year):
    return GetFirstDayByRange(year, 1, 19, 4)

# Góa
# hefst á sunnudegi í átjándu viku vetrar, eða 18. til 24. febrúar.
# Monday is 0 and Sunday is 6.
def GetGoa(year):
    return GetFirstDayByRange(year, 2, 18, 6)

# Sumardagurinn fyrsti
# Á Íslandi ber sumardaginn fyrsta alltaf upp á fimmtudag á tímabilinu frá 19.-25. apríl (það er fyrsta fimmtudag eftir 18. apríl).
# Monday is 0 and Sunday is 6. Thursday is 3.
def GetSumardagurinnFyrsti(year):
    return GetFirstDayByRange(year, 4, 19, 3)

# Fyrsti vetrardagur
# Fyrsti vetrardagur er fyrsti laugardagur að lokinni 26. viku sumars.
# Fyrsta vetrardag ber upp á 21.-27. október.
# Monday is 0 and Sunday is 6. Saturday is 5.
def GetFyrstiVetrardagur(year):
    return GetFirstDayByRange(year, 10, 21, 5)

# Verslunarmannahelgin
# Verslunarmannahelgin er helgin á undan frídegi verslunarmanna sem árlega er haldið upp á fyrsta mánudag í ágústmánuði.
# Monday is 0 and Sunday is 6.
def GetVerslunarmannahelgin(year):
    return GetFirstDayByRange(year, 8, 1, 0)

# Menningarnótt er afmælishátíð Reykjavíkurborgar og verið haldin árlega síðan 1996.
# Er hún fyrsta laugardag eftir hið eiginlega afmæli borgarinnar sem er þann 18. ágúst eða 18. ágúst ef hann fellur á laugardag[1]
# Monday is 0 and Sunday is 6. Saturday is 5.
def GetMenningarnott(year):
    return GetFirstDayByRange(year, 8, 18, 5)

# Algengast er að þjóðir láti hann bera upp á annan sunnudag maímánaðar (8 – 14. maí) ár hvert.
# Þannig er það til dæmis á Íslandi og í Bandaríkjunum.
# Monday is 0 and Sunday is 6.
def GetMaedradagurinn(year):
    return GetFirstDayByRange(year, 5, 8, 6) # Byrja á degi 8 til að fá annan sunnudag mánaðarins.

# Ísland, Noregur, Svíþjóð, Finnland og Eistland halda upp á hann annan sunnudag í nóvember ár hvert.
# Monday is 0 and Sunday is 6.
def GetFedradagurinn(year):
    return GetFirstDayByRange(year, 11, 8, 6) # Byrja á degi 8 til að fá annan sunnudag mánaðarins.

# Hann hefst á þriðjudegi í 22. viku vetrar, eða 20. til 26. mars.
# Monday is 0 and Sunday is 6. thursday is 1.
def GetEinmanudur(year):
    return GetFirstDayByRange(year, 3, 20, 1)

year = 2031

Paskadagur = GetCatholicEaster(year)
print(f"Paskadagur............: {Paskadagur.strftime('%Y-%m-%d %A')}")

Bolludagur = Paskadagur - datetime.timedelta(days=48)
Sprengidagur = Paskadagur - datetime.timedelta(days=46)
Oskudagur = Paskadagur - datetime.timedelta(days=45)

print(f"Bolludagur............: {Bolludagur.strftime('%Y-%m-%d %A')}")
print(f"Sprengidagur..........: {Sprengidagur.strftime('%Y-%m-%d %A')}")
print(f"Öskudagur.............: {Oskudagur.strftime('%Y-%m-%d %A')}")

Palmasunnudagur = Paskadagur - datetime.timedelta(days=7)
Skirdagur = Paskadagur - datetime.timedelta(days=3)
FostudagurinnLangi = Paskadagur - datetime.timedelta(days=2)

print(f"Pálmasunnudagur.......: {Palmasunnudagur.strftime('%Y-%m-%d %A')}")
print(f"Skírdagur.............: {Skirdagur.strftime('%Y-%m-%d %A')}")
print(f"FöstudagurinnLangi....: {FostudagurinnLangi.strftime('%Y-%m-%d %A')}")

AnnarIPaskum = Paskadagur + datetime.timedelta(days=1)
Uppstigningardagur = Paskadagur + datetime.timedelta(days=39)
Hvitasunnudagur = Paskadagur + datetime.timedelta(days=49)
AnnariHvitasunnu = Paskadagur + datetime.timedelta(days=50)

Sjomannadagurinn = GetSjomannadagurinn(Hvitasunnudagur)
print(f"Sjomannadagurinn......: {Sjomannadagurinn.strftime('%Y-%m-%d %A')}")

Þorri = GetÞorri(year) # Bóndadagur, upphaf Þorra
print(f"Þorri.................: {Þorri.strftime('%Y-%m-%d %A')}")

Goa = GetGoa(year) # Konudagur, upphaf Góu
print(f"Góa...................: {Goa.strftime('%Y-%m-%d %A')}")

SumardagurinnFyrsti = GetSumardagurinnFyrsti(year) # fyrsti dagur Hörpu.
print(f"Sumardagurinn Fyrsti..: {SumardagurinnFyrsti.strftime('%Y-%m-%d %A')}")

Fyrsti_Vetrardagur = GetFyrstiVetrardagur(year)
print(f"Fyrsti vetrardagur....: {Fyrsti_Vetrardagur.strftime('%Y-%m-%d %A')}")

Verslunarmannahelgin = GetVerslunarmannahelgin(year)
print(f"Verslunarmannahelgin..: {Verslunarmannahelgin.strftime('%Y-%m-%d %A')}")

Gleðigangan = Verslunarmannahelgin + datetime.timedelta(days=5) # Fyrsta laugardag eftir verzló.
print(f"Gleðigangan...........: {Gleðigangan.strftime('%Y-%m-%d %A')}")

Menningarnott = GetMenningarnott(year)
print(f"Menningarnótt.........: {Menningarnott.strftime('%Y-%m-%d %A')}")

Maedradagurinn = GetMaedradagurinn(year)
print(f"Mæðradagurinn.........: {Maedradagurinn.strftime('%Y-%m-%d %A')}")

Fedradagurinn = GetFedradagurinn(year)
print(f"Feðradagurinn.........: {Fedradagurinn.strftime('%Y-%m-%d %A')}")

Einmanudur = GetEinmanudur(year) # Kváradagur. 2022 var ákveðið að halda daginn hátíðlegan fyrsta dag einmánaðar undir nýju nafni, til að gæta samræmis.
print(f"Einmanuður............: {Einmanudur.strftime('%Y-%m-%d %A')}") 

