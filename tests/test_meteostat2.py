
import pandas as pd
from io import StringIO as io

import meteostat

def test_get_stations_full():
    try:
        data = meteostat.get_stations_full()

        df = pd.DataFrame(data)
    
    except:
        assert False

    else:
        assert True

def test_get_lite_station():
    try:
        data = meteostat.get_stations_lite()

        df = pd.DataFrame(data)
    
    except:
        assert False

    else:
        assert True

def test_get_hourly_full_station():
    try:
        data = meteostat.get_hourly_full_station( format = 'csv' )

        df = pd.read_csv( io( data ), sep = ',' )

        data = meteostat.get_hourly_full_station( format = 'json' )

        df = pd.DataFrame(data)

    except:
        assert False
    
    else:
        assert True

def test_get_hourly_obs_station():
    try:
        data = meteostat.get_hourly_obs_station ( format = 'csv' )

        df = pd.read_csv( io( data ), sep = ',' )

        data = meteostat.get_hourly_obs_station( format = 'json' )

        df = pd.DataFrame(data)

    except:
        assert False
    
    else:
        assert True

def test_get_daily_full_stations():
    try:
        data = meteostat.get_daily_obs_station ( format = 'csv' )

        df = pd.read_csv( io( data ), sep = ',' )

        data = meteostat.get_daily_full_station( format = 'json' )

        df = pd.DataFrame(data)
    
    except:
        assert False

    else:
        assert True

def test_get_daily_obs_station():
    try:
        data = meteostat.get_daily_obs_station ( format = 'csv' )

        df = pd.read_csv( io( data ), sep = ',' )

        data = meteostat.get_daily_obs_station( format = 'json' )

        df = pd.DataFrame(data)

    except:
        assert False
    
    else:
        assert True

def test_get_monthly_full_stations():
    try:
        data = meteostat.get_monthly_obs_station ( format = 'csv' )

        df = pd.read_csv( io( data ), sep = ',' )

        data = meteostat.get_monthly_full_station( format = 'json' )

        df = pd.DataFrame(data)
    
    except:
        assert False

    else:
        assert True

def test_get_monthly_obs_station():
    try:
        data = meteostat.get_monthly_obs_station ( format = 'csv' )

        df = pd.read_csv( io( data ), sep = ',' )

        data = meteostat.get_monthly_obs_station( format = 'json' )

        df = pd.DataFrame(data)

    except:
        assert False
    
    else:
        assert True

def test_get_normals_station():
    try:
        data = meteostat.get_normals_station ( format = 'csv' )

        df = pd.read_csv( io( data ), sep = ',' )

        data = meteostat.get_normals_station ( format = 'json' )

        df = pd.DataFrame(data)

    except:
        assert False
    
    else:
        assert True

def test_get_nearby_stations():
    try:
        data = meteostat.get_nearby_stations ( 
            x_rapidapi_key='d351b58670mshcce819d6a8a3034p1c54bdjsn88f7a12fa377',
            lat=51.5085,
            lon=-0.1257
        )

    except:
        assert False

    else:
        assert True
