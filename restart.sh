docker build -t bybit-bot .

docker stop bybit-bot-container
docker rm bybit-bot-container

docker run -d --name bybit-bot-container bybit-bot