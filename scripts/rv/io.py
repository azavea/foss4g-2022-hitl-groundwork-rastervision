import json
import geopandas as gpd


def get_img_info(uri: str) -> dict:
    with open(uri, 'r') as f:
        img_info = json.load(f)['results'][0]
    return img_info


def get_task_grid(uri: str) -> gpd.GeoDataFrame:
    # TODO
    pass
