import os


class FileClassifier:

    def __init__(self):

        self.categories = {

            "Documents": [
                ".pdf",
                ".doc",
                ".docx",
                ".txt"
            ],

            "Images": [
                ".jpg",
                ".jpeg",
                ".png",
                ".gif"
            ],

            "Videos": [
                ".mp4",
                ".avi",
                ".mkv"
            ],

            "Audio": [
                ".mp3",
                ".wav"
            ],

            "Archives": [
                ".zip",
                ".rar"
            ],

            "Code": [
                ".py",
                ".js",
                ".java",
                ".cpp",
                ".html",
                ".css"
            ]

        }

    def get_category(

        self,

        filename

    ):

        extension = os.path.splitext(
            filename
        )[1].lower()

        for category, extensions in (

            self.categories.items()

        ):

            if extension in extensions:

                return category

        return "Others"