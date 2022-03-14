import shutil, os
import time
from datetime import datetime
import subprocess

steam_path = r''
save_folder = r''
game_id = 1245620

if __name__ == '__main__':
    #copy Elden Ring folder to save_folder and rename the folder with current date and time
    
    #create save folder if it doesn't exist
    os.makedirs(save_folder, exist_ok = False)
    
    #format folder name
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H.%M")
    dest = os.path.join(save_folder, 'EldenRing ' + dt_string)
    #eg EldenRing 2022-03-14 12.28

    #copy Elden Ring Steam save folder to destination folder
    shutil.copytree(steam_path, dest, dirs_exist_ok=False)
    
    #run game  
    cmd = r"C:\Program Files (x86)\Steam\Steam.exe -applaunch " + str(game_id)
    subprocess.call(cmd)