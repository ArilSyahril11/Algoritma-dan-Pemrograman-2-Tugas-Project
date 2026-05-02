# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 2
# Latihan 2 + Challenge: Modularisasi Program Bangun Datar
# ============================================================
# Dekomposisi Modular:
#   [1] luas_persegi(sisi)             → menghitung luas persegi
#   [2] luas_persegi_panjang(p, l)     → menghitung luas persegi panjang
#   [3] luas_lingkaran(jari)           → menghitung luas lingkaran
#   [4] keliling_persegi(sisi)         → menghitung keliling persegi
#   [5] keliling_persegi_panjang(p, l) → menghitung keliling persegi panjang
#   [6] keliling_lingkaran(jari)       → menghitung keliling lingkaran
#   [7] tampilkan_menu()               → menampilkan menu pilihan
#   [8] main()                         → program utama/orkestrasi
# ============================================================

import math


# --- FUNGSI LUAS ---

def luas_persegi(sisi):
    """Menghitung luas persegi. RETURN: float"""
    return sisi * sisi


def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang. RETURN: float"""
    return panjang * lebar


def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran. RETURN: float"""
    return math.pi * jari_jari * jari_jari


# --- FUNGSI KELILING ---

def keliling_persegi(sisi):
    """Menghitung keliling persegi. RETURN: float"""
    return 4 * sisi


def keliling_persegi_panjang(panjang, lebar):
    """Menghitung keliling persegi panjang. RETURN: float"""
    return 2 * (panjang + lebar)


def keliling_lingkaran(jari_jari):
    """Menghitung keliling (circumference) lingkaran. RETURN: float"""
    return 2 * math.pi * jari_jari


# --- FUNGSI TAMPILAN ---

def tampilkan_menu():
    """Menampilkan menu pilihan bangun datar."""
    print("\n" + "=" * 40)
    print("     KALKULATOR BANGUN DATAR")
    print("=" * 40)
    print("  1. Persegi")
    print("  2. Persegi Panjang")
    print("  3. Lingkaran")
    print("  0. Keluar")
    print("=" * 40)


def tampilkan_hasil_bangun(nama, luas, keliling):
    """Menampilkan luas dan keliling bangun datar."""
    print(f"\n  [{nama}]")
    print(f"  Luas      : {luas:.4f}")
    print(f"  Keliling  : {keliling:.4f}")


# --- PROGRAM UTAMA ---

def main():
    # Demo pengujian otomatis
    print("=" * 40)
    print("   [DEMO OTOMATIS BANGUN DATAR]")
    print("=" * 40)

    # Persegi sisi=5
    s = 5
    tampilkan_hasil_bangun(
        f"Persegi (sisi={s})",
        luas_persegi(s),
        keliling_persegi(s)
    )

    # Persegi Panjang panjang=8, lebar=4
    p, l = 8, 4
    tampilkan_hasil_bangun(
        f"Persegi Panjang (p={p}, l={l})",
        luas_persegi_panjang(p, l),
        keliling_persegi_panjang(p, l)
    )

    # Lingkaran r=7
    r = 7
    tampilkan_hasil_bangun(
        f"Lingkaran (r={r})",
        luas_lingkaran(r),
        keliling_lingkaran(r)
    )

    # Mode interaktif
    print("\n[Mode Interaktif]")
    while True:
        tampilkan_menu()
        try:
            pilih = int(input("Pilih menu: "))

            if pilih == 0:
                print("\nKeluar dari program.")
                break

            elif pilih == 1:
                sisi = float(input("  Masukkan sisi: "))
                if sisi <= 0:
                    print("  Dimensi harus positif!")
                    continue
                tampilkan_hasil_bangun(
                    "Persegi",
                    luas_persegi(sisi),
                    keliling_persegi(sisi)
                )

            elif pilih == 2:
                panjang = float(input("  Masukkan panjang: "))
                lebar   = float(input("  Masukkan lebar  : "))
                if panjang <= 0 or lebar <= 0:
                    print("  Dimensi harus positif!")
                    continue
                tampilkan_hasil_bangun(
                    "Persegi Panjang",
                    luas_persegi_panjang(panjang, lebar),
                    keliling_persegi_panjang(panjang, lebar)
                )

            elif pilih == 3:
                jari = float(input("  Masukkan jari-jari: "))
                if jari <= 0:
                    print("  Jari-jari harus positif!")
                    continue
                tampilkan_hasil_bangun(
                    "Lingkaran",
                    luas_lingkaran(jari),
                    keliling_lingkaran(jari)
                )

            else:
                print("  Pilihan tidak valid!")

        except ValueError:
            print("  Input tidak valid! Masukkan angka.")

    print("\nTerima kasih!")


if __name__ == "__main__":
    main()
