from google.cloud import bigquery
from google.cloud import storage

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Key/de-trainig-bq-key.json"

client = bigquery.Client()
dataset_ref = client.dataset('ncaa_basketball', project='bigquery-public-data')


def main(): 
    #read_from_bqtable
    ncaa_dataset = client.get_dataset(dataset_ref)
    
    for x in client.list_tables(ncaa_dataset):
        write_data_to_gcp(x.table_id)
        write_gcp_to_bigqeury(x.table_id)
    
def write_data_to_gcp(table_name):
    query = 'SELECT * FROM `bigquery-public-data.ncaa_basketball.' + table_name + '`'
    print(query)
    client = bigquery.Client()    
    storage_client = storage.Client()
    
    bucket_name = 'gosha-de-project'
    blob_name = table_name + '.parquet'
    destination_uri = f'gs://{bucket_name}/{blob_name}'
    
    query_job = client.query(query)
    destination_blob = storage_client.bucket(bucket_name).blob(blob_name)
    destination_blob.content_type = 'parquet'
    query_job.result().to_dataframe().to_parquet(destination_blob.open('wb'), index=False) 


def write_gcp_to_bigqeury(table_name):


    clientw = bigquery.Client()

    table_id = f'de-trainig.de_project.{table_name}'

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    uri = f'gs://gosha-de-project/{table_name}.parquet'
    
    load_job = clientw.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = clientw.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))


#read_from_bqtable()

#gcp_to_bigqeury()
if __name__ == '__main__':
    main() 
