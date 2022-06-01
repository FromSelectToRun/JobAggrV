"""create JobRawData table

Revision ID: c530d06b1cd1
Revises: 
Create Date: 2022-06-02 00:57:02.563722

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Boolean, Column,DateTime, Integer, Text, String

# revision identifiers, used by Alembic.
revision = 'c530d06b1cd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('jobarrgv_jobrawdata',
     Column('id',Integer, primary_key=True, index=True),
     Column('detail_url',String(512)),
     Column('job_title',String(512)),
     Column('company',String(512)),
     Column('location',String(512)),
     Column('from_where',String(512)),
     Column('crawled_time',DateTime),
     Column('post_time',DateTime),
     Column('category',String(512)),
     Column('extra',Text),
     Column('raw',Text),
     )
    


def downgrade():
    op.drop_table('jobarrgv_jobrawdata')
