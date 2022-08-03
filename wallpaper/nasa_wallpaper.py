# API key is tGN9bVvv9x0nIfTKBH8Re1bWIcVe337dyzzrbdS6

import requests
import platform
import pwd
import os
from datetime import date

url = "https://api.nasa.gov/planetary/apod?api_key=tGN9bVvv9x0nIfTKBH8Re1bWIcVe337dyzzrbdS6"
FILENAME = f"nasa_pic{date.today()}.png"


def get_filename():
    username = pwd.getpwuid(os.getuid()).pw_name
    directory = "/home/" + username + "/Pictures/Wallpapers/"
    

    return os.path.join(directory, FILENAME)


def download_pic_of_day():
    r = requests.get(url)

    if r.status_code != 200:
        print('error')
        return

    picture_url = r.json()['url']
    if "jpg" not in picture_url:
        print("No image for today, must be a video")
    else:
        pic = requests.get(picture_url , allow_redirects=True)
        filename = get_filename()

        open(filename, 'wb').write(pic.content)

        print(f"saved picture of the day to {filename}!")


if __name__ == '__main__':
    download_pic_of_day()

    filename = get_filename()

    # set background
    cmd = "gsettings set org.gnome.desktop.background picture-uri file:" + filename

    os.system(cmd)
