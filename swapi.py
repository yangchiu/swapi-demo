from query import query_all, query
from enum import Enum


class ResourceType(Enum):
    FILM = 'films'
    VEHICLE = 'vehicles'


def get_all(resource, search=None):
    if resource is ResourceType.FILM:
        results = query_all(ResourceType.FILM.value, search)
    elif resource is ResourceType.VEHICLE:
        results = query_all(ResourceType.VEHICLE.value, search)
    return results


def get(resource, id):
    if resource is ResourceType.FILM:
        result = query(ResourceType.FILM.value, id)
    elif resource is ResourceType.VEHICLE:
        result = query(ResourceType.VEHICLE.value, id)
    return result
