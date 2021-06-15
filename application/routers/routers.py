from ..apis import balao, blog_api


def init_apis(app):
    app.include_router(blog_api.router, prefix="/blog-api", tags=['Blog'])
    app.include_router(balao.router, prefix="/blog-api/balao", tags=['Balao'])
