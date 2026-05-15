# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 7
# Topik: Integrasi Searching, Sorting, dan Modular Programming
# Simulasi UTS — Sistem Pengolahan Nilai Mahasiswa
# ============================================================
# Pipeline Sistem (IPO Terintegrasi):
#   INPUT  → input_data_mahasiswa()
#   PROSES → hitung_nilai_akhir()  [berbobot, dengan validasi]
#          → bubble_sort_desc()    [urutkan nilai tertinggi]
#          → insertion_sort_desc() [versi alternatif - challenge]
#          → linear_search()       [cari mahasiswa by nama]
#          → binary_search()       [cari nilai - data sudah terurut]
#   OUTPUT → tampilkan_data()      [laporan terstruktur]
#
# Analisis Kompleksitas Total:
#   input_data()      : O(n)
#   hitung_nilai()    : O(n)
#   bubble_sort()     : O(n²) worst, O(n) best
#   insertion_sort()  : O(n²) worst, O(n) best
#   linear_search()   : O(n)
#   binary_search()   : O(log n)  -- setelah data terurut
#   tampilkan_data()  : O(n)
#   ─────────────────────────────
#   TOTAL DOMINAN     : O(n²)  -- didominasi oleh sorting
# ============================================================

import time


# ============================================================
# LAYER 1 — INPUT
# ============================================================

