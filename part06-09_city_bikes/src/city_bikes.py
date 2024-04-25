# Write your solution here
import math

def get_station_data(filename: str):
    with open(filename) as station_file:
        location_dict = {}
        for line in station_file:
            station = line.strip().split(";")
            if station[0] == "Longitude":
                continue
           
            location_dict[station[3]] = (float(station[0]), float(station[1]))
        
        return location_dict

def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    greatest_dist = 0
    farthest_stations = ()
    for location1 in stations:
        for location2 in stations:
            d = distance(stations, location1, location2)
            if d == greatest_dist:
                continue
            elif d > greatest_dist:
                greatest_dist = d
                farthest_stations = (location1, location2, d)
    
    return farthest_stations
            
    


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    print(greatest_distance(stations))