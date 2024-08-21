Script di atas adalah bot Telegram untuk memonitor perangkat FlightFeeder dari FlightAware. Bot ini memiliki beberapa fitur utama:

/status: Menampilkan informasi status perangkat dari URL JSON yang diberikan.
/detail [hex_code]: Memberikan detail spesifik dari pesawat berdasarkan kode hex.
/list_now: Menampilkan daftar pesawat yang saat ini berada dalam jangkauan radar.
Monitoring Pesawat: Memberikan notifikasi otomatis ketika pesawat baru masuk jangkauan radar atau keluar dari jangkauan.
Bot ini secara berkala memeriksa pesawat dalam jangkauan dan mengirimkan notifikasi di Telegram sesuai dengan data JSON yang diterima.

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
