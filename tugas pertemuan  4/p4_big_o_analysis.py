# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 4
# Topik: Analisis Kompleksitas Algoritma (Big-O Intuitif)
# ============================================================
# Cakupan:
#   [A] Latihan 1 - Loop Tunggal O(n)
#   [B] Latihan 2 - Dua Loop Berurutan O(n)
#   [C] Latihan 3 - Loop Bersarang O(n²)
#   [D] Latihan 4 - Linear Search vs Nested Loop
#   [E] Tabel Perbandingan Iterasi
# ============================================================

import time


# ============================================================
# A. LATIHAN 1 — Loop Tunggal O(n)
# ============================================================

def loop_tunggal(n, verbose=False):
    """
    Mencetak angka dari 0 sampai n-1 dan menghitung iterasi.
    Kompleksitas: O(n) — iterasi bertumbuh LINEAR seiring n.
    """
    count = 0
    for i in range(n):
        if verbose:
            print(f"  i = {i}")
        count += 1
    return count


# ============================================================
# B. LATIHAN 2 — Dua Loop Berurutan O(n)
# ============================================================

def dua_loop_berurutan(n):
    """
    Dua loop yang berjalan berurutan (bukan bersarang).
    Total iterasi = n + n = 2n → tetap O(n) karena konstanta diabaikan.
    """
    count = 0
    for i in range(n):      # Loop pertama: n iterasi
        count += 1
    for j in range(n):      # Loop kedua: n iterasi
        count += 1
    return count             # Total = 2n → O(n)


# ============================================================
# C. LATIHAN 3 — Loop Bersarang O(n²)
# ============================================================

def loop_bersarang(n):
    """
    Loop bersarang: untuk setiap i, j berjalan n kali.
    Total iterasi = n × n = n² → O(n²).
    Pertumbuhan KUADRATIK — jauh lebih cepat membesar dari O(n).
    """
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count             # Total = n²


# ============================================================
# D. LATIHAN 4 — Linear Search vs Nested Loop
# ============================================================

def linear_search_count(data, target):
    """
    Linear Search: menelusuri satu per satu dari kiri ke kanan.
    Best Case : O(1) — target di indeks 0
    Worst Case: O(n) — target tidak ada atau di akhir
    """
    count = 0
    for item in data:
        count += 1
        if item == target:
            return count, True
    return count, False


def nested_loop_count(data):
    """
    Nested Loop: pasangkan setiap elemen dengan semua elemen lain.
    Kompleksitas: O(n²) — tidak peduli posisi target.
    """
    count = 0
    for i in data:
        for j in data:
            count += 1
    return count


# ============================================================
# HELPER — Tabel Perbandingan
# ============================================================

def cetak_tabel_perbandingan():
    """Mencetak tabel iterasi untuk n = 5, 10, 20."""
    nilai_n = [5, 10, 20]

    print("\n" + "=" * 70)
    print("  TABEL PERBANDINGAN ITERASI")
    print("=" * 70)
    print(f"  {'n':>4} | {'O(1)':>6} | {'O(n) x1':>9} | {'O(n) x2':>9} | {'O(n²)':>8} | Rasio n²/n")
    print("  " + "-" * 66)

    for n in nilai_n:
        o1   = 1
        on   = loop_tunggal(n)
        on2x = dua_loop_berurutan(n)
        on2  = loop_bersarang(n)
        rasio = on2 / on if on > 0 else 0
        print(f"  {n:>4} | {o1:>6} | {on:>9} | {on2x:>9} | {on2:>8} | {rasio:.1f}x lebih banyak")

    print("=" * 70)
    print("  Keterangan:")
    print("    O(1)    = operasi konstan, tidak bergantung n")
    print("    O(n) x1 = satu loop tunggal")
    print("    O(n) x2 = dua loop berurutan → tetap O(n) karena 2n ≈ n")
    print("    O(n²)   = loop bersarang → pertumbuhan kuadratik")
    print("=" * 70)


def cetak_tabel_search():
    """Tabel perbandingan Linear Search vs Nested Loop."""
    data_kecil  = [1, 3, 5, 7, 9]           # n=5
    data_sedang = list(range(1, 11, 2))      # n=10 → [1,3,5,...,19]
    data_besar  = list(range(1, 41, 2))      # n=20 → [1,3,5,...,39]
    datasets    = [data_kecil, data_sedang, data_besar]

    print("\n" + "=" * 65)
    print("  TABEL: Linear Search vs Nested Loop")
    print("=" * 65)
    print(f"  {'n':>4} | {'Lin.Search (worst)':>20} | {'Nested Loop':>13} | Rasio")
    print("  " + "-" * 59)

    for ds in datasets:
        n = len(ds)
        # Worst case linear search: target tidak ada
        ls_steps, _ = linear_search_count(ds, -1)
        nl_steps     = nested_loop_count(ds)
        rasio = nl_steps / ls_steps if ls_steps > 0 else 0
        print(f"  {n:>4} | {ls_steps:>20} | {nl_steps:>13} | {rasio:.1f}x")

    print("=" * 65)
    print("  Kesimpulan:")
    print("    Saat n=5 : Nested loop 5x lebih banyak langkah dari Linear Search")
    print("    Saat n→∞ : Gap terus melebar secara kuadratik!")
    print("=" * 65)


