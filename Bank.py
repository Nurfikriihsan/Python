class ATM:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def cek_saldo(self):
        return self.saldo

    def tarik_tunai(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup")
        else:
            self.saldo -= jumlah
            print(f"Tarik tunai sebesar Rp {jumlah} berhasil")

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setor tunai sebesar Rp {jumlah} berhasil")

def main():
    atm = ATM(1000000)  # saldo awal Rp 1.000.000
    while True:
        print("\nMenu ATM:")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            print(f"Saldo Anda: Rp {atm.cek_saldo()}")
        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah tarik tunai: "))
            atm.tarik_tunai(jumlah)
        elif pilihan == "3":
            jumlah = int(input("Masukkan jumlah setor tunai: "))
            atm.setor_tunai(jumlah)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan ATM")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()