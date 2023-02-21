import json
import logging
import os

import requests
from telegram.ext import Application, CommandHandler

from handlers import base, chatgpt, dalle

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def set_commands():
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/setMyCommands"
    commands = {
        "commands": json.dumps(
            [
                {"command": command[0], "description": command[1]}
                for command in base.get_commands()
            ]
        )
    }
    response = requests.post(url, data=commands)
    logger.info(response.json())


def main() -> None:
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    application.add_handler(CommandHandler(["start", "help"], base.help))
    application.add_handler(CommandHandler("hello", base.hello))

    application.add_handler(chatgpt.conv_handler)
    application.add_handler(dalle.conv_handler)

    application.run_polling()


if __name__ == "__main__":
    set_commands()
    main()
