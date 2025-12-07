import configparser

config = configparser.ConfigParser()
config.read('config.ini')

sections = config.sections()
print("Semua sections dalam file:", sections)
# Fungsi: Mengambil semua section yang ada dalam file konfigurasi.
# Kondisi: Ketika Anda ingin melihat semua pengaturan yang ada.
