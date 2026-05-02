# LAPORAN PRAKTIKUM — Algoritma dan Pemrograman 2
# Pertemuan 1, 2, dan 3 | STTPA

---

## PERTEMUAN 1 — Implementasi Algoritma Berbasis IPO dalam Python

### Alur Logika Program (5–7 Kalimat)

Program diskon menerima satu input berupa total belanja dalam bentuk float.
Nilai tersebut kemudian diperiksa menggunakan struktur kondisional if-elif-else
untuk menentukan persentase diskon yang sesuai: 20% jika belanja >= 500.000,
10% jika >= 250.000, dan 0% jika di bawah 250.000.
Setelah persentase ditentukan, nominal diskon dihitung lalu dikurangi dari
total belanja untuk menghasilkan total yang harus dibayar.
Hasilnya kemudian ditampilkan ke layar sebagai output akhir program.
Program juga dilengkapi validasi untuk mencegah input berupa angka negatif.

---

### Refleksi Pertemuan 1

**1. Apa perbedaan langsung coding vs analisis IPO terlebih dahulu?**

Langsung coding cenderung menghasilkan *spaghetti code* — kode yang panjang,
tidak terstruktur, dan sulit di-debug karena logika bercampur tanpa arah yang
jelas. Ketika ada kesalahan logika di awal, seluruh kode harus dirombak total.

Sebaliknya, analisis IPO terlebih dahulu memaksa kita berpikir sistematis:
  - INPUT   : data apa yang dibutuhkan?
  - PROCESS : transformasi logika apa yang terjadi?
  - OUTPUT  : hasil apa yang diharapkan?

Dengan blueprint IPO, proses coding menjadi lebih cepat, lebih terarah, dan
hasil akhirnya mudah diverifikasi karena setiap bagian sudah jelas tujuannya.
Prinsip utamanya: **Think First, Code Later.**

**2. Mengapa urutan kondisi pada if–elif penting?**

Python mengevaluasi kondisi if-elif secara berurutan dari atas ke bawah dan
berhenti pada kondisi pertama yang bernilai True. Jika urutan terbalik
(misal: cek >= 250.000 sebelum >= 500.000), maka belanja sebesar 600.000
akan jatuh ke blok 10% karena >= 250.000 juga benar untuk 600.000.
Urutan dari kondisi yang paling ketat (nilai besar) ke yang lebih longgar
memastikan setiap nilai dievaluasi dengan benar.

---

## PERTEMUAN 2 — Implementasi Modular Programming dalam Python

### Penjelasan Pembagian Fungsi (5–7 Kalimat)

Program nilai akhir mahasiswa dipecah menjadi lima fungsi yang masing-masing
memiliki satu tanggung jawab tunggal (Single Responsibility Principle).
Fungsi `input_nilai()` bertugas hanya menerima dan mengembalikan data dari
pengguna tanpa melakukan kalkulasi apapun.
Fungsi `validasi_nilai()` memisahkan logika validasi sehingga dapat digunakan
ulang (reusable) tanpa duplikasi kode.
Fungsi `hitung_nilai()` hanya mengerjakan kalkulasi matematis berbobot dan
mengembalikan hasilnya, menjaga agar logika bisnis terisolasi.
Fungsi `tentukan_grade()` memastikan logika penentuan huruf mudah diubah tanpa
mempengaruhi bagian lain dari program.
Fungsi `tampilkan_hasil()` memisahkan lapisan presentasi dari kalkulasi,
sehingga format output bisa diubah tanpa menyentuh logika perhitungan.
Arsitektur modular ini membuat program lebih mudah dibaca, diuji per-fungsi,
dan dikembangkan di masa depan.

---

### Refleksi Pertemuan 2

**1. Apa keuntungan modular programming dibanding program monolitik?**

