#please enter your MinİO credentials
MINIO_user_name = 'AMIRKHAN'#Enter minIO username
MINIO_password = 'amirkhan13'#Enter minIO password
bucket_names = 'newbucket'#Enter your bucket which you want to archive files
#use this local directory for using minio server execution
local_dir = '/home/ubuntu/Desktop/dirforminIO'
##ENTER YOUR CODE TO BELOW---------------------------------------------------------
import os
import pandas as pd 
import xml.etree.ElementTree as ET

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
convert_all_xml_in_directory(local_dir)