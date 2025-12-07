import configparser

config = configparser.ConfigParser()
config.read('multi_section_config.ini')

database_name = config['DATABASE']['DatabaseName']
user = config['DATABASE']['User']
print(f"Connecting to {database_name} as {user}")
# Fungsi: Menggunakan data dari file konfigurasi untuk koneksi database.
# Kondisi: Ketika Anda ingin menggunakan pengaturan koneksi dari file konfigurasi.
