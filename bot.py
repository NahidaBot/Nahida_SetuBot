import logging
from aiogram import Bot, Dispatcher, types
import aiogram.dispatcher.filters as filters
from aiogram.utils import executor
import asyncio
from cfg import Cfg

from websites_adapter.ArtInfo import ArtInfo
from websites_adapter.lolicon_api import get_setu

from utils.escaper import md_esc

# Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=Cfg.BOT_TOKEN)
commands: list[types.BotCommand] = []
commands.append(types.BotCommand("start", "Hello"))
commands.append(types.BotCommand("help", "帮助"))
commands.append(types.BotCommand("setu", "(test) 获取一张涩图"))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["help"])
async def help_handler(event: types.Message):
    msg = f"""\
此机器人还在测试中，目前只有获取涩图一个功能\\~

/setu \\- 获取一张涩图
"""
    await event.reply(msg, types.ParseMode.MARKDOWN_V2)

@dp.message_handler(commands=["start", "restart"])
async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )

@dp.message_handler(commands=["setu"])
async def setu_handler(event: types.Message):

    me = await bot.get_me()

    tags = event.text.replace('/setu','').replace(f'@{me.username}', '').strip()    # 处理原始命令

    artList = await get_setu(tags)

    if len(artList) == 0:
        await event.answer("获取失败！")
    else:
        artInfo = artList[0]
        caption = f"*{md_esc(artInfo.title)}*"

        key_PID = types.InlineKeyboardButton(f"PID: {artInfo.pid}", artInfo.post_url)
        key_UID = types.InlineKeyboardButton(f"UID: {artInfo.userId}", f"https://www.pixiv.net/users/{artInfo.userId}")
        inline_keyboard = types.InlineKeyboardMarkup(2, [[key_PID, key_UID]])

        await event.answer_photo(artInfo.images[0].thumb, caption, types.ParseMode.MARKDOWN, reply_markup=inline_keyboard)

async def main():
    try:
        await bot.set_my_commands(commands)
        # 跳过所有未处理消息
        await dp.skip_updates()
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())    
    # executor.start_polling(dp, skip_updates=True)
    # executor.start_polling(dp, skip_updates=False)