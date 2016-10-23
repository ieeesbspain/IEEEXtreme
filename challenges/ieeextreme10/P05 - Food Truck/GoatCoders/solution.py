"""Solution to problem 5 of IEEEXtreme 10.0."""

from __future__ import print_function
from math import radians, cos, sin, asin, sqrt
from datetime import datetime


EARTH_RADIUS = 6378.137  # in km


def haversine(point1, point2):
    """Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance in km bewteen the two points.
    """
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * EARTH_RADIUS * asin(sqrt(d))
    return h  # in kilometers


def main():
    """Main application logic."""
    my_location = map(float, raw_input().split(','))
    distance = float(raw_input())
    raw_input()  # discard table header

    cell_data = {}
    inp = raw_input()
    while True:
        str_date, lat, lon, phone = inp.split(',')
        date = datetime.strptime(str_date, '%m/%d/%Y %H:%M')
        if phone not in cell_data:
            cell_data[phone] = {'date': date, 'loc': (float(lat), float(lon))}
        else:
            if date > cell_data[phone]['date']:
                cell_data[phone] = {'date': date, 'loc': (float(lat), float(lon))}
        try:
            inp = raw_input()
        except EOFError:
            break
    # print(cell_data)

    out_list = []

    for phone in cell_data:
        if haversine(my_location, cell_data[phone]['loc']) < distance:
            out_list.append(phone)
    out_list.sort()
    if len(out_list) > 0:
        print(out_list[0], end='')
        for p in out_list[1:]:
            print(',', end='')
            print(p, end='')
    else:
        print()


if __name__ == "__main__":
    main()
