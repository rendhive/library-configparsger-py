import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config.remove_section('NEW_SECTION')  # Menghapus section yang ditambahkan sebelumnya

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print("Section 'NEW_SECTION' berhasil dihapus dari 'config.ini'.")
# Fungsi: Menghapus section dari file konfigurasi.
# Kondisi: Ketika Anda tidak perlu lagi menyimpan pengaturan dalam section tertentu.
