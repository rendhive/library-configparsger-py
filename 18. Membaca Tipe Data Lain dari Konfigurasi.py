import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

volume = int(config['SETTINGS']['Volume'])
brightness = int(config['SETTINGS']['Brightness'])

print(f"Volume: {volume}, Brightness: {brightness}")
# Fungsi: Mengambil nilai numerik dari file konfigurasi.
# Kondisi: Ketika Anda memerlukan konversi dari string ke tipe data yang sesuai.
