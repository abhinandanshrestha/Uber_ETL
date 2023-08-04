import pandas as pd

def extract(url):
    # url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet'
    # output_file = 'yellow_tripdata_2023-01.parquet'

    # response = requests.get(url)
    # if response.status_code == 200:
    #     with open(output_file, 'wb') as f:
    #         f.write(response.content)
    #     print('File downloaded successfully.')
    # else:
    #     print(f'Failed to download the file. Status code: {response.status_code}')

    df=pd.read_csv(url,sep=',')
    print("Extraction of data completed....")
    return df