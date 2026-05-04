# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 6
# Topik: Implementasi Sorting Dasar (Bubble, Selection, Insertion)
# ============================================================
# Cakupan:
#   [A] Bubble Sort    → O(n²) — swap elemen bersebelahan
#   [B] Selection Sort → O(n²) — temukan minimum, taruh di depan
#   [C] Insertion Sort → O(n²) best O(n) — sisipkan ke posisi tepat
#   [D] Tabel Perbandingan 3 Algoritma
#   [E] Challenge — Insertion Sort: data hampir terurut vs acak
# ============================================================

import random
import time
import copy


# ============================================================
# A. BUBBLE SORT
# ============================================================

def bubble_sort(data, trace=False):
    """
    Membandingkan pasangan elemen bersebelahan dan menukarnya
    jika urutan salah. 'Gelembung' terbesar naik ke atas setiap pass.

    Kompleksitas:
      Best Case : O(n)   — data sudah terurut (dengan optimasi flag)
      Worst Case: O(n²)  — data terbalik
      Space     : O(1)   — in-place sorting

    RETURN: (data_terurut, jumlah_perbandingan, jumlah_swap)
    """
    arr   = data[:]
    n     = len(arr)
    comp  = 0   # jumlah perbandingan
    swap  = 0   # jumlah pertukaran

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comp += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap += 1
                swapped = True
                if trace:
                    print(f"    Swap {arr[j+1]} ↔ {arr[j]}  → {arr}")
        if not swapped:
            break   # Optimasi: jika pass tanpa swap, data sudah terurut

    return arr, comp, swap


# ============================================================
# B. SELECTION SORT
# ============================================================

def selection_sort(data, trace=False):
    """
    Setiap iterasi: cari elemen MINIMUM dari sisa data yang belum terurut,
    lalu tukar dengan elemen di posisi pertama bagian belum terurut.

    Kompleksitas:
      Best/Worst/Avg: O(n²) — selalu melakukan n*(n-1)/2 perbandingan
      Space         : O(1)  — in-place sorting
      Keunggulan    : Jumlah swap minimum (paling banyak n-1 swap)

    RETURN: (data_terurut, jumlah_perbandingan, jumlah_swap)
    """
    arr  = data[:]
    n    = len(arr)
    comp = 0
    swap = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap += 1
            if trace:
                print(f"    Swap indeks {i}({arr[min_idx]}) ↔ {min_idx}({arr[i]})  → {arr}")

    return arr, comp, swap


# ============================================================
# C. INSERTION SORT
# ============================================================

def insertion_sort(data, trace=False):
    """
    Membangun bagian terurut satu per satu. Setiap elemen baru
    disisipkan ke posisi yang tepat dalam bagian yang sudah terurut.
    Analogi: mengurutkan kartu di tangan saat bermain kartu.

    Kompleksitas:
      Best Case : O(n)   — data sudah terurut (tidak perlu geser)
      Worst Case: O(n²)  — data terbalik (geser semua)
      Space     : O(1)   — in-place sorting
      Keunggulan: Sangat efisien untuk data hampir terurut

    RETURN: (data_terurut, jumlah_perbandingan, jumlah_shift)
    """
    arr   = data[:]
    comp  = 0
    shift = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j   = i - 1

        while j >= 0 and arr[j] > key:
            comp  += 1
            shift += 1
            arr[j + 1] = arr[j]
            j -= 1
            if trace:
                print(f"    Geser {arr[j+2]} ke kanan  → {arr}")

        # Satu perbandingan terakhir (kondisi keluar loop)
        if j >= 0:
            comp += 1

        arr[j + 1] = key

    return arr, comp, shift


# ============================================================
# D. TABEL PERBANDINGAN TIGA SORTING
# ============================================================

