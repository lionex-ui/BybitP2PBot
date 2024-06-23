
# BybitP2PBot

This Telegram bot is designed to search for orders matching your conditions on the ByBit exchange.

## .env file

```env
  REDIS_HOST=redis_host
  REDIS_PORT=redis_port
  TOKEN=bot_token
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/lionex-ui/BybitP2PBot.git
```

Go to the project directory

```bash
  cd BybitP2PBot
```

Install dependencies

```bash
  poetry install
```

Start the bot

```bash
  poetry run python3 main.py
```

## Run using Dockerfile

Clone the project

```bash
  git clone https://github.com/lionex-ui/BybitP2PBot.git
```

Go to the project directory

```bash
  cd BybitP2PBot
```

Build image

```bash
  docker build -t <image-name> .
```

Run container

```bash
  docker run -d --name <container-name> <image-name>
```


## Restart Dockerfile

Before launching, change the container and image names to your own.

Make the script executable

```bash
  chmod +x ./restart.sh
```

Run script

```bash
  ./restart.sh
```


## How To Use

### 1) Registration
- Send start command to the bot
- Send User ID
### 2) Settings
- ...


## Tech Stack

**Telegram Bot** - aiogram

**Interaction with API** - aiohttp

**Config files** - betterconf, python-dotenv


## Authors

- [lionex-ui](https://github.com/lionex-ui)

