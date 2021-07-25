from constant import API_KEY, mkad_points
from shapely.geometry import Polygon, Point
from math import cos, sqrt
import requests
from lxml import etree


def get_coordinates(params: dict) -> tuple:
    """
    function that takes params and make GET request to YANDEX GEOCODER API
    return coordinates of address
    :param params
    :return: coordinates
    """
    headers = {}
    r = requests.get('https://geocode-maps.yandex.ru/1.x/', headers=headers,
                     params=params)
    root = etree.fromstring(bytes(r.text, encoding='utf-8'))
    longitude, latitude = tuple(root[0][1][0][4][0].text.split(' '))
    coordinates = (float(longitude), float(latitude))
    return coordinates


def make_params(address: str) -> dict:
    """
    function to make params to GET request to function get_coordinates
    :param address
    :return: params
    """
    address_to_str = address.replace(" ", "+")
    params = {
        'apikey': API_KEY,
        'geocode': address_to_str
    }
    return params


def min_distance(coordinates: tuple) -> float:
    """
    function takes longitude and latitude tuple
    min_dist from MKAD to point in km
    :param coordinates: tuple
    :return: min_dist
    """
    min_dist = 0
    for longitude, latitude in mkad_points:
        average_latitude = (latitude + coordinates[1]) / 2
        distance = sqrt(((longitude - coordinates[0]) ** 2) *
                        (111.32137777 ** 2) * cos(average_latitude) +
                        ((latitude - coordinates[1]) ** 2) *
                        (111.134861111 ** 2))
        if distance < min_dist or min_dist == 0:
            min_dist = distance
    return min_dist


def make_request(address: str) -> object:
    """
    function that takes address from POST request 
    return a JSON result 
    Function uses Point, Polygon from shapely.geometry to search point in MKAD
    :param address
    :return: message
    """
    try:
        coordinates = get_coordinates(make_params(address))
        mkad_polygon = Polygon(tuple(mkad_points))
        if mkad_polygon.contains(Point(coordinates)):
            message = {'message': 'Entered address is in MKAD-area'}
        else:
            min_dist = min_distance(coordinates)
            message = {
                'min_distance': float(round(min_dist, 5)),
                'message': "Success"
            }

    except Exception as e:
        message = {
            'message': str(e)
        }
    return message
