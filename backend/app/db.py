from collections.abc import AsyncGenerator
import uuid
import os
from urllib.parse import quote

from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Uuid
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

## Função pra ler o arquivo do Docker Secrets (Onde estão os dados sensiveis)
def readSecret(path):
    with open(path) as f:
        return f.read().strip()

# ## Usa o readSecret para armazenar os dados sensíveis
# DB_USER = readSecret(os.getenv("DB_USER_FILE"))
# DB_PASSWORD = readSecret(os.getenv("DB_PASSWORD_FILE"))
# DB_NAME = readSecret(os.getenv("DB_NAME_FILE"))
# DB_HOST = readSecret(os.getenv("DB_HOST_FILE"))
# DB_PORT = int(os.getenv("DB_PORT")) ## Esse não é dado sensível, não esta no docker secrets

## Essas linhas sao usadas APENAS pra rodar o sistema localmente, quando for buildar deve usar as linhas comentadas acima
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))


## Declara a URL pra criar a engine depois, usa as variaveis de ambiente
DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{quote(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}" ## Aqui a função quote é utilizada por existirem carac. especiais na senha

class Base(DeclarativeBase):
    pass 


class Post(Base):
    __tablename__ = "posts"

    ## ID, KEY e gera um ID único sempre (Uuid)
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(Text)
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


## Cria a session para poder usar o DB
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session