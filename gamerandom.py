from random import randint

bilAcak=randint(1,100)
benar=False
nJawab=0

while (not benar):
    jawab=eval(input("Tebakan anda ?"))
    if (jawab>bilAcak):
        msg="Tebakan anda terlalu besar..."
        nJawab +=1
    elif(jawab<bilAcak):
        msg="Tebakan anda terlalu kecil..."
        nJawab+=1
    else :
        benar=True
        msg="Horeee...anda berhasil menebak"

    print(msg)

print("Anda menjawab sebanyak :", nJawab)            
if (nJawab>=10) :
    status="Idiot"
elif(nJawab>=5):
    status="Lumayan"
else:
    status="Jenius"

print("Anda orang ", status)        