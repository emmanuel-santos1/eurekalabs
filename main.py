from core.config import settings
from sql_app.base import Base
from sql_app.session import engine
from sql_app.utils import check_db_connected
from sql_app.utils import check_db_disconnected
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from base import api_router as web_app_router


def include_router(app):
    app.include_router(web_app_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app


app = start_application()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()
