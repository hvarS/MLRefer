# -*- coding: utf-8 -*-
"""easykaggleapi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jdVEAFjBwfaqigJS79Cu102ilbyWImxh

###API Setup
"""

from google.colab import drive
drive.mount('/content/gdrive')

import os

# Commented out IPython magic to ensure Python compatibility.
def setup(api):
  import shutil
  ss = api.split()
  folder = ss[-1]
  os.environ['KAGGLE_CONFIG_DIR'] = "/content/gdrive/My Drive/Kaggle/"+folder
  print(folder)
#   %cd /content/gdrive/My Drive/Kaggle/
  !mkdir $folder
  shutil.copy2("kaggle.json","./"+folder+"/kaggle.json")
#   %cd $folder
  !kaggle competitions download -c $folder

setup("kaggle competitions download -c house-prices-advanced-regression-techniques")
!pwd

"""____________________________________________________________________________________"""