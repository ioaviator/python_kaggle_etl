import os

def download_file(download_dir):
    zip_file_path = os.path.join(f"{download_dir}", 'orders.csv.zip')

    if os.path.exists(zip_file_path):
        print('file already exists')
    else:
        os.system(f'kaggle datasets download ankitbansal06/retail-orders -f orders.csv -p {download_dir}')
