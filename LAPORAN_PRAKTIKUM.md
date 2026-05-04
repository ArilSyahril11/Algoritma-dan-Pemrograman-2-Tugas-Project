# 📘 Algoritma dan Pemrograman 2 — STTPA
## Laporan Tugas Praktikum Lengkap (Pertemuan 1–6)

**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Algoritma dan Pemrograman 2  
**Dosen:** Yudi Herdiana, S.T., M.T.

---

## 📁 Struktur File

```
Alpro2_Praktikum/
│
├── Pertemuan1/
│   ├── p1_diskon.py              ← Latihan 1: Kalkulator Diskon
│   ├── p1_nilai_mahasiswa.py     ← Latihan 2: Nilai Akhir + Validasi
│   └── p1_konversi_suhu.py       ← Challenge: Konversi Suhu (°C → °F & K)
│
├── Pertemuan2/
│   ├── p2_nilai_modular.py       ← Latihan 1: Nilai Mahasiswa Modular
│   └── p2_bangun_datar.py        ← Latihan 2+Challenge: Bangun Datar Modular
│
├── Pertemuan3/
│   └── p3_rekursi_iterasi.py     ← Faktorial, Jumlah, Fibonacci, Pangkat
│
├── Pertemuan4/
│   └── p4_big_o_analysis.py      ← O(1), O(n), O(n²) + Tabel Iterasi
│
├── Pertemuan5/
│   └── p5_searching.py           ← Linear Search + Binary Search + Challenge
│
├── Pertemuan6/
│   └── p6_sorting.py             ← Bubble, Selection, Insertion Sort
│
├── LAPORAN_PRAKTIKUM.md          ← Jawaban Refleksi Pertemuan 1–3
└── README.md                     ← File ini
```

---

## 🗂️ Ringkasan Per Pertemuan

---

### Pertemuan 1 — Implementasi Algoritma Berbasis IPO

**Topik:** Kerangka IPO (Input–Process–Output), Pseudocode → Python

| File | Topik | Konsep |
|------|-------|--------|
| `p1_diskon.py` | Kalkulator diskon belanja | `if-elif-else`, validasi input |
| `p1_nilai_mahasiswa.py` | Nilai akhir berbobot | Rumus berbobot, validasi range |
| `p1_konversi_suhu.py` | Konversi °C → °F dan Kelvin | Rumus matematika, tabel output |

**Aturan Diskon:**
- Belanja ≥ Rp500.000 → Diskon 20%
- Belanja ≥ Rp250.000 → Diskon 10%
- Lainnya → Diskon 0%

**Refleksi:**
> *Mengapa urutan kondisi `if-elif` penting?*  
> Python mengevaluasi dari atas ke bawah dan berhenti pada kondisi pertama yang `True`. Kondisi paling spesifik (nilai terbesar) harus ditulis lebih dahulu agar tidak terjadi kesalahan klasifikasi.

---

### Pertemuan 2 — Modular Programming

**Topik:** Dekomposisi, Single Responsibility, Return Value

| File | Fungsi-fungsi |
|------|--------------|
| `p2_nilai_modular.py` | `input_nilai()`, `validasi_nilai()`, `hitung_nilai()`, `tentukan_grade()`, `tampilkan_hasil()` |
| `p2_bangun_datar.py` | `luas_persegi()`, `luas_persegi_panjang()`, `luas_lingkaran()`, + keliling masing-masing |

**4 Prinsip Emas Modular:**
1. **Single Responsibility** — Satu fungsi, satu tugas
2. **Reusability** — Fungsi dapat dipanggil berulang kali
3. **Readability** — Kode mudah dibaca manusia
4. **Maintainability** — Mudah diubah tanpa merusak bagian lain

**Refleksi:**
> *Apa keuntungan modular vs monolitik?*  
> Kode modular lebih terstruktur, mudah di-debug per fungsi, dapat dipakai ulang, dan penambahan fitur baru tidak berisiko merusak bagian yang sudah berjalan.

---

### Pertemuan 3 — Rekursi vs Iterasi

**Topik:** Base Case, Recursive Case, Call Stack, Fibonacci

| Fungsi | Rekursif | Iteratif | Kompleksitas |
|--------|----------|----------|--------------|
| Faktorial(n) | ✓ | ✓ | O(n) rekursi linear |
| Jumlah 1..n | ✓ | ✓ | O(n) |
| Fibonacci(n) | ✓ | ✓ | O(2ⁿ) rekursi / O(n) iterasi |
| Pangkat a^n | ✓ | — | O(n) |

