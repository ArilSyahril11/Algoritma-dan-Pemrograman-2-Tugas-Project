101# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 1
# Latihan 1: Implementasi Kasus Diskon
# ============================================================
# IPO Analysis:
#   INPUT  : total_belanja (float)
#   PROCESS: Cek kondisi diskon menggunakan if-elif-else
#            - >= 500000 → diskon 20%
#            - >= 250000 → diskon 10%
#            - lainnya   → diskon 0%
#            Hitung total_bayar = total_belanja - diskon
#   OUTPUT : nominal diskon & total bayar
# ============================================================

def hitung_diskon(total_belanja):
    """Menghitung diskon berdasarkan total belanja."""
    if total_belanja >= 500000:
        diskon = 0.20 * total_belanja
    elif total_belanja >= 250000:
        diskon = 0.10 * total_belanja
    else:
        diskon = 0

    total_bayar = total_belanja - diskon
    return diskon, total_bayar


def main():
    print("=" * 45)
    print("     PROGRAM KALKULATOR DISKON BELANJA")
    print("=" * 45)
    print("Aturan Diskon:")
    print("  • Belanja >= Rp500.000  → Diskon 20%")
    print("  • Belanja >= Rp250.000  → Diskon 10%")
    print("  • Belanja < Rp250.000   → Tanpa Diskon")
    print("=" * 45)

    # Pengujian wajib dengan 3 variasi input
    test_inputs = [600000, 300000, 100000]

    for total_belanja in test_inputs:
        diskon, total_bayar = hitung_diskon(total_belanja)
        persen = (diskon / total_belanja * 100) if total_belanja > 0 else 0

        print(f"\nTotal Belanja : Rp{total_belanja:,.0f}")
        print(f"Diskon ({persen:.0f}%)   : Rp{diskon:,.0f}")
        print(f"Total Bayar   : Rp{total_bayar:,.0f}")
        print("-" * 45)

    # Mode interaktif
    print("\n[Mode Interaktif]")
    while True:
        try:
            inp = input("\nMasukkan total belanja (atau 'q' untuk keluar): Rp")
            if inp.lower() == 'q':
                break
            total_belanja = float(inp)
            if total_belanja < 0:
                print("Input tidak valid! Total belanja tidak boleh negatif.")
                continue
            diskon, total_bayar = hitung_diskon(total_belanja)
            persen = (diskon / total_belanja * 100) if total_belanja > 0 else 0
            print(f"Diskon ({persen:.0f}%)   : Rp{diskon:,.0f}")
            print(f"Total Bayar   : Rp{total_bayar:,.0f}")
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    print("\nTerima kasih!")


if __name__ == "__main__":
    main()
