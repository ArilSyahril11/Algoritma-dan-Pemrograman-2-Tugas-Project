# 📘 Algoritma dan Pemrograman 2 — STTPA
## Kumpulan Tugas Praktikum Lengkap (Pertemuan 1–7)

**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Algoritma dan Pemrograman 2  
**Dosen:** Yudi Herdiana, S.T., M.T.  
**Semester:** Genap 2026

---

## 📁 Struktur File

```
Alpro2_Praktikum/
│
├── Pertemuan1/
│   ├── p1_diskon.py                    ← Latihan 1: Kalkulator Diskon
│   ├── p1_nilai_mahasiswa.py           ← Latihan 2: Nilai Akhir + Validasi
│   └── p1_konversi_suhu.py             ← Challenge: Konversi Suhu
│
├── Pertemuan2/
│   ├── p2_nilai_modular.py             ← Latihan 1: Nilai Mahasiswa (5 Fungsi Modular)
│   └── p2_bangun_datar.py              ← Latihan 2+Challenge: Bangun Datar Modular
│
├── Pertemuan3/
│   └── p3_rekursi_iterasi.py           ← Faktorial, Jumlah, Fibonacci, Pangkat + Trace
│
├── Pertemuan4/
│   └── p4_big_o_analysis.py            ← O(1), O(n), O(n²) + Tabel Iterasi + Uji Waktu
│
├── Pertemuan5/
│   └── p5_searching.py                 ← Linear Search + Binary Search + Trace + Challenge
│
├── Pertemuan6/
│   └── p6_sorting.py                   ← Bubble + Selection + Insertion Sort + Challenge
│
├── Pertemuan7/
│   └── p7_sistem_nilai_terintegrasi.py ← Sistem Integrasi Lengkap (Simulasi UTS)
│
├── LAPORAN_PRAKTIKUM.md                ← Laporan & Refleksi Lengkap Pertemuan 1–7
└── README.md                           ← File ini
```

---

## 🗂️ Ringkasan Per Pertemuan

---

### Pertemuan 1 — Implementasi Algoritma Berbasis IPO

**Topik:** Kerangka IPO (Input–Process–Output), Pseudocode → Python

| File | Topik | Konsep Utama |
|------|-------|--------------|
| `p1_diskon.py` | Kalkulator diskon belanja | `if-elif-else`, validasi input |
| `p1_nilai_mahasiswa.py` | Nilai akhir berbobot | Rumus berbobot, validasi range 0–100 |
| `p1_konversi_suhu.py` | Konversi °C → °F & Kelvin | Rumus matematika, tabel output |

**Aturan Diskon:** ≥Rp500rb → 20% | ≥Rp250rb → 10% | lainnya → 0%

> **Prinsip:** *Think First, Code Later* — analisis IPO sebelum menulis kode.

---

### Pertemuan 2 — Modular Programming

**Topik:** Dekomposisi, Single Responsibility, Return Value

**Fungsi `p2_nilai_modular.py`:** `input_nilai()` → `validasi_nilai()` → `hitung_nilai()` → `tentukan_grade()` → `tampilkan_hasil()`

**4 Prinsip Emas:** Single Responsibility · Reusability · Readability · Maintainability

---

### Pertemuan 3 — Rekursi vs Iterasi

**Topik:** Base Case, Recursive Case, Call Stack, Overlapping Subproblems

| Fungsi | Rekursif | Iteratif | Kompleksitas Rekursif |
|--------|:--------:|:--------:|----------------------|
| `faktorial(n)` | ✓ | ✓ | O(n) — linear |
| `jumlah(n)` | ✓ | ✓ | O(n) |
| `fibonacci(n)` | ✓ | ✓ | O(2ⁿ) — bercabang dua |
| `pangkat(a,n)` | ✓ | — | O(n) |

> **Bahaya:** Tanpa Base Case → Infinite Recursion → Stack Overflow

---

### Pertemuan 4 — Analisis Kompleksitas Algoritma (Big-O)

**Topik:** O(1), O(n), O(n²), Aturan Big-O, Menghitung Iterasi Aktual

**Tabel Iterasi Wajib:**

