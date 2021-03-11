from environs import Env
from cfenv import AppEnv
from requests_aws4auth import AWS4Auth


def config_from_env():
    return AppConfig()


class Config:
    def __init__(self):
        self.env_parser = Env()
        self.cf_parser = AppEnv()
        self.PORT = self.env_parser.int("PORT", 8080)


class AppConfig(Config):
    def __init__(self):
        super().__init__()
        self.TESTING = False
        self.DEBUG = self.env_parser.bool("DEBUG", False)
        self.ES = self.cf_parser.get_service(label="aws-elasticsearch")
        print(self.ES.credentials)
        self.AUTH = AWS4Auth(
            self.ES.credentials["access_key"],
            self.ES.credentials["secret_key"],
            "us-gov-west-1",
            "es",
        )
