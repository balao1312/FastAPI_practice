from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def main():
    return {'host': 'on'}

@app.get('/balao')
def balao():
    return {'data': 
        {
            'name': 'balao',
            'age': '38',
            'gender': 'male',
            'profession': 'ToDiGong'
        }
    }

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
