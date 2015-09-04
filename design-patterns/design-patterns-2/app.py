# -*- coding: utf-8 -*-

import MySQLdb
from connection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()

cursor = connection.cursor()
cursor.execute('SELECT * FROM cursor')

for linha in cursor:
	print linha

connection.close()