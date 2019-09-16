import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import ContentType, \
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.exceptions import TelegramAPIError, MessageNotModified

from config import TOKEN

logging.basicConfig(level=logging.INFO)


bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


def is_reply(message: types.Message):
    # return message.reply_to_message
    if message.reply_to_message:
        return {'r_msg': message.reply_to_message}


@dp.message_handler(user_id=777)
async def welcome_777(m: types.Message):
    await m.reply('Hello 777!')
    raise SkipHandler


@dp.message_handler(commands=('start', 'help'))
async def command_start(message: types.Message):
    text = 'Hello'
    if message.text.startswith('/help'):
        text += ' help'
    text += '!'
    return await message.reply(text)


@dp.message_handler(commands='key')
async def send_markup(message: types.Message):
    kb = ReplyKeyboardMarkup()
    # yes = KeyboardButton('YES')
    # no = KeyboardButton('NO')
    kb.add(*(KeyboardButton(text) for text in ('YES', 'NO')))

    ask_phone = KeyboardButton('Send phone number', request_contact=True)
    kb.add(ask_phone)

    remove = KeyboardButton('remove')
    remove_cmd= KeyboardButton('/remove')
    kb.add(remove)
    kb.add(remove_cmd)
    await message.reply('Kb is here:', reply_markup=kb)



@dp.message_handler(commands='btn')
async def send_inline_keyboard(message: types.Message):
    kb = InlineKeyboardMarkup()
    # yes = InlineKeyboardButton('YES', callback_data='yes')
    # no = InlineKeyboardButton('NO', callback_data='no')
    # kb.add(yes, no)

    kb.add(*(InlineKeyboardButton(text, callback_data=text.lower()) for text in ('YES', 'NO')))

    url_btn = InlineKeyboardButton('OTUS', url='https://otus.ru/')
    kb.add(url_btn)

    remove_btn = InlineKeyboardButton('remove kb', callback_data='remove')
    kb.add(remove_btn)
    await message.reply('Buttons here:', reply_markup=kb)


@dp.message_handler(is_reply)
async def answer_replied_message(message: types.Message, r_msg: types.Message):
    text = 'Is reply to '
    if r_msg.text:
        text += f'"{r_msg.text}"'
    else:
        text += f'a {r_msg.content_type}'
    await message.reply(text)


@dp.callback_query_handler(text='yes')
async def handle_callback_query_yes(callback_query: types.CallbackQuery):
    await callback_query.answer('Cool!')


@dp.callback_query_handler(text='no')
async def handle_callback_query_no(callback_query: types.CallbackQuery):
    await callback_query.answer('Why not?', show_alert=True)


@dp.callback_query_handler(text='remove')
async def remove_inline_keyboard(callback_query: types.CallbackQuery):
    # await bot.edit_message_text(callback_query.from_user.id)
    # await bot.edit_message_text(callback_query.message.from_user)
    await callback_query.answer('Removing kb..')
    # await callback_query.message.edit_reply_markup()
    await callback_query.message.edit_text('Buttons were here...')
    # await callback_query.message.edit_text('Buttons were here...')


@dp.callback_query_handler()
async def handle_all_callback_queries(callback_query: types.CallbackQuery):
    # await bot.answer_callback_query(callback_query.id)
    await callback_query.answer()


@dp.message_handler(text='remove')
@dp.message_handler(commands='remove')
async def remove_markup(message: types.Message):
    # await message.reply('Removed...', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(message.chat.id, 'Removed...', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands='help')
# async def command_help(message: types.Message):
#     await message.reply('Hello help!')


@dp.message_handler()
async def echo_message(message: types.Message):
    # await bot.send_message(message.chat.id, message.text)
    await message.reply(message.text)


@dp.message_handler(content_types=ContentType.STICKER)
async def echo_sticker(message: types.Message):
    # await bot.send_sticker(message.chat.id, message.sticker.file_id)
    await message.reply_sticker(message.sticker.file_id, reply=False)
    # msg = await bot.send_photo(message.chat.id, '/home/otus/d../img.png')
    # logging.info('photo id', msg.photo[-1].file_id)
    # await bot.send_photo(message.chat.id, msg.photo[-1].file_id)


@dp.errors_handler(exception=MessageNotModified)
async def handle_error_message_not_modified(update: types.Update, e):
    logging.info('Not modified update is %s', update)
    return True


# @dp.errors_handler(exception=TelegramAPIError)
# async def handle_telegram_api_error(update, e):
#     logging.error('Unexpected error!', exc_info=True)
#     return True


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


if __name__ == "__main__":
    executor.start_polling(dp)
