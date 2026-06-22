import os
import shutil

from file_classifier import (
    FileClassifier
)


def organize_folder(folder_path):

    classifier = FileClassifier()

    report = []

    files = os.listdir(
        folder_path
    )

    for file in files:

        full_path = os.path.join(

            folder_path,

            file

        )

        if os.path.isfile(
            full_path
        ):

            category = (

                classifier
                .get_category(file)

            )

            destination_folder = (

                os.path.join(

                    folder_path,

                    category

                )

            )

            os.makedirs(

                destination_folder,

                exist_ok=True

            )

            destination_file = (

                os.path.join(

                    destination_folder,

                    file

                )

            )

            shutil.move(

                full_path,

                destination_file

            )

            report.append(

                f"{file} -> {category}"

            )

    with open(

        os.path.join(

            folder_path,

            "organization_report.txt"

        ),

        "w",

        encoding="utf-8"

    ) as file:

        file.write(

            "\n".join(report)

        )

    print(
        "\nOrganization Complete"
    )

    print(
        "\nGenerated:"
    )

    print(
        "organization_report.txt"
    )


if __name__ == "__main__":

    print(
        "\n========================="
    )

    print(
        "SMART FILE ORGANIZER"
    )

    print(
        "========================="
    )

    folder = input(
        "\nFolder Path:\n"
    )

    if os.path.exists(
        folder
    ):

        organize_folder(
            folder
        )

    else:

        print(
            "\nInvalid Folder Path"
        )