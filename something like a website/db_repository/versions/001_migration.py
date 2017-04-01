from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
languages = Table('languages', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('language', String(length=120)),
    Column('nonicon', String(length=20)),
    Column('url', String(length=120)),
    Column('icon_pattern', String(length=120)),
    Column('expression_pattern', String(length=120)),
    Column('word_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['languages'].columns['nonicon'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['languages'].columns['nonicon'].drop()
