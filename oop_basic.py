class Karyawan:
    ''' Ini kelas karyawan, untuk deskripsi bla..bla  '''
    jum_karyawan=0
    
    def __init__(self,nama,nik,gapok,kartap,jamLembur):
        self.nama=nama
        self.nik=nik
        self.gapok=gapok
        self.kartap=kartap
        self.jamLembur=jamLembur
        Karyawan.jum_karyawan +=1
       
    def uang_lembur(self):
        return (self.jamLembur*self.gapok)/173

    def bonus(self):
        if(self.kartap):
            return self.gapok*3
        else:
            return 0

rafi=Karyawan('Rafi','001',1000,False,10)  ## Proses instansiasi objek rafi dari instance kelas karyawan
lili=Karyawan('Lili','002',1000,True,20)

print("NIK :",rafi.nik)
print("Nama :",rafi.nama)
print("Gaji Pokok :",rafi.gapok)

print("Kartap :","Iya" if rafi.kartap else "Bukan")

print("NIK :",lili.nik)
print("Nama :",lili.nama)
print("Gaji Pokok :",lili.gapok)

print("Kartap :","Iya" if lili.kartap else "Bukan")
print("Uang Lembur :",lili.uang_lembur())
print("Uang Bonus :",lili.bonus())

print("Uang Lembur :",rafi.uang_lembur())
print("Uang Bonus :",rafi.bonus())



print("Jumlah karyawan:", Karyawan.jum_karyawan)
