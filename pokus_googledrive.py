#přístup na google drive
import pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#spustí se prohlížeč, autorizuj se ve svém google accountu a povol přístup ke svému accountu aplikaci "Python" (nevím, proč jsem to 
# tak pojmenovala)
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = "d:/nagympl/nagympl/client_secrets.json" #zde zadej cestu k souboru 
#client_secrets.json. měl by být ve stejné složce s tímto scriptem
drive = GoogleDrive(gauth)

#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for file1 in file_list:
#  print('title: %s, id: %s' % (file1['title'], file1['id']))

page_token = None
while True:
    response = drive_service.files().list(q = "mimeType ='application/vnd.google-apps.folder'",
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    for file in response.get('files', []):
        # Process change
        print(f'Found file: {file.get(name)}, ID: {file.get(id)}')
    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break

#chyba: NameError: name 'drive_service' is not defined


import tabula
#df = tabula.read_pdf("D:/data_gymply/GJH-2019.pdf", pages = 'all')
#with open(r"D:/pythonprocvicovani/tabulatest.csv") as soubor:
#    soubor.write(df)

#soubor.close()