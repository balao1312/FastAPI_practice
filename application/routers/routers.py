from ..apis import balao, blog


def init_apis(app):
    app.include_router(blog.router, prefix="/blog-api", tags=['Blog'])
    app.include_router(balao.router, prefix="/blog-api/balao", tags=['Balao'])
