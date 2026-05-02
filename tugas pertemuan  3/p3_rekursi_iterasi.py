# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 3
# Implementasi Rekursi dan Perbandingan dengan Iterasi
# ============================================================
# Cakupan:
#   [A] Faktorial  - Rekursif & Iteratif
#   [B] Jumlah 1..n - Rekursif
#   [C] Fibonacci  - Rekursif
#   [D] Challenge  - Validasi input negatif + Trace Recursion
# ============================================================

import time


# ============================================================
# A. FAKTORIAL
# ============================================================

def faktorial_rekursif(n, depth=0):
    """
    Menghitung n! secara rekursif.
    Base Case    : n == 0  → return 1
    Recursive Case: return n * faktorial_rekursif(n-1)
    """
    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    if n == 0:
        return 1                          # Base Case
    return n * faktorial_rekursif(n - 1) # Recursive Case


def faktorial_iteratif(n):
    """
    Menghitung n! secara iteratif menggunakan loop.
    Tidak memerlukan call stack — hanya satu variabel `hasil`.
    """
    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil


def faktorial_trace(n, depth=0):
    """
    Versi trace: menampilkan proses pemanggilan rekursif step-by-step.
    """
    indent = "  " * depth
    print(f"{indent}→ faktorial({n}) dipanggil")

    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    if n == 0:
        print(f"{indent}← BASE CASE: faktorial(0) = 1")
        return 1

    sub = faktorial_trace(n - 1, depth + 1)
    hasil = n * sub
    print(f"{indent}← faktorial({n}) = {n} × {sub} = {hasil}")
    return hasil


# ============================================================
# B. JUMLAH 1 s.d. N (Rekursif)
# ============================================================

def jumlah_rekursif(n):
    """
    Menghitung total penjumlahan: 1 + 2 + ... + n secara rekursif.
    Base Case    : n == 1  → return 1
    Recursive Case: return n + jumlah_rekursif(n-1)
    """
    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    if n == 1:
        return 1                         # Base Case
    return n + jumlah_rekursif(n - 1)   # Recursive Case


def jumlah_iteratif(n):
    """Versi iteratif sebagai pembanding."""
    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    return sum(range(1, n + 1))


# ============================================================
# C. FIBONACCI (Rekursif)
# ============================================================

def fibonacci(n):
    """
    Menghitung suku Fibonacci ke-n secara rekursif.
    Base Case    : n <= 1  → return n
    Recursive Case: return fibonacci(n-1) + fibonacci(n-2)
    Catatan: Sangat lambat untuk n besar karena overlapping subproblems.
    """
    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    if n <= 1:
        return n                                      # Base Case
    return fibonacci(n - 1) + fibonacci(n - 2)       # Recursive Case (Bercabang)


def fibonacci_iteratif(n):
    """Versi iteratif fibonacci — jauh lebih efisien (O(n) memori)."""
    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ============================================================
# D. CHALLENGE — Pangkat (a^n) Rekursif
# ============================================================

def pangkat_rekursif(a, n):
    """
    Menghitung a^n secara rekursif.
    Base Case    : n == 0  → return 1
    Recursive Case: return a * pangkat_rekursif(a, n-1)
    """
    if n < 0:
        raise ValueError("n tidak boleh negatif!")
    if n == 0:
        return 1                              # Base Case
    return a * pangkat_rekursif(a, n - 1)    # Recursive Case


# ============================================================
# HELPER: Tampilkan Perbandingan
# ============================================================

def bandingkan_waktu(nama_fungsi, rekursif_fn, iteratif_fn, arg):
    print(f"\n  [{nama_fungsi}({arg})]")

    t0 = time.perf_counter()
    hasil_r = rekursif_fn(arg)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    hasil_i = iteratif_fn(arg)
    t3 = time.perf_counter()

    print(f"  Rekursif : {hasil_r}  (waktu: {(t1-t0)*1000:.4f} ms)")
    print(f"  Iteratif : {hasil_i}  (waktu: {(t3-t2)*1000:.4f} ms)")
    print(f"  Hasil sama? {'✓ YA' if hasil_r == hasil_i else '✗ TIDAK'}")


