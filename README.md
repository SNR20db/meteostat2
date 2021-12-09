# meteostat2
meteostat2 is an alternative API for python. No manipulation of data occurs, simple and intuitive. Feast yourself on data already prepared to be immideately consumed.

# Set up.
Using Pypi.

```
pip install meteostat2
```

# Get data.
Import the package

```
import meteostat2
```

Choose between csv (comma separated) or json,

A list of stations id along with its metadata can be found, as follows,

```
response = {}

response = meteostat2.get_stations_full()
```

or use the lite version with ```get_stations_lite()```.

Download data per station (hourly, daily, monthly, normals)

```
response = ""

response = get_hourly_full_station( 
    station = '47423', format = 'csv' )

```

or get a json using,

```
response = {}

response = get_hourly_full_station( 
    station = '47423', format = 'json' )

``` 

istead. Specify the data you want to get with using ```get_hourly_obs_station, get_daily_full_station, get_daily_obs_station, get_monthly_full_station,  get_daily_obs_station, get_monthly_full_station, get_monthly_obs_station, get_normals_station``` in either case (down below).

Use geolocation to localize stations. Hoewever you'll need to register (also down below).

```
response = {}

response = get_nearby_stations( 
    x_rapidapi_key = '{key}', lat = {float}, lon = {float}, limit = {int/units}, radius = {int/meters}
)
```

Download all available data,

```
response = ""

response = get_hourly_full_all_stations(
    format = 'csv'
)
```

Similarly,

```
response = {}

response = get_hourly_full_all_stations(
    format = 'json'
)
```

Discover the rest by yourself.

# Client.
Use the client with exactly the same functionalities presented above.

# More information
See:

    https://dev.meteostat.net/bulk/

    With 500 free - requests per month[^*].

    [^*]: Will apply only for **geo-location**.  

    https://rapidapi.com/meteostat/api/meteostat/pricing

for more information.

# Additional notes

You can parse a csv file format to json but can't perform the inverse process. If that was of interes, let me know.

Why did I build up so many methods instead of using a parameter? I tried to satisfy the user, taking for granted that he is not going to read the documentation and is not going likewise pay attention to the naming of methods. However I am willing to agglomarate those methods into just one parameter if I've got some feedback.