from urllib.request import urlopen
url = "https://www.mit.edu/~ecprice/wordlist.10000"
teksti = urlopen(url).read().decode("UTF-8")

merkit={}
for sana in teksti:
    for merkki in sana:
        if merkki not in merkit:
            merkit[merkki]= 0
        merkit[merkki] +=1

aakkoset=sorted(merkit.items())
for avain, arvo in aakkoset:
    if avain.isalpha():
        print(f"Aakkonen {avain} löytyi {arvo} kertaa.")