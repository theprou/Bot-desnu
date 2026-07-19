import telebot
import google.generativeai as genai
import time

TOKEN = "8952147732:AAE53xfyPZyADUFs613zXxPnKCZzNzXb3f8"
CLAVE = "AQ.Ab8RN6JU80NtzucXTmeZeKav12kh8D8SBXqob3mN-aTMPJGz_8w"

bot = telebot.TeleBot(TOKEN)
genai.configure(api_key=CLAVE)
modelo = genai.GenerativeModel("gemini-1.5-flash")

@bot.message_handler(commands=["start"])
def bienvenida(msg):
    bot.send_message(msg.chat.id, "✅ ¡Hola! Ya estoy listo. Pregúntame lo que quieras.")

@bot.message_handler(func=lambda m: True)
def responder(msg):
    try:
        res = modelo.generate_content(msg.text)
        bot.reply_to(msg, res.text)
    except Exception as e:
        print(f"ERROR: {e}")
        bot.reply_to(msg, f"Ups: {str(e)}")

print("✅ BOT INICIADO!")
while True:
    try:
        bot.polling(non_stop=True, interval=1, timeout=20)
    except Exception as e:
        print(f"Reconectando: {e}")
        time.sleep(5)
      