# ============================================================
# PROGRAM UTAMA
# ============================================================

def main():
    print("=" * 55)
    print("   ALGORITMA DAN PEMROGRAMAN 2 — PERTEMUAN 3")
    print("        Rekursi vs. Iterasi — Demo Lengkap")
    print("=" * 55)

    # ---- A. Faktorial ----
    print("\n" + "─" * 55)
    print("A. FAKTORIAL (n = 3, 5, 7)")
    print("─" * 55)
    for n in [3, 5, 7]:
        bandingkan_waktu("Faktorial", faktorial_rekursif, faktorial_iteratif, n)

    # ---- A. Trace Rekursi ----
    print("\n" + "─" * 55)
    print("A. TRACE CALL STACK — faktorial(4)")
    print("─" * 55)
    hasil = faktorial_trace(4)
    print(f"\n  Hasil Akhir faktorial(4) = {hasil}")

    # ---- B. Jumlah 1..n ----
    print("\n" + "─" * 55)
    print("B. JUMLAH 1 s.d. n (Rekursif vs Iteratif)")
    print("─" * 55)
    for n in [5, 10, 15]:
        bandingkan_waktu("Jumlah", jumlah_rekursif, jumlah_iteratif, n)

    # ---- C. Fibonacci ----
    print("\n" + "─" * 55)
    print("C. FIBONACCI (n = 5, 6, 10)")
    print("─" * 55)
    for n in [5, 6, 10]:
        bandingkan_waktu("Fibonacci", fibonacci, fibonacci_iteratif, n)

    print("\n  [Observasi Fibonacci n=20 — rekursi mulai lambat]")
    t0 = time.perf_counter()
    fibonacci(20)
    t1 = time.perf_counter()
    print(f"  fibonacci(20) rekursif selesai dalam {(t1-t0)*1000:.2f} ms")

    # ---- D. Pangkat (Challenge) ----
    print("\n" + "─" * 55)
    print("D. CHALLENGE — Pangkat a^n (Rekursif)")
    print("─" * 55)
    test_pangkat = [(2, 10), (3, 5), (5, 4)]
    for a, n in test_pangkat:
        hasil = pangkat_rekursif(a, n)
        print(f"  pangkat_rekursif({a}, {n}) = {hasil}  [verifikasi: {a}^{n} = {a**n}]")

    # ---- Validasi Input Negatif ----
    print("\n" + "─" * 55)
    print("D. CHALLENGE — Validasi Input Negatif")
    print("─" * 55)
    for val in [-1, -5]:
        try:
            faktorial_rekursif(val)
        except ValueError as e:
            print(f"  faktorial_rekursif({val}) → ERROR: {e}")

    # ---- Kesimpulan Perbandingan ----
    print("\n" + "=" * 55)
    print("  KESIMPULAN: Rekursi vs. Iterasi")
    print("=" * 55)
    print("""
  ┌──────────────────┬─────────────────┬────────────────────┐
  │ Aspek            │ Rekursi         │ Iterasi            │
  ├──────────────────┼─────────────────┼────────────────────┤
  │ Mekanisme        │ Function call   │ Loop (for/while)   │
  │ Memori           │ Call Stack (++)  │ Satu variabel      │
  │ Keterbacaan      │ Elegan/ringkas  │ Kadang lebih panjang│
  │ Perlu            │ Base Case       │ Kondisi loop       │
  │ Bahaya           │ Infinite recur. │ Infinite loop      │
  └──────────────────┴─────────────────┴────────────────────┘

  Kapan pakai Rekursi?
   • Masalah dapat dipecah jadi sub-masalah identik
   • Struktur pohon / data bercabang (misal: Fibonacci, pohon direktori)
   • Algoritma Divide and Conquer (misal: Merge Sort, Quick Sort)

  Kapan pakai Iterasi?
   • Komputasi linear sederhana (faktorial, sum, dll.)
   • Performa & memori menjadi prioritas utama
    """)
    print("=" * 55)


if __name__ == "__main__":
    main()
