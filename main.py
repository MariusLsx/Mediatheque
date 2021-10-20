#coding:utf-8
import sqlite3

connection = sqlite3.connect("mediathequebdd.db")
cursor = connection.cursor()

my_username = ("Jason",)
cursor.execute('SELECT * FROM med_users WHERE user_name = ?', my_username)
result = cursor.fetchone()[1]

print(f"Le nom d'utilisateur est : {result}")



connection.close()