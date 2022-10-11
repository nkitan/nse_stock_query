import requests
import zipfile as zf
from io import BytesIO
from config import securities_url, bhavcopy_url

def get_securities():
    print('fetching securities')
    r = requests.get(securities_url)  
    with open(r'./securities/securities.csv', 'wb') as f:
        f.write(r.content)

def get_bhavcopy():
    print('fetching bhavcopy')
    r = requests.get(bhavcopy_url)
    zipfile = zf.ZipFile(BytesIO(r.content))
    zipfile.extractall(r'./bhavcopy/')