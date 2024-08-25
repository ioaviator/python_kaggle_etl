import shutil 
import zipfile

def extract_file(zip_file_path, download_dir):
    dataset_dir = "data"
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(f'{dataset_dir}/orders')
            print(f"Downloaded and extracted to: {dataset_dir}")
    except:
        print("Failed to download the file.")
    finally:
        shutil.rmtree(f"{download_dir}")
        print('done')