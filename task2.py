#from pprint import pprint

import requests

from reddit import Reddit
from ya_disk import YandexDisk

TOKEN = ""



if __name__ == '__main__':
    yd = YandexDisk(token=TOKEN)
    #pprint(yd.get_files_list())
    yd.upload_file_to_disk("text1.txt", "test1.txt")