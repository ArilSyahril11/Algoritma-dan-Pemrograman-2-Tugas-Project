# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 5
# Topik: Implementasi Linear Search dan Binary Search
# ============================================================
# Cakupan:
#   [A] Latihan 1 - Linear Search  → O(n)
#   [B] Latihan 2 - Binary Search  → O(log n)
#   [C] Latihan 3 - Uji Data 1-100
#   [D] Challenge - Binary Search pada data TIDAK terurut
#   [E] Tabel perbandingan langkah
# ============================================================

import math
import random


# ============================================================
# A. LINEAR SEARCH
# ============================================================

def linear_search(data, target):
    """
    Menelusuri data satu per satu dari indeks 0 ke n-1.
    Tidak memerlukan data terurut.

    Best Case : O(1) — target di indeks 0
    Worst Case: O(n) — target tidak ada / di akhir
    Average   : O(n/2) → O(n)

    RETURN: (posisi, jumlah_langkah)
            posisi = -1 jika tidak ditemukan
    """
    count = 0
    for i in range(len(data)):
        count += 1
        if data[i] == target:
            return i, count
    return -1, count


# ============================================================
# B. BINARY SEARCH
# ============================================================

def binary_search(data, target):
    """
    Mencari target dengan membagi ruang pencarian menjadi dua.
    SYARAT WAJIB: data HARUS dalam kondisi terurut ascending.

    Mekanisme:
      1. Hitung mid = (low + high) // 2
      2. Jika data[mid] == target → DITEMUKAN
      3. Jika data[mid] < target  → cari di paruh KANAN (low = mid+1)
      4. Jika data[mid] > target  → cari di paruh KIRI (high = mid-1)

    Kompleksitas: O(log n) — ruang pencarian DIBAGI DUA setiap iterasi.

    RETURN: (posisi, jumlah_langkah)
            posisi = -1 jika tidak ditemukan
    """
    low   = 0
    high  = len(data) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if data[mid] == target:
            return mid, count
        elif data[mid] < target:
            low = mid + 1       # Buang paruh kiri
        else:
            high = mid - 1      # Buang paruh kanan

    return -1, count


def binary_search_trace(data, target):
    """
    Versi trace: menampilkan proses pembagian ruang pencarian.
    """
    low   = 0
    high  = len(data) - 1
    count = 0

    print(f"  Data  : {data}")
    print(f"  Target: {target}")
    print(f"  {'Step':>4} | {'low':>4} | {'mid':>4} | {'high':>4} | {'data[mid]':>10} | Aksi")
    print("  " + "-" * 55)

    while low <= high:
        count += 1
        mid = (low + high) // 2
        aksi = ""

        if data[mid] == target:
            aksi = "✓ DITEMUKAN!"
            print(f"  {count:>4} | {low:>4} | {mid:>4} | {high:>4} | {data[mid]:>10} | {aksi}")
            return mid, count
        elif data[mid] < target:
            aksi = f"→ Cari kanan (low={mid+1})"
            print(f"  {count:>4} | {low:>4} | {mid:>4} | {high:>4} | {data[mid]:>10} | {aksi}")
            low = mid + 1
        else:
            aksi = f"← Cari kiri (high={mid-1})"
            print(f"  {count:>4} | {low:>4} | {mid:>4} | {high:>4} | {data[mid]:>10} | {aksi}")
            high = mid - 1

    print(f"  {'─':─>55}")
    print(f"  ✗ Target {target} TIDAK DITEMUKAN setelah {count} langkah")
    return -1, count


# ============================================================
# C. UJI DATA 1-100
# ============================================================

def uji_data_besar():
    """Uji kedua algoritma pada data 1-100."""
    data = list(range(1, 101))    # [1, 2, 3, ..., 100]
    targets = [
        (1,   "Angka 1   (paling awal)"),
        (50,  "Angka 50  (tengah)"),
        (100, "Angka 100 (paling akhir)"),
        (999, "Angka 999 (tidak ada)"),
    ]

    print("\n" + "=" * 65)
    print("  LATIHAN 3 — Uji Data Besar (n=100)")
    print("=" * 65)
    print(f"  {'Target':>10} | {'Linear':>8} | {'Binary':>8} | Hemat")
    print("  " + "-" * 50)

    for t, label in targets:
        _, ls = linear_search(data, t)
        _, bs = binary_search(data, t)
        hemat = ls - bs
        print(f"  {label:<26} | {ls:>8} | {bs:>8} | {hemat:>4} langkah")

    print("=" * 65)


# ============================================================
# D. CHALLENGE — Binary Search pada data TIDAK terurut
# ============================================================

