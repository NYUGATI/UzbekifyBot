import telebot
import random

# Вставь сюда свой токен от BotFather
TOKEN = "ТОКЕН_ТВОЕГО_БОТА"
bot = telebot.TeleBot(TOKEN)

# Замена гласных
vowel_map = {"а": "о", "и": "о", "е": "о", "у": "о", "я": "о", "ы": "о", "ю": "о", "э": "о"}

# Окончания для имён
male_suffixes = ["джон", "бек", "хон", "улло"]
female_suffixes = ["ой", "хон", "зор"]

# Функция для изменения фамилии
def transform_surname(surname):
    if surname.endswith("ский"):
        return surname[:-4] + "ов"
    elif surname.endswith("енко"):
        return surname[:-4] + "онов"
    elif surname.endswith(("ин", "ов", "ев")):
        return surname + "ов"
    else:
        return surname + "ов"

# Функция для узбекизации имени
def uzbekify_name(full_name, gender="male"):
    parts = full_name.split()
    
    uzbek_name = "".join([vowel_map.get(char, char) for char in parts[0].lower()]).capitalize()
    
    if gender == "male":
        uzbek_name += random.choice(male_suffixes)
    else:
        uzbek_name += random.choice(female_suffixes)
    
    uzbek_surname = transform_surname(parts[1]) if len(parts) > 1 else ""
    
    return f"{uzbek_name} {uzbek_surname}"

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне любое имя, и я сделаю его узбекским. Если имя мужское, напиши '/m', если женское — '/f'.")

# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()
    gender = "male" if text.endswith("/m") else "female" if text.endswith("/f") else "male"
    
    if text.endswith("/m") or text.endswith("/f"):
        text = text[:-2].strip()
    
    uzbek_name = uzbekify_name(text, gender)
    bot.reply_to(message, f"✅ Узбекская версия: {uzbek_name}")

# Запуск бота
bot.polling()
          
