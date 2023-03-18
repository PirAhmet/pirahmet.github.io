import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with your own Google Drive API credentials file
credentials_file = "credentials.json"

# Replace with the ID of the folder you want to start with
root_folder_id = "18ZoQnaWoxAUbW8KaCvHX3R9IQhjzTdyS"

# Create a Google Drive API client using the credentials file
credentials = service_account.Credentials.from_service_account_file(credentials_file)
service = build("drive", "v3", credentials=credentials)

def get_files_in_folder(folder_id):
    """Returns a list of files in the given folder ID"""
    results = []
    query = f"'{folder_id}' in parents and trashed = false"
    page_token = None
    while True:
        response = service.files().list(q=query,
                                         fields="nextPageToken, files(id, name, mimeType, parents)",
                                         pageToken=page_token).execute()
        files = response.get("files", [])
        results.extend(files)
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return results

def get_folder_path(folder_id):
    """Returns the full path of the given folder ID"""
    folder = service.files().get(fileId=folder_id, fields="id, name, parents").execute()
    folder_name = folder["name"]
    parent_id = folder.get("parents", [])[0]
    if parent_id:
        parent_path = get_folder_path(parent_id)
        return os.path.join(parent_path, folder_name)
    else:
        return folder_name

def print_folder_tree(folder_id, indent=0):
    """Recursively generates a tree view of the given folder ID"""
    files = get_files_in_folder(folder_id)
    for file in files:
        if file["mimeType"] == "application/vnd.google-apps.folder":
            print(" " * indent + "- " + file["name"] + " (folder) - " + get_folder_path(file["id"]))
            print_folder_tree(file["id"], indent+2)
        else:
            print(" " * indent + "- " + file["name"] + " (file) - " + get_folder_path(file["id"]))


# Example usage:
def main():
    print_folder_tree(root_folder_id)

main()
