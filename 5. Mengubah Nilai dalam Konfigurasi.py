import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config['DEFAULT']['ServerPort'] = '9090'  # Mengubah nilai ServerPort

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print("Nilai ServerPort berhasil diubah.")
# Fungsi: Mengubah nilai dari konfigurasi yang ada.
# Kondisi: Ketika Anda perlu memperbarui pengaturan yang sudah ada.
