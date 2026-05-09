import telebot # type: ignore
from config import TG_BOT_TOKEN, ADMIN_CHAT_ID
from messages import command_start_message, command_add_user_message, command_delete_user_message, success_add_user_message, success_delete_user_message
from database import Database

bot = telebot.TeleBot(TG_BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, command_start_message)
@bot.message_handler(commands=['add_user'])
def add_user_command(message):
    if message.chat.id == ADMIN_CHAT_ID:
        bot.send_message(message.chat.id, command_add_user_message)
        bot.register_next_step_handler(message, add_user)
def add_user(message):
    chat_id = message.text
    with Database() as db:
        db.add_user(chat_id)
    bot.send_message(message.chat.id, success_add_user_message.format(chat_id))
@bot.message_handler(commands=['delete_user'])
def delete_user_command(message):
    if message.chat.id == ADMIN_CHAT_ID:
        bot.send_message(message.chat.id, command_delete_user_message)
        bot.register_next_step_handler(message, delete_user)
def delete_user(message):
    chat_id = message.text
    with Database() as db:
        db.delete_user(chat_id)
    bot.send_message(message.chat.id, success_delete_user_message.format(chat_id))
def send_message(chat_id, text):
    bot.send_message(chat_id, text)
@bot.message_handler(commands=['get_id'])
def get_id(message):
    bot.send_message(message.chat.id, f'Ваш chat_id: {message.chat.id}')

def bot_polling():
    bot.polling()
if __name__ == '__main__':
    print('Telegram bot started')
    bot_polling()
    print('Telegram bot stopped')