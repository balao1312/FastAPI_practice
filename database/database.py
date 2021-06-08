from datetime import datetime, date
import psycopg2
from psycopg2.extras import RealDictCursor
from credential import db_info


class PostgreSQL_connection():
    def __init__(self, host, database, user, password, port=5432):
        self.con = psycopg2.connect(
            host=db_info['host'],
            user=db_info['user'],
            database=db_info['database'],
            password=db_info['password'],
            port=db_info['port']
        )
        self.cursor = self.con.cursor(cursor_factory=RealDictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

    def show_all_databases(self):
        self.cursor.execute('SELECT datname FROM pg_database;')
        return self.cursor.fetchall()

    def get_blog_by_pk(self, pk):
        if not pk.isdigit():
            return {'error': 'pk is not digit.'}

        self.cursor.execute(f"SELECT * from blogs where pk = '{pk}'")

        result = self.cursor.fetchall()
        if not result:
            return {'error': 'target is not exist.'}

        return result

    def delete_blog_by_pk(self, pk):
        if not pk.isdigit():
            return {'error': 'pk is not digit.'}
        self.cursor.execute(f"delete from blogs where pk = '{pk}'")
        return True

    def show_all_blogs(self):
        self.cursor.execute('SELECT * from blogs;')
        aa = self.cursor.fetchall()
        return aa

    def create_new_blog(self, author, title, content, m_time, comments, likes):
        sql = f'''INSERT INTO blogs (author, title, content, m_time, comments, likes)
        VALUES ('{author}', '{title}', '{content}', '{m_time}', '{comments}', {likes});'''
        self.cursor.execute(sql)
        self.con.commit()
        return True

    # Will RESET table blogs!! Use with care!!
    def reset_table_blogs(self):
        sql = f'''drop table if exists blogs;
            drop sequence if exists blogs_pk_seq;
            create sequence blogs_pk_seq;
            create table blogs (
            pk integer not null default nextval('blogs_pk_seq'::regclass),
            author text not null,
            title text not null,
            content text COLLATE pg_catalog."default" NOT NULL,
            m_time timestamp not null,
            comments jsonb,
            likes integer,
            CONSTRAINT blogs_pkey PRIMARY KEY (pk)
            )
            tablespace pg_default;'''
        self.cursor.execute(sql)
        self.con.commit()


db_con = PostgreSQL_connection(
    host=db_info['host'],
    user=db_info['user'],
    database=db_info['database'],
    password=db_info['password'],
    port=db_info['port']
)
