#include <iostream>
#include <cmath>
#include <random>
using namespace std;

const double R = 3963.1; // in miles

double toRadians(double degree) {
    return degree * (M_PI / 180.0); //convert to rad by times with pi/180
}

double calculate_distance(double lat1, double lon1, double lat2, double lon2)
{
    lat1 = toRadians(lat1);
    lon1 = toRadians(lon1);
    lat2 = toRadians(lat2);
    lon2 = toRadians(lon2);
    
    double dlat = lat2 - lat1;
    double dlon = lon2 - lon1;
    
    double a = sin(dlat / 2) * sin(dlat / 2) +
               cos(lat1) * cos(lat2) * 
               sin(dlon / 2) * sin(dlon / 2);
    double c = 2 * atan2(sqrt(a), sqrt(1 - a));
    
    double distance = R * c;
    
    return distance;
};

void sendAlert(double newDistance)
{
    cout << newDistance;
};

int main() {
    cout << "testing" << endl;
    double amb_lat = rand() % 181 -90;

    double amb_lon = rand() % 361 -180;

    // need to find car on the route of the ambulance

    double veh_lat = rand() % 181 -90; // this car should be found to be on the route of the ambulance

    double veh_lon = rand() % 361 -180;// this car should be found to be on the route of the ambulance

    double distance = calculate_distance(amb_lat, amb_lon, veh_lat, veh_lon);
     
    cout << "distance: " << distance << endl;

    if (distance <= 1)
    {
        //sendAlert(distance);
        cout << "Alert!!! Ambulance is on the way. Pull to the right." << endl;
    }

    return 0;
}

