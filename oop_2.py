class Karyawan:
    ''' Ini kelas karyawan '''
    
    def __init__(self,nama,gapok,lembur,kartap):
        self.nama=nama
        self.gapok=gapok
        self.lembur=lembur
        self.kartap=kartap
    
    def uang_lembur(self):
        return (self.lembur*self.gapok)/173
    
    def bonus(self):  
        if(self.kartap):
            return self.gapok*3
        else:
            return 0
    def total(self):
        return self.gapok+self.uang_lembur()+self.bonus()
    
karyawan1=Karyawan('Khoerunnisa',1000,10,True)
print("Deskripsi kelas :", Karyawan.__doc__)
print("Nama :", karyawan1.nama)
print("Gaji Pokok :", karyawan1.gapok)
print("Lembur (jam) :", karyawan1.lembur)
print("Status Karyawan :", "Tetap" if karyawan1.kartap else "Kontrak")
print("Uang Lembur :", karyawan1.uang_lembur())
print("Bonus :", karyawan1.bonus())
print("Total THP :", karyawan1.total())
