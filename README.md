# OTB - OpenAI Telegram Bot

This is a Telegram bot that uses OpenAI's API to generate responses to user inputs.
## Run Locally

### Run with docker-compose

1. Create a `.env` file including the following environment variables

```
OPENAI_API_KEY=
TELEGRAM_BOT_TOKEN=
```

2. Run the app with `docker-compose`

```bash
docker-compose up --build -d
```
## Commands Available

```bash
/start
/help
/dalle 
/davinci
```

## Demo

You can check how the bot works here:

https://user-images.githubusercontent.com/29598954/220421332-545419de-bd2e-4fb4-9805-50ee77f184c2.MP4

## License

This project is licensed under the MIT License.
