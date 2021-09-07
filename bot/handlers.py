import aiofiles
from aiogram import types, Dispatcher, Bot
from django.conf import settings
from loguru import logger

from users.services import update_or_create_user
from .services import get_random_voice_path, get_generated_text


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome_message(message: types.Message):
    """Отправляет приветственное сообщение"""
    await update_or_create_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name,
    )
    await message.answer(settings.WELCOME_TEXT)
    logger.info('The welcome message was sent successfully')


@dp.message_handler(commands=['voice'])
async def send_random_voice(message: types.Message):
    """Отправляет случайное голосовое сообщение"""
    path = await get_random_voice_path()
    async with aiofiles.open(path, 'rb') as voice:
        await message.answer_voice(voice)
    logger.info('A voice message was sent successfully')


@dp.message_handler(commands=['balaboba'])
async def send_balaboba_text(message: types.Message):
    """Отправляет дополненный Балабобой текст"""
    try:
        phrase = message.text.split()[1]
        generated_text = await get_generated_text(phrase)
        await message.answer(generated_text)
        logger.info('A generated message was sent successfully')
    except IndexError:
        await message.answer(settings.BALABOBA_ERROR_TEXT)
        logger.info('The balaboba error message was sent successfully')
