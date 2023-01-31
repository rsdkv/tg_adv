from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')
# main menu - Приветствие
btnEdu = KeyboardButton('Учиться')
btnImprove = KeyboardButton('Стать лучше')
btnFun = KeyboardButton('Развлечься')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEdu, btnImprove, btnFun, btnMain)

# edu menu - из кнопок: вызов главного меню  --   Обучение
eduMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnImprove, btnMain)

# меню для -- Библиотеки ф м к др мат назад
btnFilms = KeyboardButton('Фильмы')
btnMusics = KeyboardButton('Музыка')
btnBooks = KeyboardButton('Книги')
btnOtherMaterials = KeyboardButton('Другие материалы')
btnLibrary = KeyboardButton('Библиотека')
libraryMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFilms, btnMusics, btnBooks, btnMain)

# меню для -- Трейдеру - traderMenu
btnArbitrage = KeyboardButton('Арбитражи')
btnLinks = KeyboardButton('Ссылки на ресурсы')
traderMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnArbitrage, btnEdu, btnBooks, btnMain)

# меню для Фильмы
filmsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFun, btnMain)

# меню для Музыка
musicsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFun, btnMain)

# меню для Книги
booksMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnImprove, btnMain)

# подменю для арбитража
arbitrageMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnImprove, btnMain)
