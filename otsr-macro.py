# -*- coding: utf-8 -*-
"""
2020
@author: wuffalo

Manipulates files to stage for vba macro that prepares ots research
"""

import os
import shutil
import glob

path_to_Downloads = '/mnt/c/Users/WMINSKEY/Downloads/'
path_to_Source = '/mnt/c/Users/WMINSKEY/OneDrive - Schenker AG/Documents/OTS Research/Files/'

list_of_ASN = glob.glob(path_to_Downloads + 'Find ASN*.csv') # * means all if need specific format then *.csv
latest_file = max(list_of_ASN, key=os.path.getctime)
path_to_ASN = latest_file
name_ASN = os.path.basename(path_to_ASN)

list_of_OCS = glob.glob(path_to_Downloads + 'ordercurrentstatus*.csv') # * means all if need specific format then *.csv
latest_file = max(list_of_OCS, key=os.path.getctime)
path_to_OCS = latest_file
name_OCS = os.path.basename(path_to_OCS)

shutil.copy(path_to_ASN, path_to_Source+'Find ASN.csv')
shutil.copy(path_to_OCS, path_to_Source+'ordercurrentstatus.csv')


