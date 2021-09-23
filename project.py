import requests

while True:

    pokemon = input("which pokemon do you want to choose?")
    pokemon = pokemon.lower()

    url =  f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    
    req = requests.get(url)
    
    if req.status_code == 200 :
        data = req.json()
        print(f"Name is\t\t{data['name']}")
        print("version:\n\n")
        for application in data['game_indices']:
            print(application['version']['name'])
        print("Abilities:\n\n")
        for ability in data['abilities']:
            print(ability['ability']['name'])
        print("Moves:\n\n")
        for move in data['moves']:
            print(move['move']['name'])
        print("Types:\n\n")
        for types in data['types']:
            print(types['type']['name'])

    else:
        print("Pokemon not found")



