# -*- coding: utf-8 -*-

import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.utils.markdown import text, pre, bold
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from config import TOKEN
from lang import *
from menu import *
from translate_phrase_func import *
from back_translate_func import *


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        con = sqlite3.connect(r'databases\users.db')
        cur = con.cursor()
        check_user = cur.execute(
            f'SELECT user_id FROM users WHERE user_id = {user_id}').fetchone()
        if check_user:
            await message.answer(dict_ru['msg_auto'])
        else:
            cur.execute(
                f'INSERT INTO users VALUES ({user_id}, "ru", "False", "False", "False", "False")')
            con.commit()
            await message.answer(dict_ru['msg_start'].format(user_name))
    except Exception as ex:
        print(ex)
    finally:
        con.close()


@dp.message_handler(commands=['translate_phrase'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        con = sqlite3.connect(r'databases\users.db')
        cur = con.cursor()
        cur.execute(
            f'UPDATE users SET translate_phrase_flag = "True" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET translate_audio_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_text_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_audio_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        await message.answer(dict_ru['msg_translate_phrase_q'])
    except Exception as ex:
        print(ex)
    finally:
        con.close()


@dp.message_handler(commands=['translate_audio'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        con = sqlite3.connect(r'databases\users.db')
        cur = con.cursor()
        cur.execute(
            f'UPDATE users SET translate_phrase_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET translate_audio_flag = "True" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_text_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_audio_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        await message.answer(dict_ru[...])
    except Exception as ex:
        print(ex)
    finally:
        con.close()


@dp.message_handler(commands=['back_translate_text'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        con = sqlite3.connect(r'databases\users.db')
        cur = con.cursor()
        cur.execute(
            f'UPDATE users SET translate_phrase_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET translate_audio_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_text_flag = "True" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_audio_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        await message.answer(dict_ru['msg_back_translate_text_q'])
    except Exception as ex:
        print(ex)
    finally:
        con.close()


@dp.message_handler(commands=['back_translate_audio'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        con = sqlite3.connect(r'databases\users.db')
        cur = con.cursor()
        cur.execute(
            f'UPDATE users SET translate_phrase_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET translate_audio_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_text_flag = "False" WHERE user_id = {user_id}')
        con.commit()
        cur.execute(
            f'UPDATE users SET back_translate_audio_flag = "True" WHERE user_id = {user_id}')
        con.commit()
        await message.answer(...)
    except Exception as ex:
        print(ex)
    finally:
        con.close()


@dp.message_handler()
async def list_status(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    msg = message.text
    try:
        con = sqlite3.connect(r'databases\users.db')
        cur = con.cursor()
        check_load = cur.execute(
            f'SELECT * FROM users WHERE user_id = {user_id}').fetchone()
        if check_load[2] == "True":
            cur.execute(
                f'UPDATE users SET translate_phrase_flag = "False" WHERE user_id = {user_id}')
            con.commit()
            await message.answer(dict_ru['msg_translate_phrase'].format(msg) + text(pre(translate_phrase(msg))) + '\n\n#DashAndDot', parse_mode=ParseMode.MARKDOWN)
        elif check_load[3] == "True":
            cur.execute(
                f'UPDATE users SET translate_audio_flag = "False" WHERE user_id = {user_id}')
            con.commit()
        elif check_load[4] == "True":
            cur.execute(
                f'UPDATE users SET back_translate_text_flag = "False" WHERE user_id = {user_id}')
            con.commit()
            await message.answer(dict_ru['msg_back_translate_text'].format(msg, back_translate(msg)))
        elif check_load[5] == "True":
            cur.execute(
                f'UPDATE users SET back_translate_audio_flag = "False" WHERE user_id = {user_id}')
            con.commit()
        else:
            await message.answer(text(bold('Я лучший DaD на свете!')), parse_mode=ParseMode.MARKDOWN)
    except Exception as ex:
        print(ex)
    finally:
        con.close()

if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(dp)
        except Exception as ex:
            print(f'Reload... ::: {ex}')
