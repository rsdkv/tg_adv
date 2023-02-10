from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config as cfg

import markup as nav
import emoji

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)


async def check_sub_channels(channels, user_id):
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    return True


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, '{0.first_name}, с помощью бота вы можете найти фильм по коду'.format(
        message.from_user) + emoji.emojize(":eyes:"), reply_markup=nav.menuMain())


@dp.callback_query_handler(text='introduction')
async def introduction(message: types.Message):
    # await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Напиши код фильма для поиска '.format(
        message.from_user) + emoji.emojize(":eyes:"))


@dp.callback_query_handler(text='subdone')
async def subdone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)

    if await check_sub_channels(cfg.CHANNELS, message.from_user.id):
        await bot.send_message(message.from_user.id, 'Привет {0.first_name}, напиши код фильма для поиска '.format(
            message.from_user) + emoji.emojize(":eyes:"), reply_markup=nav.menuChannels())
        await bot.send_message.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    else:
        await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.menuChannels())

@dp.message_handler()
async def echo_message(message: types.Message):
    temp = message.text
    await bot.send_message(message.from_user.id, 'Ваш фильм: {film}'.format(film=temp))
    # if await check_sub_channels(cfg.CHANNELS, message.from_user.id):
    #     temp = message.text
    #     await bot.send_message(message.from_user.id, 'Ваш фильм: {film}'.format(film=temp))
    # else:
    #     await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.menuChannels())


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("С помощью этого бота ты можешь получить название фильма по его коду")


if __name__ == '__main__':
    executor.start_polling(dp)
