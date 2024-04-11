from .image_storage import ImageStorage
import numpy as np
import h5py

class Hdf5Image(ImageStorage):

    filename = "test.h5"
    format_name = "HDF5"

    def save(self, images, labels):
        shape_x, shape_y, shape_z = [], [], []
        for img in images:
            shape = np.shape(img)
            shape_x.append(shape[0])
            shape_y.append(shape[1])
            if len(shape) > 2:
                shape_z.append(shape[2])
            else:
                shape_z.append(0)

        dt = h5py.vlen_dtype(np.dtype("uint8"))

        with h5py.File(self.filename, "w") as hdf5_file:
            images_ds = hdf5_file.create_dataset(name="images", shape=len(images), dtype=dt)
            hdf5_file.create_dataset(name="labels", data=labels, dtype=np.uint8)
            hdf5_file.create_dataset(name="shape_x", data=shape_x, dtype=np.uint16)
            hdf5_file.create_dataset(name="shape_y", data=shape_y, dtype=np.uint16)
            hdf5_file.create_dataset(name="shape_z", data=shape_z, dtype=np.uint16)

            for i, img_bytes in enumerate(images):
                images_ds[i] = np.ravel(img_bytes)

    def read(self):
        with h5py.File(self.filename, "r") as hdf5_file:
            labels = hdf5_file["labels"][:].astype("uint8").tolist()
            images = []

            ds_len = len(labels)
            for i in range(ds_len):
                if hdf5_file["shape_z"][i] == 0:
                    shape = (hdf5_file["shape_x"][i], hdf5_file["shape_y"][i])
                else:
                    shape = (hdf5_file["shape_x"][i], hdf5_file["shape_y"][i], hdf5_file["shape_z"][i])
                
                arr = hdf5_file["images"][i].reshape(shape)
                images.append(arr)

        return images, labels