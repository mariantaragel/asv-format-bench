##
# @file generator.py
# @author Marián Tarageľ (xtarag01)
# @brief Create and load datasets

from datasets import load_dataset
from .gen_dtype import GenDtype
from .dataset import Dataset
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import random
import h5py
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
    def load_cifar_10(entries: int) -> Dataset:
        """
        Load Cifar-10 dataset

        entries : number of imges to load
        """
        cifar_10 = load_dataset("cifar10", split="train")
        
        images = []
        for img in cifar_10["img"]:
            img_array = np.array(img)
            images.append(img_array)

        return Dataset("Cifar-10", images=images[:entries], labels=cifar_10["label"][:entries])

    @staticmethod
    def load_imagenet_100(entries: int) -> Dataset:
        """
        Load Imagenet-100 dataset

        entries : number of imges to load
        """
        imagenet_100 = load_dataset("clane9/imagenet-100", split="train")

        images = []
        for img in imagenet_100["image"]:
            img_array = np.array(img)
            images.append(img_array)

        return Dataset("Imagenet-100", images=images[:entries], labels=imagenet_100["label"][:entries])

    @staticmethod
    def load_webface10M() -> Dataset:
        """Load Webface10M datset"""
        filename = "/home/xtarag01/synthetic_webface10M.h5"

        with h5py.File(filename, "r") as f:
            webface_key = list(f.keys())[1]
            webface = f[webface_key]
            webface_data = webface[:]

            df = pd.DataFrame(webface_data)

        columns = ["bbox", "db_id", "image_container_path", "image_id", "ipt_str", "subject_id"]
        df.loc[:,columns] = df[columns].map(str)
        
        return Dataset("Webface10M", df=df)