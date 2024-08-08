import asyncio
import logging
import sys
import wikipedia
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7386584013:AAH0apBiMLiJS3zHWfFQtWGbIUyfA_dwA5Y"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
wikipedia.set_lang('uz')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def wiki_info(message: Message) -> None:
    try:
        user_text = message.text
        if len(user_text.split()) < 3:
            result = "\n".join(wikipedia.search(user_text))
            text = "Mavjud maqolalar ro'yxati\n" + result
        else:
            text = wikipedia.summary(user_text)
        await message.answer(text=text)
    except wikipedia.PageError:
        await message.answer("Bunday ma'lumot topilmadi. Use ur common sense")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())