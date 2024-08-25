import os

def download_file(download_dir:str) -> tuple[str,str]:
    '''
        connects to the kaggle api, authenticates and downloads the specified file

        args:
            download_dir(str): path to created directory where downloaded files are stored
        
            return:
                tuple[str,str]: 
                absolute file path for downloded file
                directory name where downloaded files are stored
    '''

    zip_file_path = os.path.join(f"{download_dir}", 'orders.csv.zip')

    if os.path.exists(zip_file_path):
        print('file already exists')
    else:
        os.system(f'kaggle datasets download ankitbansal06/retail-orders -f orders.csv -p {download_dir}')

    return zip_file_path, download_dir