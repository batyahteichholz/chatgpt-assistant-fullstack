from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .app_config import AppConfig

# Create a base model:
BaseModel = declarative_base()


class Dal:
    def __init__(self):
        self.engine = create_engine(
            AppConfig.connection_string,
            connect_args={"use_pure": True},
        )
        self.session_creator = sessionmaker(bind=self.engine)
        BaseModel.metadata.create_all(self.engine)

    def create_session(self):
        return self.session_creator()


dal = Dal()
