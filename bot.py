import telebot 
from telebot.types import Message 
from telebot import types

from itertools import cycle
import numpy as np

from rail_fence import encode_rail_fence_cipher, decode_rail_fence_cipher

TOKEN = '1205700823:AAEpDgfc9v_L-RmaKk8N04NfwZnWG4AvMrM'
bot = telebot.TeleBot(TOKEN)


global inputs
inputs = []



# //////////////////// Block Start ////////////////////
@bot.message_handler(commands=['start'])
def start(message: Message):
	bot.reply_to(message, 'Я бот, созданный Аланом Тьюрингом, для работы с Шифром Железнодорожной Изгороди. Для дешифрования введите /decrypt, для шифрования введите /encrypt ')



# //////////////////// Block Decrypt ////////////////////
@bot.message_handler(commands=['decrypt'])
def decrypt(message: Message):
	message = bot.reply_to(message, 'Введите шифрованный текст, который хотите дешифровать')
	bot.register_next_step_handler(message, decode_text)


def decode_text(message: Message):
	global inputs
	inputs.append(message.text)

	message = bot.reply_to(message, 'Хорошо, теперь введите ключ дешифрования(любое целое число, не превышающие количества символов в шифрованном тексте')
	bot.register_next_step_handler(message, decode_key)


def decode_key(message: Message):
	global inputs
	inputs.append(message.text)
	
	try:
		message = bot.reply_to(message, '{}'.format(decode_rail_fence_cipher(inputs[0], int(inputs[1]))))

	except:
		message = bot.reply_to(message, 'Что-то пошло не так :/')
		
	inputs = []



# //////////////////// Block Encrypt ////////////////////
@bot.message_handler(commands=['encrypt'])
def encrypt(message: Message):
	message = bot.reply_to(message, 'Введите текст, который хотите зашифровать')
	bot.register_next_step_handler(message, encrypt_text)


def encrypt_text(message: Message):
	global inputs
	inputs.append(message.text)

	message = bot.reply_to(message, 'Хорошо, теперь введите ключ шифрования(любое целое число, не превышающие количества символов в тексте')
	bot.register_next_step_handler(message, encrypt_key)


def encrypt_key(message: Message):
	global inputs
	inputs.append(message.text)
	
	try:
		message = bot.reply_to(message, '{}'.format(encode_rail_fence_cipher(inputs[0], int(inputs[1]))))

	except:
		message = bot.reply_to(message, 'Что-то пошло не так :/')
	inputs = []




bot.polling(timeout=70000)
