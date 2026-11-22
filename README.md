# FlightFeeder Telegram Monitoring Bot

A Telegram bot designed to monitor FlightAware FlightFeeder devices. It reports real-time receiver status, lists aircraft currently within radar range, provides detailed aircraft info via hex code, and sends automated radar zone alerts. 

The bot fetches live JSON data dumped by the `tar1090` service running on the FlightFeeder receiver.

## 🚀 Features
- **`/status`**: Check the operational health and status of the FlightFeeder device.
- **`/list_now`**: Display all aircraft currently detected by the radar.
- **`/detail [hex_code]`**: View specific details for an aircraft using its hex code.
- **Automated Alerts**: Real-time notifications when aircraft enter or leave the radar tracking range.

---

## 📋 Requirements
- Python 3.8+
- Required Python libraries:
  - `python-telegram-bot` (v13.7)
  - `requests`

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/hugosabdo97/FlightFeeder-Telegram-Bot.git
cd FlightFeeder-Telegram-Bot
```

### 2. Install Dependencies
```bash
pip install python-telegram-bot==13.7 requests
```

### 3. Create a Telegram Bot
1. Message [@BotFather](https://t.me/BotFather) on Telegram to create a new bot and obtain your **Telegram Bot Token**.
2. Retrieve your **Telegram Chat ID** (you can use bots like `@userinfobot`).

### 4. Configure `ff_tele.py`
Open `ff_tele.py` in your text editor:
```bash
nano ff_tele.py
```

Update the configuration variables with your details:
```python
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
STATUS_URL = "http://YOUR_FLIGHTFEEDER_IP/status.json"
AIRCRAFT_URL = "http://YOUR_FLIGHTFEEDER_IP/skyaware/data/aircraft.json"

# In the job queue section, replace 'xxxxxxx' with your Telegram Chat ID:
job_queue.run_repeating(monitor_aircraft, interval=10, first=0, context=YOUR_CHAT_ID)
```
Save and close the file.

---

## ▶️ Running the Bot

### Manual Execution
```bash
python3 ff_tele.py
```

### Production (Background Service)
It is highly recommended to run the bot persistently using a **systemd service** or **GNU Screen**:

#### Using Screen:
```bash
screen -S flightfeeder-bot
python3 ff_tele.py
# Press Ctrl+A then D to detach
```
