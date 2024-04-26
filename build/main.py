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


@dp.message_handler(commands=['other_functions'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        await message.answer(dict_ru['msg_other_functions'], reply_markup=other_func_menu)
    except Exception as ex:
        print(ex)


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        await message.answer(dict_ru['msg_help'])
    except Exception as ex:
        print(ex)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('leson_morse'))
async def process_callback_button1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.full_name
    try:
        code = callback_query.data[-1]
        if code.isdigit():
            code = int(code)
        if code == 0:
            await bot.send_message(user_id, dict_ru['msg_leson_morse_1'], reply_markup=leson_morse_1_menu)
        elif code == 1:
            await bot.send_message(user_id, dict_ru['msg_leson_morse_2'], reply_markup=leson_morse_2_menu)
        elif code == 2:
            await bot.send_message(user_id, dict_ru['msg_leson_morse_3'], reply_markup=leson_morse_3_menu)
        elif code == 3:
            await bot.send_message(user_id, dict_ru['msg_sub'], reply_markup=sub_menu)
    except Exception as ex:
        print(ex)


@dp.callback_query_handler(lambda c: c.data == 'help_me')
async def process_callback_button1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.full_name
    try:
        await bot.send_message(user_id, 'С любой проблемой обращаться к @Vanilb_ka')
    except Exception as ex:
        print(ex)


@dp.callback_query_handler(lambda c: c.data == 'table_trans')
async def process_callback_button1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.full_name
    try:
        photo = open('photo/morse_photo.jpg', 'rb')
        await bot.send_message(user_id, dict_ru['msg_table_trans'])
        await bot.send_photo(user_id, photo)
    except Exception as ex:
        print(ex)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('check_self'))
async def process_callback_button1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.full_name
    try:
        code = callback_query.data[-1]
        if code.isdigit():
            code = int(code)
        else:
            await bot.send_message(user_id, dict_ru['msg_check_self'], reply_markup=check_self_1)
        if code == 1:
            await bot.send_poll(user_id, 'Расшифровка: • — • •  • • — —  — • • •  — — —  • — —  — • • —',
                                ['Счастье', 'Любовь', 'Разум', 'Точка-тире'],
                                type='quiz', correct_option_id=1, is_anonymous=True, reply_markup=check_self_2)
        elif code == 2:
            await bot.send_poll(user_id, 'Средство для общения по Азбуке Морзе',
                                ['Маятник', 'Телескоп', 'Телеграф'],
                                type='quiz', correct_option_id=2, is_anonymous=True, reply_markup=check_self_3)
        elif code == 3:
            await bot.send_poll(user_id, 'Как на Азбуке Морзе будет СОС',
                                ['• • •  — — —  • • •', '• • •  — — —  • • •  — — —',
                                    '• • •  • •  • • •', '• • •  — — —  • • •  • —  —  — • • —'],
                                type='quiz', correct_option_id=0, is_anonymous=True, reply_markup=check_self_4)
        elif code == 4:
            await bot.send_poll(user_id, 'Расшифровка: • — • •  • • — —',
                                ['Ром', 'Кар', 'Блум', 'Лю'],
                                type='quiz', correct_option_id=3, is_anonymous=True, reply_markup=check_self_5)
        elif code == 5:
            await bot.send_poll(user_id, 'Нужна ли Азбука Морзе сейчас? (2024 год)',
                                ['Очень нужна', 'Сомневаюсь', 'Нет.'],
                                type='quiz', correct_option_id=2, is_anonymous=True, reply_markup=check_self_finish)
        elif code == 6:
            await bot.send_message(user_id, 'Спасибо за участие, ты молодец в любом случае!')
    except Exception as ex:
        print(ex)


@dp.callback_query_handler(lambda c: c.data == 'sub')
async def process_callback_button1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.full_name
    try:
        await bot.send_message(user_id, dict_ru['msg_sub_full'], reply_markup=sub_full_menu)
    except Exception as ex:
        print(ex)


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
