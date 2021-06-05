from fastapi import FastAPI
import uvicorn

from models.blogs import Blog
from database.database import db_con

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


@app.get('/blog')
def show_all_blogs():
    data = db_con.show_all_blogs()
    return {'data': data}

@app.get('/blog/{pk}')
def get_blog_by_pk(pk):
    data = db_con.get_blog_by_pk(pk)
    if 'error' in data:
        return data
    return {'data': data}

@app.post('/blog')
def create_blog(blog: Blog):
    db_con.create_new_blog(
        author=blog.author,
        title=blog.title,
        content=blog.content,
        m_time=blog.m_time,
        comments=blog.comments,
        likes=blog.likes
    )
    return {
        'status': 'blog created successfully.',
        'data': blog
    }

# Will RESET table blogs!! Use with care!!


@app.get('/reset_table_blogs')
def reset_table_blogs():
    db_con.reset_table_blogs()
    return {'status': 'reset table blogs successfully.'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
