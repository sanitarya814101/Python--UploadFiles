import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = "sl.A3YfvljFidU1zccrCgxrmmRZWTox-BA2ZkrTNjLT0dteyPW6HpUMq1ThPusimARtLBafh9brztQJwqVS06oU-1HkHyb-FwsaBRKraJVSWf-zk4fA9ATBGXHN_C2UUDcZFz0ft7I"
    transfer_data = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the file path to upload the dropbox: ")

    transfer_data.upload_file(file_from, file_to)
    print("Files have been moved sucessfully...")


main()