def buat_data_uji(n, mode="random"):
    """Membuat data uji sesuai mode."""
    if mode == "random":
        return random.sample(range(1, n * 3), n)
    elif mode == "sorted":
        return list(range(1, n + 1))
    elif mode == "reversed":
        return list(range(n, 0, -1))
    elif mode == "nearly":
        data = list(range(1, n + 1))
        # Tukar 10% elemen secara acak
        for _ in range(max(1, n // 10)):
            i, j = random.randint(0, n-1), random.randint(0, n-1)
            data[i], data[j] = data[j], data[i]
        return data


def cetak_tabel_perbandingan():
    """Tabel perbandingan jumlah perbandingan untuk n=6,10,20."""
    random.seed(42)

    print("\n" + "=" * 75)
    print("  TABEL PERBANDINGAN JUMLAH OPERASI SORTING (Data Acak)")
    print("=" * 75)
    print(f"  {'n':>4} | {'Bubble (comp)':>14} | {'Bubble (swap)':>13} | "
          f"{'Select (comp)':>14} | {'Insert (comp)':>14}")
    print("  " + "-" * 69)

    for n in [6, 10, 20]:
        data = buat_data_uji(n, "random")
        _, bc, bs = bubble_sort(data)
        _, sc, ss = selection_sort(data)
        _, ic, ish = insertion_sort(data)
        print(f"  {n:>4} | {bc:>14} | {bs:>13} | {sc:>14} | {ic:>14}")

    print("=" * 75)

    # Tabel worst case teoritis
    print("\n  TABEL WORST CASE TEORITIS: n*(n-1)/2")
    print("  " + "-" * 45)
    print(f"  {'n':>4} | {'Teoritis n(n-1)/2':>20} | {'Bubble Opt.':>12}")
    print("  " + "-" * 45)
    for n in [6, 10, 20]:
        teoritis = n * (n - 1) // 2
        data_rev = buat_data_uji(n, "reversed")
        _, bc, _ = bubble_sort(data_rev)
        print(f"  {n:>4} | {teoritis:>20} | {bc:>12}")
    print("=" * 75)


def cetak_tabel_data_mode():
    """Tabel perbandingan berdasarkan jenis data."""
    random.seed(42)
    n = 10
    modes = [
        ("random",   "Data Acak"),
        ("sorted",   "Data Terurut  (best case Insertion)"),
        ("reversed", "Data Terbalik (worst case semua)"),
        ("nearly",   "Hampir Terurut"),
    ]

    print("\n" + "=" * 75)
    print(f"  PERBANDINGAN BERDASARKAN JENIS DATA (n={n})")
    print("=" * 75)
    print(f"  {'Jenis Data':<35} | {'Bubble':>7} | {'Selection':>10} | {'Insertion':>10}")
    print("  " + "-" * 69)

    for mode, label in modes:
        data = buat_data_uji(n, mode)
        _, bc, _ = bubble_sort(data)
        _, sc, _ = selection_sort(data)
        _, ic, _ = insertion_sort(data)
        print(f"  {label:<35} | {bc:>7} | {sc:>10} | {ic:>10}")

    print("=" * 75)
    print("  ★ Insertion Sort unggul signifikan pada data hampir terurut!")
    print("=" * 75)


# ============================================================
# E. CHALLENGE — Insertion Sort: hampir terurut vs acak
# ============================================================

def challenge_insertion_sort():
    """Membandingkan Insertion Sort pada data hampir terurut vs acak."""
    random.seed(99)
    n = 20

    data_nearly = buat_data_uji(n, "nearly")
    data_random = buat_data_uji(n, "random")
    data_sorted = buat_data_uji(n, "sorted")
    data_rev    = buat_data_uji(n, "reversed")

    print("\n" + "=" * 65)
    print("  CHALLENGE — Insertion Sort: Berbagai Jenis Data (n=20)")
    print("=" * 65)

    datasets = [
        (data_sorted,  "Data Terurut       (best case)"),
        (data_nearly,  "Hampir Terurut     (near-best)"),
        (data_random,  "Data Acak          (average)"),
        (data_rev,     "Data Terbalik      (worst case)"),
    ]

    for ds, label in datasets:
        _, comp, shift = insertion_sort(ds)
        print(f"  {label:<37}: {comp:>4} perbandingan, {shift:>4} shift")

    print(f"""
  Penjelasan Perbedaan:
    Data Terurut: Insertion Sort hanya melakukan n-1 perbandingan
    (satu per elemen) karena tidak ada yang perlu digeser → O(n).

    Hampir Terurut: Hanya sedikit elemen yang "salah tempat",
    sehingga jumlah shift sangat kecil — Insertion Sort sangat
    efisien di sini dibanding Bubble dan Selection Sort.

    Data Acak: Rata-rata n²/4 perbandingan → O(n²).

    Data Terbalik: Setiap elemen harus digeser ke depan sepenuhnya
    — ini adalah worst case Insertion Sort dengan n*(n-1)/2 operasi.

  Kesimpulan: Insertion Sort adalah pilihan terbaik untuk
  data yang "hampir terurut" atau ukuran data kecil (n < 50).
  """)
    print("=" * 65)


# ============================================================
# PROGRAM UTAMA
# ============================================================

def main():
    random.seed(42)

    print("=" * 65)
    print("   ALGORITMA DAN PEMROGRAMAN 2 — PERTEMUAN 6")
    print("          Sorting: Bubble, Selection, Insertion")
    print("=" * 65)

    data_demo = [5, 2, 9, 1, 5, 6]

    # ---- A. Bubble Sort ----
    print("\n" + "─" * 65)
    print("A. BUBBLE SORT")
    print("─" * 65)
    print(f"  Input  : {data_demo}")
    hasil, comp, swap = bubble_sort(data_demo)
    print(f"  Output : {hasil}")
    print(f"  Perbandingan : {comp}")
    print(f"  Swap         : {swap}")

    print("\n  [Trace Bubble Sort pada [3,1,4,2]]")
    bubble_sort([3, 1, 4, 2], trace=True)

    # ---- B. Selection Sort ----
    print("\n" + "─" * 65)
    print("B. SELECTION SORT")
    print("─" * 65)
    print(f"  Input  : {data_demo}")
    hasil, comp, swap = selection_sort(data_demo)
    print(f"  Output : {hasil}")
    print(f"  Perbandingan : {comp}")
    print(f"  Swap         : {swap}")

    print("\n  [Trace Selection Sort pada [3,1,4,2]]")
    selection_sort([3, 1, 4, 2], trace=True)

    # ---- C. Insertion Sort ----
    print("\n" + "─" * 65)
    print("C. INSERTION SORT")
    print("─" * 65)
    print(f"  Input  : {data_demo}")
    hasil, comp, shift = insertion_sort(data_demo)
    print(f"  Output : {hasil}")
    print(f"  Perbandingan : {comp}")
    print(f"  Shift        : {shift}")

    print("\n  [Trace Insertion Sort pada [3,1,4,2]]")
    insertion_sort([3, 1, 4, 2], trace=True)

    # ---- D. Tabel Perbandingan ----
    cetak_tabel_perbandingan()
    cetak_tabel_data_mode()

    # ---- E. Challenge ----
    challenge_insertion_sort()

    # ---- Uji Performa Waktu ----
    print("\n" + "─" * 65)
    print("  UJI WAKTU EKSEKUSI (n=500, data acak)")
    print("─" * 65)
    data_besar = random.sample(range(1, 2000), 500)
    for nama, fn in [("Bubble Sort   ", bubble_sort),
                     ("Selection Sort", selection_sort),
                     ("Insertion Sort", insertion_sort)]:
        t0 = time.perf_counter()
        fn(data_besar)
        t1 = time.perf_counter()
        print(f"  {nama}: {(t1-t0)*1000:.3f} ms")

    # ---- Verifikasi Kebenaran ----
    print("\n" + "─" * 65)
    print("  VERIFIKASI KEBENARAN (hasil harus sama)")
    print("─" * 65)
    data_v = [64, 25, 12, 22, 11]
    b, _, _ = bubble_sort(data_v)
    s, _, _ = selection_sort(data_v)
    i, _, _ = insertion_sort(data_v)
    ref     = sorted(data_v)
    print(f"  Input          : {data_v}")
    print(f"  Python sorted  : {ref}")
    print(f"  Bubble Sort    : {b}  {'✓' if b==ref else '✗'}")
    print(f"  Selection Sort : {s}  {'✓' if s==ref else '✗'}")
    print(f"  Insertion Sort : {i}  {'✓' if i==ref else '✗'}")

    # ---- Kesimpulan ----
    print("\n" + "=" * 65)
    print("  KESIMPULAN: Perbandingan Tiga Sorting")
    print("=" * 65)
    print("""
  ┌─────────────────┬──────────┬──────────┬──────────────────────┐
  │ Algoritma       │ Best     │ Worst    │ Keunggulan           │
  ├─────────────────┼──────────┼──────────┼──────────────────────┤
  │ Bubble Sort     │ O(n)     │ O(n²)    │ Mudah dipahami       │
  │ Selection Sort  │ O(n²)    │ O(n²)    │ Min. jumlah swap     │
  │ Insertion Sort  │ O(n)     │ O(n²)    │ Terbaik: data near-  │
  │                 │          │          │ sorted, online sort  │
  └─────────────────┴──────────┴──────────┴──────────────────────┘

  Panduan Memilih:
    • Bubble Sort    : tujuan edukasi / data sangat kecil
    • Selection Sort : minimasi swap penting (misal: write-heavy storage)
    • Insertion Sort : data hampir terurut / data datang bertahap (stream)

  Untuk production: gunakan TimSort (Python built-in sorted())
  yang menggabungkan Insertion Sort + Merge Sort → O(n log n).
  """)
    print("=" * 65)


if __name__ == "__main__":
    main()
