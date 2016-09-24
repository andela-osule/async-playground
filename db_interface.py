import sqlite3

class DB:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', '')
    
    def action(self, sql, params=()): # non-select query
        self._db.execute(sql, params)
        self._db.commit()
    
    def query(self, sql, params=()):
        """ @yields: RowFactory
        """
        cursor = self._db.cursor()
        cursor.execute(sql, params)
        for row in cursor:
            yield row
    
    def query_row(self, sql, params=()):
        cursor = self._db.cursor()
        cursor.execute(sql, params)
        return cursor.fetchone()
    
    def query_value(self, sql, params=()):
        cursor = self._db.cursor()
        cursor.execute(sql, params)
        return cursor.fetchone()[0]
    
    def get_record(self, id):
        query = "SELECT * FROM {} WHERE id=?".format(self.table)
        cursor = self._db.execute(query, (id, ))
        return cursor.fetchone()
    
    def get_records(self):
        query = "SELECT * FROM {}".format(self.table)
        cursor = self._db.execute(query)
        for row in cursor:
            yield row
    
    def insert(self, record):
        keys = sorted(record.keys())
        values = [record[key] for key in keys]
        query = "INSERT INTO {} ({}) VALUES ({})".format(
            self.table,
            ', '.join(keys),
            ', '.join('?' for i in range(len(values)))
        )
        cursor = self._db.execute(query, values)
        self._db.commit()
        return cursor.lastrowid
    
    def update(self, id, record):
        keys = sorted(record.keys())
        values = [record[key] for key in keys]
        
        for i, key in enumerate(keys):
            if key == 'id':
                del keys[i]
                del values[i]
        query = "UPDATE {} SET {} WHERE id=?".format(
            self.table,
            ', '.join(map(lambda str: '{}=?'.format(str), keys))
        )
        self._db.execute(q, values + [id])
        self._db.commit()
    
    def delete(self, id):
        query = "DELETE FROM {} WHERE id=?".format(self.table)
        self._db.execute(query, [id])
        self._db.commit()
    
    def count_records(self):
        query = "SELECT COUNT(*) FROM {}".format(self.table)
        cursor = self._db.cursor()
        cursor.execute(query)
        return cursor.fetchone()

    @property
    def filename(self):
        return self._db_filename

    @filename.setter
    def filename(self, filename):
        self._db_filename = filename
        self._db = sqlite3.connect(filename)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self):
        self.close()
    
    def close(self):
        self._db.close()
        del self._db_filename

def test():
    filename = ":memory:"
    table = "foo"

    records = [

    ]
