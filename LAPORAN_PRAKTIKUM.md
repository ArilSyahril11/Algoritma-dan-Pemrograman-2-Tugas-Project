

---

## PERTEMUAN 4 — Analisis Kompleksitas Algoritma (Big-O Intuitif)

### Tabel Perbandingan Iterasi (Wajib)

| n  | O(1) | O(n) ×1 | O(n) ×2 | O(n²)  |
|----|:----:|:-------:|:-------:|:------:|
| 5  | 1    | 5       | 10      | 25     |
| 10 | 1    | 10      | 20      | 100    |
| 20 | 1    | 20      | 40      | 400    |

### Kesimpulan (5–7 Kalimat)

Kompleksitas O(n) berarti jumlah operasi bertumbuh secara proporsional dengan ukuran input n; ketika n digandakan, waktu eksekusi ikut berlipat dua. Kompleksitas O(n²) tumbuh secara kuadratik: ketika n digandakan dari 10 ke 20, iterasi melonjak dari 100 menjadi 400 (empat kali lipat). Dua loop berurutan menghasilkan 2n iterasi namun tetap diklasifikasikan O(n) karena konstanta diabaikan dalam notasi asimtotik. Loop bersarang menghasilkan n×n = n² iterasi karena setiap elemen luar diproses bersama seluruh elemen dalam. Perbedaan antara O(n) dan O(n²) tampak kecil untuk n=5 (5 vs 25) namun menjadi sangat besar pada n=1.000 (1.000 vs 1.000.000 operasi). Linear Search O(n) jauh lebih efisien dari Nested Loop O(n²) terutama ketika pencarian dapat berhenti lebih awal (best case O(1)). Big-O mengukur pola pertumbuhan terburuk sehingga membantu memilih algoritma yang tepat sebelum membangun sistem berskala besar.

### Refleksi Pertemuan 4

**1. Mengapa O(n²) jauh lebih lambat ketika n besar?**

Saat n=1.000, O(n) memerlukan 1.000 operasi sedangkan O(n²) memerlukan 1.000.000 operasi — 1.000× lebih banyak. Saat n=10.000, selisihnya menjadi 10.000×. Pertumbuhan kuadratik menyebabkan algoritma menjadi tidak praktis dengan sangat cepat seiring bertambahnya data.

**2. Mengapa konstanta tidak diperhitungkan dalam Big-O?**

Big-O mengukur pola pertumbuhan asimtotik, bukan nilai absolut. Untuk n yang sangat besar, konstanta (2, 5, atau 100) menjadi tidak signifikan dibanding faktor pertumbuhan dominan. Misalnya 100n masih jauh lebih kecil dari n² saat n > 100.

**3. Mana yang lebih penting: kebenaran algoritma atau efisiensi?**

Kebenaran harus menjadi prioritas pertama — algoritma cepat namun salah tidak berguna. Namun efisiensi kritis untuk data berskala besar. Standar profesional: pastikan benar dulu, lalu optimalkan.

---

## PERTEMUAN 5 — Implementasi Linear Search dan Binary Search

### Tabel Perbandingan Langkah (Wajib)

| n      | Linear Search (worst) | Binary Search (worst) | Binary lebih cepat |
|--------|:---------------------:|:---------------------:|:-----------------:|
| 10     | 10                    | 4                     | ~2.5×             |
| 100    | 100                   | 7                     | ~14×              |
| 1.000  | 1.000                 | 10                    | ~100×             |
| 10.000 | 10.000                | 14                    | ~714×             |

### Kesimpulan (5–7 Kalimat)

Linear Search menelusuri setiap elemen dari awal hingga akhir tanpa memerlukan data terurut, menjadikannya fleksibel namun tidak efisien untuk dataset besar dengan kompleksitas O(n). Binary Search membagi ruang pencarian menjadi dua setiap iterasi sehingga hanya memerlukan sekitar log₂(n) langkah — untuk satu juta data hanya ~20 langkah. Syarat mutlak Binary Search adalah data harus terurut; pelanggaran syarat ini menghasilkan jawaban yang salah atau tidak konsisten karena asumsi pembagian ruang pencarian tidak berlaku. Pengujian pada data [4,8,15,16,23,42] menunjukkan Linear Search memerlukan 6 langkah untuk worst case sedangkan Binary Search hanya 3 langkah pada dataset yang sama. Untuk pencarian berulang pada dataset besar yang sudah terurut, Binary Search adalah pilihan yang jauh lebih unggul. Namun jika data belum terurut, biaya pengurutan O(n log n) harus dipertimbangkan sebelum memutuskan menggunakan Binary Search. Linear Search lebih tepat untuk data kecil, data tidak terurut, atau pencarian yang hanya dilakukan satu kali.

