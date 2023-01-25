from django.db import models
from django.contrib.auth import get_user_model

class Agenda(models.Model):
    descricao = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.descricao


"""import MySQLdb
 
connection = MySQLdb.connect(
    host="localhost",
    user="<mysql_user>",
    passwd="<mysql_password>",
    db="<database_name>"
)
 
cursor = connection.cursor()
cursor.execute("select database();")
db = cursor.fetchone()
 
if db:
    print("Você está conectado ao banco de dados: ", db)
else:
    print('Não conectado.')"""