from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from config import CHANNELS

btnProfile = KeyboardButton('Профиль')
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btnProfile)


def menuChannels():
    keyboard = InlineKeyboardMarkup(row_width=1)

    for channel in CHANNELS:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        keyboard.insert(btn)

    btnDoneSub = InlineKeyboardButton(text='Я подписался', callback_data='subdone')
    keyboard.insert(btnDoneSub)
    return keyboard


def menuMain():
    keyboard = InlineKeyboardMarkup(row_width=1)

    btnMain = InlineKeyboardButton(text='Найти фильм по коду', callback_data='introduction')
    keyboard.insert(btnMain)
    return keyboard
