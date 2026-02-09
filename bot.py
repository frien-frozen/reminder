import os
import time
import threading
import schedule
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from telegram import Bot
from telegram.constants import ParseMode

os.environ["TZ"] = "Asia/Tashkent"
time.tzset()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({"status": "ok"})

@app.head("/")
def root_head():
    return JSONResponse({"status": "ok"})

def send(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode=ParseMode.HTML)

def morning():
    send("Good morning ☀️ Rise and shine. Today is another step closer to your goals. Let’s start strong.")

def tlf_maths():
    send("5:00–7:00 TLF Maths time 🧠 Focus hard, no distractions. You’ve got this.")

def session(msg):
    send(msg)

schedule.every().day.at("05:00").do(tlf_maths)
schedule.every().day.at("09:00").do(session, "You crushed the morning session 💪 Take a short break, hydrate, and reset.")
schedule.every().day.at("12:00").do(session, "Midday check-in 👀 How’s it going? Stay consistent.")
schedule.every().day.at("17:00").do(session, "Evening grind time 🔥 One more push today.")
schedule.every().day.at("21:30").do(session, "Day’s almost done 🌙 Wrap up, relax, and be proud of yourself.")

def scheduler_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=scheduler_loop, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)