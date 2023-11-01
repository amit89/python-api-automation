import os
from pathlib import Path


class PathHelper:

    @staticmethod
    def get_root_path() -> Path:
        return Path(os.path.dirname(os.path.abspath(__file__))).parent

    @staticmethod
    def get_folder_path(folder_name) -> str:
        folder_path = os.path.join(PathHelper.get_root_path(), "request_data", folder_name)
        os.makedirs(folder_name, exist_ok=True)
        return folder_path

    @staticmethod
    def get_file_path(folder_name, file_name) -> str:
        return os.path.join(PathHelper.get_folder_path(folder_name), file_name)
