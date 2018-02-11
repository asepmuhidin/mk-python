makanan=['Pizza','Bakso','Cilok','Spageti','Chicken','Seblak']
lokal=['Bakso','Seblak','Cilok']
print("saya mau makan", makanan[3])
print("saya mau makan", makanan[1:4])

makanan[2]='Burger'
print("saya mau makan", makanan[1:4])

del makanan[1]
del makanan[4]
print(makanan)
print("saya punya ", len(makanan), " makanan")

semua_makanan=makanan+lokal
print(semua_makanan)

print("Hello "* 5)
print(lokal*3)

