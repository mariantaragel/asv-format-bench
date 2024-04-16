##
# @file base64_string.py
# @author Marián Tarageľ (xtarag01)

from .image_storage import ImageStorage
import numpy as np
import base64
import csv
import sys

class Base64String(ImageStorage):
    """Encoding images to Base64 strings"""

    filename = "test.csv"
    format_name = "Base64"

    def save(self, images, labels):
        images_strings = []
        shape_x, shape_y, shape_z = [], [], []
        for img_arr in images:
            shape = np.shape(img_arr)
            shape_x.append(shape[0])
            shape_y.append(shape[1])
            if len(shape) > 2:
                shape_z.append(shape[2])
            else:
                shape_z.append(None)

            base64_string = base64.b64encode(img_arr).decode()
            images_strings.append(base64_string)

        with open(self.filename, "w", newline="") as csvfile:
            csv_witer = csv.writer(csvfile, quotechar=None, quoting=csv.QUOTE_NONE)
            csv_witer.writerow(["label", "image", "shape_x", "shape_y", "shape_z"])
            csv_witer.writerows(list(zip(labels, images_strings, shape_x, shape_y, shape_z)))

    def read(self) -> tuple[list, list]:
        csv.field_size_limit(sys.maxsize)

        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            labels, images = [], []
            for line_number, line in enumerate(csv_reader):
                if line_number == 0:
                    continue
                else:
                    label = int(line[0])
                    base64_string = line[1]
                    shape_x = int(line[2])
                    shape_y = int(line[3])
                    shape_z = line[4]

                    labels.append(label)

                    bytes = base64.decodebytes(base64_string.encode())
                    arr = np.frombuffer(bytes, dtype=np.uint8)
                    if shape_z == "":
                        arr_reshaped = arr.reshape(shape_x, shape_y)
                    else:
                        arr_reshaped = arr.reshape(shape_x, shape_y, int(shape_z))

                    images.append(arr_reshaped)

        return images, labels