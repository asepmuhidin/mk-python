list1= ['physics', 'chemistry', 1997, 2000];
list2= [1, 2, 3, 4, 5, 6, 7 ];
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list1[0]='Math'
print(list1)
del list1[3]
print(list1)

print("jumlah elemen list1 =",len(list1))
list3=list1+list2
print(list3)
list4=['hello']
print (list4*3)
print("kamu.."*10)

makanan=['bakwan','bakso','mie ayam','soto','seblak']

tanya=input("Silahkan input makanan yang anda suka ?")
cari=tanya in makanan
if(cari):
    print("Silahkan makan ", tanya)
else:
    print("Tidak ada di daftar menu")

print("Daftar menu kantin tini")
for menu in makanan:
    print (menu)   


