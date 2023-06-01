#Nama  : Dian Ardiyanti Saputri
#Npm   : G1A022084
#Kelas : B-Informatika
#Tugas2

#Nomor 1
#Implementasi Kelas Mahasiswa, Jurusan, dan Universitas
#Membuat kelas Mahasiswa dengan fungsi yang berisi atribut nama,nim,jurusan,alamat,email,nomor hp, dan tanggal lahir
class Mahasiswa: 
    def __init__(self, nama, nim, jurusan, alamat, email, noHp, tgl_lahir):
    '''Mendefinisikan metode __init__ yang merupakan konstruktor kelas Mahasiswa. Konstruktor ini akan dipanggil saat membuat objek Mahasiswa baru. 
    Metode ini memiliki parameter self yang merujuk pada objek Mahasiswa itu sendiri, serta beberapa parameter lain yang akan digunakan untuk 
    menginisialisasi atribut-atribut objek Mahasiswa.'''
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
        self.email = email
        self.noHp = noHp
        self.tgl_lahir = tgl_lahir

#Membuat fungsi untuk menampilkan atribut pada kelas Mahasiswa
    def tampilkan_info(self):
    '''Mendefinisikan metode tampilkan_info yang akan menampilkan informasi atribut-atribut objek Mahasiswa.'''
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
    '''Mendefinisikan metode __init__ yang merupakan konstruktor kelas Jurusan. Metode ini akan dipanggil saat membuat objek Jurusan baru. 
    Metode ini memiliki parameter self yang merujuk pada objek Jurusan itu sendiri, serta parameter nama_jurusan yang akan digunakan untuk
    menginisialisasi atribut NamaJurusan pada objek Jurusan.'''
        self.NamaJurusan = nama_jurusan #Menginisialisasi atribut NamaJurusan pada objek Jurusan dengan nilai dari parameter nama_jurusan.
        self.DaftarMahasiswa = [] #Membuat atribut DaftarMahasiswa untuk menyimpan objek mahasiswa

#Membuat fungsi untuk menambahkan objek mahasiswa ke dalam atribut DaftarMahasiswa pada kelas Jurusan
    def tambah_mahasiswa(self, mahasiswa):
    '''Mendefinisikan metode tambah_mahasiswa yang akan menambahkan objek Mahasiswa ke dalam atribut DaftarMahasiswa pada objek Jurusan.'''
        self.DaftarMahasiswa.append(mahasiswa) #Menambahkan objek mahasiswa ke dalam list DaftarMahasiswa pada objek Jurusan.

#Menampilkan daftar mahasiswa pada kelas Jurusan dengan memanggil fungsi tampilkan_info pada kelas Mahasiswa
    def tampilkan_daftar_mahasiswa(self):
    '''Mendefinisikan metode tampilkan_daftar_mahasiswa yang akan menampilkan daftar mahasiswa dalam jurusan.'''
        print("\nDaftar Mahasiswa di Jurusan",self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa: #Melakukan iterasi untuk setiap objek Mahasiswa dalam list DaftarMahasiswa pada objek Jurusan.
            mahasiswa.tampilkan_info() #Memanggil metode tampilkan_info() pada objek Mahasiswa untuk menampilkan informasi mahasiswa.

#Membuat kelas Fakultas dengan atribut nama fakultas
class Fakultas:
    def __init__(self, nama_Fakultas):
    '''Mendefinisikan metode __init__ yang merupakan konstruktor kelas Fakultas. Metode ini memiliki parameter self yang merujuk pada objek 
    Fakultas itu sendiri, serta parameter nama_Fakultas yang akan digunakan untuk menginisialisasi atribut NamaFakultas pada objek Fakultas.'''
        self.NamaFakultas = nama_Fakultas #Menginisialisasi atribut NamaFakultas pada objek Fakultas dengan nilai dari parameter nama_Fakultas.

#Membuat kelas Universitas dengan fungsi yang berisi atribut nama universitas
class Universitas:
    def __init__(self, nama_universitas):
    '''Mendefinisikan metode __init__ yang merupakan konstruktor kelas Universitas. Metode ini memiliki parameter self yang merujuk pada objek 
    Universitas itu sendiri, serta parameter nama_universitas yang akan digunakan untuk menginisialisasi atribut NamaUniversitas pada objek Universitas.'''
        self.NamaUniversitas = nama_universitas #Menginisialisasi atribut NamaUniversitas pada objek Universitas dengan nilai dari parameter nama_universitas.
        self.DaftarJurusan = [] #Membuat atribut DaftarJurusan untuk menyimpan objek jurusan
        self.DaftarFakultas = [] #Membuat atribut DaftarFakultas untuk menyimpan objek fakultas

#Membuat fungsi untuk menambahkan objek jurusan pada atribut DaftarJurusan yang ada pada kelas Universitas
    def tambah_jurusan(self, jurusan):
    '''Mendefinisikan metode tambah_jurusan yang akan menambahkan objek Jurusan ke dalam atribut DaftarJurusan pada objek Universitas.'''
        self.DaftarJurusan.append(jurusan) #Menambahkan objek jurusan ke dalam list DaftarJurusan pada objek Universitas.

#Menampilkan daftar jurusan pada kelas Universitas dengan memanggil atribut DaftarJurusan
    def tampilkan_daftar_jurusan(self):
    '''Mendefinisikan metode tampilkan_daftar_jurusan yang akan menampilkan daftar jurusan dalam universitas.'''
        print("Daftar Jurusan di Universitas",self.NamaUniversitas)
        print("--------------------------------------------")
        for jurusan in self.DaftarJurusan: #Melakukan iterasi untuk setiap objek Jurusan dalam list DaftarJurusan pada objek Universitas.
            print(jurusan.NamaJurusan) #Memanggil atribut NamaJurusan pada kelas Jurusan

#Membuat fungsi untuk menambahkan objek fakultas pada atribut DaftarFakultas yang ada pada kelas Universitas
    def tambah_fakultas(self, fakultas):
    '''Mendefinisikan metode tambah_fakultas yang akan menambahkan objek Fakultas ke dalam atribut DaftarFakultas pada objek Universitas.''''
        self.DaftarFakultas.append(fakultas) #Menambahkan objek fakultas ke dalam list DaftarFakultas pada objek Universitas.
        
#Menampilkan daftar fakultas pada kelas Universitas dengan memanggil atribut DaftarFakultas
    def tampilkan_daftar_fakultas(self):
    '''Mendefinisikan metode tampilkan_daftar_fakultas yang akan menampilkan daftar fakultas dalam universitas.'''
        print("\nDaftar Fakultas di Universitas",self.NamaUniversitas)
        print("--------------------------------------------")
        for fakultas in self.DaftarFakultas: #Melakukan iterasi untuk setiap objek Fakultas dalam list DaftarFakultas pada objek Universitas.
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
Daftar Jurusan di Universitas XYZ University
--------------------------------------------
Teknik Informatika

Daftar Fakultas di Universitas XYZ University
--------------------------------------------
Fakultas Teknik

Daftar Mahasiswa di Jurusan Teknik Informatika
--------------------------------------------
Nama         : Dian Ardiyanti Saputri
NIM          : G1A022084
Jurusan      : Teknik Informatika
Alamat       : Jalan Air Sebakul Perumnas Alfatindo
Email        : dianardiyantisaputri@gmail.com
Nomor Hp     : 08987654321
Tanggal Lahir: 23 Januari 2004
