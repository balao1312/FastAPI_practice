from ..apis import balao, main


def init_apis(app):
    app.include_router(main.router, prefix="/blog-api", tags=['Main'])
    app.include_router(balao.router, prefix="/blog-api/balao", tags=['Balao'])
