from service.connection import Connection
from model.CartaoModel import ItemCreate

class Metodos:
    @staticmethod
    def _get_cursor():
        """Cria e retorna uma conexão e um cursor para o banco de dados."""
        conn = Connection.get_db_connection()
        return conn, conn.cursor()

    @classmethod
    def create_table(cls):
        conn, cursor = cls._get_cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CARTAO (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                RESPONSAVEL TEXT NOT NULL,
                LOCAL TEXT NOT NULL,
                VALOR REAL,
                DATAUSO TEXT
            )
        ''')
        conn.commit()
        conn.close()

    @classmethod
    def insert(cls, item: ItemCreate):
        conn, cursor = cls._get_cursor()
        cursor.execute('''
            INSERT INTO CARTAO (RESPONSAVEL, LOCAL, VALOR, DATAUSO) VALUES (?, ?, ?, ?)
        ''', (item.responsavel, item.local, item.valor, item.datauso))
        item_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return {"id": item_id, "responsavel": item.responsavel, "local": item.local}

    @classmethod
    def get(cls):
        conn, cursor = cls._get_cursor()
        cursor.execute('SELECT * FROM CARTAO')
        items = cursor.fetchall()
        conn.close()
        return {"items": [dict(item) for item in items]}

    @classmethod
    def count(cls):
        conn, cursor = cls._get_cursor()
        cursor.execute("SELECT COUNT(*) FROM CARTAO")
        count = cursor.fetchone()[0]
        conn.close()
        return {"quantidade total de uso ": count}
    
    @classmethod
    def delete_id(cls, item_id: int):
        conn, cursor = cls._get_cursor()
        cursor.execute("DELETE FROM CARTAO WHERE ID = ?", (item_id))
        conn.commit()
        conn.close()
        return{"response ": f"Registro ID {item_id} DELETADO"}
