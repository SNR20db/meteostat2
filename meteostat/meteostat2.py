# Copyright (c) 2021

#  Permission is hereby granted, free of charge, to any person
#  obtaining a copy of this software and associated documentation
#  files (the "Software"), to deal in the Software without
#  restriction, including without limitation the rights to use,
#  copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following
#  conditions:

#  The above copyright notice and this permission notice shall be
#  included in all copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#  OTHER DEALINGS IN THE SOFTWARE.

"""Meteostat API client for Python"""

__all__ = ['get_stations_full', 'get_stations_lite', 'get_hourly_full_station'
, 'get_hourly_obs_station', 'get_daily_full_station', 'get_daily_obs_station'
,'get_monthly_full_station', 'get_monthly_obs_station', 'get_normals_station']

import os
import csv
import json
import gzip

import requests
from requests.exceptions import HTTPError
from requests.models import Response

ENDPOINT = '//bulk.meteostat.net/v2/'
HOURLY_CSV_DATA_HEADER = ('date', 'hour', 'temp', 'dwpt', 'rhum', 'prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun', 'coco')
DAILY_CSV_DATA_HEADER = ('date', 'tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun')
MONTHLY_CSV_DATA_HEADER = ('year', 'month', 'tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun')
NORMALS_CSV_DATA_HEADER = ('star', 'end', 'month', 'tmin', 'tmax', 'prcp', 'wspd', 'pres', 'tsun')

class OptionsManager(object):
    """Class for option managment"""

    def __init__(self) -> None:

        self.api_version='0'
        self.use_https=True

        proxies={
            'http': os.environ.get('http_proxy', None),
            'https': os.environ.get('https_proxy', None)
        }

        self.requests={'proxies': proxies}

    def __str__(self) -> str:
        return "Endpoint: {}, Use https: {}".format(
            ENDPOINT, self.use_https
        )

    def __repr__(self) -> str:
        return self.__str__()

#    def __getattribute__(self, name: str) -> Any:
#        return super().__getattribute__(name)
    
#    def __setattr__(self, name: str, value: Any) -> None:
#        return super().__setattr__(name, value)

options=OptionsManager()

def _get_endpoint_url() -> str:
    """Create the endpoint url."""

    components = {"http": "https:" if options.use_https else "http:",
        "endpoint": ENDPOINT
    }

    return "{http}{endpoint}".format(**components)

def _get_data_from_endpoint(url:str = None, **kwargs) -> str:
    """Gets data from the stablished endpoint."""
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print('Invalid request. Code: {}, reason: {}, text: {}'.format
        (response.status_code, response.reason, response.text)
        )

        pass
    else:
        return gzip.decompress(response.content)

def _get_json_from_csv(data:str = None, fieldnames:tuple = None, **kwargs) -> json:
    """Parses data from csv to json dict."""
    
    result = csv.DictReader(data.decode('utf-8'), fieldnames=fieldnames, restkey='Excess', restval=None)

    for row in result:
        print(row)

    return result

def get_stations_full(**kwargs) -> json:
    """retrieves station full information."""
    endpoint = _get_endpoint_url()

    components={
        "action": "stations/full.json.gz"
    }

    url = "{}{action}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return json.loads(response)

def get_stations_lite(**kwargs) -> json:
    """retrieves station lite information. See: 
    
    https://dev.meteostat.net/bulk/stations.html#endpoints
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "stations/lite.json.gz"
    }

    url = "{}{action}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return json.loads(response)    

def get_hourly_full_station(station:str = '47423', format:str = 'csv', **kwargs) -> str:
    """retrieves station hourly full information. 
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "hourly/full/",
        "station": station,
        "extension": ".csv.gz"
    }

    url = "{}{action}{station}{extension}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    if format == 'json':
        result = _get_json_from_csv(data=response, fieldnames=HOURLY_CSV_DATA_HEADER)

        return result
    else:
        return response

def get_hourly_obs_station(station:str = '47423',**kwargs) -> str:
    """retrieves station hourly observation information. 
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "hourly/obs/",
        "station": station,
        "extension": ".csv.gz"
    }

    url = "{}{action}{station}{extension}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return response

def get_daily_full_station(station:str = '47423',**kwargs) -> str:
    """retrieves station daily full information. 
    See: 
    
    https://dev.meteostat.net/bulk/daily.html
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "daily/full/",
        "station": station,
        "extension": ".csv.gz"
    }

    url = "{}{action}{station}{extension}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return response

