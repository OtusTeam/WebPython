import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import CommandHelp
from aiogram.dispatcher.handler import SkipHandler, CancelHandler
from aiogram.dispatcher.webhook import SendMessage

from config import TOKEN

logging.basicConfig(level=logging.INFO)


bot = Bot(TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())



# @dp.message_handler(content_types=types.ContentType.ANY)
# def filter_users(message: types.Message):
#     if message.from_user.id not in (622348102, 777):
#         # raise SkipHandler
#         raise CancelHandler
#     raise SkipHandler


# @dp.message_handler(commands=['start', 'help'])
@dp.message_handler(commands='start')
async def handle_command_start(message: types.Message):
    return await message.answer(f'Nice to meet you {message.from_user.full_name}')


# @dp.message_handler(commands='help')
@dp.message_handler(CommandHelp())
async def handle_command_help(message: types.Message):
    return await message.answer('This is help')


@dp.message_handler(commands='kb')
async def send_reply_keyboard_markup(message: types.Message):
    btn_yes = types.KeyboardButton('YES')
    btn_no = types.KeyboardButton('NO')
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(btn_yes, btn_no)
    return await message.reply('Btns!', reply_markup=kb)


@dp.message_handler(commands='remove')
async def send_reply_keyboard_remove(message: types.Message):
    return SendMessage(message.chat.id, text='Removed!', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands='inline')
async def send_inline_kb(message: types.Message):
    btn_yes = types.InlineKeyboardButton('YES', callback_data='yes')
    btn_no = types.InlineKeyboardButton('NO', callback_data='no')
    kb = types.InlineKeyboardMarkup()
    kb.add(btn_yes, btn_no)
    return await message.answer('Here are buttons:', reply_markup=kb)


@dp.callback_query_handler(text='yes')
async def answer_callback_yes(cb: types.CallbackQuery):
    # return await cb.answer('Nice!')
    return await bot.answer_callback_query(cb.id, 'Nice!')


@dp.callback_query_handler(text='no')
async def answer_callback_no(cb: types.CallbackQuery):
    return await cb.answer('Why?!', show_alert=True)


@dp.callback_query_handler()
async def handle_all_callback_queries(cb: types.CallbackQuery):
    await cb.answer()


@dp.message_handler()
async def echo_message(message: types.Message):
    # await bot.send_message(message.chat.id, message.text)
    # await message.reply(message.text)
    # await message.reply(message.text, reply=False)
    # await message.answer(message.text)
    return SendMessage(message.chat.id, message.text)


@dp.message_handler(content_types=types.ContentType.STICKER)
async def echo_sticker(message: types.Message):
    # await bot.send_sticker(message.chat.id, message.sticker.file_id)
    await message.answer_sticker(message.sticker.file_id)
    await message.answer(message.sticker.file_id)


#
# Этого не было на занятии, добавляю для примера

@dp.inline_handler()
async def handle_default_inline(inline_query: types.InlineQuery):
    results = []
    offset = 0
    if inline_query.offset:
        if not inline_query.offset.isdigit():
            return await inline_query.answer(results, cache_time=1)
        offset = int(inline_query.offset)

    if offset >= 50:
        return await inline_query.answer(results, cache_time=1)

    for _ in range(10):
        offset += 1
        input_content = InputTextMessageContent(f'Hello inline text #{offset}!')
        title = f'Result #{offset}'
        result = InlineQueryResultArticle(
            id=f'with_offset_{offset}',
            title=title,
            input_message_content=input_content,
        )
        results.append(result)

    await inline_query.answer(results, cache_time=1, next_offset=str(offset))


if __name__ == '__main__':
    executor.start_polling(dp)
