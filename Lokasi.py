# Mengimpor modul dari pustaka phonenumbers
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Meminta pengguna untuk memasukkan nomor telepon
mobileNo = input("Masukkan nomor: ")

# Mengurai (parsing) nomor telepon yang dimasukkan
parsed_number = phonenumbers.parse(mobileNo)

# Menampilkan zona waktu dari nomor telepon
print("Zona Waktu:", timezone.time_zones_for_number(parsed_number))

# Menampilkan nama provider/operator dari nomor telepon
print("Provider:", carrier.name_for_number(parsed_number, "en"))

# Menampilkan lokasi negara dari nomor telepon
print("Negara:", geocoder.description_for_number(parsed_number, "en"))

# Memvalidasi apakah nomor telepon tersebut valid
print("Nomor Valid:", phonenumbers.is_valid_number(parsed_number))

# Mengecek apakah nomor tersebut memungkinkan (secara format dan panjang)
print("Kemungkinan Nomor Valid:", phonenumbers.is_possible_number(parsed_number))
