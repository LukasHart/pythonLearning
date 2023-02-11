class Player:
    all_players = []
    def __init__(self, players):
        self.name = players['name']
        self.age = players['age']
        self.position = players['position']
        self.team = players['team']
        Player.all_players.append(self)

    def display_player_info(self):
        print('-------------------------------------')
        print(f'Players Name: {self.name}\nPlayers age: {self.age}\nPlayers position: {self.position}\nPlayers Team: {self.team}')
        return self
    
    @classmethod
    def show_all_players(cls):
        for player in cls.all_players:
            print(f'Players profile - {player.name}, {player.age}, {player.position}, {player.team}') 


players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
]



player_kevin = Player(players[0])
player_jason = Player(players[1])
player_kyrie = Player(players[2])
player_damian = Player(players[3])
player_joel = Player(players[4])

# player_kevin.display_player_info()
Player.show_all_players()
