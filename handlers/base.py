from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes, ConversationHandler


def get_commands():
    return [
        ["start", "Start the bot"],
        ["help", "Show help message"],
        ["hello", "Say hello to the bot"],
        ["dalle", "Generate or search for images using a prompt"],
        ["davinci", "ChatGPT with Davinci"],
        ["cancel", "End the running command"],
    ]


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "You ended the command.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "".join(f"/{command[0]} {command[1]} \n" for command in get_commands())
    await update.message.reply_markdown_v2("*Available Commands* \n\n" + text)
