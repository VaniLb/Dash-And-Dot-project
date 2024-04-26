from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
other_func_menu_btn = [
    [InlineKeyboardButton(text="📝 Обучение Азбуке Морзе",
                          callback_data="leson_morse_0")],
    [InlineKeyboardButton(text="🔎 Таблица переводов", callback_data="table_trans"),
     InlineKeyboardButton(text="✅ Проверь себя!", callback_data="check_self")],
    [InlineKeyboardButton(text="⁉️ Техническая поддержка", callback_data="help_me")]]

other_func_menu = InlineKeyboardMarkup(inline_keyboard=other_func_menu_btn)

leson_morse_1_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📝 Получить 2 Урок",
                                                                                 callback_data="leson_morse_1")]])

leson_morse_2_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📝 Получить 3 Урок",
                                                                                 callback_data="leson_morse_2")]])

leson_morse_3_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📝 Получить 4 урок",
                                                                                 callback_data="leson_morse_3")]])

sub_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="💎 Оформить подписку",
                                                                       callback_data="sub")]])

sub_full_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="💎 Premium плейлист",
                                                                            url="https://ru.wikipedia.org/wiki/Облом")]])

check_self_1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❓ 1 Вопрос",
                                                                           callback_data="check_self_1")]])

check_self_2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❓ 2 Вопрос",
                                                                           callback_data="check_self_2")]])

check_self_3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❓ 3 Вопрос",
                                                                           callback_data="check_self_3")]])

check_self_4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❓ 4 Вопрос",
                                                                           callback_data="check_self_4")]])

check_self_5 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❓ 5 Вопрос",
                                                                           callback_data="check_self_5")]])

check_self_finish = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❓ Результаты",
                                                                                callback_data="check_self_6")]])
exit_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[
                                [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
