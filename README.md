# TUGAS-2-PBO
TUGAS 2 PBO Membuat Kelas Mahasiswa, Jurusan, Fakultas, dan Universitas

Nama  : Dian Ardiyanti Saputri

Npm   : G1A022084

Tugas 2 PBO

# **Deskripsi Tentang Kode Program**
Program tersebut merupakan implementasi dari konsep pemrograman berorientasi objek pada bahasa Python untuk mengelola data mahasiswa di sebuah universitas. Program terdiri dari tiga kelas objek yang saling terhubung, yaitu Mahasiswa, Jurusan, dan Universitas. Pada kode program ini dikembangkan lagi satu kelas dengan nama kelas Fakultas untuk menambahkan data fakultas pada sebuah universitas.

# **Kelas Mahasiswa**
Kelas Mahasiswa memiliki beberapa atribut seperti nama, nim, jurusan, alamat, email, nomor hp, dan tanggal lahir yang dipanggil atau di set pada fungsi __init__. Kemudian, terdapat fungsi tampilkan_info untuk menampilkan atribut-atribut tersebut. Hal ini sesuai dengan perintah pada soal. Kelas Mahasiswa digunakan untuk menyimpan data dari mahasiswa yang akan ditambahkan.

# **Kelas Jurusan**
Kelas Jurusan memiliki atribut nama jurusan dan DaftarMahasiswa untuk menyimpan objek mahasiswa pada jurusan tersebut. Terdapat fungsi tambah_mahasiswa untuk menambahkan objek mahasiswa ke dalam atribut DaftarMahasiswa dan fungsi tampilkan_daftar_mahasiswa untuk menampilkan daftar mahasiswa pada jurusan tersebut. Tujuan dari kelas jurusan adalah membantu mengelola program dan aktivitas yang terkait dengan jurusan tertentu. Kelas jurusan membantu meningkatkan efisiensi dan efektivitas program dan aktivitas, sambil memfasilitasi komunikasi dan kolaborasi di antara staf dan mahasiswa.

# **Kelas Fakultas**
Kelas Fakultas hanya memiliki atribut nama fakultas. Kelas fakultas biasanya dibuat dalam struktur universitas untuk mengorganisir kumpulan program studi atau departemen akademik yang terkait. Tujuan dari kelas fakultas adalah untuk mempermudah manajemen universitas dalam mengatur dan mengawasi program studi, penelitian, dan kegiatan lainnya yang terkait dengan fakultas tersebut. Dengan demikian, kelas fakultas dapat membantu universitas untuk meningkatkan efisiensi dan efektivitas operasional serta meningkatkan kualitas pendidikan dan penelitian yang diselenggarakan. Selain itu, kelas fakultas juga membantu dalam memfasilitasi komunikasi dan kolaborasi antara anggota fakultas dan staf akademik dengan mahasiswa dan pihak luar.

# **Kelas Universitas**
Kelas Universitas memiliki atribut nama universitas, DaftarJurusan untuk menyimpan objek jurusan, dan DaftarFakultas untuk menyimpan objek fakultas. Terdapat fungsi tambah_jurusan untuk menambahkan objek jurusan ke dalam atribut DaftarJurusan dan fungsi tampilkan_daftar_jurusan untuk menampilkan daftar jurusan pada universitas tersebut. Selain itu, terdapat fungsi tambah_fakultas untuk menambahkan objek fakultas ke dalam atribut DaftarFakultas dan fungsi tampilkan_daftar_fakultas untuk menampilkan daftar fakultas pada universitas tersebut. Tujuan dari kelas universitas adalah mengelola program dan aktivitas universitas secara keseluruhan. Kelas universitas membantu meningkatkan efisiensi dan efektivitas program dan aktivitas, sambil memfasilitasi komunikasi dan kolaborasi di antara staf dan mahasiswa. Kelas universitas juga membantu mengembangkan keterampilan belajar dan keterampilan karir, serta meningkatkan inklusi dan keragaman di antara mahasiswa.

# **Implementasi dari Kode Program**
Tujuan dari implementasi kode program ini adalah untuk membuat objek Universitas, Jurusan, Fakultas, dan Mahasiswa serta menambahkannya ke dalam hierarki yang sesuai. Pada nomor 2, objek Universitas "XYZ University" dibuat. Pada nomor 3, objek Jurusan "Teknik Informatika" dibuat dan ditambahkan ke dalam objek Universitas "XYZ University". Objek Fakultas "Fakultas Teknik" juga dibuat dan ditambahkan ke dalam objek Universitas "XYZ University". Pada nomor 4, objek Mahasiswa dengan nama "Dian Ardiyanti Saputri" dibuat dan ditambahkan ke dalam objek Jurusan "Teknik Informatika" di Universitas "XYZ University". Pada nomor 5 dan 6, daftar jurusan, fakultas, dan mahasiswa ditampilkan sesuai dengan hierarki yang telah dibuat sebelumnya.
