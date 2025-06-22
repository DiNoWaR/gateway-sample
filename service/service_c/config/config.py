from dataclasses import dataclass
import os


@dataclass
class Config:
    server_host: str
    server_port: int

    @classmethod
    def from_env(cls):
        return cls(
            server_host=os.getenv('SERVER_HOST', '0.0.0.0'),
            server_port=int(os.getenv('SERVER_PORT', '9092')),
        )


APP_CONFIG = Config.from_env()
