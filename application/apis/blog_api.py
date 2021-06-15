from fastapi import APIRouter
from ..database import database
from ..sqlalchemy_models.tables import blog_table
from ..pydantic_models.blog import Blog, UpdateBlog

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


@router.post("/blog")
async def create_human_resource(blog: Blog):
    query = blog_table.insert().values(
        author=blog.author,
        title=blog.title,
        content=blog.content,
        m_time=blog.m_time,
        comments=blog.comments,
        likes=blog.likes
    )
    await database.execute(query)
    return {
        "status": "Blog successfully created!",
        'data': blog
    }


@router.put('/blog/{pk}')
async def update_blog_by_pk(pk: int, blog: UpdateBlog):
    if_exist_query = blog_table.select().where(blog_table.c.pk == pk)
    data = await database.execute(if_exist_query)
    if not data:
        return {'detail': 'target does not exist.'}
    query = blog_table.update().where(blog_table.c.pk == pk).values(
		title=blog.title,
		content=blog.content,
		m_time=blog.m_time
	)
    await database.execute(query)
    return {'status': f'blog with pk = {pk} updated successfully'}


@router.delete('/blog/{pk}')
async def delete_blog_by_pk(pk: int):
    if_exist_query = blog_table.select().where(blog_table.c.pk == pk)
    blog = await database.execute(if_exist_query)
    if not blog:
        return {'detail': 'target does not exist.'}
    query = blog_table.delete().where(blog_table.c.pk == pk)
    await database.execute(query)
    return {'status': f'blog with pk = {pk} deleted successfully'}