**Anatomi Rekursi:**
```
Fungsi rekursif(n):
    Jika kondisi_berhenti:   ← Base Case (WAJIB ADA)
        kembalikan nilai_pasti
    Else:
        kembalikan rekursif(n-1)  ← Recursive Case
```

**Trace faktorial(4):**
```
→ faktorial(4) → faktorial(3) → faktorial(2) → faktorial(1) → faktorial(0)=1
← 1×1=1 ← 2×1=2 ← 3×2=6 ← 4×6=24
```

**Refleksi:**
> *Mengapa Fibonacci rekursif lebih lambat?*  
> Fibonacci rekursif melahirkan **dua** percabangan setiap langkah (rekursi bercabang). Sub-masalah yang sama dihitung berulang kali (overlapping subproblems), menghasilkan kompleksitas O(2ⁿ).

---

### Pertemuan 4 — Analisis Kompleksitas Algoritma (Big-O Intuitif)

**Topik:** O(1), O(n), O(n²), Aturan Big-O, Menghitung Iterasi

| Latihan | Pola Kode | Kompleksitas | Iterasi (n=10) |
|---------|-----------|--------------|----------------|
| 1 | Satu loop | O(n) | 10 |
| 2 | Dua loop berurutan | O(n) | 20 → tetap O(n) |
| 3 | Loop bersarang | O(n²) | 100 |
| 4 | Linear Search | O(n) worst | ≤ n langkah |

**Tabel Perbandingan Iterasi:**

| n | O(1) | O(n) ×1 | O(n) ×2 | O(n²) | Rasio n²/n |
|---|------|---------|---------|-------|------------|
| 5 | 1 | 5 | 10 | 25 | 5× |
| 10 | 1 | 10 | 20 | 100 | 10× |
| 20 | 1 | 20 | 40 | 400 | 20× |

**Aturan Big-O:**
- Konstanta diabaikan: `2n → O(n)`, `5n² → O(n²)`
- Loop berurutan: `O(n) + O(n) = O(n)` *(bukan O(2n))*
- Loop bersarang: `O(n) × O(n) = O(n²)`
- Ambil suku terbesar: `O(n² + n) → O(n²)`

**Refleksi:**
> *Mengapa O(n²) jauh lebih lambat saat n besar?*  
> Saat n=1000, O(n) butuh 1.000 operasi sedangkan O(n²) butuh **1.000.000** operasi — 1000× lebih banyak. Saat n=10.000, perbedaannya menjadi 10.000×. Pertumbuhan kuadratik menjadi tidak praktis dengan cepat.

> *Mengapa konstanta tidak diperhitungkan dalam Big-O?*  
> Big-O mengukur **pola pertumbuhan**, bukan nilai absolut. Untuk n yang sangat besar, konstanta 2 atau 5 menjadi tidak signifikan dibanding faktor pertumbuhan (n vs n²).

---

### Pertemuan 5 — Linear Search dan Binary Search

**Topik:** O(n) vs O(log n), syarat Binary Search, perbandingan langkah

| Algoritma | Kompleksitas | Syarat Data | Cocok Untuk |
|-----------|--------------|-------------|-------------|
| Linear Search | O(n) | Bebas (tidak perlu terurut) | Data kecil, data tidak terurut |
| Binary Search | O(log n) | **WAJIB terurut** | Data besar yang terurut |

**Tabel Perbandingan Langkah (Worst Case):**

| n | Linear Search | Binary Search | log₂(n) | Binary lebih cepat |
|---|---------------|---------------|---------|-------------------|
| 10 | 10 | 3 | 4 | ~3× |
| 100 | 100 | 6 | 7 | ~17× |
| 1.000 | 1.000 | 9 | 10 | ~111× |
| 10.000 | 10.000 | 13 | 14 | ~769× |

**Mekanisme Binary Search:**
```
low=0, high=n-1
Selama low <= high:
    mid = (low+high)//2
    Jika data[mid] == target → DITEMUKAN
    Jika data[mid] < target  → low = mid+1   (cari kanan)
    Jika data[mid] > target  → high = mid-1  (cari kiri)
```

**Challenge — Binary Search data tidak terurut:**  
Binary Search pada data acak menghasilkan hasil yang **tidak dapat dipercaya**. Ia membuang setengah ruang pencarian berdasarkan asumsi keterurutan yang tidak terpenuhi, sehingga target yang ada bisa dianggap tidak ada.

**Refleksi:**
> *Kapan Linear Search lebih tepat dari Binary Search?*  
> Saat data tidak terurut, saat biaya pengurutan lebih mahal dari pencarian, atau saat data sangat kecil (n < 10) di mana overhead Binary Search tidak sepadan.

---

