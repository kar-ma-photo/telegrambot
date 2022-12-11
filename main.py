import sqlite3
import telebot
from telebot import types


bot = telebot.TeleBot("5635009160:AAFw76CFWiBUFxTlLSHGYNrZySAWDRN8ttQ")

conn = sqlite3.connect('bd/database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(name: str, user_id: int, plus: int):
    cursor.execute('INSERT INTO event1 (name, user_id, plus) VALUES (?, ?, ?)',
                   (name, user_id, plus))
    conn.commit()




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Хочу прийти на вечер")
    btn2 = types.KeyboardButton("Пожертвовать")
    btn3 = types.KeyboardButton("Кто будет петь?")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Что хочешь сделать?".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Пожертвовать"):
        bot.send_message(message.chat.id, text="https://www.sberbank.com/ru/person/dl/jc?linkname=Yztbi8ULKAaN26SQQ")
    elif (message.text == "Хочу прийти на вечер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Один/одна")
        btn2 = types.KeyboardButton("+1")
        btn3 = types.KeyboardButton("+2")
        btn4 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Ты придешь один/одна или с друзьями?", reply_markup=markup)

    elif (message.text == "Один/одна"):
        name = message.from_user.first_name
        user_id = message.from_user.id
        plus = 1
        db_table_val(name=name, user_id=user_id, plus=plus)
        bot.send_message(message.chat.id, text="Отлично, записали!")
    elif (message.text == "+1"):
        name = message.from_user.first_name
        user_id = message.from_user.id
        plus = 2
        db_table_val(name=name, user_id=user_id, plus=plus)
        bot.send_message(message.chat.id, text="Отлично, записали!")
    elif (message.text == "+2"):
        name = message.from_user.first_name
        user_id = message.from_user.id
        plus = 3
        db_table_val(name=name, user_id=user_id, plus=plus)
        bot.send_message(message.chat.id, text="Отлично, записали!")


    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу прийти на вечер")
        btn2 = types.KeyboardButton("Пожертвовать")
        btn3 = types.KeyboardButton("Кто будет петь?")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Привет, {0.first_name}! Что хочешь сделать?".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Кто будет петь?"):

        bot.send_message(message.chat.id,
                         text="'Егор не помню'. Больше песен этой замечательной группы - в группе Вконтакте: https://vk.com/egornepomnyu")
        photo = open('img/egor.jpg', 'rb')

        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         text="Минутку, сейчас всё выгрузим...")
        audio = open('audio/Егор не помню спасите кота.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()

        bot.send_message(message.chat.id,
                         text="'Морфинизм пыльцы', Проходим по ссылке и слушаем https://vk.com/morfinizm")
        photo = open('img/morfinism.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         text="Ещё пару мгновений...")
        audio = open('audio/Морфинизм Пыльцы - Пост-бард.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()






    else:
        bot.send_message(message.chat.id, text="Я тебя не понимаю, котик")


bot.polling(none_stop=True)