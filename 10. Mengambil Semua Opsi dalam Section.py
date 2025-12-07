import configparser

config = configparser.ConfigParser()
config.read('config.ini')

for option in config['DEFAULT']:
    print(option, ":", config['DEFAULT'][option])
# Fungsi: Mengambil semua opsi dalam section tertentu.
# Kondisi: Ketika Anda ingin menampilkan semua pengaturan yang terkait di dalam section.
