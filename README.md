# FlightFeeder Monitoring Bot

Bot Telegram ini digunakan untuk memonitor perangkat FlightFeeder dari FlightAware, menampilkan status perangkat, daftar pesawat dalam jangkauan radar, serta memberikan notifikasi jika ada pesawat yang masuk atau keluar dari jangkauan radar. Source yang digunakan ialah hasil dump file JSON dari service tar1090 pada FLightFeeder.

Fitur
- /status: Menampilkan status perangkat FlightFeeder.
- /detail [hex_code]: Menampilkan detail pesawat berdasarkan kode hex.
- /list_now: Menampilkan daftar pesawat yang saat ini terdeteksi oleh radar.
- Notifikasi otomatis saat pesawat masuk atau keluar jangkauan radar.

# Persyaratan
Python 3.x
Library Python:
- python-telegram-bot v13.7
- requests

# Cara Install :

1. Pastikan Python 3.x terpasang.
2. Instal dependency yang diperlukan:
    - pip install python-telegram-bot requests

3. Buat bot Telegram menggunakan @BotFather.
4. Simpan token API yang diberikan.

5. Clone Repository
  - git clone https://github.com/username/FlightFeeder-Telegram-Bot.git
  - cd FlightFeeder-Telegram-Bot
6. Edit file ff_tele.py
  - nano ff_tele.py

7. pada bagian

- TELEGRAM_TOKEN = '729xxxx:xxxxxxxxxxxxxxxxx'
- STATUS_URL = "http://Ipflightfeeder/status.json"
- AIRCRAFT_URL = "http://Ipflightfeede/skyaware/data/aircraft.json"
- job_queue.run_repeating(monitor_aircraft, interval=10, first=0, context=xxxxxxx) / XXXX=chat ID

sesuaikan dengan milik anda,mulai telegram token,chat ID dan IP flightfeeder dan lalu save

8. jalankan script
- python3 ff_tele.py

# disarankan running as service atau bisa menggunakan screen
