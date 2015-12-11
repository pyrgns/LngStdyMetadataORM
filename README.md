# Loading Longitudinal Study Metadata into an Object Relational Mapper

This file uses the [composite foreign keys](https://en.wikipedia.org/wiki/Compound_key) 
available in legacy or questionably formatted survey metadata to create models for an [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) 
aka Object Relational Mapper. 

It uses the Python Object Relational Mapper and Toolkit [SQLAlchemy](http://www.sqlalchemy.org/) Version '0.9.8'

For more information on how to use SQLAlchemy please see this tutorial:

(http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html)

Please see the comments in the code below regarding the relationships. 

This is using [sqlite](https://www.sqlite.org/) as a database but SQLAlchemy supports a variety of 
relational databases. 