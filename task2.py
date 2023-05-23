#from pprint import pprint

import requests

from reddit import Reddit
from ya_disk import YandexDisk

TOKEN = "y0_AgAAAAACrMhFAADLWwAAAADjV8UKlgi4Bap8SUKfTNgeQvsYooQKnzY"



if __name__ == '__main__':
    yd = YandexDisk(token=TOKEN)
    #pprint(yd.get_files_list())
    yd.upload_file_to_disk("text1.txt", "test1.txt")