### Pertemuan 6 — Sorting Dasar (Bubble, Selection, Insertion)

**Topik:** Tiga algoritma sorting O(n²), perbandingan operasi, best/worst case

**Implementasi Data Demo `[5, 2, 9, 1, 5, 6]`:**

| Algoritma | Hasil | Perbandingan | Swap/Shift |
|-----------|-------|--------------|------------|
| Bubble Sort | [1,2,5,5,6,9] | 14 | 6 swap |
| Selection Sort | [1,2,5,5,6,9] | 15 | 4 swap |
| Insertion Sort | [1,2,5,5,6,9] | 9 | 6 shift |

**Tabel Perbandingan (Data Acak):**

| n | Bubble (comp) | Selection (comp) | Insertion (comp) |
|---|---------------|------------------|------------------|
| 6 | ~9 | 15 | ~7 |
| 10 | ~45 | 45 | ~35 |
| 20 | ~190 | 190 | ~107 |

**Perbandingan Berdasarkan Jenis Data (n=10):**

| Jenis Data | Bubble | Selection | Insertion |
|------------|--------|-----------|-----------|
| Data Acak | ~39 | 45 | ~24 |
| Data Terurut (best) | 9 | 45 | **9** |
| Data Terbalik (worst) | 45 | 45 | 45 |
| Hampir Terurut | ~45 | 45 | **~24** |

**Kompleksitas:**

| Algoritma | Best Case | Worst Case | Space | Keunggulan |
|-----------|-----------|------------|-------|------------|
| Bubble Sort | O(n) | O(n²) | O(1) | Mudah dipahami |
| Selection Sort | O(n²) | O(n²) | O(1) | Jumlah swap minimum |
| Insertion Sort | **O(n)** | O(n²) | O(1) | Terbaik untuk data hampir terurut |

**Challenge — Insertion Sort:**
- Data terurut: 19 perbandingan, **0 shift** → O(n)
- Hampir terurut: ~44 perbandingan, ~25 shift → mendekati O(n)
- Data acak: ~83 perbandingan, ~66 shift → O(n²)
- Data terbalik: 190 perbandingan, 190 shift → worst case O(n²)

**Refleksi:**
> *Mana yang paling stabil pada data hampir terurut?*  
> **Insertion Sort** — karena hanya menggeser elemen yang memang salah posisi. Elemen yang sudah berada di tempat yang tepat tidak tersentuh sama sekali.

> *Panduan memilih algoritma sorting:*
> - **Bubble Sort** → edukasi / data sangat kecil
> - **Selection Sort** → minimize operasi write/swap (storage khusus)
> - **Insertion Sort** → data hampir terurut, data streaming/real-time
> - **Python `sorted()`** → production code (TimSort: O(n log n))

---

## 🔗 Peta Konsep Keseluruhan

```
Pertemuan 1: Analisis Masalah & IPO
    ↓
Pertemuan 2: Modular Programming (Dekomposisi Fungsi)
    ↓
Pertemuan 3: Rekursi vs Iterasi (Call Stack, Base Case)
    ↓
Pertemuan 4: Analisis Kompleksitas Big-O (O(1), O(n), O(n²))
    ↓
Pertemuan 5: Algoritma Pencarian (O(n) vs O(log n))
    ↓
Pertemuan 6: Algoritma Pengurutan (Bubble, Selection, Insertion)
```

## 📊 Hierarki Kompleksitas Algoritma

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
Terbaik                                          Terburuk
```

| Notasi | Nama | Contoh |
|--------|------|--------|
| O(1) | Konstan | Akses array by index |
| O(log n) | Logaritmik | Binary Search |
| O(n) | Linear | Linear Search, loop tunggal |
| O(n²) | Kuadratik | Bubble/Selection/Insertion Sort |
| O(2ⁿ) | Eksponensial | Fibonacci rekursif naif |

---

## ▶️ Cara Menjalankan

```bash
# Pertemuan 1
python3 Pertemuan1/p1_diskon.py
python3 Pertemuan1/p1_nilai_mahasiswa.py
python3 Pertemuan1/p1_konversi_suhu.py

# Pertemuan 2
python3 Pertemuan2/p2_nilai_modular.py
python3 Pertemuan2/p2_bangun_datar.py

# Pertemuan 3
python3 Pertemuan3/p3_rekursi_iterasi.py

# Pertemuan 4
python3 Pertemuan4/p4_big_o_analysis.py

# Pertemuan 5
python3 Pertemuan5/p5_searching.py

# Pertemuan 6
python3 Pertemuan6/p6_sorting.py
```

---

*"Good code is the documentation of good thought." — Algoritma & Pemrograman 2, STTPA*