### Refleksi Pertemuan 5

**Challenge — Binary Search pada data tidak terurut:**

Binary Search gagal pada data acak karena ia membuang setengah ruang pencarian berdasarkan perbandingan data[mid] dengan target, dengan asumsi bahwa semua elemen di satu sisi lebih besar dan sisi lain lebih kecil. Pada data acak, asumsi ini tidak berlaku — target yang sebenarnya ada bisa berada di bagian yang sudah dibuang. Hasilnya: Binary Search mengembalikan "tidak ditemukan" meskipun target ada, atau mengembalikan indeks yang salah.

---

## PERTEMUAN 6 — Implementasi Sorting Dasar

### Tabel Perbandingan Jumlah Perbandingan (Wajib)

| Jumlah Data | Bubble Sort | Selection Sort | Insertion Sort |
|:-----------:|:-----------:|:--------------:|:--------------:|
| 6           | ~9          | 15             | ~7             |
| 10          | ~39         | 45             | ~24            |
| 20          | ~190        | 190            | ~107           |

### Perbandingan Berdasarkan Jenis Data (n=10)

| Jenis Data            | Bubble | Selection | Insertion |
|-----------------------|:------:|:---------:|:---------:|
| Data Acak             | ~39    | 45        | ~24       |
| Data Terurut (best)   | 9      | 45        | **9**     |
| Data Terbalik (worst) | 45     | 45        | 45        |
| Hampir Terurut        | ~39    | 45        | **~15**   |

### Kesimpulan (5–7 Kalimat)

Ketiga algoritma memiliki kompleksitas worst case O(n²) namun menunjukkan perilaku berbeda tergantung kondisi data. Bubble Sort membandingkan dan menukar pasangan bersebelahan secara berulang; mudah dipahami tetapi relatif lambat karena banyak operasi swap. Selection Sort selalu melakukan n*(n-1)/2 perbandingan tanpa peduli kondisi data — konsisten tetapi tidak adaptif; keunggulannya adalah meminimalkan jumlah swap (≤ n-1). Insertion Sort adalah pilihan terbaik untuk data hampir terurut karena bersifat adaptif: elemen yang sudah di posisi tepat tidak disentuh sehingga kompleksitasnya mendekati O(n). Untuk data acak, ketiga algoritma setara dalam orde O(n²) meskipun koefisiennya berbeda. Dalam praktik produksi, Python menggunakan TimSort yang menggabungkan Insertion Sort dan Merge Sort menghasilkan O(n log n). Pemilihan algoritma harus mempertimbangkan ukuran data, kondisi awal data, dan batasan memori yang tersedia.

### Refleksi Pertemuan 6

**1. Mana paling sedikit perbandingan untuk data acak?**
Insertion Sort secara rata-rata melakukan lebih sedikit perbandingan dari Bubble Sort pada data acak karena proses sisipan berhenti begitu posisi tepat ditemukan, tidak harus menyelesaikan seluruh sub-array.

**2. Mana paling stabil pada data hampir terurut?**
Insertion Sort — karena hanya elemen yang salah posisi yang dipindahkan. Pada data hampir terurut, hanya sedikit shift yang diperlukan sehingga mendekati O(n).

**Challenge — Insertion Sort (n=20):**

| Kondisi Data      | Perbandingan | Shift |
|-------------------|:------------:|:-----:|
| Terurut (best)    | 19           | **0** |
| Hampir Terurut    | ~44          | ~25   |
| Data Acak (avg)   | ~83          | ~66   |
| Terbalik (worst)  | 190          | 190   |

---

## PERTEMUAN 7 — Integrasi Searching, Sorting, dan Modular Programming

### Analisis Kompleksitas (≥5 Kalimat)

