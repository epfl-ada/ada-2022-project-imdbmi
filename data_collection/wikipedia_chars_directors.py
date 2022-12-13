import requests
from pathlib import Path
import json
from multiprocessing import Pool
import time
from tqdm import tqdm
import pandas as pd
import numpy as np





WIKIDATA_DIR = '../wikidata/'
DST_DIR = '../wikidata_chars/'
CAST_PROPERTY_ID =  'P161'
DIRECTOR_PROPERTY_ID = 'P57'
PRODUCER_PROPERTY_ID = 'P162'
BOX_OFFICE_ID = 'P2142'
USER_AGENT = 'akgokce'
WIKIDATA_URI = 'https://www.wikidata.org/entity/'

wikidata_path = Path(WIKIDATA_DIR)
wikidata_chars_folder = Path(DST_DIR)



def get_wikidata(wikidata_uri: str) -> dict:
    r = requests.get(wikidata_uri, headers={'User-Agent': USER_AGENT, 'Accept':'JSON'})
    try:
        return r.json()
    except:
        time.sleep(60)
        try:
            r = requests.get(wikidata_uri, headers={'User-Agent': USER_AGENT, 'Accept':'JSON'})
            return r.json()
        except:
            print('JSONDecodeError')
    
def get_director_data(wikidata: dict, wikidata_id: str, dst_path: Path) -> str:
    '''
    Get the director of a movie from its Wikidata.
    '''
    try:
        # Get the director Wikidata ID
        claims = wikidata.get('entities').get(wikidata_id).get('claims')
        director_id = claims.get(DIRECTOR_PROPERTY_ID)[0].get('mainsnak').get('datavalue').get('value').get('id')
        
        dst_path = dst_path.joinpath(director_id+'.json')
        if not dst_path.exists():
            # Send a request to get directors's Wikidata
            wikidata_uri = WIKIDATA_URI + director_id + '.json'
            director_data =  get_wikidata(wikidata_uri)

            # Save the Wikidata to a file
            with open(dst_path, 'w') as file:
                json.dump(director_data, file, indent=2)
                
        return director_id
    except:
        return None


def get_producer_data(wikidata: dict, wikidata_id: str, dst_path: Path) -> str:
    '''
    Get the producer of a movie from its Wikidata.
    '''
    try:
        # Get the director Wikidata ID
        claims = wikidata.get('entities').get(wikidata_id).get('claims')
        producer_id = claims.get(PRODUCER_PROPERTY_ID)[0].get('mainsnak').get('datavalue').get('value').get('id')
        
        dst_path = dst_path.joinpath(producer_id+'.json')
        if not dst_path.exists():
            # Send a request to get producers's Wikidata
            wikidata_uri = WIKIDATA_URI + producer_id + '.json'
            producer_data =  get_wikidata(wikidata_uri)

            # Save the Wikidata to a file
            with open(dst_path, 'w') as file:
                json.dump(producer_data, file, indent=2)
                
        return producer_id
    except:
        return None
    
def get_top5_characters(wikidata: dict, wikidata_id: str, dst_path: Path) -> str:
    '''
    Get the top 5 characters of a movie from its Wikidata.
    '''
    try:
        # Get cast Wikidata IDs
        claims = wikidata.get('entities').get(wikidata_id).get('claims')
        cast_list = claims.get(CAST_PROPERTY_ID)
    
        cast_id_list = []
        for i in range(min(5, len(cast_list))):
            # For each cast member, send a request to get their Wikidata
            cast_id = cast_list[i].get('mainsnak').get('datavalue').get('value').get('id')
            
            dst_path = dst_path.joinpath(cast_id+'.json')
            if not dst_path.exists():
                wikidata_uri = WIKIDATA_URI + cast_id + '.json'
                cast_data = get_wikidata(wikidata_uri)
                
                # Save the Wikidata to a file
                with open(dst_path, 'w') as file:
                    json.dump(cast_data, file, indent=2)
                
            cast_id_list.append(cast_id)
                
        return cast_id_list
    except:
        return None
    
def get_box_office_value(wikidata: dict, wikidata_id: str) -> float:
    '''
    Get the box office value of a movie from its Wikidata.
    '''
    try:
        # Get the box office value
        claims = wikidata.get('entities').get(wikidata_id).get('claims')
        revenue = claims.get(BOX_OFFICE_ID)[0].get('mainsnak').get('datavalue').get('value').get('amount')
        return float(revenue)
    except:
        return None


def get_data(movie_file: Path, dst_path: Path=wikidata_chars_folder):
    wikidata_id = movie_file.stem
    dst_path = dst_path.joinpath(wikidata_id)
    with open(movie_file, 'r') as file:
        movie_data = json.load(file)
        
    if not dst_path.exists():
        dst_path.mkdir()
    
        
    director_id = get_director_data(movie_data, wikidata_id, dst_path)
    producer_id = get_producer_data(movie_data, wikidata_id, dst_path)
    cast_data = get_top5_characters(movie_data, wikidata_id, dst_path)
    box_office_value = get_box_office_value(movie_data, wikidata_id)
    
    # Pad the cast data with None
    if cast_data is None:
        cast_data = [None] * 5
    else:
        cast_data += [None] * (5 - len(cast_data))
    
    data = {
        'movie_id': wikidata_id,
        'director_id': director_id,
        'producer_id': producer_id,
        'box_office_value': box_office_value,
        'cast_id_0': cast_data[0],
        'cast_id_1': cast_data[1],
        'cast_id_2': cast_data[2],
        'cast_id_3': cast_data[3],
        'cast_id_4': cast_data[4]
    }
    time.sleep(0.01)
    
    return data
            
if __name__ == '__main__':

    # Create the folder to store the Wikidata of the directors, producers and characters
    if not wikidata_chars_folder.exists():
        wikidata_chars_folder.mkdir()
    
    # Create a pool of 8 processes
    with Pool(processes=40) as pool:
        # Split the list of movies into 1000 chunks
        movie_list= list(wikidata_path.glob('*.json'))
        splits = np.array_split(movie_list, 1000)
        
        results = []
        # For each chunk, send a request to get the Wikidata of the director, producer and top 5 characters
        for split in tqdm(splits):
            res = pool.imap_unordered(get_data, split)
            results.extend(res)

    # Save the results to a CSV file
    df = pd.DataFrame.from_dict(results, orient='columns')
    df.set_index('movie_id', inplace=True, drop=True)
    df.to_csv(wikidata_chars_folder.joinpath('wikidata_chars.csv'), index=True, header=True)