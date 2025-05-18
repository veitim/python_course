sanasto={'ant':'muurahainen','bear':'karhu','bee':'mehiläinen','butterfly':'perhonen',
'cat':'kissa','chicken':'kana','cow':'lehmä','crab':'rapu','crow':'korppi',
'dog':'koira','dove':'kyyhky','eagle':'kotka','elephant':'elefantti',
'fly':'kärpänen','frog':'sammakko','giraffe':'kirahvi','goldfish':'kultakala',
'hamster':'hamsteri','horse':'hevonen','lion':'leijona','monkey':'apina',
'owl':'pöllö','pig':'sika','pigeon':'kyyhky','rabbit':'kani','rat':'rotta',
'shark':'hai','sheep':'lammas','snake':'käärme','spider':'hämähäkki',
'tiger':'tiikeri','wasp':'ampiainen'}

while True:
    sana = input("Anna englanninkielinen sana (quit lopettaa): ")
    if sana == "quit":
        break
    elif sana in sanasto:
        print(f"Sana {sana} on suomeksi {sanasto[sana]}")
    elif sana not in sanasto:
        print(f"Sanaa {sana} ei ole sanastossa.")
        sana_fin = input("Anna sen käännös suomeksi: ")
        sanasto[sana]=sana_fin