Sistem Pengolahan Nilai Mahasiswa mengintegrasikan seluruh konsep dari pertemuan 1 hingga 6 dalam satu pipeline algoritma yang utuh. Kompleksitas total sistem ditentukan oleh komponen dengan kompleksitas tertinggi, yaitu fungsi sorting (Bubble Sort atau Insertion Sort) yang beroperasi pada O(n²) — sehingga kompleksitas keseluruhan sistem adalah O(n²). Fungsi-fungsi lain seperti input_data(), hitung_nilai(), linear_search(), dan tampilkan_data() bersifat linear O(n) dan diabaikan dalam analisis asimtotik karena O(n²) + O(n) = O(n²). Setelah data diurutkan oleh sorting, Binary Search dapat dimanfaatkan untuk pencarian nilai dengan hanya O(log n) langkah — strategi terbaik adalah melakukan sorting satu kali di awal kemudian menggunakan Binary Search untuk semua pencarian berikutnya. Untuk sistem nyata dengan ribuan mahasiswa, sorting O(n²) harus diganti dengan algoritma O(n log n) seperti Merge Sort atau TimSort agar performa tetap dapat diterima. Penggunaan modular programming memastikan setiap komponen dapat diuji, dioptimalkan, dan diganti secara independen tanpa mengganggu keseluruhan sistem.

### Tabel Kompleksitas Seluruh Fungsi

| Fungsi                    | Kompleksitas | Keterangan                         |
|---------------------------|:------------:|------------------------------------|
| `input_data_mahasiswa()`  | O(n)         | Loop input n mahasiswa             |
| `hitung_nilai()`          | O(n)         | Loop kalkulasi n mahasiswa         |
| `bubble_sort_desc()`      | O(n²)        | Loop bersarang, worst case         |
| `insertion_sort_desc()`   | O(n²)        | Loop + while, worst case           |
| `linear_search()`         | O(n)         | Telusuri satu per satu by nama     |
| `binary_search_nilai()`   | O(log n)     | Bagi dua ruang pencarian           |
| `tampilkan_data()`        | O(n)         | Cetak n baris output               |
| `tampilkan_statistik()`   | O(n)         | Scan nilai min/max/rata-rata       |
| **TOTAL DOMINAN**         | **O(n²)**    | Didominasi oleh komponen sorting   |

### Challenge — Bubble Sort vs Insertion Sort (n=8)

| Metrik              | Bubble Sort | Insertion Sort | Pemenang             |
|---------------------|:-----------:|:--------------:|----------------------|
| Perbandingan        | 28          | **19**         | Insertion Sort       |
| Swap / Shift        | 14          | 14             | Seri                 |

**Algoritma mana yang lebih efisien untuk data kecil?**

Insertion Sort lebih efisien untuk data kecil (n < 20) karena tiga alasan: pertama, Insertion Sort berhenti lebih awal per elemen begitu posisi sisipan ditemukan, sementara Bubble Sort harus menyelesaikan seluruh pass meskipun sudah optimal. Kedua, jumlah perbandingan Insertion Sort sama dengan jumlah inversions dalam data — semakin sedikit inversions (data hampir terurut), semakin cepat. Ketiga, Bubble Sort melakukan swap berulang untuk memindahkan satu elemen ke posisi akhirnya, sedangkan Insertion Sort melakukannya dengan satu operasi sisipan. Secara asimtotik keduanya O(n²), namun untuk data kecil konstanta dan koefisien Insertion Sort lebih kecil sehingga unggul secara praktis.

### Refleksi Pertemuan 7

**Strategi Eksekusi UTS (dari Blueprint Pertemuan 7):**
1. Baca Cermat — Pahami spesifikasi dan batasan masalah
2. Identifikasi Tipe — Apakah rekursi, searching, atau sorting?
3. Pilih Algoritma — Sesuaikan dengan kondisi data
4. Analisis Kompleksitas — Hitung efisiensi Big-O
5. Implementasi Modular — Tulis kode terstruktur dan terpecah

**Pelajaran kunci dari integrasi:**
Sebuah sistem yang baik bukan hanya sistem yang benar, tetapi sistem yang dirancang dengan arsitektur jelas, setiap komponen terisolasi dan dapat diuji secara mandiri, serta pilihan algoritma didasarkan pada analisis kompleksitas yang tepat — bukan sekadar "yang pertama terpikirkan".
