from datetime import datetime, timedelta
import requests
import zipfile as zf
from io import BytesIO
from config import securities_url, bhavcopy_base_url, debug

# get securities.csv and store it
def get_securities():
    print('fetching securities')
    r = requests.get(securities_url)  
    with open(r'./securities/securities.csv', 'wb') as f:
        f.write(r.content)

# get bhavcopy url for given date
def get_bhavcopy_url(date):
    url = '/' + str(date.strftime("%Y/%^b/cm%d%^b%Y"))
    url += 'bhav.csv.zip'
    return url

# get bhavcopy.csv for given date
def get_bhavcopy_for(date):
    print('fetching bhavcopy for ' + str(date))
    url = bhavcopy_base_url + get_bhavcopy_url(date)
    debug and print(url)
    try:
        r = requests.get(url, timeout=(1,2))
        zipfile = zf.ZipFile(BytesIO(r.content))
        zipfile.extractall(r'./bhavcopy/')
    except:
        print()

# get latest bhavcopy
def get_latest_bhavcopy():
    print('fetching latest bhavcopy')
    get_bhavcopy_for(datetime.now() - timedelta(days = 1))

# get bhavcopy for last 30 days
def get_monthly_bhavcopy():
    for i in range(1, 31):
        get_bhavcopy_for(datetime.now() - timedelta(days = i))