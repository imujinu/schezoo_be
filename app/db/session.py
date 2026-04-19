from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/schezoo_db"
# echo는 쿼리 로그를 출력
engine = create_async_engine(DATABASE_URL, echo=True)
# AsyncSession 클래스는 비동기적으로 처리하기 위함, expire_on_commit은 클래스 초기화 없이 사용
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise 
        # except를 발생시킨 에러를 다시 터트림
        finally:
            await session.close()
