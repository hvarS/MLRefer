from google.colab import drive
drive.mount('/content/gdrive')


def setup_dataset(text):
  import shutil
  import os
  %cd /content/gdrive/My Drive/Kaggle/
  strings = text.split(' ')[-1]
  folder = strings.split('/')[1]
  os.environ['KAGGLE_CONFIG_DIR'] = "/content/gdrive/My Drive/Kaggle/"+folder
  print(strings)
  print(folder)
  !mkdir $folder
  shutil.copy2("kaggle.json","./"+folder+"/kaggle.json")
  %cd $folder
  !kaggle datasets download -d $strings
  
setup_dataset("kaggle datasets download -d luizfmatos/reddit-english-depression-related-submissions")
