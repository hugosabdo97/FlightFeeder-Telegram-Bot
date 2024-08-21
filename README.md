# FlightFeeder Monitoring Bot

Bot Telegram ini digunakan untuk memonitor perangkat FlightFeeder dari FlightAware, menampilkan status perangkat, daftar pesawat dalam jangkauan radar, serta memberikan notifikasi jika ada pesawat yang masuk atau keluar dari jangkauan radar.

Fitur
/status: Menampilkan status perangkat FlightFeeder.
/detail [hex_code]: Menampilkan detail pesawat berdasarkan kode hex.
/list_now: Menampilkan daftar pesawat yang saat ini terdeteksi oleh radar.
Notifikasi otomatis saat pesawat masuk atau keluar jangkauan radar.

# Persyaratan
Python 3.x
Library Python:
python-telegram-bot
requests

# Cara Install :

Pastikan Python 3.x terpasang.
Instal dependency yang diperlukan:
pip install python-telegram-bot requests

Buat bot Telegram menggunakan @BotFather.
Simpan token API yang diberikan.

Clone Repository
git clone https://github.com/username/FlightFeeder-Telegram-Bot.git
cd FlightFeeder-Telegram-Bot
nano ff_tele.py

pada bagian

ELEGRAM_TOKEN = '729xxxx:xxxxxxxxxxxxxxxxx'
STATUS_URL = "http://Ipflightfeeder/status.json"
AIRCRAFT_URL = "http://Ipflightfeede/skyaware/data/aircraft.json"

# Schedule monitoring job,masukan chat ID di XXXXX
job_queue.run_repeating(monitor_aircraft, interval=10, first=0, context=xxxxxxx)

sesuaikan dengan milik anda,mulai telegram token,chat ID dan IP flightfeeder

save

running python3 ff_tele.py

disarankan running as service
