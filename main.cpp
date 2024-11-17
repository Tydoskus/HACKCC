R = 3963.1; 
# in miles
PI = 3.14159265358979;

def calculate_distance( lat1,  lon1,  lat2, lon2):
    lat1 = math.radians(lat1);
    lon1 = math.radians(lon1);
    lat2 = math.radians(lat2);
    lon2 = math.radians(lon2);
    
     dlat = lat2 - lat1;
     dlon = lon2 - lon1;
    
     a = math.sin(dlat / 2) * math.sin(dlat / 2) +
               math.cos(lat1) * math.cos(lat2) * 
               math.sin(dlon / 2) * math.sin(dlon / 2);
     c = 2 * math.atan2(sqrt(a), math.sqrt(1 - a));
    
    distance = R * c;
    
    return distance;
};


int main() {
    #cout << "testing" << endl;
     amb_lat = 0;
     amb_lon = 0;

    # num of cars on the route = ???
    # while ??? > 0
    
     veh_lat =0; 
     veh_lon = 0;
     distance = calculate_distance(amb_lat, amb_lon, veh_lat, veh_lon);
     
    print ("distance: " , distance , end="\n")

    if distance <= 1:
        print () "Alert!!! Ambulance is on the way. Pull to the right." )
    
}

