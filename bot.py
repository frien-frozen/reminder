import os
import time
import schedule
import random
from telegram import Bot
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError("Set BOT_TOKEN and CHAT_ID environment variables")

bot = Bot(token=BOT_TOKEN)

# Function to send messages and log in Render
def send(text):
    bot.send_message(chat_id=CHAT_ID, text=text)
    print(f"{datetime.now()} ✅ Sent: {text}")

# 🌅 Morning greeting (Mon–Thu)
for day in ["monday", "tuesday", "wednesday", "thursday"]:
    getattr(schedule.every(), day).at("08:30").do(
        send, "🌅 Good morning! Fresh day ahead. What’s your top goal today?"
    )

# 🔒 Daily TLF Maths (Mon–Thu) — 5:00–7:00 PM
for day in ["monday", "tuesday", "wednesday", "thursday"]:
    getattr(schedule.every(), day).at("17:00").do(
        send, "🔥 5:00–7:00 PM: TLF Maths. Phone away, focus on problems. Let’s cook 🧠"
    )

# 📅 Monday
schedule.every().monday.at("19:00").do(send, "📘 7:00–8:00 PM: Edexcel Physics. Small steps > perfect steps.")
schedule.every().monday.at("20:00").do(send, "🏆 8:00–9:00 PM: Asian Championship Prep. Stay sharp.")
schedule.every().monday.at("21:00").do(send, "😌 9:00–9:30 PM: Rest. Breathe. You earned it.")

# 📅 Tuesday
schedule.every().tuesday.at("19:00").do(send, "➗ 7:00–8:00 PM: Edexcel Maths. Clean solutions, no rush.")
schedule.every().tuesday.at("20:00").do(send, "🚀 8:00–9:00 PM: Develop Knowly. Ship something small.")
schedule.every().tuesday.at("21:00").do(send, "🎮 9:00–9:30 PM: Gaming time. No guilt, just vibes.")

# 📅 Wednesday
schedule.every().wednesday.at("19:00").do(send, "💻 7:00–8:00 PM: Edexcel CS. Think like a compiler 🤓")
schedule.every().wednesday.at("20:00").do(send, "🏆 8:00–9:00 PM: Asian Championship Prep. One more push.")
schedule.every().wednesday.at("21:00").do(send, "😌 9:00–9:30 PM: Chill. Stretch a bit.")

# 📅 Thursday
schedule.every().thursday.at("19:00").do(send, "🎉 7:00–8:00 PM: Finish study + reward yourself. Close loops.")
schedule.every().thursday.at("20:00").do(send, "🧠 8:00–9:00 PM: Free revision. Patch weak spots.")
schedule.every().thursday.at("21:00").do(send, "🎮 9:00–9:30 PM: Game time. Then log off and sleep well.")

# 💬 Mid-evening check-in (Mon–Thu)
for day in ["monday", "tuesday", "wednesday", "thursday"]:
    getattr(schedule.every(), day).at("18:30").do(
        send, "👀 Quick check-in: how’s it going so far? Stuck or flowing?"
    )

# 🌙 Night wrap-up (Mon–Thu)
for day in ["monday", "tuesday", "wednesday", "thursday"]:
    getattr(schedule.every(), day).at("21:25").do(
        send, "🌙 Wrap-up: name 1 win from today. Tiny wins count."
    )

# 🎉 Random friendly messages every 2–3 hours
friendly_messages = [
    "💬 How’s it going? Remember to take tiny breaks!",
    "💡 Fun fact: Even 5 mins of review can make a big difference.",
    "😎 Keep pushing! Small progress is still progress.",
    "☕ Don’t forget water. Brain fuel, my friend!",
    "🧠 Focus time! You got this.",
    "🎶 Hum your favorite song while studying — mood boost!"
]

def random_friendly():
    msg = random.choice(friendly_messages)
    send(msg)

# Random messages: every 2 hours from 10:00–20:00
for hour in range(10, 20, 2):
    schedule.every().monday.at(f"{hour:02}:10").do(random_friendly)
    schedule.every().tuesday.at(f"{hour:02}:10").do(random_friendly)
    schedule.every().wednesday.at(f"{hour:02}:10").do(random_friendly)
    schedule.every().thursday.at(f"{hour:02}:10").do(random_friendly)

print("🤖 Friendly Telegram Study Bot is running...")
while True:
    try:
        schedule.run_pending()
    except Exception as e:
        send(f"⚠️ Bot error: {e}")
        print(f"⚠️ Bot error: {e}")
    time.sleep(30)