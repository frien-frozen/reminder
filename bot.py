import os
import time
import threading
import random
import schedule
from datetime import datetime, date
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

os.environ["TZ"] = "Asia/Tashkent"
time.tzset()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=BOT_TOKEN)
app_tg = ApplicationBuilder().token(BOT_TOKEN).build()

app = FastAPI()

paused = False
streak = 0
last_done = None

motivations = [
    "Small steps every day build unstoppable momentum.",
    "Your future self is watching. Don’t disappoint them.",
    "Discipline today creates freedom tomorrow.",
    "You are closer than you think. Keep going.",
    "Consistency beats motivation."
]

@app.api_route("/", methods=["GET", "HEAD"])
async def root(request: Request):
    return JSONResponse({"status": "ok"})

def send(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg)

def random_motivation():
    return random.choice(motivations)

def tlf_maths():
    if not paused:
        send("5:00–7:00 TLF Maths time 🧠 Lock in. " + random_motivation())

def block(msg):
    if not paused:
        send(msg + " " + random_motivation())

def daily_wrap():
    if not paused:
        send("Wrap-up time 🌙 Be proud of today. " + random_motivation())

def weekday_plan():
    d = datetime.now().weekday()
    if d == 0:
        block("Today focus: Asian Championship and Edexcel Physics")
    elif d == 1:
        block("Today focus: Edexcel Maths and Edexcel CS")
    elif d == 2:
        block("Today focus: Develop Knowly and Physics revision")
    elif d == 3:
        block("Today focus: Mixed revision and problem solving")

schedule.every().day.at("05:00").do(tlf_maths)
schedule.every().day.at("09:00").do(weekday_plan)
schedule.every().day.at("12:00").do(block, "Midday check-in 👀 Stay consistent.")
schedule.every().day.at("17:00").do(block, "Evening focus session 🔥 Final push.")
schedule.every().day.at("21:30").do(daily_wrap)

def scheduler_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running. Reminders active.")

async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global paused
    paused = True
    await update.message.reply_text("Reminders paused.")

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global paused
    paused = False
    await update.message.reply_text("Reminders resumed.")

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global streak, last_done
    today = date.today()
    if last_done == today:
        await update.message.reply_text("Already counted for today.")
        return
    if last_done == today.replace(day=today.day - 1):
        streak += 1
    else:
        streak = 1
    last_done = today
    await update.message.reply_text(f"Nice work. Current streak: {streak} days.")

app_tg.add_handler(CommandHandler("status", status))
app_tg.add_handler(CommandHandler("pause", pause))
app_tg.add_handler(CommandHandler("resume", resume))
app_tg.add_handler(CommandHandler("done", done))

threading.Thread(target=scheduler_loop, daemon=True).start()
threading.Thread(target=app_tg.run_polling, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)