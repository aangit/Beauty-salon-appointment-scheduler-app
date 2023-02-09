import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.user_type.routes import user_type_router
from app.user.routes import user_router
from app.contact_type.routes import contact_type_router

Base.metadata.create_all(bind=engine)

def init_app():
    app = FastAPI()
    app.include_router(user_type_router)
    app.include_router(user_router)
    app.include_router(contact_type_router)
    return app

app = init_app()

@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)