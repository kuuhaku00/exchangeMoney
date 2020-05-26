import json
import requests

a=requests.get("https://api.exchangeratesapi.io/latest")
a = json.loads(a.text)
print(a['rates'])
b=a['rates']
print(b['TRY'])
 
def islem(miktar):
    sonuc=(float(b[bozulan])/float(b[alim]))*miktar
    print(sonuc)
bozulan=input("bozulan doviz turu")
alim=input("alinan dovuz turu")
miktar=float(input(f"ne kadar {bozulan} bozudurmak istiyorsunuz"))
islem(miktar)