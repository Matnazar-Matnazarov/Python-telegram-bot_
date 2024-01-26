import logging
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Bot tokenini o'zgartiring
TOKEN = 'token'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Barcha foydalanuvchilarni ma'lumotlarini saqlash uchun faylni nomi
USER_DATA_FILE = "user_data.txt"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    await message.reply(f"Salom, {user.first_name}!")

# Bu handler yangi bir matn yuborilganda ishlaydi
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def on_start(message: types.Message):
    user_id = message.from_user.id
   # full_name = f"{message.from_user.first_name} {message.from_user.last_name}"
    link = f"https://t.me/{message.from_user.username}"
    text = message.text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ma'lumotlarni faylga yozish
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"User ID: {user_id}\n")
        #file.write(f"Full Name: {full_name}\n")
        file.write(f"Telegram Link: {link}\n")
        file.write(f"Text: {text}\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write("\n")  # Qatorlar orqali farq qilish

    # await message.reply("Sizni yozgan ma'lumotlar saqlandi!")
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
if __name__ == '__main__':
    from aiogram import executor
    # Pollingni boshlash
    executor.start_polling(dp, skip_updates=True)
