import os
import shutil

def organize_downloads(download_folder):
    # Define target folders
    images_folder = os.path.join(download_folder, 'images')
    data_folder = os.path.join(download_folder, 'data')
    docs_folder = os.path.join(download_folder, 'docs')
    archive_folder = os.path.join(download_folder, 'archive')

    # Create target folders if they don't exist
    for folder in [images_folder, data_folder, docs_folder, archive_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Get list of files in download folder
    files = os.listdir(download_folder)

    # Move files to respective folders
    for file in files:
        file_path = os.path.join(download_folder, file)
        if os.path.isfile(file_path):
            if file.lower().endswith(('.jpg', '.jpeg')):
                shutil.move(file_path, images_folder)
            elif file.lower().endswith(('.csv', '.xlsx')):
                shutil.move(file_path, data_folder)
            elif file.lower().endswith(('.txt', '.doc', '.pdf')):
                shutil.move(file_path, data_folder)
            elif file.lower().endswith('.zip'):
                shutil.move(file_path, archive_folder)

if __name__ == "__main__":
    download_folder = r'C:\Users\student\Downloads'
    organize_downloads(download_folder)