| n | O(1) | O(n) | O(n) ×2 | O(n²) | Rasio n²/n |
|:-:|:----:|:----:|:-------:|:-----:|:----------:|
| 5 | 1 | 5 | 10 | 25 | 5× |
| 10 | 1 | 10 | 20 | 100 | 10× |
| 20 | 1 | 20 | 40 | 400 | 20× |

**Aturan:** Konstanta diabaikan · Loop berurutan tetap O(n) · Loop bersarang = O(n²)

---

### Pertemuan 5 — Linear Search dan Binary Search

**Topik:** O(n) vs O(log n), Syarat Binary Search

| Algoritma | Kompleksitas | Syarat Data |
|-----------|:------------:|-------------|
| Linear Search | O(n) | Bebas |
| Binary Search | O(log n) | **WAJIB terurut** |

**Tabel Perbandingan Langkah (Worst Case):**

| n | Linear | Binary | Selisih |
|:-:|:------:|:------:|:-------:|
| 100 | 100 | 7 | ~14× |
| 1.000 | 1.000 | 10 | ~100× |
| 10.000 | 10.000 | 14 | ~714× |

> **Challenge:** Binary Search pada data tidak terurut → hasil **tidak dapat dipercaya**.

---

### Pertemuan 6 — Sorting Dasar

**Topik:** Bubble Sort, Selection Sort, Insertion Sort

**Tabel Perbandingan (Data Acak):**

| n | Bubble (comp) | Selection (comp) | Insertion (comp) |
|:-:|:-------------:|:----------------:|:----------------:|
| 6 | ~9 | 15 | ~7 |
| 10 | ~39 | 45 | ~24 |
| 20 | ~190 | 190 | ~107 |

**Kompleksitas:**

| Algoritma | Best | Worst | Keunggulan |
|-----------|:----:|:-----:|------------|
| Bubble Sort | O(n) | O(n²) | Mudah dipahami |
| Selection Sort | O(n²) | O(n²) | Jumlah swap minimum |
| Insertion Sort | **O(n)** | O(n²) | Terbaik untuk data hampir terurut |

> **Challenge:** Insertion Sort data terurut → **0 shift** (O(n)) vs data terbalik → 190 shift (O(n²))

---

### Pertemuan 7 — Integrasi Algoritma (Simulasi UTS) ⭐

**Topik:** Menggabungkan seluruh konsep pertemuan 1–6 dalam satu sistem nyata

**Pipeline Sistem Pengolahan Nilai Mahasiswa:**
```
input_data()  →  hitung_nilai()  →  bubble_sort()      →  tampilkan_data()
   O(n)            O(n)               O(n²)                   O(n)
                                  insertion_sort()
                                      O(n²)
                                  linear_search()  (by nama)
                                      O(n)
                                  binary_search()  (by nilai, post-sort)
                                      O(log n)
```

**Fungsi-fungsi Wajib (Modul Praktikum):**

| Fungsi | Kompleksitas | Deskripsi |
|--------|:------------:|-----------|
| `input_data_mahasiswa()` | O(n) | Input nama + 3 komponen nilai per mahasiswa |
| `hitung_nilai()` | O(n) | Kalkulasi nilai akhir berbobot + tentukan grade |
| `bubble_sort_desc()` | O(n²) | Urutkan descending, hitung perbandingan & swap |
| `insertion_sort_desc()` | O(n²) | Alternatif sorting — lebih efisien untuk n kecil |
| `linear_search()` | O(n) | Cari mahasiswa by nama (case-insensitive) |
| `binary_search_nilai()` | O(log n) | Cari nilai setelah data terurut |
| `tampilkan_data()` | O(n) | Output tabel terstruktur dengan header |
| `tampilkan_statistik()` | O(n) | Statistik min, max, rata-rata, distribusi grade |

**Kompleksitas Total:**
```
O(n) + O(n) + O(n²) + O(n) + O(log n) + O(n) = O(n²)
Komponen dominan: Sorting → menentukan performa keseluruhan sistem
```

**Challenge — Bubble Sort vs Insertion Sort (n=8, data acak):**

| Metrik | Bubble Sort | Insertion Sort | Pemenang |
|--------|:-----------:|:--------------:|:--------:|
| Perbandingan | 28 | **19** | Insertion Sort |
| Swap / Shift | 14 | 14 | Seri |

