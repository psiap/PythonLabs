from datetime import datetime, timedelta

from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

bot = Bot(token='2080900303:AAGxSIIWS4YIvEO29r3fhTxGmMOAIbQATVs', validate_token=True, parse_mode="HTML")
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()
scheduler.start()

async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def send_msg(message: types.Message):
    msg = await message.answer("Тик")
    date = datetime.now() + timedelta(seconds=5)
    scheduler.add_job(edit_msg, "date", run_date=date, kwargs={"message": msg})


async def edit_msg(message: types.Message):
    await send_message(-1001607259284,'test')
    await message.edit_text("Так")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)