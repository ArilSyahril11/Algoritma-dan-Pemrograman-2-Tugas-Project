# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 1
# Latihan 2: Implementasi Nilai Akhir Mahasiswa
# ============================================================
# IPO Analysis:
#   INPUT  : nilai tugas, UTS, UAS (float, 0–100)
#   PROCESS: Validasi input (0 <= nilai <= 100)
#            Hitung nilai_akhir = 0.3*tugas + 0.3*uts + 0.4*uas
#   OUTPUT : nilai akhir (float)
# ============================================================

def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir dengan bobot: Tugas 30%, UTS 30%, UAS 40%."""
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)


def validasi_nilai(tugas, uts, uas):
    """Memvalidasi bahwa semua nilai berada di rentang 0–100."""
    return (0 <= tugas <= 100) and (0 <= uts <= 100) and (0 <= uas <= 100)


def main():
    print("=" * 45)
    print("    PROGRAM KALKULATOR NILAI AKHIR MAHASISWA")
    print("=" * 45)
    print("Komponen Penilaian:")
    print("  • Tugas : 30%")
    print("  • UTS   : 30%")
    print("  • UAS   : 40%")
    print("=" * 45)

    # Pengujian dengan 3 kombinasi nilai
    test_cases = [
        (80, 75, 90, "Mahasiswa A"),
        (60, 55, 70, "Mahasiswa B"),
        (50, 45, 55, "Mahasiswa C"),
    ]

    print("\n[Pengujian Otomatis]")
    for tugas, uts, uas, nama in test_cases:
        if validasi_nilai(tugas, uts, uas):
            nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
            print(f"\n{nama}:")
            print(f"  Tugas={tugas}, UTS={uts}, UAS={uas}")
            print(f"  Nilai Akhir : {nilai_akhir:.2f}")
        else:
            print(f"\n{nama}: Input tidak valid!")
        print("-" * 45)

    # Mode interaktif
    print("\n[Mode Interaktif]")
    while True:
        try:
            inp = input("\nHitung nilai? (y/n): ").lower()
            if inp != 'y':
                break

            tugas = float(input("Nilai Tugas (0-100): "))
            uts   = float(input("Nilai UTS   (0-100): "))
            uas   = float(input("Nilai UAS   (0-100): "))

            if validasi_nilai(tugas, uts, uas):
                nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
                print(f"Nilai Akhir : {nilai_akhir:.2f}")
            else:
                print("Input tidak valid! Nilai harus antara 0–100.")
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    print("\nTerima kasih!")


if __name__ == "__main__":
    main()
