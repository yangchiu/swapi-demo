from swapi import get_all, get, ResourceType

if __name__ == '__main__':

    '''
    print(f'\n[1] Number of Species Test:\n')

    films = get_all(ResourceType.FILM, 'Revenge of the Sith')
    for film in films:
       if film['title'] == 'Revenge of the Sith':
           target = film
           break

    print(f'{len(target["species"])} species in Revenge of the Sith')
    '''

    print(f'\n[1] Number of Species Test:\n')

    film = get(ResourceType.FILM, 6)
    print(f'{len(film["species"])} species in Revenge of the Sith')

    print(f'\n[2] Films Episode Id Test:\n')

    films = get_all(ResourceType.FILM)
    films.sort(key=lambda elem: elem['episode_id'])
    for film in films:
        print(f'{film["title"]:28s} - episode id = {film["episode_id"]}')

    print(f'\n[3] Vehicles Max Atomosphering Speed Test:\n')

    vehicles = get_all(ResourceType.VEHICLE)
    for vehicle in vehicles:
        try:
            vehicle['max_atmosphering_speed'] = int(vehicle['max_atmosphering_speed'])
        except:
            vehicle['max_atmosphering_speed'] = -1

    vehicles.sort(key=lambda elem: elem['max_atmosphering_speed'])
    for vehicle in vehicles:
        if vehicle['max_atmosphering_speed'] > 1000:
            print(f'{vehicle["name"]:28s} - max atmosphereing speed = {vehicle["max_atmosphering_speed"]}')
