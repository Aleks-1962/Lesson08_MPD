import requests
import shutil
import pandas as pd


zip_file_url= ['https://data.gov.ru/sites/default/files/opendata/2310032408-mfks_p/data-2017-12-27T00-00-00-structure-2017-12-27T00-00-00.csv']

for num, i in enumerate(zip_file_url):
    response = requests.get(i , stream = True)
    with open(f'data_csv/{num}.csv','wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


df = pd.read_csv('data_csv/0.csv')


print(df.info())
print(df.columns)
df = pd.read_csv('data_csv/0.csv').drop(['short_type', 'type', 'title'], axis=1)
pd.DataFrame(df).to_csv('data_csv/0_1.csv')
param = df['adr'].unique()
for pr in param:
    print(pr)