| Aspek         | Monolitik                    | Modular                           |
|---------------|------------------------------|-----------------------------------|
| Keterbacaan   | Sulit dinavigasi             | Terstruktur & rapi                |
| Debugging     | Satu error merusak sistem    | Diuji per-fungsi secara terpisah  |
| Reusability   | Tulis ulang tiap dibutuhkan  | Fungsi dipanggil berkali-kali     |
| Pengembangan  | Tambah fitur = risiko tinggi | Tambah fungsi tanpa ganggu sistem |

**2. Apa yang terjadi jika satu fungsi terlalu banyak tanggung jawab?**

Fungsi yang melakukan banyak tugas sekaligus (God Function) melanggar
prinsip Single Responsibility dan menyebabkan berbagai masalah:
  - Sulit diuji karena tidak bisa di-test secara terpisah
  - Sulit dibaca karena alur logika bercampur
  - Satu perubahan kecil berisiko merusak banyak fitur sekaligus
  - Tidak bisa dipakai ulang di konteks yang berbeda
Solusinya: setiap fungsi harus mengerjakan tepat satu tugas logis.

---

## PERTEMUAN 3 — Implementasi Rekursi dan Perbandingan dengan Iterasi

### Penjelasan Perbandingan Rekursi dan Iterasi (5–7 Kalimat)

Rekursi adalah teknik di mana fungsi memanggil dirinya sendiri untuk
menyelesaikan versi yang lebih kecil dari masalah yang sama, dan memerlukan
dua komponen wajib: Base Case (kondisi berhenti) dan Recursive Case
(pemanggilan diri dengan parameter yang mengecil).
Iterasi menggunakan struktur perulangan (for/while) yang memperbarui variabel
lokal secara berurutan tanpa membuat tumpukan memori baru.
Dari sisi memori, rekursi lebih boros karena setiap pemanggilan fungsi
membuat frame baru di Call Stack, sementara iterasi hanya membutuhkan satu
blok memori yang diperbarui terus-menerus.
Dari sisi keterbacaan, rekursi lebih elegan untuk masalah yang secara alami
bersifat rekursif seperti Fibonacci atau traversal pohon.
Sebaliknya, untuk komputasi linear seperti faktorial atau penjumlahan 1..n,
iterasi lebih efisien dan lebih aman karena tidak berisiko Stack Overflow.
Kesimpulan: pilih rekursi saat masalah memiliki struktur sub-masalah yang
identik (pohon, Divide and Conquer), dan pilih iterasi untuk performa optimal.

---

### Refleksi Pertemuan 3

**1. Mengapa base case sangat penting?**

Base case adalah "jangkar" yang menghentikan rantai pemanggilan rekursif.
Tanpa base case yang benar, fungsi akan memanggil dirinya terus-menerus
(infinite recursion) hingga memori Call Stack penuh dan program crash dengan
error RecursionError / Stack Overflow. Base case harus dapat dicapai dan
mengembalikan nilai tanpa pemanggilan rekursif lagi.

**2. Mengapa fibonacci rekursif lebih lambat dari faktorial rekursif?**

Faktorial adalah rekursi linear — setiap langkah hanya menghasilkan SATU
pemanggilan rekursif baru, sehingga total pemanggilan = n kali (O(n)).

Fibonacci adalah rekursi bercabang — setiap langkah menghasilkan DUA
pemanggilan rekursif, membentuk pohon eksponensial. Lebih parahnya,
sub-masalah yang sama dihitung berulang-ulang (overlapping subproblems):
  fibonacci(5) → fibonacci(3) dihitung 2 kali, fibonacci(2) dihitung 3 kali
Total pemanggilan fibonacci(n) mencapai O(2^n) — sangat lambat untuk n besar.

**3. Dalam kondisi apa rekursi lebih tepat digunakan?**

Rekursi paling tepat digunakan ketika:
  a) Masalah secara alami terdefinisi secara rekursif (faktorial, Fibonacci)
  b) Masalah memiliki struktur pohon atau data bercabang (traversal, direktori)
  c) Mengimplementasikan algoritma Divide and Conquer (Merge Sort, Quick Sort)
  d) Kode yang lebih ekspresif dan ringkas lebih diprioritaskan daripada
     efisiensi memori mentah
