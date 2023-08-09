from __future__ import print_function

import os.path
from os import environ

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from settings import SCOPES, GOOGLE_TOKEN, GOOGLE_CREDENTIALS

load_dotenv()
# If modifying these scopes, delete the file token.json.
# GOOGLE_CREDENTIALS_TOKEN
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = environ.get("SAMPLE_SPREADSHEET_ID")
SAMPLE_RANGE_NAME = 'Лист1!H:H'


def google_sipher():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(GOOGLE_TOKEN):
        creds = Credentials.from_authorized_user_file(GOOGLE_TOKEN, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                GOOGLE_CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(GOOGLE_TOKEN, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        cipher_lst = [i[0] for i in values if i]
        return cipher_lst
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    google_sipher()

