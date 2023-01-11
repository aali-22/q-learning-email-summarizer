import pandas as pd
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Build the GMAIL API service
flow = InstalledAppFlow.from_client_secrets_file("ali_cred.json", SCOPES)
creds = flow.run_local_server()

# load the credentials from token.json


#create the service
service = build('gmail', 'v1', credentials=creds)


#Retrieve the list of emails from the mailbox
num_emails = 5
result = service.users().messages().list(userId='me', maxResults=num_emails).execute()
messages = result.get('messages', [])

# Load the email dataset into a DataFrame
#emails_df = pd.read_csv('emails.csv')
emails_df = pd.DataFrame(columns=['subject', 'body', 'label'])

# Add the new emails from the mailbox to the dataset
for msg in messages:
    email = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
    headers = email['payload']['headers']
    subject = next(header['value'] for header in headers if header['name'] == 'Subject')
    if 'parts' in email['payload']:
        try:
            parts = email['payload']['parts']
            for p in parts:
                if p["mimeType"] in ["text/plain", "text/html"]:
                    data = base64.urlsafe_b64decode(p["body"]["data"]).decode("utf-8")
                    print(data)

        except StopIteration as e:
            print("StopIteration error handled successfully")
    else:
        body = email['payload']['body']['data']
    email_data = {
        'subject': subject,
        'body': data,
        'label': '' # add label if you use labeled data 
    }
    



# Process the emails
# ...

# Train and evaluate the model
# ...
