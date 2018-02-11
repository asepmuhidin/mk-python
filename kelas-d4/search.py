artis=['Natasya','Nikita','Sugara','Ariel','Ari','Aura','Eko']

nama_artis=input("Masukan artis idola anda :")

ketemu=nama_artis in artis

if(ketemu):
    print(nama_artis , " adalah artis terkenal")
else:
    print(nama_artis , " adalah artis kampungan")

print("-"* 15)

for nama_artis in artis:
    print(artis.index(nama_artis)+1,".",nama_artis)

print("-"* 15)    