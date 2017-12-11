
from __future__ import print_function
import httplib2
import os
import base64
from email.mime.text import MIMEText

from apiclient import discovery
from apiclient import errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def send_mail(pessoas):
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    for i in range(len(pessoas)):
      amigo = pessoas[i]
      recipiente = pessoas[(i+1)%len(pessoas)]

      message = MIMEText(
"""Bem-vindo ao amigo secreto da familia, {}.

Seu amig@ secret@ e {}.

Por favor lembre-se que os presentes devem ser no valor de ate {} reais.

Feliz natal e ate logo!""".format(amigo._nome, recipiente._nome, "80"))
      message['to'] = "alexsusemihl@gmail.com"
      message['from'] = "alexsusemihl@gmail.com"
      message['subject'] = "Ola {}, seu amigo secreto foi sorteado.".format(amigo._nome)

      message_final = {'raw': base64.urlsafe_b64encode(message.as_string())}

      try:
        message = (service.users().messages().send(userId='me', body=message_final).execute())
      except Exception as error:
        print('An error has occurred: {}'.format(error))

if __name__ == "__main__":
  send_mail()
