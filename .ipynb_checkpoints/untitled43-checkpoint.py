#please enter your credentials
MINIO_user_name = 'AMIRKHAN'
MINIO_password = 'amirkhan13'
bucket_names = 'newbucket'
#for using minio server execution
local_dir = '/home/ubuntu/Desktop/dirforminIO'

import os
import pandas as pd 
import xml.etree.ElementTree as ET

def xml_to_excel(xml_path, excel_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = []
    
    for item in root.findall('.//item'): 
        row = {child.tag: child.text for child in item} 
            excel_path = os.path.join(directory_path, filename.replace('.xml', '.xlsx'))
            xml_to_excel(xml_path, excel_path)
            os.remove(xml_path)
convert_all_xml_in_directory(local_dir)