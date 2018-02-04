from random import randint
angkaAcak=randint(1, 100)

benar=False
jumTebak=0

while(not benar):
    jawab=eval(input("Input tebakan anda :"))
    if(jawab>angkaAcak):
        pesan="Tebakan anda terlalu besar..!"
    elif(jawab<angkaAcak):
        pesan="Tebakan anda terlalu kecil"
    else:
        pesan="Horeee..tebakan benar"
        benar=True   
    jumTebak +=1         
    print(pesan)    

if(jumTebak>=10):
    level="Idiot"
elif(jumTebak>=5):
    level="Lumayan"
else:
    level="Jenius"

print("Level anda : ", level)        
