# ============================================================
# Algoritma dan Pemrograman 2 - Pertemuan 1
# Latihan Mandiri (Challenge): Konversi Suhu
# ============================================================
# IPO Analysis:
#   INPUT  : suhu dalam Celcius (float)
#   PROCESS: Konversi ke Fahrenheit dan Kelvin
#            - Fahrenheit = (9/5 × C) + 32
#            - Kelvin     = C + 273.15
#   OUTPUT : nilai Fahrenheit dan Kelvin
# ============================================================

def celcius_ke_fahrenheit(celcius):
    """Mengkonversi suhu dari Celcius ke Fahrenheit."""
    return (9 / 5 * celcius) + 32


def celcius_ke_kelvin(celcius):
    """Mengkonversi suhu dari Celcius ke Kelvin."""
    return celcius + 273.15


def main():
    print("=" * 45)
    print("       PROGRAM KONVERSI SUHU")
    print("=" * 45)
    print("Rumus Konversi:")
    print("  • Fahrenheit = (9/5 × C) + 32")
    print("  • Kelvin     = C + 273.15")
    print("=" * 45)

    # Pengujian dengan beberapa nilai umum
    test_inputs = [0, 100, 37, -40]
    print("\n[Tabel Konversi Suhu]")
    print(f"{'Celcius':>10} | {'Fahrenheit':>12} | {'Kelvin':>10}")
    print("-" * 40)
    for c in test_inputs:
        f = celcius_ke_fahrenheit(c)
        k = celcius_ke_kelvin(c)
        print(f"{c:>9}°C | {f:>10.2f}°F | {k:>8.2f} K")

    # Mode interaktif
    print("\n[Mode Interaktif]")
    while True:
        try:
            inp = input("\nMasukkan suhu Celcius (atau 'q' untuk keluar): ")
            if inp.lower() == 'q':
                break
            celcius = float(inp)
            fahrenheit = celcius_ke_fahrenheit(celcius)
            kelvin     = celcius_ke_kelvin(celcius)
            print(f"  {celcius}°C  =  {fahrenheit:.2f}°F  =  {kelvin:.2f} K")
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    print("\nTerima kasih!")


if __name__ == "__main__":
    main()
