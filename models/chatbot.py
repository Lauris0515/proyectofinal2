from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String

from database.basedatos import metaDatos,motorBD

#MODELO DE LA TABLA CHAT
chat=Table("chat", metaDatos, 
           Column("id",Integer,primary_key=True),
           Column("pregunta",String(200)),
           Column("respuestas",String(200))
           
           )

metaDatos.create_all(motorBD)