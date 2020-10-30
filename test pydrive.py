from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#spustí se prohlížeč, autorizuj se ve svém google accountu a povol přístup ke svému accountu aplikaci "Python" (nevím, proč jsem to tak pojmenovala)
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = "d:/nagympl/client_secrets.json" #zde zadej cestu k souboru client_secrets.json. měl by být ve stejné složce s tímto scriptem
drive = GoogleDrive(gauth)
#vypíše to seznam souborů v hlavním katalogu tvého accountu na google drive
#file_list = drive.ListFile({'q': "'dokumenty' in parents and trashed=false"}).GetList()
file_list = drive.ListFile({'q': "'dokumenty' in 'dokumenty'"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