def challenge_data_tidak_terurut():
    """
    Demonstrasi Binary Search pada data tidak terurut.
    Hasilnya TIDAK DAPAT DIPERCAYA karena asumsi pembagian
    ruang pencarian tidak berlaku pada data acak.
    """
    data_acak = [15, 3, 42, 8, 23, 16, 4, 11, 7, 1]
    target    = 8

    print("\n" + "=" * 65)
    print("  CHALLENGE — Binary Search pada Data TIDAK Terurut")
    print("=" * 65)
    print(f"  Data acak  : {data_acak}")
    print(f"  Target     : {target}")

    # Linear Search (benar)
    pos_ls, steps_ls = linear_search(data_acak, target)
    print(f"\n  Linear Search → posisi {pos_ls}, {steps_ls} langkah (BENAR)")

    # Binary Search (salah/tidak konsisten)
    pos_bs, steps_bs = binary_search(data_acak, target)
    print(f"  Binary Search → posisi {pos_bs}, {steps_bs} langkah (BISA SALAH!)")

    if pos_bs == -1 and pos_ls != -1:
        print(f"\n  ⚠ MASALAH TERDETEKSI!")
        print(f"     Linear Search menemukan {target} di indeks {pos_ls}")
        print(f"     Binary Search GAGAL menemukan → HASIL SALAH")
    elif pos_bs != -1 and data_acak[pos_bs] != target:
        print(f"\n  ⚠ MASALAH TERDETEKSI!")
        print(f"     Binary Search mengklaim posisi {pos_bs}")
        print(f"     Nilai di posisi tersebut = {data_acak[pos_bs]} ≠ {target}")

    print(f"""
  Penjelasan Mengapa Terjadi Kesalahan:
  Binary Search berasumsi bahwa jika data[mid] < target, maka
  semua elemen di sebelah KIRI mid pasti lebih kecil dari target,
  sehingga paruh kiri dibuang. Pada data acak, asumsi ini SALAH —
  target bisa saja berada di paruh yang sudah dibuang.
  Akibatnya, Binary Search akan melompati elemen yang seharusnya
  diperiksa dan menghasilkan "tidak ditemukan" meskipun ada,
  atau bahkan mengembalikan indeks yang salah.
  KESIMPULAN: Binary Search HANYA valid pada data TERURUT.
    """)
    print("=" * 65)


# ============================================================
# TABEL PERBANDINGAN LENGKAP
# ============================================================

def cetak_tabel_perbandingan():
    """Tabel perbandingan langkah Linear vs Binary Search."""
    print("\n" + "=" * 70)
    print("  TABEL PERBANDINGAN: Linear Search vs Binary Search")
    print("=" * 70)
    print(f"  {'n':>6} | {'Lin. (worst)':>14} | {'Bin. (worst)':>14} | {'log₂(n)':>8} | Rasio")
    print("  " + "-" * 62)

    for n in [10, 50, 100, 500, 1000, 10000]:
        data    = list(range(1, n + 1))
        _, ls   = linear_search(data, -1)          # worst case
        _, bs   = binary_search(data, -1)          # worst case
        log2_n  = math.ceil(math.log2(n + 1))
        rasio   = ls / bs if bs > 0 else ls
        print(f"  {n:>6} | {ls:>14} | {bs:>14} | {log2_n:>8} | {rasio:.1f}x lebih cepat")

    print("=" * 70)
    print("  Binary Search worst case ≈ ⌈log₂(n+1)⌉ langkah")
    print("  Semakin besar n → Binary Search makin JAUH lebih unggul")
    print("=" * 70)


# ============================================================
# PROGRAM UTAMA
# ============================================================

def main():
    print("=" * 65)
    print("   ALGORITMA DAN PEMROGRAMAN 2 — PERTEMUAN 5")
    print("        Linear Search vs Binary Search")
    print("=" * 65)

    data = [4, 8, 15, 16, 23, 42]

    # ---- A. Linear Search ----
    print("\n" + "─" * 65)
    print("A. LINEAR SEARCH — O(n)")
    print("─" * 65)
    print(f"  Data: {data}")
    test_ls = [
        (4,  "target di AWAL"),
        (16, "target di TENGAH"),
        (42, "target di AKHIR"),
        (99, "target TIDAK ADA"),
    ]
    for t, label in test_ls:
        pos, steps = linear_search(data, t)
        status = f"indeks {pos}" if pos != -1 else "tidak ditemukan"
        print(f"  Cari {t:>2} ({label:<22}) → {steps:>2} langkah  [{status}]")

    # ---- B. Binary Search ----
    print("\n" + "─" * 65)
    print("B. BINARY SEARCH — O(log n)")
    print("─" * 65)
    print(f"  Data: {data}")
    test_bs = [
        (4,  "target di AWAL"),
        (16, "target di TENGAH"),
        (42, "target di AKHIR"),
        (99, "target TIDAK ADA"),
    ]
    for t, label in test_bs:
        pos, steps = binary_search(data, t)
        status = f"indeks {pos}" if pos != -1 else "tidak ditemukan"
        print(f"  Cari {t:>2} ({label:<22}) → {steps:>2} langkah  [{status}]")

    # ---- Trace Binary Search ----
    print("\n" + "─" * 65)
    print("  TRACE Binary Search — cari 23 dalam", data)
    print("─" * 65)
    binary_search_trace(data, 23)

    print("\n" + "─" * 65)
    print("  TRACE Binary Search — cari 99 (tidak ada)")
    print("─" * 65)
    binary_search_trace(data, 99)

    # ---- C. Uji Data Besar ----
    uji_data_besar()

    # ---- D. Challenge ----
    challenge_data_tidak_terurut()

    # ---- Tabel Perbandingan ----
    cetak_tabel_perbandingan()

    # ---- Kesimpulan ----
    print("\n" + "=" * 65)
    print("  KESIMPULAN: O(n) vs O(log n)")
    print("=" * 65)
    print("""
  Linear Search (O(n)):
    • Tidak memerlukan data terurut (fleksibel)
    • Worst case: memeriksa SEMUA n elemen
    • Cocok untuk: data kecil, data tidak terurut

  Binary Search (O(log n)):
    • WAJIB data terurut (syarat mutlak)
    • Worst case: hanya ⌈log₂(n)⌉ langkah
    • Untuk n=1.000.000 → hanya ~20 langkah!
    • Cocok untuk: data besar yang sudah terurut

  Perbandingan n=1000:
    Linear Search → 1000 langkah (worst case)
    Binary Search → 10 langkah   (worst case)
    → Binary Search 100x lebih efisien!

  Intuisi Binary Search:
    Seperti mencari kata di kamus — buka tengah, lalu putuskan
    apakah target ada di bagian depan atau belakang, ulangi.
  """)
    print("=" * 65)


if __name__ == "__main__":
    main()
