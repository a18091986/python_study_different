import telebot
from telebot import types
import db_handling

# Создаем экземпляр бота
bot = telebot.TeleBot('5019813886:AAEapnTOJJCF19GTTjUHqa3TLpsFGYZtdic')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, 'Я на связи. Напиши мне что-нибудь')

def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь')

@bot.message_handler(content_types=["text"])
def handle_text(message, f = ''):
    keybord = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no')
    keybord.add(key_yes)
    keybord.add(key_no)
    bot.send_message(message.from_user.id, f'{message.text} Отправить в БД?', reply_markup = keybord)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        print(call)
        if db_handling.insert_into_db(call.message):
            bot.send_message(call.message.chat.id, f'Ваши данные успешно добавлены в БД')
        else:
            bot.send_message(call.message.chat.id, f'Возникла ошибка')

    else:
        bot.send_message(call.message.chat.id, f'Хорошо, не буду добавлять в БД')
        bot.send_message(call.message.chat.id, f'Я на связи. Напиши мне что-нибудь')

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

# Запускаем бота
bot.polling(none_stop=True, interval=0)

