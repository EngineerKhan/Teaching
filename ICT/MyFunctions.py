import math


def Sigmoid(x):
    return 1 / (1 + math.exp(-x))


def Tanh(x):
    return (math.exp(-x) + math.exp(-x)) / (math.exp(x) - math.exp(-x))  # Check if its - in the numerator or +


def Haversine(lat1: float, lon1: float, lat2: float, lon2: float):
    """
    This function takes first point's latitude and longitude, followed by the second point's latitude and longitude
    It returns the answer in a floating-point number, which we can round off as per our requirement.
    """
    R = 6371.0  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return R * c
