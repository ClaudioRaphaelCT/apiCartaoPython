import sqlite3

class Connection:
    db_path = "data/Cartao.db"

    @classmethod
    def get_db_connection(cls):
        conn = sqlite3.connect(cls.db_path)
        conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
        return conn