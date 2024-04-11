from .image_storage import ImageStorage
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import numpy as np

class ParquetImage(ImageStorage):

    filename = "test.parquet"
    format_name = "Parquet"

    def save(self, images, labels):
        images_bytes, shape_x, shape_y, shape_z = [], [], [], []
        columns = ["images", "labels", "shape_x", "shape_y", "shape_z"]

        for img in images:
            shape = np.shape(img)
            shape_x.append(shape[0])
            shape_y.append(shape[1])
            if len(shape) > 2:
                shape_z.append(shape[2])
            else:
                shape_z.append(0)

            images_bytes.append(img.tobytes())

        images_arrow = pa.array(images_bytes, type=pa.binary())
        labels_arrow = pa.array(labels, type=pa.int8())
        shape_x_arrow = pa.array(shape_x, type=pa.int16())
        shape_y_arrow = pa.array(shape_y, type=pa.int16())
        shape_z_arrow = pa.array(shape_z, type=pa.int16())

        data = [images_arrow, labels_arrow, shape_x_arrow, shape_y_arrow, shape_z_arrow]
        table = pa.table(data, names=columns)

        pq.write_table(table, self.filename)

    def read(self):
        table = pd.read_parquet(self.filename)
        images = []
        for i, img_bytes in enumerate(table["images"]):
            if table["shape_z"][i] == 0:
                shape = (table["shape_x"][i], table["shape_y"][i])
            else:
                shape = (table["shape_x"][i], table["shape_y"][i], table["shape_z"][i])
            arr = np.frombuffer(img_bytes, dtype=np.uint8).reshape(shape)
            images.append(arr)

        labels = table["labels"].tolist()

        return images, labels