def input_data_mahasiswa(demo=False):
    """
    Menerima input data mahasiswa dari pengguna.
    Setiap mahasiswa memiliki: nama, nilai tugas, UTS, UAS.

    Kompleksitas: O(n) — loop sebanyak jumlah mahasiswa.

    RETURN: list of dict [{'nama', 'tugas', 'uts', 'uas'}, ...]
    """
    data = []

    if demo:
        # Data demo untuk pengujian otomatis (tanpa input manual)
        raw = [
            ("Andi Pratama",    80, 75, 88),
            ("Budi Santoso",    65, 70, 72),
            ("Citra Dewi",      90, 88, 95),
            ("Deni Saputra",    55, 60, 58),
            ("Eva Maharani",    78, 82, 85),
            ("Fajar Nugroho",   40, 45, 50),
            ("Gita Rahayu",     92, 95, 97),
            ("Hendra Wijaya",   70, 68, 75),
        ]
        for nama, t, u, ua in raw:
            data.append({'nama': nama, 'tugas': t, 'uts': u, 'uas': ua})
        return data

    jumlah = int(input("Jumlah mahasiswa: "))
    for i in range(jumlah):
        print(f"\n--- Mahasiswa {i+1} ---")
        nama  = input("  Nama       : ")
        tugas = float(input("  Nilai Tugas (0-100): "))
        uts   = float(input("  Nilai UTS   (0-100): "))
        uas   = float(input("  Nilai UAS   (0-100): "))
        data.append({'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas})
    return data


# ============================================================
# LAYER 2 — PROSES: Hitung Nilai
# ============================================================

def validasi_nilai_komponen(tugas, uts, uas):
    """
    Memvalidasi bahwa semua komponen nilai berada di rentang 0–100.
    Kompleksitas: O(1) — operasi konstan.
    RETURN: bool
    """
    return (0 <= tugas <= 100) and (0 <= uts <= 100) and (0 <= uas <= 100)


def hitung_nilai_akhir_satu(tugas, uts, uas):
    """
    Menghitung nilai akhir satu mahasiswa.
    Bobot: Tugas 30%, UTS 30%, UAS 40%.
    Kompleksitas: O(1).
    RETURN: float
    """
    return round((0.3 * tugas) + (0.3 * uts) + (0.4 * uas), 2)


def tentukan_grade(nilai):
    """
    Menentukan grade huruf berdasarkan nilai akhir.
    Kompleksitas: O(1).
    RETURN: str (A/B/C/D/E)
    """
    if nilai >= 85: return 'A'
    elif nilai >= 70: return 'B'
    elif nilai >= 60: return 'C'
    elif nilai >= 50: return 'D'
    else: return 'E'


def hitung_nilai(data):
    """
    Menghitung nilai akhir dan grade untuk semua mahasiswa.
    Menambahkan key 'nilai_akhir' dan 'grade' ke setiap dict.
    Kompleksitas: O(n) — satu iterasi seluruh data.
    RETURN: list of dict (data diperkaya)
    """
    hasil = []
    for mhs in data:
        if validasi_nilai_komponen(mhs['tugas'], mhs['uts'], mhs['uas']):
            na    = hitung_nilai_akhir_satu(mhs['tugas'], mhs['uts'], mhs['uas'])
            grade = tentukan_grade(na)
            hasil.append({**mhs, 'nilai_akhir': na, 'grade': grade, 'valid': True})
        else:
            hasil.append({**mhs, 'nilai_akhir': 0, 'grade': 'X', 'valid': False})
    return hasil


# ============================================================
# LAYER 3 — PROSES: Sorting
# ============================================================

def bubble_sort_desc(data):
    """
    Mengurutkan data mahasiswa berdasarkan nilai_akhir DESCENDING
    (nilai tertinggi di posisi pertama) menggunakan Bubble Sort.

    Mekanisme: bandingkan pasangan bersebelahan, tukar jika
    elemen kiri LEBIH KECIL dari elemen kanan (descending).

    Kompleksitas:
      Best Case : O(n)   — data sudah terurut descending
      Worst Case: O(n²)  — data terurut ascending
      Space     : O(1)   — in-place

    RETURN: (data_terurut, jumlah_perbandingan, jumlah_swap)
    """
    arr   = data[:]
    n     = len(arr)
    comp  = 0
    swap  = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comp += 1
            if arr[j]['nilai_akhir'] < arr[j+1]['nilai_akhir']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
                swapped = True
        if not swapped:
            break   # Optimasi: tidak ada swap → sudah terurut

    return arr, comp, swap


def insertion_sort_desc(data):
    """
    Mengurutkan data mahasiswa DESCENDING menggunakan Insertion Sort.
    Analogi: menyusun kartu dari yang terbesar ke terkecil.

    Mekanisme: ambil elemen ke-i, geser elemen sebelumnya yang
    lebih KECIL ke kanan, sisipkan di posisi tepat.

    Kompleksitas:
      Best Case : O(n)   — data sudah terurut descending (0 shift)
      Worst Case: O(n²)  — data terurut ascending
      Space     : O(1)   — in-place

    RETURN: (data_terurut, jumlah_perbandingan, jumlah_shift)
    """
    arr   = data[:]
    comp  = 0
    shift = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j   = i - 1
        while j >= 0 and arr[j]['nilai_akhir'] < key['nilai_akhir']:
            comp  += 1
            shift += 1
            arr[j+1] = arr[j]
            j -= 1
        if j >= 0:
            comp += 1    # perbandingan terakhir yang menghentikan loop
        arr[j+1] = key

    return arr, comp, shift


# ============================================================
# LAYER 4 — PROSES: Searching
# ============================================================

def linear_search(data, target_nama):
    """
    Mencari mahasiswa berdasarkan NAMA secara linear.
    Tidak memerlukan data terurut — cocok untuk pencarian by nama.

    Kompleksitas: O(n) worst case.

    RETURN: (indeks, jumlah_langkah) — indeks=-1 jika tidak ada
    """
    target_lower = target_nama.lower().strip()
    count = 0
    for i in range(len(data)):
        count += 1
        if data[i]['nama'].lower().strip() == target_lower:
            return i, count
    return -1, count


def binary_search_nilai(data, target_nilai):
    """
    Mencari mahasiswa berdasarkan NILAI AKHIR menggunakan Binary Search.
    SYARAT: data harus sudah terurut (descending setelah sorting).
    Karena data terurut descending, arah pencarian dibalik.

    Kompleksitas: O(log n).

    RETURN: (indeks, jumlah_langkah) — indeks=-1 jika tidak ada
    """
    low   = 0
    high  = len(data) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if data[mid]['nilai_akhir'] == target_nilai:
            return mid, count
        elif data[mid]['nilai_akhir'] > target_nilai:
            low = mid + 1      # nilai lebih kecil ada di kanan (descending)
        else:
            high = mid - 1     # nilai lebih besar ada di kiri (descending)

    return -1, count


# ============================================================
# LAYER 5 — OUTPUT
# ============================================================

def tampilkan_data(data, judul="DATA MAHASISWA"):
    """
    Menampilkan seluruh data mahasiswa dalam format tabel terstruktur.
    Kompleksitas: O(n).
    """
    print("\n" + "=" * 72)
    print(f"  {judul}")
    print("=" * 72)
    print(f"  {'No':>3} | {'Nama':<20} | {'Tugas':>5} | {'UTS':>5} | "
          f"{'UAS':>5} | {'Nilai Akhir':>11} | {'Grade':>5}")
    print("  " + "-" * 68)

    for i, mhs in enumerate(data, 1):
        status = "" if mhs.get('valid', True) else " [INVALID]"
        print(f"  {i:>3} | {mhs['nama']:<20} | {mhs['tugas']:>5.1f} | "
              f"{mhs['uts']:>5.1f} | {mhs['uas']:>5.1f} | "
              f"{mhs['nilai_akhir']:>11.2f} | {mhs['grade']:>5}{status}")

    print("=" * 72)


def tampilkan_statistik(data):
    """
    Menghitung dan menampilkan statistik ringkas dari seluruh data.
    Kompleksitas: O(n).
    """
    valid = [m for m in data if m.get('valid', True)]
    if not valid:
        print("  Tidak ada data valid.")
        return

    nilai_list = [m['nilai_akhir'] for m in valid]
    rata  = sum(nilai_list) / len(nilai_list)
    maks  = max(nilai_list)
    mins  = min(nilai_list)

    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    for m in valid:
        dist[m['grade']] += 1

    print("\n" + "─" * 50)
    print("  STATISTIK KELAS")
    print("─" * 50)
    print(f"  Jumlah mahasiswa : {len(valid)}")
    print(f"  Nilai tertinggi  : {maks:.2f}")
    print(f"  Nilai terendah   : {mins:.2f}")
    print(f"  Rata-rata kelas  : {rata:.2f}")
    print(f"  Distribusi Grade : ", end="")
    print("  ".join(f"{g}={dist[g]}" for g in ['A','B','C','D','E']))
    print("─" * 50)


# ============================================================
# ANALISIS KOMPLEKSITAS — FUNGSI HELPER
# ============================================================

def bandingkan_sorting(data):
    """
    Membandingkan Bubble Sort vs Insertion Sort pada data yang sama.
    Menampilkan jumlah perbandingan dan shift/swap masing-masing.
    """
    print("\n" + "=" * 65)
    print("  CHALLENGE — Bubble Sort vs Insertion Sort")
    print("=" * 65)

    t0 = time.perf_counter()
    _, b_comp, b_swap = bubble_sort_desc(data)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    _, i_comp, i_shift = insertion_sort_desc(data)
    t3 = time.perf_counter()

    print(f"\n  Data: {len(data)} mahasiswa")
    print(f"\n  {'Metrik':<25} | {'Bubble Sort':>13} | {'Insertion Sort':>14}")
    print("  " + "-" * 57)
    print(f"  {'Perbandingan':<25} | {b_comp:>13} | {i_comp:>14}")
    print(f"  {'Operasi Tukar/Geser':<25} | {b_swap:>13} | {i_shift:>14}")
    print(f"  {'Waktu eksekusi (ms)':<25} | {(t1-t0)*1000:>13.4f} | {(t2-t3)*1000*-1:>14.4f}")
    print("  " + "-" * 57)

    pemenang = "Insertion Sort" if i_comp < b_comp else (
               "Bubble Sort" if b_comp < i_comp else "Seri")
    print(f"\n  Pemenang (lebih sedikit perbandingan): {pemenang}")
    print(f"""
  Analisis:
  Untuk data kecil (n < 20), Insertion Sort umumnya lebih efisien
  dari Bubble Sort karena:
   1. Insertion Sort tidak perlu menyelesaikan seluruh pass jika
      elemen sudah di posisi tepat — berhenti lebih awal.
   2. Bubble Sort selalu menyelesaikan seluruh loop luar meskipun
      dengan flag optimasi, sementara Insertion Sort per-elemen
      langsung disisipkan ke posisi yang benar.
   3. Jumlah shift Insertion Sort = jumlah inversion dalam data,
      sedangkan Bubble Sort selalu melakukan swap berulang untuk
      satu inversion yang sama.
  Pada data hampir terurut: Insertion Sort mendekati O(n).
  Pada data acak: keduanya setara di O(n²) secara asimtotik.
    """)
    print("=" * 65)


# ============================================================
# ANALISIS KOMPLEKSITAS TOTAL
# ============================================================

def cetak_analisis_kompleksitas():
    """Mencetak tabel analisis kompleksitas seluruh sistem."""
    print("\n" + "=" * 72)
    print("  ANALISIS KOMPLEKSITAS SISTEM TOTAL")
    print("=" * 72)
    print(f"  {'Fungsi':<28} | {'Kompleksitas':>14} | Keterangan")
    print("  " + "-" * 68)
    rows = [
        ("input_data_mahasiswa()",  "O(n)",      "Loop input n mahasiswa"),
        ("hitung_nilai()",          "O(n)",      "Loop kalkulasi n mahasiswa"),
        ("bubble_sort_desc()",      "O(n²)",     "Loop bersarang, worst case"),
        ("insertion_sort_desc()",   "O(n²)",     "Loop + while, worst case"),
        ("linear_search()",         "O(n)",      "Telusuri 1 per 1 by nama"),
        ("binary_search_nilai()",   "O(log n)",  "Bagi dua ruang pencarian"),
        ("tampilkan_data()",        "O(n)",      "Cetak n baris"),
        ("tampilkan_statistik()",   "O(n)",      "Scan nilai min/max/avg"),
    ]
    for fn, comp, ket in rows:
        print(f"  {fn:<28} | {comp:>14} | {ket}")

    print("  " + "─" * 68)
    print(f"  {'KOMPLEKSITAS TOTAL DOMINAN':<28} | {'O(n²)':>14} | "
          f"Didominasi oleh sorting")
    print("=" * 72)
    print("""
  Penjelasan Kompleksitas Total (≥5 kalimat):

  [1] Kompleksitas total suatu sistem ditentukan oleh komponen dengan
      kompleksitas TERTINGGI — dalam hal ini sorting (O(n²)).

  [2] Fungsi input, hitung_nilai, searching, dan tampilkan bersifat
      linear O(n), yang jauh lebih kecil dari O(n²) sehingga diabaikan
      dalam analisis asimtotik: O(n²) + O(n) + O(n) = O(n²).

  [3] Bubble Sort dengan n=100 mahasiswa membutuhkan hingga 4.950
      perbandingan (n*(n-1)/2), sedangkan Linear Search hanya 100
      — perbedaan 50× untuk ukuran data yang sama.

  [4] Setelah data diurutkan oleh sorting, Binary Search dapat
      digunakan untuk pencarian nilai dengan hanya O(log n) langkah,
      meningkatkan efisiensi pencarian secara dramatis.

  [5] Untuk sistem nyata dengan ribuan mahasiswa, sorting O(n²)
      harus diganti dengan algoritma O(n log n) seperti Merge Sort
      atau TimSort agar performa sistem tetap dapat diterima.

  [6] Strategi integrasi yang benar: lakukan sorting SATU KALI di
      awal, lalu manfaatkan Binary Search O(log n) untuk semua
      pencarian berikutnya — investasi O(n²) sekali, hemat O(log n)
      selamanya.
  """)
    print("=" * 72)


# ============================================================
# PROGRAM UTAMA
# ============================================================

def main():
    print("=" * 72)
    print("   ALGORITMA DAN PEMROGRAMAN 2 — PERTEMUAN 7")
    print("   Sistem Pengolahan Nilai Mahasiswa — Integrasi Algoritma")
    print("=" * 72)
    print("""
  Pipeline Sistem:
  INPUT → Hitung Nilai → Sorting (desc) → Searching → OUTPUT
  [O(n)]    [O(n)]         [O(n²)]          [O(n)]    [O(n)]
  """)

    # ─── STEP 1: INPUT ───────────────────────────────────────
    print("─" * 72)
    print("STEP 1 — INPUT DATA MAHASISWA (Demo Otomatis)")
    print("─" * 72)
    data_raw = input_data_mahasiswa(demo=True)
    print(f"  {len(data_raw)} mahasiswa berhasil diinput.")

    # ─── STEP 2: HITUNG NILAI ────────────────────────────────
    print("\n" + "─" * 72)
    print("STEP 2 — HITUNG NILAI AKHIR (Bobot: Tugas 30%, UTS 30%, UAS 40%)")
    print("─" * 72)
    data_hitung = hitung_nilai(data_raw)
    tampilkan_data(data_hitung, "DATA SEBELUM DIURUTKAN")

    # ─── STEP 3: SORTING ─────────────────────────────────────
    print("\n" + "─" * 72)
    print("STEP 3 — SORTING (Bubble Sort Descending)")
    print("─" * 72)
    data_sorted, b_comp, b_swap = bubble_sort_desc(data_hitung)
    print(f"  Bubble Sort selesai: {b_comp} perbandingan, {b_swap} swap")
    tampilkan_data(data_sorted, "DATA SETELAH DIURUTKAN (Nilai Tertinggi → Terendah)")
    tampilkan_statistik(data_sorted)

    # ─── STEP 4a: SEARCHING by NAMA (Linear Search) ──────────
    print("\n" + "─" * 72)
    print("STEP 4A — SEARCHING by NAMA (Linear Search)")
    print("─" * 72)
    nama_cari = [
        ("Citra Dewi",   "ada, peringkat 1"),
        ("Fajar Nugroho","ada, nilai rendah"),
        ("Rahmat Hidayat","tidak ada"),
    ]
    for nama, ket in nama_cari:
        idx, langkah = linear_search(data_sorted, nama)
        if idx != -1:
            mhs = data_sorted[idx]
            print(f"  Cari '{nama}' ({ket}):")
            print(f"    → Ditemukan di peringkat {idx+1}, "
                  f"Nilai Akhir: {mhs['nilai_akhir']}, Grade: {mhs['grade']}")
            print(f"    → Linear Search: {langkah} langkah")
        else:
            print(f"  Cari '{nama}' ({ket}):")
            print(f"    → Tidak ditemukan  ({langkah} langkah diperiksa)")

    # ─── STEP 4b: SEARCHING by NILAI (Binary Search) ─────────
    print("\n" + "─" * 72)
    print("STEP 4B — SEARCHING by NILAI (Binary Search — data sudah terurut)")
    print("─" * 72)
    nilai_cari = [93.10, 78.10, 99.99]
    for nv in nilai_cari:
        idx, langkah = binary_search_nilai(data_sorted, nv)
        if idx != -1:
            print(f"  Cari nilai {nv}: Ditemukan → {data_sorted[idx]['nama']} "
                  f"(peringkat {idx+1}), {langkah} langkah")
        else:
            print(f"  Cari nilai {nv}: Tidak ditemukan ({langkah} langkah)")

    # ─── STEP 5: CHALLENGE ───────────────────────────────────
    print("\n" + "─" * 72)
    print("STEP 5 — CHALLENGE: Bubble Sort vs Insertion Sort")
    print("─" * 72)
    bandingkan_sorting(data_hitung)

    # ─── STEP 6: ANALISIS KOMPLEKSITAS ───────────────────────
    cetak_analisis_kompleksitas()

    # ─── DEMO: Input Manual (optional) ───────────────────────
    print("\n" + "─" * 72)
    print("  MODE INPUT MANUAL (tekan Ctrl+C untuk lewati)")
    print("─" * 72)
    try:
        lanjut = input("\n  Ingin input data manual? (y/n): ").strip().lower()
        if lanjut == 'y':
            data_manual = input_data_mahasiswa(demo=False)
            data_manual = hitung_nilai(data_manual)
            data_sorted_m, mc, ms = bubble_sort_desc(data_manual)
            tampilkan_data(data_sorted_m, "HASIL INPUT MANUAL — TERURUT")
            tampilkan_statistik(data_sorted_m)
            print(f"\n  Sorting selesai: {mc} perbandingan, {ms} swap")

            nama = input("\n  Cari mahasiswa (nama): ")
            idx, lk = linear_search(data_sorted_m, nama)
            if idx != -1:
                mhs = data_sorted_m[idx]
                print(f"  Ditemukan: Peringkat {idx+1}, "
                      f"Nilai {mhs['nilai_akhir']}, Grade {mhs['grade']}")
                print(f"  Linear Search: {lk} langkah")
            else:
                print(f"  '{nama}' tidak ditemukan ({lk} langkah diperiksa)")
    except (KeyboardInterrupt, EOFError):
        print("\n  [Mode manual dilewati]")

    print("\n" + "=" * 72)
    print("  Program selesai. Semua komponen terintegrasi berhasil.")
    print("=" * 72)


if __name__ == "__main__":
    main()
