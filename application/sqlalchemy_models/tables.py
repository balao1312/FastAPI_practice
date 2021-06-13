import sqlalchemy
from ..database import metadata

blog_table = sqlalchemy.Table(
    "blogs",
    metadata,
    sqlalchemy.Column("pk", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("author", sqlalchemy.Text),
    sqlalchemy.Column("title", sqlalchemy.Text),
    sqlalchemy.Column("content", sqlalchemy.Text),
    sqlalchemy.Column("m_time", sqlalchemy.DateTime),
    sqlalchemy.Column("comments", sqlalchemy.JSON),
    sqlalchemy.Column("likes", sqlalchemy.Integer),
)
