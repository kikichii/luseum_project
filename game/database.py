import sqlite3

class Database:
    def __init__(self, db_name='game_data.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        # Создаем таблицу, если она не существует
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT,
                points INTEGER
            )
        ''')
        self.conn.commit()

    def add_record(self, time, points):
        # Метод для записи данных в БД
        self.cursor.execute('''
            INSERT INTO scores (time, points) VALUES (?, ?)
        ''', (time, points))
        self.conn.commit()

    def view_record(self, record_id):
        # Метод для просмотра записи по ID
        self.cursor.execute('SELECT * FROM scores WHERE id = ?', (record_id,))
        record = self.cursor.fetchone()
        if record:
            return {
                'id': record[0],
                'time': record[1],
                'points': record[2]
            }
        else:
            return None

    def view_all_records(self):
        # Метод для просмотра всех данных
        self.cursor.execute('SELECT * FROM scores')
        records = self.cursor.fetchall()
        return [
            {'id': record[0], 'time': record[1], 'points': record[2]}
            for record in records
        ]

    def delete_record(self, record_id=None):
        # Метод для удаления записи по ID или всех записей
        if record_id is not None:
            self.cursor.execute('DELETE FROM scores WHERE id = ?', (record_id,))
        else:
            self.cursor.execute('DELETE FROM scores')
        self.conn.commit()

    def close(self):
        # Закрываем соединение с базой данных
        self.conn.close()