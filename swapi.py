from query import query_all
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
