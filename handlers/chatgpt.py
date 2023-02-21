from asyncio.log import logger

from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from auth import restricted
from client import generate_response
from handlers import base

PROMPT = range(1)


@restricted
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Send /cancel to stop talking to me.\n\n" "Please provide a prompt.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return PROMPT


async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["prompt"] = update.message.text
    logger.info(f"{update.effective_user.username} {context.user_data}")
    response = generate_response(**context.user_data)
    logger.info(f"{update.effective_user.username} {response}")
    if response is None:
        await update.message.reply_text("**Error**" "No results found.")
    else:
        for text in response:
            if len(text) > 2000:
                for i in range(0, len(text), 2000):
                    await update.message.reply_text(
                        text[i: i + 2000],  # noqa E203
                        reply_markup=ReplyKeyboardRemove(),
                    )
            await update.message.reply_text(text, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("davinci", start)],
    states={
        PROMPT: [MessageHandler(filters.TEXT, handle_response)],
    },
    fallbacks=[CommandHandler("cancel", base.cancel)],
)
