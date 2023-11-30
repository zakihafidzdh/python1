import datetime

class Parkir :
    def __init__(self, nomor_plat, waktu_masuk, harga_perjam):
        self.nomor_plat = nomor_plat
        self.waktu_masuk = waktu_masuk
        self.waktu_keluar = None
        self.biaya_parkir = 0

    def get_nomor_plat(self):
        return self.nomor_plat
    
    def get_waktu_masuk(self):
        return self.waktu_masuk
    
    def set_waktu_keluar(self, waktu_keluar):
        self.waktu_keluar = waktu_keluar

    def hitung_biaya_parkir(self):
        selisih_waktu = self.waktu_keluar - self.waktu_masuk
        jumlah_jam = selisih_waktu.total_seconds () / 3600
        self.biaya_parkir = jumlah_jam * self.harga_perjam

    def get_biaya_parkir(self):
        return self.biaya_parkir
    
def main():
    parkir = (input("A 1351 WV"), datetime.datetime.now(), 20000)
    
    input("Tekan ENTER Untuk Keluar")

    parkir.set_waktu_keluar(datetime.datetime.now())

    parkir.hitung_biaya_parkir()

    print("-------------------------")
    print("     SELAMAT DATANG      ")
    print("-------------------------")
    print("Nomor Plat Kendaraan: ", parkir.get_nomor_plat())
    print("Waktu Masuk : ", parkir.get_waktu_masuk())
    print("Waktu Keluar : ", parkir.get_waktu_keluar())
    print("Biaya Parkir : ", parkir.get_biaya_parkir())
