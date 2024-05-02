##
# @file lmdb_storage.py
# @author Marián Tarageľ (xtarag01)

from .image_storage import ImageStorage
import pickle
import lmdb
import os

class LmdbImage(ImageStorage):
    """Storing images to a Lightning Memory-Mapped Database"""

    filename = "test.lmdb"
    format_name = "LMDB"

    def save(self, images, labels):
        map_size = len(images) * images[0].nbytes * 10
        env = lmdb.open(self.filename, map_size=map_size)

        with env.begin(write=True) as txn:
            for i in range(len(images)):
                key = str(i)
                value = (images[i], labels[i])
                txn.put(key.encode(), pickle.dumps(value))

        env.close()

    def read(self) -> tuple[list, list]:
        images, labels = [], []
        env = lmdb.open(self.filename, readonly=True)

        with env.begin() as txn:
            with txn.cursor() as cur:
                for key, value in cur:
                    data = pickle.loads(value)
                    images.append(data[0])
                    labels.append(data[1])
        
        env.close()

        return images, labels
    
    def remove(self):
        os.remove(self.filename + "/data.mdb")
        os.remove(self.filename + "/lock.mdb")
        os.rmdir(self.filename)

    def size(self):
        return os.path.getsize(self.filename + "/data.mdb") + os.path.getsize(self.filename + "/lock.mdb")