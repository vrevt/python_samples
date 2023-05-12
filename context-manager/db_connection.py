import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(':memory:')
    with conn:
        # начинаем новую db
        conn.execute('create table mytable (id int primary key, name char(50))')
        conn.execute('insert into mytable(id) values (?)', (1, 'avni'))
        # если что-то пошло не так, то таблица в БД создана не будет
        # транзакция вернёт БД к исходному состоянию
        ...
    # conn.commit() вызов.
