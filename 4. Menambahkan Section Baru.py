import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config['NEW_SECTION'] = {'Feature': 'Enabled', 'Version': '1.0'}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print("Section baru berhasil ditambahkan ke 'config.ini'.")
# Fungsi: Menambahkan section baru ke file konfigurasi.
# Kondisi: Ketika Anda ingin menambah konfigurasi baru di dalam file yang ada.
