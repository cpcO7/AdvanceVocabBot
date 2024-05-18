# import random
#
# with open('units/Unit_1\n.txt') as f:
#     read_file = f.readlines()
#     eng = [i.split('-')[0] for i in read_file]
#     read_file = [i.split('-') for i in read_file]
#     for _ in range(10):
#         a = random.sample(read_file, 4)
#         print(a)
#         b = random.choice(a)
#         print(b)
#         for i, v in enumerate(eng):
#             if v == b:
#                 eng.pop(i)
#         for i, v in enumerate(a):
#             if b == v:
#                 break
#         print(i)
#
# import asyncio
# import json
# import logging
# import sys
# from redis_dict import RedisDict
# from aiogram import Bot, Dispatcher, F
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.methods import SendPoll
# from aiogram.types import Message, KeyboardButton, InlineKeyboardButton, CallbackQuery, InputMediaAnimation, FSInputFile
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
# from aiogram.utils.markdown import hbold
import asyncio
import logging
import random
import sys
from aiogram.filters import CommandStart

from aiogram import Bot, Dispatcher, types

TOKEN = '6975892912:AAHutOXieRvQu-gVsPm32RvbjiXjmfjosG0'

API_TOKEN = 'your_api_token'
dp = Dispatcher()

# Sample quiz questions and options
quiz_questions = [
    "What is the capital of France?",
    "What is the largest mammal?",
    "Who painted the Mona Lisa?",
    # Add more questions here
]

quiz_options = [
    ["Paris", "Rome", "Berlin"],
    ["Elephant", "Whale", "Giraffe"],
    ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
    # Add more options here
]


@dp.message(CommandStart())
async def start(message: types.Message, bot : Bot):
    await message.answer("Welcome to the quiz poll! Click the button to start the quiz.")
    await send_quiz(message.chat.id, bot)


async def send_quiz(chat_id, bot :Bot):
    # Randomly select a question
    question_index = random.randint(0, len(quiz_questions) - 1)
    question_text = quiz_questions[question_index]
    options = quiz_options[question_index]

    # Create list of button labels for options
    option_labels = [types.KeyboardButton(option) for option in options]

    # Shuffle the options so they appear in random order
    random.shuffle(option_labels)

    # Create inline keyboard with shuffled options
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_markup.add(*option_labels)

    # Send the question with options
    await bot.send_message(chat_id, question_text, reply_markup=keyboard_markup)


@dp.message()
async def handle_answer(message: types.Message):
    # Handle user's answer
    if message.text in quiz_options[0]:
        await message.answer("Correct answer! 🎉")
    else:
        await message.answer("Incorrect answer. 😔")


#
# async def start_quiz(chat_id, bot: Bot):
#     import random
#     read_file = [k + '-' + v for k, v in tests.items()]
#     await bot.send_poll(chat_id, question, options=answers, is_anonymous=False, type='quiz', open_period=30,
#                         correct_option_id=correct_option)
#
#
# @dp.message(CommandStart())
# async def callback_query_start(message: Message, bot: Bot):
#     with open('units/Unit_1\n.txt', 'r') as file:
#         for test in file.readlines():
#             test = test.split('-')
#             print(test)
#             tests[test[0]] = test[1:]
#
#
#
# @dp.poll_answer()
# async def poll_answer(poll: SendPoll, bot: Bot):
#     await start_quiz(poll.user.id, bot)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
