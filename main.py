from fastapi import FastAPI
import uvicorn
from application.routers.routers import init_apis
from fastapi.middleware.cors import CORSMiddleware
from application.database import database

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_apis(app)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/zong_yu')
def zong_yu():
    return {'data':
            {
                'name': 'zong_yu',
                'age': '30',
                'gender': 'male',
                'profession': 'av actor'
            }
            }


@app.get('/yiling')
def yiling():
    return {'data':
            {
                'name': 'yiling',
                'age': '32',
                'gender': 'female',
                'profession': 'Cat Addict'
            }
            }


@app.get('/yulin')
def yulin():
    return {'data':
            {
                'name': 'yulin',
                'age': '29',
                'gender': 'male',
                'profession': 'dog Addict'
            }
            }


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
