import os

DATA_FOLDER = "data"


def list_documents():

    files = []

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".pdf"):

            files.append(file)

    return files


def delete_document(filename):

    file_path = os.path.join(
        DATA_FOLDER,
        filename
    )

    if os.path.exists(file_path):

        os.remove(file_path)

        return True

    return False