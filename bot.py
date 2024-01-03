import asyncio
import logging
import random
import uuid
from time import sleep

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command, CommandObject
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from parliament import Parliament

ID2GAME = {}
MAX_SLEEP_DURATION = 2

logging.basicConfig(level=logging.INFO)
with open("token.txt") as f:
    token = f.readline()
bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("vote"))
async def cmd_vote(message: Message, command: CommandObject):
    if command.args is None:
        await message.answer(
            "Не переданы аргументы.\nПример: /vote <@president> <@chancellor>",
            parse_mode=None,
        )
        return
    try:
        president, chancellor = command.args.split()
    except ValueError:
        await message.answer(
            "Неправильный формат команды.\nПример: /vote <@president> <@chancellor>",
            parse_mode=None,
        )
        return
    try:
        if ID2GAME[message.chat.id].is_voting:
            await message.answer("Предыдущие голосование еще не закончилось!")
        else:
            # remove @ symbol at the beginning
            ID2GAME[message.chat.id].start_voting(president[1:], chancellor[1:])
            buttons = [
                [InlineKeyboardButton(text="Ja!", callback_data="vote_yes")],
                [InlineKeyboardButton(text="Nein!", callback_data="vote_no")],
            ]
            keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
            await message.answer(
                f"Начинаем голосование за партию:\n<b>Президент</b>: {president}\n<b>Канцлер</b>: {chancellor}",
                reply_markup=keyboard,
            )
    except KeyError:
        await message.answer("Вы еще не начали игру, пропишите /new_game")


@dp.callback_query(F.data.startswith("vote_"))
async def register_vote(callback: CallbackQuery):
    action = callback.data.split("_")[1]
    parliament: Parliament = ID2GAME[callback.message.chat.id]
    if callback.from_user.username != parliament.president_candidate and parliament.is_voting:
        if action == "yes":
            parliament.positive_votes += 1
        elif action == "no":
            parliament.negative_votes += 1
        if parliament.positive_votes + parliament.negative_votes == parliament.num_voters:
            sleep(random.random() * MAX_SLEEP_DURATION)
            await callback.message.edit_text(parliament.end_voting())
        await callback.answer()


@dp.message(Command("new_game"))
async def cmd_new_game(message: Message):
    game_id = uuid.uuid4().hex
    num_voters = await bot.get_chat_member_count(message.chat.id) - 2
    ID2GAME[message.chat.id] = Parliament(chat=message.chat, num_voters=num_voters)
    logging.debug(ID2GAME[message.chat.id])
    await message.answer(f"Id вашей игры: `{game_id}`", parse_mode="MarkdownV2")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())