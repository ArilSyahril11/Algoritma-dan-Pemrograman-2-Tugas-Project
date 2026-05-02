# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 2
# Latihan 1: Modularisasi Program Nilai Mahasiswa
# ============================================================
# Dekomposisi Modular:
#   [1] input_nilai()       → mengambil input dari user
#   [2] validasi_nilai()    → memvalidasi rentang nilai 0–100
#   [3] hitung_nilai()      → menghitung nilai akhir berbobot
#   [4] tentukan_grade()    → menentukan grade huruf
#   [5] tampilkan_hasil()   → menampilkan output ke layar
# ============================================================


# --- LAYER DEFINISI FUNGSI ---

def input_nilai():
    """
    Fungsi untuk menerima input nilai dari pengguna.
    OUTPUT: tuple (tugas, uts, uas)
    """
    print("\n[Input Nilai]")
    tugas = float(input("  Nilai Tugas (0-100): "))
    uts   = float(input("  Nilai UTS   (0-100): "))
    uas   = float(input("  Nilai UAS   (0-100): "))
    return tugas, uts, uas


def validasi_nilai(tugas, uts, uas):
    """
    Fungsi untuk memvalidasi bahwa semua nilai di rentang 0–100.
    RETURN: True jika valid, False jika tidak
    """
    return (0 <= tugas <= 100) and (0 <= uts <= 100) and (0 <= uas <= 100)


def hitung_nilai(tugas, uts, uas):
    """
    Fungsi untuk menghitung nilai akhir dengan bobot:
      Tugas 30%, UTS 30%, UAS 40%
    RETURN: nilai_akhir (float)
    """
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)


def tentukan_grade(nilai_akhir):
    """
    Fungsi untuk menentukan grade berdasarkan nilai akhir.
    RETURN: grade huruf (str)
    """
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'


def tampilkan_hasil(tugas, uts, uas, nilai_akhir, grade):
    """
    Fungsi untuk menampilkan hasil akhir ke layar.
    """
    print("\n" + "=" * 40)
    print("         HASIL NILAI AKHIR")
    print("=" * 40)
    print(f"  Nilai Tugas  : {tugas:.1f}")
    print(f"  Nilai UTS    : {uts:.1f}")
    print(f"  Nilai UAS    : {uas:.1f}")
    print("-" * 40)
    print(f"  Nilai Akhir  : {nilai_akhir:.2f}")
    print(f"  Grade        : {grade}")
    print("=" * 40)


# --- PROGRAM UTAMA (Orkestrasi) ---

def main():
    print("=" * 40)
    print("  PROGRAM NILAI AKHIR MAHASISWA (MODULAR)")
    print("=" * 40)

    # Pengujian otomatis minimal 3 kombinasi
    test_cases = [
        (90, 85, 88),
        (70, 65, 72),
        (40, 45, 50),
    ]

    print("\n[Pengujian Otomatis - 3 Kombinasi]")
    for i, (t, u, ua) in enumerate(test_cases, 1):
        print(f"\n--- Data Mahasiswa {i} ---")
        if validasi_nilai(t, u, ua):
            na    = hitung_nilai(t, u, ua)
            grade = tentukan_grade(na)
            tampilkan_hasil(t, u, ua, na, grade)
        else:
            print("  Input tidak valid!")

    # Mode interaktif
    print("\n[Mode Interaktif]")
    while True:
        lanjut = input("\nHitung nilai baru? (y/n): ").lower()
        if lanjut != 'y':
            break
        try:
            tugas, uts, uas = input_nilai()
            if validasi_nilai(tugas, uts, uas):
                nilai_akhir = hitung_nilai(tugas, uts, uas)
                grade       = tentukan_grade(nilai_akhir)
                tampilkan_hasil(tugas, uts, uas, nilai_akhir, grade)
            else:
                print("  Input tidak valid! Nilai harus antara 0–100.")
        except ValueError:
            print("  Input tidak valid! Masukkan angka.")

    print("\nTerima kasih!")


if __name__ == "__main__":
    main()
