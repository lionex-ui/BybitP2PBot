from enum import Enum
from dotenv import load_dotenv
from betterconf import Config, field

load_dotenv()


class RedisConfig(Config):
    redis_host = field("REDIS_HOST")
    redis_port = field("REDIS_PORT")

    def get_connection_string(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"


class BotConfig(Config):
    token = field("TOKEN")


class PaymentMethods(Enum):
    MONOBANK = ("Monobank", "43")
    PRIVATBANK = ("Privat Bank", "60")
    ABANK = ("A-Bank", "1")
