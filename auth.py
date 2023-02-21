import logging
from functools import wraps

from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

WHITELISTED_USERS = ["flpedraz", "simonesay"]


def restricted(func):
    @wraps(func)
    async def wrapped(
        update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
    ):
        username = update.effective_user.username
        if username not in WHITELISTED_USERS:
            logger.info(f"Unauthorized access denied for {username}.")
            await update.message.reply_text(
                "You don't have access to this resource.",
                reply_markup=ReplyKeyboardRemove(),
            )
        else:
            return await func(update, context, *args, **kwargs)

    return wrapped
