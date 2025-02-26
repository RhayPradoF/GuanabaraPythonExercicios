
import mysql.connector

try:
	conexao = mysql.connector.connect(host='localhost', user='root', password='', database='senai_saude')

	if conexao.is_connected():
		print("Conexão Realizada!")

except Exception as e:
	print("Erro:", e)