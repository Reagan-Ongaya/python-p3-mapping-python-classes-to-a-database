from config import CONN, CURSOR

import pytest; pytest.set_trace()

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album
        self.album = album    
        
    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)
        
        
        
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

    
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song