# Import PyDrive and associated libraries.
# This only needs to be done once per notebook.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
import pandas as pd
df=pd.DataFrame(columns=('title', 'id','createdDate','modifiedDate','downloadUrl'))
# List .txt files in the root.
#
# Search query reference:
# https://developers.google.com/drive/v2/web/search-parameters
listed = drive.ListFile({'q': "'18ZoQnaWoxAUbW8KaCvHX3R9IQhjzTdyS' in parents and trashed=false"}).GetList()
file.FetchMetadata()
for file in listed:
 
  listoffile=pd.DataFrame([[file['title'],file['id'],file['createdDate'],file['modifiedDate'],'https://docs.google.com/uc?export=download&id='+file['id']]],columns=('title', 'id','createdDate','modifiedDate','downloadUrl'))
  df=df.append(listoffile)