# ============================================================
# PROGRAM UTAMA
# ============================================================

def main():
    print("=" * 65)
    print("   ALGORITMA DAN PEMROGRAMAN 2 — PERTEMUAN 4")
    print("         Analisis Kompleksitas Algoritma (Big-O)")
    print("=" * 65)

    # ---- A. Loop Tunggal ----
    print("\n" + "─" * 65)
    print("A. LATIHAN 1 — Loop Tunggal O(n)")
    print("─" * 65)
    for n in [5, 10, 20]:
        iterasi = loop_tunggal(n)
        print(f"  n = {n:>2}  →  iterasi = {iterasi:>4}  (O(n) = {n})")
    print("\n  [Demo n=5 verbose]")
    loop_tunggal(5, verbose=True)

    # ---- B. Dua Loop Berurutan ----
    print("\n" + "─" * 65)
    print("B. LATIHAN 2 — Dua Loop Berurutan → tetap O(n)")
    print("─" * 65)
    for n in [5, 10, 20]:
        iterasi = dua_loop_berurutan(n)
        print(f"  n = {n:>2}  →  iterasi = {iterasi:>4}  (2n = 2×{n} = {2*n}, diabaikan → O(n))")

    # ---- C. Loop Bersarang ----
    print("\n" + "─" * 65)
    print("C. LATIHAN 3 — Loop Bersarang O(n²)")
    print("─" * 65)
    for n in [5, 10, 20]:
        iterasi = loop_bersarang(n)
        print(f"  n = {n:>2}  →  iterasi = {iterasi:>4}  (n² = {n}² = {n*n})")

    # ---- D. Linear Search vs Nested Loop ----
    print("\n" + "─" * 65)
    print("D. LATIHAN 4 — Linear Search vs Nested Loop")
    print("─" * 65)
    data_ls = [1, 3, 5, 7, 9, 11, 13]
    data_nl = [1, 3, 5, 7, 9]

    targets = [
        (1,  "target di AWAL    (best case)"),
        (7,  "target di TENGAH  (avg case)"),
        (13, "target di AKHIR   (worst case)"),
        (99, "target TIDAK ADA  (worst case)"),
    ]

    print("\n  [Linear Search — data = {0}]".format(data_ls))
    for t, label in targets:
        steps, found = linear_search_count(data_ls, t)
        status = "✓ DITEMUKAN" if found else "✗ TIDAK ADA"
        print(f"  Cari {t:>2} ({label}) → {steps:>2} langkah  {status}")

    nl_steps = nested_loop_count(data_nl)
    print(f"\n  [Nested Loop — data = {data_nl}]")
    print(f"  Total langkah = {nl_steps}  (n² = {len(data_nl)}² = {len(data_nl)**2})")

    # ---- Tabel Perbandingan ----
    cetak_tabel_perbandingan()
    cetak_tabel_search()

    # ---- Uji Waktu Eksekusi ----
    print("\n" + "─" * 65)
    print("  UJI WAKTU EKSEKUSI (n = 1000)")
    print("─" * 65)
    N = 1000
    t0 = time.perf_counter(); loop_tunggal(N);         t1 = time.perf_counter()
    t2 = time.perf_counter(); dua_loop_berurutan(N);   t3 = time.perf_counter()
    t4 = time.perf_counter(); loop_bersarang(N);       t5 = time.perf_counter()
    print(f"  O(n)  loop tunggal     : {(t1-t0)*1000:.4f} ms")
    print(f"  O(n)  dua loop berurut : {(t3-t2)*1000:.4f} ms")
    print(f"  O(n²) loop bersarang   : {(t5-t4)*1000:.4f} ms")

    # ---- Kesimpulan ----
    print("\n" + "=" * 65)
    print("  KESIMPULAN: Big-O Intuitif")
    print("=" * 65)
    print("""
  Kompleksitas waktu adalah cara mengukur SEBERAPA CEPAT jumlah
  operasi bertumbuh seiring bertambahnya ukuran input (n).

  Hierarki kompleksitas (dari terbaik ke terburuk):
    O(1)      → Konstan  : tidak dipengaruhi n sama sekali
    O(log n)  → Logaritmik: sangat efisien (Binary Search)
    O(n)      → Linear   : iterasi bertumbuh proporsional dengan n
    O(n²)     → Kuadratik: berbahaya untuk n besar (loop bersarang)

  Aturan Big-O:
    • Konstanta DIABAIKAN  : 2n → O(n), 5n² → O(n²)
    • Loop berurutan       : O(n) + O(n) = O(n)  (bukan O(2n))
    • Loop bersarang       : O(n) × O(n) = O(n²)
    • Ambil suku terbesar  : O(n² + n) → O(n²)
  """)
    print("=" * 65)


if __name__ == "__main__":
    main()
