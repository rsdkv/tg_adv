from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint
from config import TOKEN

import markup as nav
import emoji

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# обработчик списка фильмов
with open('text_films.txt', encoding='utf8') as f:
    lines = f.readlines()
films_text = ''
for item in lines:
    films_text += item

# обработчик списка книг
with open('text_books.txt', encoding='utf8') as f:
    lines = f.readlines()
books_text = ''
for item in lines:
    books_text += item

# обработчик текста обучения
with open('text_edu.txt', encoding='utf8') as f:
    lines = f.readlines()
edu_text = ''
for item in lines:
    edu_text += item

# обработчик текста музыки
with open('text_musics.txt', encoding='utf8') as f:
    lines = f.readlines()
music_text = ''
for item in lines:
    music_text += item

# обработчик текста ссылок
with open('text_links.txt', encoding='utf8') as f:
    lines = f.readlines()
links_text = ''
for item in lines:
    links_text += item

# обработчик текста арбитража
with open('text_arbitrage.txt', encoding='utf8') as f:
    text_arbitrage = f.read()


# # старт
# @dp.message_handler(commands=['start', 'начать', 'старт'])
# async def command_start(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Привет {0.first_name} '
#                                                  'Напишите код фильма для поиска (+эмодзи) '
#                                                  ''.format(message.from_user),
#                            reply_markup=nav.mainMenu)


# # меню
# @dp.message_handler()
# async def with_puree(message: types.Message):
#     # главное меню
#     if message.text == 'Главное меню':
#         await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)
#     elif message.text == 'Учиться':
#         await bot.send_message(message.from_user.id,
#                                'Здесь вы можете найти всё, что вам может понадобиться для обучения:\n' + edu_text,
#                                reply_markup=nav.eduMenu)
#     elif message.text == 'Стать лучше':
#         await bot.send_message(message.from_user.id,
#                                'Здесь вы можете найти все, что вам может понадобиться. Выберите интересующую вас тему',
#                                reply_markup=nav.traderMenu)
#     elif message.text == 'Развлечься':
#         await bot.send_message(message.from_user.id, 'Вы можете не только развлечься, но и прокачать свой мозг',
#                                reply_markup=nav.libraryMenu)
#         # библиотека подменю
#     elif message.text == 'Фильмы':
#         await bot.send_message(message.from_user.id, 'Список для просмотра:\n' + films_text,
#                                reply_markup=nav.filmsMenu)
#     elif message.text == 'Книги':
#         await bot.send_message(message.from_user.id, 'Список книг, которые могут изменить вышу жизнь:\n' + books_text,
#                                reply_markup=nav.booksMenu)
#     elif message.text == 'Музыка':
#         await bot.send_message(message.from_user.id, 'Ссылки на ресурсы для прослушивания:\n' + music_text,
#                                reply_markup=nav.musicsMenu)
#     elif message.text == 'Другие материалы':
#         await bot.send_message(message.from_user.id, 'Ссылки на ресурсы:\n' + links_text,
#                                reply_markup=nav.mainMenu)
#     elif message.text == 'Трейдеру':
#         await bot.send_message(message.from_user.id, 'Здесь есть всё, что вам может понадобиться',
#                                reply_markup=nav.traderMenu)
#     elif message.text == 'Арбитражи':
#         await bot.send_message(message.from_user.id, text_arbitrage,
#                                reply_markup=nav.arbitrageMenu)
#     else:
#         await message.reply('Неизветсная команда')


# старт
# @dp.message_handler(commands=['start', 'начать', 'старт'])
# async def command_start(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Привет {0.first_name} '
#                                                  'Напишите код фильма для поиска (+эмодзи) '
#                                                  ''.format(message.from_user), reply_markup=keyboard)
#     buttons = [
#         types.InlineKeyboardButton(text="GitHub", url="https://github.com")]
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#     keyboard.add(*buttons)
#     await message.answer("Кнопки-меню", reply_markup=keyboard)

@dp.message_handler(commands=['start', 'старт'])
async def cmd_start(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text='Найти фильм по коду', callback_data='url'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer('Привет {0.first_name}, напиши код фильма для поиска '.format(
        message.from_user) + emoji.emojize(":eyes:"), reply_markup=keyboard)


@dp.callback_query_handler(text='random_value')
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10)))


@dp.callback_query_handler(text='url')
async def send_random_value(call: types.CallbackQuery):
    # await call.message.answer(str(randint(1, 10)))

    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="1", url="https://t.me/test_film_123"),
        types.InlineKeyboardButton(text="2", url="tg://resolve?domain=telegram"),
        types.InlineKeyboardButton(text="3", url="tg://resolve?domain=telegram"),
        types.InlineKeyboardButton(text="4", url="tg://resolve?domain=telegram"),
        types.InlineKeyboardButton(text="5", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer("Кнопки-ссылки", reply_markup=keyboard)


@dp.message_handler(commands='inline_url')
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="первый паблик", url="https://t.me/test_film_123"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)


# echo - заглушка


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("С помощью этого бота ты можешь получить много полезной информации и записаться на обучение")


if __name__ == '__main__':
    executor.start_polling(dp)
