import telebot
import time
import random
import threading

# ضع هنا توكن البوت الخاص بك
TOKEN = "8337489100:AAFGQ0G7k-EURcWhvrvhoXR1RQ1nj85Coj4"
CHANNEL_ID = "@gshhsjsjssiwi"  # اسم القناة مع @

bot = telebot.TeleBot(TOKEN)

# قائمة العملات
coins = [
    "$BTC", "$ETH", "$SOL", "$AVAX", "$DOGE", "$XRP", "$ENA", "$PUMP",
    "$XPLUS", "$BNB", "$AKE", "$MIRA", "$ORDER", "$LIGHT", "$XAN", "$FF",
    "$EDEN", "$NOM", "$TRUTH", "$Z", "$EVAA", "$AI", "$COAI", "$TRADOO",
    "$BLESS", "$DOOD", "$ASTER", "$BABY", "$ALCH", "$PTB", "$C", "$BARD",
    "$LINEA", "$M", "$MYX", "$VFY", "$BID", "$FORM", "$USELESS", "$DASH",
    "$PLUMP", "$EPIC", "$XVG", "$MYRO", "$AEO", "$IOU", "$PROVE", "$CELO",
    "$ASTR", "$YGG", "$OG", "$MUBARAK", "$VVV"
]

# تحليلات عشوائية قصيرة
analyses = [
    "المؤشرات توحي ببداية تصحيح بسيط قبل الارتداد 💹",
    "ضغط بيعي خفيف لكن الاتجاه العام صاعد 📈",
    "احتمال ارتداد قريب من مناطق الدعم القوية 🔄",
    "السيولة المنخفضة قد تسبب حركة عنيفة ⚠️",
    "العملة تتحرك بشكل عرضي، انتظر الكسر 🔍",
    "تجميع واضح في المستويات الحالية 💎",
    "الزخم في ازدياد، راقب مناطق الدخول 🔥",
]

def send_signal(coin):
    analysis = random.choice(analyses)
    message = f"""
🎯 خطة الصفقة (للعقود الآجلة)

🚀 سيناريو الشراء 

دخول مثالي: عند **منطقة الدعم الحالية**
الهدف الأول: +5%
الهدف الثاني: +10%
وقف الخسارة: أسفل آخر قاع

---

⚠️ ملاحظات مهمة:
{analysis}

📊 العملة: {coin}

مع تحيات أخوكم عبودي 💚  
لا تنسَ المتابعة واللايك والشير للقناة لنستمر بالمزيد 🔥
"""
    bot.send_message(CHANNEL_ID, message, parse_mode="Markdown")

def auto_poster():
    while True:
        for coin in coins:
            send_signal(coin)
            time.sleep(60)  # دقيقة واحدة بين كل توصية

threading.Thread(target=auto_poster).start()

print("✅ البوت يعمل الآن وينشر توصيات تلقائية كل دقيقة")
bot.polling(none_stop=True)
