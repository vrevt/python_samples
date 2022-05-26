import sqlite3
from random import randint

db = sqlite3.connect('db.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
	login TEXT,
	password TEXT, 
	cash BIGINT
)""")

db.commit()


def addUser():
	user_login = input('Login: ')
	user_password = input('Password: ')

	sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
	if sql.fetchone() is None:
		sql.execute(f"INSERT INTO users VALUES ('{user_login}', '{user_password}', {0})")
		db.commit()
		print('recorded')
	else:
		print('already in db')

	return user_login

def changeUser(user_login):
	user_login = input('Login: ')
	sql.execute(f'UPDATE users SET cash = {randint(1, 100)} WHERE login = "{user_login}"')
	print('updated')


def out():
	for value in sql.execute("SELECT * FROM users"):
		print(value)
	print('DB')


user_login = addUser()
changeUser(user_login)
out()
