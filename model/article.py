# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    body = Column(Text)
    publish_time = Column(String)
    source_site = Column(String)

