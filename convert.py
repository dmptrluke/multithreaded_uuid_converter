""" a multithreaded UUID converter
"""


from multiprocessing import Pool

import sys
import os
import math
import urllib2
import json
import time
import shutil
import uuid
from nbt import nbt


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

# how many to convert at a time
CONVERT_COUNT = 20

# URL to the data API
API_URL = "https://api.mojang.com/profiles/minecraft"

pool = Pool(5)

def create_folders(path):
    player_data_path = os.path.join(path, 'players')
    target_data_path = os.path.join(path, 'playerdata')
    missing_data_path = os.path.join(path, 'players.missing')
    converted_data_path = os.path.join(path, 'players.converted')
    invalid_data_path = os.path.join(path, 'players.invalid')


def get_chunks(player_files):
    """ splits a list of files into manageable chunks of names
    """
    return chunks(player_files, CONVERT_COUNT)


def convert_uuid(player_data):
    pass
    # this does nothing


def process_chunk(chunk):
    """ converts a chunk of player.dat files and returns UUID
    """
    payload = []
    # this does nothing


def convert(source_path, target_path):
    # stores a player name and file path
    player_files = {}

    if not os.path.isdir(source_path):
        print 'Path is not directory or does not exist: {}'.format(source_path)
        return False

    # get a list of files in source_path
    file_list = os.listdir(source_path)

    # store the player name and file path for each player
    for player_file in file_list:
        if player_file.endswith('.dat'):
            file_name = os.path.basename(player_file)
            name = os.path.splitext(file_name)[0].lower()
            player_files[name] = os.path.join(source_path, file_name)

    if not player_files:
        sys.stderr.write('No player data found!\n')
        return False

    # splits data up into chunks of 30 to send to worker threads
    data_chunks = get_chunks(player_files)

    for chunk in data_chunks:
        # TODO: run this with multiprocessing
        process_chunk(chunk)

