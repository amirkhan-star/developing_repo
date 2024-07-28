from minio import Minio
from minio.error import S3Error
import os
import boto3
import pandas as pd
import xml.etree.ElementTree as ET

MINIO_USER_NAME = 'AMIRKHAN'
MINIO_PASSWORD = 'amirkhan13'
BUCKET_NAME = 'newbucket'

local_dir = '/home/ubuntu/Desktop/dirforminIO'

minIO_client = boto3.client(
    's3',
    endpoint_url='http://192.168.0.114:9000',
    aws_access_key_id=MINIO_USER_NAME,
    aws_secret_access_key=MINIO_PASSWORD
)

def xml_to_excel(xml_path, excel_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = []

    for item in root.findall('.//item'):
        row = {child.tag: child.text for child in item}
        data.append(row)
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)

def convert_all_xml_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            xml_path = os.path.join(directory_path, filename)
            excel_path = os.path.join(directory_path, filename.replace('.xml', '.xlsx'))
            xml_to_excel(xml_path, excel_path)
            os.remove(xml_path)

def process_files_from_minio(bucket_name, local_dir):
    objects = minio_client.list_objects(bucket_name, recursive=True)
    for obj in objects:
        if obj.object_name.endswith('.xml'):
            # Dosyayı indir
            local_file_path = os.path.join(local_dir, obj.object_name)
            minio_client.fget_object(bucket_name, obj.object_name, local_file_path)
    
    convert_all_xml_in_directory(local_dir)
    
    for filename in os.listdir(local_dir):
        if filename.endswith('.xlsx'):
            local_file_path = os.path.join(local_dir, filename)
            minio_client.fput_object(bucket_name, filename, local_file_path)
            os.remove(local_file_path)

os.makedirs(local_dir, exist_ok=True)

process_files_from_minio(BUCKET_NAME, local_dir)