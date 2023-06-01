#Nama  : Dian Ardiyanti Saputri
#Npm   : G1A022084
#Kelas : B-Informatika
#Tugas2

#Nomor 1
#Implementasi Kelas Mahasiswa, Jurusan, dan Universitas
#Membuat kelas Mahasiswa dengan fungsi yang berisi atribut nama,nim,jurusan,alamat,email,nomor hp, dan tanggal lahir
class Mahasiswa: 
    def __init__(self, nama, nim, jurusan, alamat, email, noHp, tgl_lahir):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
        self.email = email
        self.noHp = noHp
        self.tgl_lahir = tgl_lahir

#Membuat fungsi untuk menampilkan atribut pada kelas Mahasiswa
    def tampilkan_info(self):
        print("--------------------------------------------")
        print("Nama         :", self.nama)
        print("NIM          :", self.nim)
        print("Jurusan      :", self.jurusan.NamaJurusan)
        print("Alamat       :", self.alamat)
        print("Email        :", self.email)
        print("Nomor Hp     :", self.noHp)
        print("Tanggal Lahir:", self.tgl_lahir)

#Membuat kelas Jurusan dengan fungsi yang berisi atribut nama jurusan
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = [] #Membuat atribut DaftarMahasiswa untuk menyimpan objek mahasiswa

#Membuat fungsi untuk menambahkan objek mahasiswa ke dalam atribut DaftarMahasiswa pada kelas Jurusan
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

#Menampilkan daftar mahasiswa pada kelas Jurusan dengan memanggil fungsi tampilkan_info pada kelas Mahasiswa
    def tampilkan_daftar_mahasiswa(self):
        print("\nDaftar Mahasiswa di Jurusan",self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            mahasiswa.tampilkan_info()

#Membuat kelas Fakultas dengan atribut nama fakultas
class Fakultas:
    def __init__(self, nama_Fakultas):
        self.NamaFakultas = nama_Fakultas

#Membuat kelas Universitas dengan fungsi yang berisi atribut nama universitas
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = [] #Membuat atribut DaftarJurusan untuk menyimpan objek jurusan
        self.DaftarFakultas = [] #Membuat atribut DaftarFakultas untuk menyimpan objek fakultas

#Membuat fungsi untuk menambahkan objek jurusan pada atribut DaftarJurusan yang ada pada kelas Universitas
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

#Menampilkan daftar jurusan pada kelas Universitas dengan memanggil atribut DaftarJurusan
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas",self.NamaUniversitas)
        print("--------------------------------------------")
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan) #Memanggil atribut NamaJurusan pada kelas Jurusan

#Membuat fungsi untuk menambahkan objek fakultas pada atribut DaftarFakultas yang ada pada kelas Universitas
    def tambah_fakultas(self, fakultas):
        self.DaftarFakultas.append(fakultas)
        
#Menampilkan daftar fakultas pada kelas Universitas dengan memanggil atribut DaftarFakultas
    def tampilkan_daftar_fakultas(self):
        print("\nDaftar Fakultas di Universitas",self.NamaUniversitas)
        print("--------------------------------------------")
        for fakultas in self.DaftarFakultas:
            print(fakultas.NamaFakultas) #Memanggil atribut NamaFakultas pada kelas Fakultas

#Nomor 2
#Membuat objek Universitas "XYZ University"
xyz_Universitas = Universitas("XYZ University")

#Nomor 3
#Membuat objek Jurusan "Teknik Informatika" dan menambahkannya ke dalam Universitas "XYZ University"
jur_TI = Jurusan("Teknik Informatika")
xyz_Universitas.tambah_jurusan(jur_TI)

#Membuat objek Fakultas "Fakultas Teknik" dan menambahkannya ke dalam Universitas "XYZ University"
fak_Teknik = Fakultas("Fakultas Teknik")
xyz_Universitas.tambah_fakultas(fak_Teknik)

#Nomor 4
#Membuat objek Mahasiswa dengan nama "Dian Ardiyanti Saputri", NIM "G1A022084", serta atribut lainnya dan menambahkannya ke dalam Jurusan "Teknik Informatika" di Universitas "XYZ University"
dianAr = Mahasiswa("Dian Ardiyanti Saputri", "G1A022084",jur_TI,"Jalan Air Sebakul Perumnas Alfatindo", "dianardiyantisaputri@gmail.com","08987654321","23 Januari 2004")
jur_TI.tambah_mahasiswa(dianAr)

#Nomor 5
#Menampilkan daftar jurusan yang ada di Universitas "XYZ University"
xyz_Universitas.tampilkan_daftar_jurusan()

#Menampilkan daftar fakultas yang ada di Universitas "XYZ University"
xyz_Universitas.tampilkan_daftar_fakultas()

#Nomor 6
#Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan "Teknik Informatika" di Universitas "XYZ University"
jur_TI.tampilkan_daftar_mahasiswa()

#Output
