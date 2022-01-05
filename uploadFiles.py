import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload(self,file_to,file_from):
        dbx = dropbox.Dropbox(self.access_token)

        for root,direcs, files in os.walk(file_from):
            
            for filename in files:
                local_path = os.path.join(root,filename)

                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))

def main():
    access_token =  'sl.A_dQYerpw8mG9fy6gtTaTYJQ_wJl9cQ4DXChTvF-AuJm9qXEe0mhj-JJpL4cdznyADSC_FxtFsy0lhMHK3MtAyAuIHJRi4bTnqiKMr2DFBoBU7JuEMu_i8bKH8J9Ua4r7lzD98o'
    tD =TransferData(access_token)

    file_from = input("Enter the folder path to transfer :-")
    file_to = input("Enter the full path to upload to DropBox :-")

    tD.upload_file(file_from,file_to)
    print("File has been moved succefully")

main()