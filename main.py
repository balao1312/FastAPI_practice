from fastapi import FastAPI
import uvicorn
from urls.api_urls import init_apis

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    version="0.1.0",
)

init_apis(app)


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
