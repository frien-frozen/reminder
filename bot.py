import os
import time
import schedule
from telegram import Bot
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError("Set BOT_TOKEN and CHAT_ID environment variables")

bot = Bot(token=BOT_TOKEN)

def send(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

# 🌅 Morning greeting (Mon–Thu)
for day in ["monday", "tuesday", "wednesday", "thursday"]:
    getattr(schedule.every(), day).at("08:30").do(
        send, "🌅 Good morning! New day, fresh brain. You’ve got this. What’s your top goal today?"
    )

# 🔒 Daily TLF Maths (Mon–Thu) — 5:00–7:00 PM
for day in ["monday", "tuesday", "wednesday", "thursday"]:
    getattr(schedule.every(), day).at("17:00").do(
        send, "🔥 5:00–7:00 PM: TLF Maths time. Phone away, focus on problems. Let’s cook 🧠"
    )

# 📅 Monday
schedule.every().monday.at("19:00").do(send, "📘 7:00–8:00 PM: Edexcel Physics. Small steps > perfect steps.")
schedule.every().monday.at("20:00").do(send, "🏆 8:00–9:00 PM: Asian Championship prep. Stay sharp.")
schedule.every().monday.at("21:00").do(send, "😌 9:00–9:30 PM: Rest. Breathe. You earned it.")

# 📅 Tuesday
schedule.every().tuesday.at("19:00").do(send, "➗ 7:00–8:00 PM: Edexcel Maths. Clean solutions, no rush.")
schedule.every().tuesday.at("20:00").do(send, "🚀 8:00–9:00 PM: Develop Knowly. Ship something small.")
schedule.every().tuesday.at("21:00").do(send, "🎮 9:00–9:30 PM: Gaming time. No guilt, just vibes.")

# 📅 Wednesday
schedule.every().wednesday.at("19:00").do(send, "💻 7:00–8:00 PM: Edexcel CS. Think like a compiler 🤓")
schedule.every().wednesday.at("20:00").do(send, "🏆 8:00–9:00 PM: Asian Championship prep. One more push.")
schedule.every().wednesday.at("21:00").do(send, "😴 9:00–9:30 PM: Chill. Stretch a bit.")

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

print("🤖 Friendly Telegram Study Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(30)