# -*- coding:utf-8 -*-
import sqlite3

class Connect():
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print 'Banco: ', db_name
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print 'SQLite version: %s' % self.data
        except sqlite3.Error:
            print 'Erro ao abrir o banco'
            return False

    def close_db(self):
        if self.conn:
            self.conn.close()
            print 'conexão fechada'

class MinhasNotasDB(object):
    tb_name = 'minhasnotas'
    
    def __init__(self):
        self.db = Connect('minhasnotas.db')
        self.tb_name
        
    def close_connection(self):
        self.db.close_db()

    def criar_schema(self, schema_name='sql/materias_schema.sql'):
        print 'Criando tabela %s ...' % self.tb_name

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
                
        except sqlite3.Error:
            print 'Aviso: a tabela %s já existe.' % self.tb_name
            return False

        print 'Tabela %s criada com sucesso' % self.tb_name
        
if __name__ == '__main__':
    m =  MinhasNotasDB()
    m.criar_schema()
