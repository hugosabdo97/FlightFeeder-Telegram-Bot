FlightFeeder Monitoring Bot
Bot Telegram ini digunakan untuk memonitor perangkat FlightFeeder dari FlightAware, menampilkan status perangkat, daftar pesawat dalam jangkauan radar, serta memberikan notifikasi jika ada pesawat yang masuk atau keluar dari jangkauan radar.

Fitur
/status: Menampilkan status perangkat FlightFeeder.
/detail [hex_code]: Menampilkan detail pesawat berdasarkan kode hex.
/list_now: Menampilkan daftar pesawat yang saat ini terdeteksi oleh radar.
Notifikasi otomatis saat pesawat masuk atau keluar jangkauan radar.

Persyaratan
Python 3.x
Library Python:
python-telegram-bot
requests

Cara Install :

Pastikan Python 3.x terpasang.
Instal dependency yang diperlukan:
pip install python-telegram-bot requests

Buat bot Telegram menggunakan @BotFather.
Simpan token API yang diberikan.

cd FlightFeeder-Telegram-Bot
nano ff_tele.py
masukan token dari botfather dan chat id
save

running python3 ff_tele.py

disarankan running as service
