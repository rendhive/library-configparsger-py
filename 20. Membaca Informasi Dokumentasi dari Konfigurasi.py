import configparser

config = configparser.ConfigParser()
config.read('doc_config.ini')

print("Title:", config['DOCUMENTATION']['Title'])
print("Version:", config['DOCUMENTATION']['Version'])
print("Author:", config['DOCUMENTATION']['Author'])
# Fungsi: Membaca informasi dokumentasi dari file konfigurasi.
# Kondisi: Ketika Anda ingin menampilkan informasi penting tentang aplikasi.
