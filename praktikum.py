import os
class Mahasiswa:

  def __init__(self):
    self.nama = []
    self.nim = []
    self.nilai_tugas = []
    self.nilai_uts = []
    self.nilai_uas = []
    self.nilai_akhir = []

  def tambah_data(self):
    nama = input('nama: ')
    self.nama.append(nama)
    nim = int(input('nim: '))
    self.nim.append(nim)
    nilai_tugas = int(input('nilai tugas: '))
    self.nilai_tugas.append(nilai_tugas)
    nilai_uts = int(input('nilai uts: '))
    self.nilai_uts.append(nilai_uts)
    nilai_uas = int(input('nilai uas: '))
    self.nilai_uas.append(nilai_uas)
    nilai_akhir = nilai_tugas * .3 + nilai_uts * .35 + nilai_uas * .35
    self.nilai_akhir.append(nilai_akhir) 
    os.system("cls")

  def tampil_data(self):
      for i, data in enumerate(self.nama):
        print(f"data ke-{i+1}")
        print(f"Nama Mahasiswa: {self.nama[i]}")
        print(f"NIM Mahasiswa : {self.nim[i]}")
        print(f"Nilai Tugas   : {self.nilai_tugas[i]}")
        print(f"Nilai UTS     : {self.nilai_uts[i]}")
        print(f"Nilai UAS     : {self.nilai_uas[i]}")
        print(f"Nilai Akhir   : {self.nilai_akhir[i]}")
        print("======================================")

  def ubah_data(self, nama):
    if nama in self.nama:
      index = self.nama.index(nama)
      self.nim[index] = int(input("NIM : "))
      self.nilai_tugas[index] = int(input("Nilai Tugas : "))
      self.nilai_uts[index] = int(input("Nilai UTS : "))
      self.nilai_uas[index] = int(input("Nilai UAS : "))
      self.nilai_akhir[index] = self.nilai_tugas[index] * .3 + self.nilai_uts[index] * .35 + self.nilai_uas[index] * .35
      os.system("cls")

  def hapus_data(self, nama):
    if nama in self.nama:
      index = self.nama.index(nama)
      del self.nama[index]
      del self.nim[index]
      del self.nilai_tugas[index]
      del self.nilai_uts[index]
      del self.nilai_uas[index]
      del self.nilai_akhir[index]


data = Mahasiswa()
# print(data.__dict__)
# data.tambah_data()
# data.tambah_data()
# print(data.__dict__)
# data.ubah_data("daffa", 0)
# print(data.__dict__)
# data.hapus_data("daffa", 0)
# print(data.__dict__)
# data.tampil_data()

while True:
  user = input("(T)ambah Data (U)bah Data (H)apus Data (L)ihat Data (K)eluar: ")
  if user.lower() == "t":
    os.system("cls")
    data.tambah_data()
  elif user.lower() == "u":
    nama = input("Masukkan nama : ")
    if nama in data.nama:
      os.system("cls")
      print("nama tersedia, silahkan ubah")
      data.ubah_data(nama)
    else:
      os.system("cls")
      print(f"{nama} tidak ada atau belum diinputkan")
  elif user.lower() == "h":
    os.system("cls")
    nama = input("Masukkan nama : ")
    if nama in data.nama:
      print("nama tersedia, data telah terhapus")
      data.hapus_data(nama)
    else:
      os.system("cls")
      print(f"{nama} tidak ada atau belum diinputkan")
  elif user.lower() == "l":
    if data.nama:
      os.system("cls")
      data.tampil_data()
    else:
      os.system("cls")
      print("tidak ada data")
  elif user.lower() == "k":
    os.system("cls")
    break