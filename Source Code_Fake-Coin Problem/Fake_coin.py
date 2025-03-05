import random

koin_asli = 1.0
koin_palsu = 0.9  

def acak_koin(jumlah_koin):
    """Membuat daftar koin dengan satu koin palsu dan mengacaknya"""
    global koin  
    koin = [koin_asli] * (jumlah_koin - 1) + [koin_palsu]  # Satu koin palsu dimasukkan
    random.shuffle(koin)  
    return koin  

def timbang(koin1, koin2):
    """Membandingkan berat dua kelompok koin"""
    berat_kiri = sum(koin1)
    berat_kanan = sum(koin2)

    if berat_kiri < berat_kanan:
        return -1  # Bagian kiri lebih ringan
    elif berat_kiri > berat_kanan:
        return 1   # Bagian kanan lebih ringan
    else:
        return 0   # Kedua bagian sama berat

def cari_koin_palsu(kiri, kanan):
    """Menemukan koin palsu dengan membagi koin sesuai prosedur yang diberikan"""
    if kiri == kanan:  # Basis rekursi: hanya satu koin tersisa
        print(f"Koin palsu ada di indeks {kiri + 1} dengan berat {koin[kiri]}")
        return
    
    jumlah_koin = kanan - kiri + 1  # Hitung jumlah koin yang tersisa

    if jumlah_koin % 2 == 1:  # Jika jumlah koin ganjil, sisihkan satu koin terakhir
        koin_terakhir = kanan
        kanan -= 1  
    else:
        koin_terakhir = None  # Tidak ada koin yang disisihkan

    tengah = (kanan + kiri) // 2  # Bagi dua bagian
    hasil_timbangan = timbang(koin[kiri:tengah + 1], koin[tengah + 1:kanan + 1])

    if hasil_timbangan == -1:  # Bagian kiri lebih ringan
        cari_koin_palsu(kiri, tengah)
    elif hasil_timbangan == 1:  # Bagian kanan lebih ringan
        cari_koin_palsu(tengah + 1, kanan)
    else:  # Jika kedua bagian sama berat, koin yang disisihkan adalah yang palsu
        print(f"Koin palsu ada di indeks {koin_terakhir + 1} dengan berat {koin[koin_terakhir]}")

jumlah_koin = int(input("Masukkan jumlah koin: "))
acak_koin(jumlah_koin)
print("Daftar berat koin:", koin)  
cari_koin_palsu(0, jumlah_koin - 1)
