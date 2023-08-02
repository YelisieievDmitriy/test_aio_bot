# test_aio_bot
# Test Telegram Bot for Selling Products


This is a test Telegram bot built on the aiogram library to facilitate the sale of various products. The bot is developed using asynchronous programming and is intended for demonstration purposes.

# Features
Asynchronous communication with Telegram using the aiogram library.
Admin mode: Ability to manage product catalog, including adding, modifying, and deleting product entries (name, description, price, and images).
User mode: Regular users can browse the product catalog and make purchases.
# How to Use
Clone the repository.
Create and activate a virtual environment.

# python3 -m venv venv
# source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Install the required dependencies from the requirements.txt file.

# pip install -r requirements.txt

Create a new folder named data in the root directory of the project.
In the data/config.py file, add your Telegram token and admin user ID.
To run the bot, execute the app.py module.

# python app.py

If you want to enable the admin and user mode selection upon bot startup, uncomment the admin_mode and user_mode functions in app.py.
Please note that this project is purely for demonstration purposes. Feel free to explore the code and adapt it for your own projects.
------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------
# Тестовый Telegram бот для продажи товаров

Это тестовый Telegram бот, созданный на библиотеке aiogram для удобной продажи различных товаров. Бот разработан с использованием асинхронного программирования и предназначен для демонстрационных целей.

# Особенности
Асинхронное взаимодействие с Telegram с помощью библиотеки aiogram.
Режим администратора: Возможность управления каталогом товаров, включая добавление, изменение и удаление записей о товарах (название, описание, цена и изображения).
Режим пользователя: Обычные пользователи могут просматривать каталог товаров и делать покупки.
# Инструкции по использованию
Клонируйте репозиторий.
Создайте и активируйте виртуальное окружение.

# python3 -m venv venv
# source venv/bin/activate  # На Windows используйте: venv\Scripts\activate

Установите необходимые зависимости из файла requirements.txt.

# pip install -r requirements.txt

В корневой директории проекта создайте новую папку с именем data.
В файле data/config.py добавьте свой токен и ID администратора Telegram.
Запустите бота, выполнив модуль app.py.

# python app.py

Если вы хотите предоставить выбор режима администратора или пользователя при запуске бота, раскомментируйте функции admin_mode и user_mode в файле app.py.
Обратите внимание, что этот проект предназначен исключительно для демонстрационных целей. Вы можете изучить его код и адаптировать для своих собственных проектов.
