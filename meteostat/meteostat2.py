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
import gzip
import json

import requests

ENDPOINT = '//bulk.meteostat.net/v2/'

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

def get_stations_full(**kwargs) -> json:
    """retrieves station full information."""
    endpoint = _get_endpoint_url()

    components={
        "action": "stations/full.json.gz"
    }

    url = "{}{action}".format(endpoint, **components)

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return json.loads(res)

def get_stations_lite(**kwargs) -> json:
    """retrieves station lite information. See: 
    
    https://dev.meteostat.net/bulk/stations.html#endpoints
    
    for details"""
    endpoint = _get_endpoint_url()

    components={
        "action": "stations/lite.json.gz"
    }

    url = "{}{action}".format(endpoint, **components)

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return json.loads(res)    

def get_hourly_full_station(station:str = '47423',**kwargs) -> str:
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

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return res

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

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return res

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

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return res

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

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return res

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

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return res

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

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return res

def get_normals_station(station:str = '47423',**kwargs) -> str:
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

    response = requests.get(url)

    res = gzip.decompress(response.content)

    return res