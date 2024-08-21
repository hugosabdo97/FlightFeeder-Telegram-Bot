import requests
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, JobQueue

TELEGRAM_TOKEN = '729xxxx:xxxxxxxxxxxxxxxxx'
STATUS_URL = "http://172.16.50.253/status.json"
AIRCRAFT_URL = "http://172.16.50.253/skyaware/data/aircraft.json"

detected_aircraft = set()

def get_status():
    response = requests.get(STATUS_URL)
    data = response.json()
    status_message = (
        f"*FlightFeeder Status:*\n"
        f"Software Version: `{data['software_version']}`\n"
        f"Serial: `{data['serial']}`\n"
        f"CPU Load: `{data['cpu_load_percent']}%`\n"
        f"Uptime: `{data['system_uptime']} seconds`\n"
        f"CPU Temperature: `{data['cpu_temp_celcius']}°C`\n"
        f"[Site URL]({data['site_url']})"
    )
    return status_message

def status(update: Update, context: CallbackContext):
    status_message = get_status()
    update.message.reply_text(status_message, parse_mode=ParseMode.MARKDOWN)

def aircraft_detail(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text("Gunakan: /detail [hex_code]")
        return

    hex_code = context.args[0]
    response = requests.get(AIRCRAFT_URL)
    aircraft_data = response.json()["aircraft"]

    for aircraft in aircraft_data:
        if aircraft.get("hex") == hex_code:
            flight = aircraft.get("flight", "Unknown Flight")
            altitude = aircraft.get("alt_baro", "Unknown")
            speed = aircraft.get("gs", "Unknown")
            lat = aircraft.get("lat", "Unknown")
            lon = aircraft.get("lon", "Unknown")
            category = aircraft.get("category", "Unknown")
            detail_message = (
                f"*Detail Pesawat {flight}* (Hex: `{hex_code}`):\n"
                f"Kategori: `{category}`\n"
                f"Ketinggian: `{altitude} ft`\n"
                f"Kecepatan: `{speed} knots`\n"
                f"Lokasi: `{lat}, {lon}`"
            )
            update.message.reply_text(detail_message, parse_mode=ParseMode.MARKDOWN)
            return

    update.message.reply_text(f"Pesawat dengan Hex: `{hex_code}` tidak ditemukan.", parse_mode=ParseMode.MARKDOWN)

def list_now(update: Update, context: CallbackContext):
    response = requests.get(AIRCRAFT_URL)
    aircraft_data = response.json()["aircraft"]

    if not aircraft_data:
        update.message.reply_text("Tidak ada pesawat dalam cakupan radar saat ini.")
    else:
        categories = {}
        for aircraft in aircraft_data:
            category = aircraft.get("category", "Unknown")
            flight = aircraft.get("flight", "Unknown Flight")
            hex_code = aircraft.get("hex")
            altitude = aircraft.get("alt_baro", "Unknown")
            speed = aircraft.get("gs", "Unknown")
            categories.setdefault(category, []).append(f"`{flight}` (Hex: `{hex_code}`) - `{altitude} ft`, `{speed} knots`")

        message = (
            f"*Total pesawat dalam cakupan radar: {len(aircraft_data)}*\n"
            f"{'-'*30}\n"
        )
        for category, aircrafts in categories.items():
            message += f"\n*Kategori {category}:*\n" + "\n".join(aircrafts) + "\n"

        update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)

def monitor_aircraft(context: CallbackContext):
    global detected_aircraft
    response = requests.get(AIRCRAFT_URL)
    aircraft_data = response.json()["aircraft"]

    current_hexes = {aircraft.get("hex") for aircraft in aircraft_data}
    
    # Deteksi pesawat baru yang masuk jangkauan
    for aircraft in aircraft_data:
        hex_code = aircraft.get("hex")
        if hex_code not in detected_aircraft:
            detected_aircraft.add(hex_code)
            flight = aircraft.get("flight", "Unknown Flight")
            altitude = aircraft.get("alt_baro", "Unknown")
            speed = aircraft.get("gs", "Unknown")
            category = aircraft.get("category", "Unknown")
            message = (
                f"*Pesawat {flight}* (Hex: `{hex_code}`) terdeteksi:\n"
                f"Kategori: `{category}`\n"
                f"Ketinggian: `{altitude} ft`\n"
                f"Kecepatan: `{speed} knots`"
            )
            context.bot.send_message(chat_id=context.job.context, text=message, parse_mode=ParseMode.MARKDOWN)

    # Deteksi pesawat yang keluar jangkauan
    for hex_code in detected_aircraft.copy():
        if hex_code not in current_hexes:
            context.bot.send_message(chat_id=context.job.context, text=f"Pesawat dengan Hex: `{hex_code}` sudah keluar dari jangkauan.", parse_mode=ParseMode.MARKDOWN)
            detected_aircraft.remove(hex_code)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    job_queue = updater.job_queue

    dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("detail", aircraft_detail))
    dp.add_handler(CommandHandler("list_now", list_now))

    # Schedule monitoring job,masukan chat ID di XXXXX
    job_queue.run_repeating(monitor_aircraft, interval=10, first=0, context=xxxxxxx)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
