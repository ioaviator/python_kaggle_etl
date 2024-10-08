import os


def create_download_dir() -> str:
    '''
        creates directory for data downloaded from api

        return:
            str -> directory name where files will be saved
    '''

    download_dir = "data/downloads"

    if not os.path.exists(download_dir):
        os.makedirs(f"{download_dir}", exist_ok=True)
    
    return download_dir

