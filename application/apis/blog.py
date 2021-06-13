from fastapi import APIRouter
from ..database import db_con
from ..models.blogs import Blog

router = APIRouter()


@router.get('/')
def status():
    return {'host': 'on'}

@router.get('/blog')
def show_all_blogs():
    data = db_con.show_all_blogs()
    return {'data': data}


@router.get('/blog/{pk}')
def get_blog_by_pk(pk):
    data = db_con.get_blog_by_pk(pk)
    if 'error' in data:
        return data
    return {'data': data}


@router.post('/blog')
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


@router.delete('/blog/{pk}')
def delete_blog_by_pk(pk):
    data = db_con.delete_blog_by_pk(pk)
    if 'error' in data:
        return data
    return {'status': f'blog with pk = {pk} deleted successfully'}


@router.get('/reset_table_blogs')
def reset_table_blogs():
    db_con.reset_table_blogs()
    return {'status': 'reset table blogs successfully.'}