> **Kesimpulan:** Untuk n kecil, Insertion Sort lebih sedikit perbandingan karena berhenti lebih awal per elemen. Asimtotik keduanya O(n²).

**Hasil Eksekusi Demo (8 mahasiswa, terurut descending):**

| # | Nama | Nilai Akhir | Grade |
|:-:|------|:-----------:|:-----:|
| 1 | Gita Rahayu | 94.90 | A |
| 2 | Citra Dewi | 91.40 | A |
| 3 | Eva Maharani | 82.00 | B |
| 4 | Andi Pratama | 81.70 | B |
| 5 | Hendra Wijaya | 71.40 | B |
| 6 | Budi Santoso | 69.30 | C |
| 7 | Deni Saputra | 57.70 | D |
| 8 | Fajar Nugroho | 45.50 | E |

---

## 🔗 Peta Konsep Keseluruhan

```
P1: Analisis Masalah & IPO
 └─→ P2: Modular Programming (Dekomposisi Fungsi)
      └─→ P3: Rekursi vs Iterasi (Call Stack, Base Case)
           └─→ P4: Analisis Kompleksitas Big-O
                └─→ P5: Algoritma Pencarian (O(n) vs O(log n))
                     └─→ P6: Algoritma Pengurutan (Bubble/Selection/Insertion)
                          └─→ P7: INTEGRASI SISTEM — Simulasi UTS ⭐
                               (IPO + Modular + Sort + Search + Analisis)
```

---

## 📊 Hierarki Kompleksitas Algoritma

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
Terbaik ──────────────────────────────────────── Terburuk
```

| Notasi | Nama | Contoh dalam Praktikum |
|--------|------|------------------------|
| O(1) | Konstan | Akses array by index, `validasi_nilai()` |
| O(log n) | Logaritmik | Binary Search |
| O(n) | Linear | Linear Search, `input_data()`, `hitung_nilai()` |
| O(n²) | Kuadratik | Bubble / Selection / Insertion Sort |
| O(2ⁿ) | Eksponensial | Fibonacci rekursif naif |

---

## 🗺️ Matriks Pemilihan Algoritma

| Kebutuhan | Kondisi Data | Pilihan Terbaik | Kompleksitas |
|-----------|:------------:|-----------------|:------------:|
| Pencarian | Tidak terurut | Linear Search | O(n) |
| Pencarian | Terurut | Binary Search | O(log n) |
| Pengurutan | Hampir terurut / n kecil | Insertion Sort | O(n) ~ O(n²) |
| Pengurutan | Minimize swap | Selection Sort | O(n²) |
| Pengurutan | Production / n besar | `sorted()` / TimSort | O(n log n) |
| Komputasi berulang | Sub-masalah identik | Rekursi | Bergantung kasus |

---

## 📋 Strategi Eksekusi UTS (Blueprint Pertemuan 7)

1. **Baca Cermat** — Pahami spesifikasi dan batasan masalah secara menyeluruh
2. **Identifikasi Tipe** — Apakah masalah rekursi, searching, atau sorting?
3. **Pilih Algoritma** — Tentukan algoritma paling sesuai kondisi data
4. **Analisis Kompleksitas** — Hitung efisiensi Big-O dari pilihan algoritma
5. **Implementasi Modular** — Tulis pseudocode/kode secara terstruktur dan terpecah

---

## ▶️ Cara Menjalankan

```bash
python3 Pertemuan1/p1_diskon.py
python3 Pertemuan1/p1_nilai_mahasiswa.py
python3 Pertemuan1/p1_konversi_suhu.py
python3 Pertemuan2/p2_nilai_modular.py
python3 Pertemuan2/p2_bangun_datar.py
python3 Pertemuan3/p3_rekursi_iterasi.py
python3 Pertemuan4/p4_big_o_analysis.py
python3 Pertemuan5/p5_searching.py
python3 Pertemuan6/p6_sorting.py
python3 Pertemuan7/p7_sistem_nilai_terintegrasi.py   # ← Integrasi lengkap
```

---

*"Good code is the documentation of good thought."*  
*"Pemrograman modular bukan sekadar memecah kode — ini tentang mengisolasi kompleksitas."*  
— Algoritma & Pemrograman 2, STTPA
