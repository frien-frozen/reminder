import os
import threading
import time
import schedule
from fastapi import FastAPI
import uvicorn
from telegram import Bot

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=TOKEN)

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

def run_web():
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

def send(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

def morning():
    send("Good morning legend 🌅 Ready to cook today? From 5 to 7 it’s TLF Maths. Lock in.")

def tlf_maths():
    send("5–7 PM: TLF Maths time. Focus mode on. You got this.")

def study_block(day):
    if day == "Monday":
        send("Today’s plan: Asian Championship 1h, Edexcel Physics 1h, Develop Knowly 1h, then chill 1h. Start strong.")
    elif day == "Tuesday":
        send("Today’s plan: Edexcel Maths 1h, Edexcel CS 1h, Develop Knowly 1h, rest 1h. Keep the pace.")
    elif day == "Wednesday":
        send("Today’s plan: Asian Championship 1h, Edexcel Physics 1h, Edexcel Maths 1h, rest 1h. Midweek grind.")
    elif day == "Thursday":
        send("Today’s plan: Edexcel CS 1h, Develop Knowly 1h, Asian Championship 1h, rest 1h. Finish strong.")

def checkin():
    send("How’s it going? Still focused or need to reset? Take a breath and continue.")

threading.Thread(target=run_web, daemon=True).start()

schedule.every().day.at("08:00").do(morning)
schedule.every().day.at("17:00").do(tlf_maths)
schedule.every().monday.at("19:00").do(lambda: study_block("Monday"))
schedule.every().tuesday.at("19:00").do(lambda: study_block("Tuesday"))
schedule.every().wednesday.at("19:00").do(lambda: study_block("Wednesday"))
schedule.every().thursday.at("19:00").do(lambda: study_block("Thursday"))
schedule.every().day.at("18:30").do(checkin)

while True:
    schedule.run_pending()
    time.sleep(30)