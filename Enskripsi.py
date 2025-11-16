def enkripsi_caesar(teks, shift):
    hasil = ""
    for char in teks:
        if char.isalpha():  
            kode = ord(char)
            if char.isupper():
                hasil += chr((kode - 65 + shift) % 26 + 65)
            else:
                hasil += chr((kode - 97 + shift) % 26 + 97)
        else:
            hasil += char  
    return hasil

def dekripsi_caesar(teks, shift):
    return enkripsi_caesar(teks, -shift)

if __name__ == "__main__":
    print("=== Program Enkripsi - Caesar Cipher ===")
    teks = input("Masukkan teks: ")
    shift = int(input("Masukkan kunci pergeseran : "))

    teks_terenkripsi = enkripsi_caesar(teks, shift)
    print(f"\nHasil Enkripsi  : {teks_terenkripsi}")

    teks_dekripsi = dekripsi_caesar(teks_terenkripsi, shift)
    print(f"Hasil Dekripsi  : {teks_dekripsi}")
