##
# @file image_storage.py
# @author Marián Tarageľ (xtarag01)
# @brief Base class for all image storages

import os

class ImageStorage:

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return self.format_name

    def save(self, images, labels):
        """
        Save images and labels to the images storage

        images : list of images (numpy.ndarray)
        labels : list of labels (uint8)
        """
        pass

    def read(self) -> tuple[list, list]:
        """Read images and labels from the image storage"""
        pass

    def size(self) -> int:
        """Get the total size of created files"""
        return os.path.getsize(self.filename)

    def remove(self):
        """Remove all created files"""
        if os.path.exists(self.filename):
            os.remove(self.filename)