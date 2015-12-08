from datetime import datetime

from sqlalchemy import (create_engine, MetaData, Table, Column, Integer,
    String, DateTime, Float, ForeignKey, and_, ForeignKeyConstraint)
from sqlalchemy.orm import mapper, relationship, Session, subqueryload, lazyload
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////Users/pdy/code/SurveyORM/dbs/survey')

Base = declarative_base()

Base.metadata.create_all(engine)

# Variable Class
class VariableList(Base):

    __tablename__ = 'variablelist'

    ROWID = Column(Integer, primary_key=True)
    name = Column(String)
    section = Column(String)
    level = Column(String)
    question = Column(String)

    def __init__(self, name):
        self.name = name    


    # This uses name, section and level as a key to join the variables table (variables) to the code frames table(codeframes).
    # This is a one (variables) to many (codeframes) relationship. 

    # The technique I used was not in the documentation but in this thread on the mailing list.  

    # https://groups.google.com/forum/#!searchin/sqlalchemy/foreign_keys/sqlalchemy/lq_e0Frr4qY/Ru132ljwmmQJ


    code_frames = relationship("CodeFrames", primaryjoin="and_(foreign(VariableList.name)==CodeFrames.variable, foreign(VariableList.section)==CodeFrames.section, foreign(VariableList.level)==CodeFrames.level)", backref='variablelist', uselist=True, ) 

# Code Frequency Class
class CodeFrequencies(Base):

    __tablename__ = 'codefrequencies'

    ROWID = Column(Integer, primary_key=True)
    variable = Column(String)
    section = Column(String)
    frequency = Column(Integer)
    number = Column(Integer)
    level = Column(String)


    def __init__(self, frequency):
        self.frequency = frequency

    def __repr__(self):
        return 'CodeFrequencies(%r)' % (
                    self.frequency
                )

# Codeframe Class
class CodeFrames(Base):

    __tablename__ = 'codeframes'


    ROWID = Column(Integer, primary_key=True)
    variable = Column(String)
    section = Column(String)
    text = Column(String)
    number = Column(Integer)
    level = Column(String)

    def __init__(self, text, number):
        self.text = text
        self.number = number
    
    code_freqs = relationship("CodeFrequencies", uselist=False, primaryjoin="and_(foreign(CodeFrames.variable)==CodeFrequencies.variable, foreign(CodeFrames.section)==CodeFrequencies.section, foreign(CodeFrames.level)==CodeFrequencies.level, foreign(CodeFrames.number)==CodeFrequencies.number)")


session = Session(engine)

vnames = session.query(VariableList, VariableList.name).all()

for v in vnames:
    v4query = v.name
    print v4query
    variable_list = session.query(VariableList).filter_by(name=v4query).one()
    print variable_list.section
    print variable_list.level
    print variable_list.question

    for code_frame in variable_list.code_frames:
        if code_frame.code_freqs is not None:
            print(code_frame.code_freqs.number, code_frame.text, code_frame.code_freqs.frequency)

