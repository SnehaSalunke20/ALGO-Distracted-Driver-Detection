from pathlib import Path
import os
import glob

from utils.load import get_project_root

def delete_files_in_directory(directory_path):
   try:
     files = glob.glob(os.path.join(directory_path, '*'))
     for file in files:
       if os.path.isfile(file):
         os.remove(file)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")

def store_doc(uploaded_file):
    # Save uploaded file to 'F:/tmp' folder.
    save_folder_path = Path(get_project_root()) / f"data/temp/"
    isExisting = os.path.exists(save_folder_path)
    if not isExisting:
       os.mkdir(save_folder_path)
    delete_files_in_directory(save_folder_path)
    save_path = Path(save_folder_path, uploaded_file.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())
    return save_path