def get_daily_obs_station(station:str = '47423',**kwargs) -> str:
    """retrieves station daily observation information. 
    See: 
    
    https://dev.meteostat.net/bulk/daily.html
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "daily/obs/",
        "station": station,
        "extension": ".csv.gz"
    }

    url = "{}{action}{station}{extension}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return response

def get_monthly_full_station(station:str = '47423',**kwargs) -> str:
    """retrieves station monthly full information. 
    See: 
    
    https://dev.meteostat.net/bulk/monthly.html#endpoints
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "monthly/full/",
        "station": station,
        "extension": ".csv.gz"
    }

    url = "{}{action}{station}{extension}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return response

def get_monthly_obs_station(station:str = '47423',**kwargs) -> str:
    """retrieves station monthly obs information. 
    See: 
    
    https://dev.meteostat.net/bulk/monthly.html#endpoints
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "monthly/obs/",
        "station": station,
        "extension": ".csv.gz"
    }

    url = "{}{action}{station}{extension}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return response

def get_normals_station(station:str = '47423', format:str = 'csv', **kwargs) -> str:
    """retrieves station normals information. 
    See: 
    
    https://dev.meteostat.net/bulk/normals.html#endpoint
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "monthly/obs/",
        "station": station,
        "extension": ".csv.gz"
    }

    url = "{}{action}{station}{extension}".format(endpoint, **components)

    response = _get_data_from_endpoint(url = url)

    return response

def get_hourly_full_all_stations(format:str = 'csv',**kwargs) -> str:
    """retrieves station hourly full information for all stations
    listed in get_stations_full().
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    stations = []
    data = []

    response = get_stations_full()

    for line in response:
        stations.append(line['id'])

    for id in stations:
        query = get_hourly_full_station(station = id, format = format)

        data.append(query)
    
    return data

def get_hourly_obs_all_stations(format:str = 'csv',**kwargs) -> str:
    """retrieves station hourly observation information for all stations
    listed in get_stations_full().
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    stations = []
    data = []

    response = get_stations_full()

    for line in response:
        stations.append(line['id'])

    for id in stations:
        query = get_hourly_obs_station(station = id, format = format)

        data.append(query)
    
    return data

def get_daily_full_all_stations(format:str = 'csv',**kwargs) -> str:
    """retrieves station daily full information for all stations
    listed in get_stations_full().
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    stations = []
    data = []

    response = get_stations_full()

    for line in response:
        stations.append(line['id'])

    for id in stations:
        query = get_daily_full_station(station = id, format = format)

        data.append(query)
    
    return data

def get_daily_obs_all_stations(format:str = 'csv',**kwargs) -> str:
    """retrieves station daily obs information for all stations
    listed in get_stations_full().
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    stations = []
    data = []

    response = get_stations_full()

    for line in response:
        stations.append(line['id'])

    for id in stations:
        query = get_daily_obs_station(station = id, format = format)

        data.append(query)
    
    return data   

def get_monthly_full_all_stations(format:str = 'csv',**kwargs) -> str:
    """retrieves station monthly full information for all stations
    listed in get_stations_full().
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    stations = []
    data = []

    response = get_stations_full()

    for line in response:
        stations.append(line['id'])

    for id in stations:
        query = get_monthly_full_station(station = id, format = format)

        data.append(query)
    
    return data      

def get_monthly_obs_all_stations(format:str = 'csv',**kwargs) -> str:
    """retrieves station daily observation information for all stations
    listed in get_stations_full().
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    stations = []
    data = []

    response = get_stations_full()

    for line in response:
        stations.append(line['id'])

    for id in stations:
        query = get_monthly_obs_station(station = id, format = format)

        data.append(query)
    
    return data     

def get_normals_all_stations(format:str = 'csv',**kwargs) -> str:
    """retrieves station normals information for all stations
    listed in get_stations_full().
    See: 
    
    https://dev.meteostat.net/bulk/hourly.html#endpoints
    
    for details"""
    stations = []
    data = []

    response = get_stations_full()

    for line in response:
        stations.append(line['id'])

    for id in stations:
        query = get_normals_station(station = id, format = format)

        data.append(query)
    
    return data
    
