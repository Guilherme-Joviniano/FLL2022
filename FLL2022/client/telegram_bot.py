
import time as tm
import math
import os
import sys
from typing import KeysView, Text
from local import get_dist_van_to_local, get_user_local
from telegram import chat, message, user
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from telegram.ext import Updater
import telegram
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
count = 0 

API_KEY = '5047659265:AAHsZ9qn1EXTEOyK6tmqtjukVxNk99hRBq4'
bot = telegram.Bot(token=API_KEY)
#local dates  
#id of the package sende
package_id = '1234'
try: 
    chat_id = bot.get_updates()[-1].message.chat_id
except IndexError:
    chat_id = 0
    
print('Telegram Client Bot start...')

def face_check(update, context):
    
    mensagem = str(update.message.text).lower()
    user_messages = str(mensagem).lower()
    
    if user_messages in ('/start'):
        context.bot.send_message(chat_id = get_chat_id(update,context), text = 'Olá, Porfavor manda a foto da sua RG para que possamos fazer o reconhecimento facial na hora da entrega.')    
    #add the id of the product to know the exactly location of the certain product.
            #Running the script to know the distance between the user and the van. if location is lessier than 10 metters the telegram bot will say that the van arrived             
    if user_messages in (package_id):
        count == 1
        print('Running localization script...')
        tm.sleep(5)
        dist = get_dist_van_to_local()
        while dist > 10:
            print('wating...')
        print('arrived')
        context.bot.send_message(chat_id= get_chat_id(update,context), text = 'Sua Encomenda Chegou 📦')
        context.bot.send_message(chat_id= get_chat_id(update, context), text ='Você está a camera da AutoVan?')
    if user_messages in ('Sim','sim', 's','Yes'):
        print('Running faces_check script...')
        context.bot.send_message(chat_id=get_chat_id(update,context), text = 'Iniciando reconhecimento facial')
        tm.sleep(10)
        os.system("client/faces_check.py")
        tm.sleep(5)

def get_chat_id(update, context):
  chat_id = -1
  if update.message is not None:
    # from a text message
    chat_id = update.message.chat.id
  elif update.callback_query is not None:
    # from a callback message
    chat_id = update.callback_query.message.chat.id
  return chat_id

def start_command(update, context):
    update.message.reply_text("Hi, i'm bot to verify you face in the sysytem of delivery, send me a picuture of yourface, and when your package arrived, it will be liberate with your face : )")

def help_command(update, context):
    update.message.reply_text('Menu de ajuda')

def handle_pictures(update, context):
    user_picture = bot.getFile(update.message.photo[-1].file_id) 
    if count < 1:   
        context.bot.send_message(chat_id = get_chat_id(update,context), text = 'Agora digite o ID do seu produto.')    
    #user_picture = context.bot.getFile(file_id)
    user_picture.download("client/faces_checkImages/user-image.png") 
    face_check(update, context)

def handle_message(update,context):
    mensagem = str(update.message.text).lower()
    user_messages= str(mensagem).lower()
    print(user_messages)
    #write here the conditions! 
def error(update, context ):
    print(f'Update {update} caused error {context.error}')

def main():
    
    updater = Updater(API_KEY, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('inicio', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    
    dp.add_handler(MessageHandler(Filters.text, face_check))
    dp.add_handler(MessageHandler(Filters.photo, handle_pictures))
    dp.add_error_handler(error)
    updater.start_polling(2)
    updater.idle()
    
while True:
        main()