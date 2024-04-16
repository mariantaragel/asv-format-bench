##
# @file generator.py
# @author Marián Tarageľ (xtarag01)
# @brief Create and load datasets

from .gen_dtype import GenDtype
from .dataset import Dataset
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import random
import glob
import math
import io

class Generator:

    @staticmethod
    def gen_dataset(
        name: str,
        entries: int,
        int_cols: int,
        float_cols: int,
        bool_cols: int,
        str_fixed_cols: int,
        str_var_cols: int,
        str_word_cols: int,
    ) -> Dataset:
        """
        Generate synthetic, tabular dataset
        
        name : name of a dataset
        entries : number of rows in a DataFrame
        int_cols : number of integer columns
        float_cols : number of float columns
        bool_cols : number of bool columns
        str_fixed_cols : number of string columns with fixed length
        str_var_cols : number of string columns with variable length
        str_word_cols : number of columns with real English words
        """
        gd = GenDtype()

        num_of_cols = int_cols + float_cols + bool_cols + str_fixed_cols + str_var_cols + str_word_cols
        cols = [f"col{i}" for i in range(num_of_cols)]

        data = []
        for i in range(int_cols):
            data.append(gd.gen_int_col(0, 100, entries))
        for i in range(float_cols):
            data.append(gd.gen_float_col(0, 100, entries))
        for i in range(bool_cols):
            data.append(gd.gen_bool_col(entries))
        for i in range(str_fixed_cols):
            data.append(gd.gen_fixed_str_col(10, entries))
        for i in range(str_var_cols):
            data.append(gd.gen_var_str_col(0, 10, entries))
        for i in range(str_word_cols):
            data.append(gd.gen_str_words(entries))

        random.shuffle(data)
        df = pd.DataFrame(dict(zip(cols, data)))

        return Dataset(name, df=df)

    @staticmethod
    def load_webface() -> Dataset:
        return Dataset("webface")

    @staticmethod
    def load_cifar_10(entries: int) -> Dataset:
        """
        Load Cifar-10 dataset

        entries : number of imges to load
        """
        pathname = "/home/marian/Projects/School/BP/asv/cifar-10/*_batch*"
        labels, images = [], []
        number_of_batches = math.ceil(entries / 10000)

        for batch_file in glob.glob(pathname)[:number_of_batches]:
            with open(batch_file, "rb") as pickle_file:
                batch = pickle.load(pickle_file, encoding="bytes")
                data_batch = batch[b"data"]
                label_batch = batch[b"labels"]
                labels += label_batch

                for img_list in data_batch:
                    img_array = np.array(img_list)
                    rgb = []

                    for i in range(3):
                        rgb.append(img_array[i * 1024 : 1024 * (i + 1)].reshape(32, 32))

                    img_raw = np.dstack(rgb)
                    images.append(img_raw)

        return Dataset("Cifar-10", images=images[:entries], labels=labels[:entries])

    @staticmethod
    def load_imagenet_100(entries: int) -> Dataset:
        """
        Load Imagenet-100 dataset

        entries : number of imges to load
        """
        df = pd.read_parquet("/home/marian/Projects/School/BP/asv/imagenet-100/ImageNet0-5.parquet")
        images_bytes = df["image"][:entries]
        labels = df["label"][:entries].to_list()
        images = []

        for img in images_bytes:
            image = Image.open(io.BytesIO(img["bytes"]))
            arr = np.asarray(image)
            images.append(arr)

        return Dataset("Imagenet-100", images=images, labels=labels)
