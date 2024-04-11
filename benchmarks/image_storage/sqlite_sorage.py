from .image_storage import ImageStorage
import numpy as np
import sqlite3

class Sqlite(ImageStorage):

    filename = "test.db"
    format_name = "SQLite"

    def save(self, images, labels):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        drop_table = "DROP TABLE IF EXISTS Data;"
        cur.execute(drop_table)
        con.commit()

        create_tabel = """CREATE TABLE Data (
            label INTEGER NOT NULL,
            image BLOB NOT NULL,
            shape_x INTEGER NOT NULL,
            shape_y INTEGER NOT NULL,
            shape_z INTEGER);"""
        
        cur.execute(create_tabel)
        con.commit()

        insert = "INSERT INTO Data (label, image, shape_x, shape_y, shape_z) VALUES (?, ?, ?, ?, ?)"

        images_len = len(images)
        for i in range(images_len):
            shape = np.shape(images[i])
            shape_x = shape[0]
            shape_y = shape[1]
            if len(shape) > 2:
                shape_z = shape[2]
            else:
                shape_z = None

            data = (labels[i], images[i].tobytes(), shape_x, shape_y, shape_z)
            cur.execute(insert, data)
        
        con.commit()

        cur.close()
        con.close()

    def read(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        images, labels = [], []

        fetch = "SELECT * FROM Data"
        records = cur.execute(fetch)

        for row in records:
            labels.append(row[0])

            if row[4] == None:
                shape = (row[2], row[3])
            else:
                shape = (row[2], row[3], row[4])

            arr = np.frombuffer(row[1], dtype=np.uint8).reshape(shape)
            images.append(arr)

        cur.close()
        con.close()

        return images, labels