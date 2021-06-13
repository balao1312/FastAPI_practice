from fastapi import APIRouter
from ..database import database
from ..sqlalchemy_models.tables import blog_table

router = APIRouter()


@router.get('/')
def status():
    return {'host': 'on'}


@router.get("/blog")
async def get_all_blogs():
    query = blog_table.select().order_by(blog_table.c.pk)
    return await database.fetch_all(query)


@router.get('/blog/{pk}')
async def get_blog_by_pk(pk: int):
    query = blog_table.select().where(blog_table.c.pk == pk)
    result = await database.fetch_all(query)
    if not result:
        return {'detail': 'target does not exist.'}
    return result

# @router.post('/blog')
# def create_blog(blog: Blog):
#     db_con.create_new_blog(
#         author=blog.author,
#         title=blog.title,
#         content=blog.content,
#         m_time=blog.m_time,
#         comments=blog.comments,
#         likes=blog.likes
#     )
#     return {
#         'status': 'blog created successfully.',
#         'data': blog
#     }


# @router.delete('/blog/{pk}')
# def delete_blog_by_pk(pk):
#     data = db_con.delete_blog_by_pk(pk)
#     if 'error' in data:
#         return data
#     return {'status': f'blog with pk = {pk} deleted successfully'}


# @router.get('/reset_table_blogs')
# def reset_table_blogs():
#     db_con.reset_table_blogs()
#     return {'status': 'reset table blogs successfully.'}
