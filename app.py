import random

print("Welcome to Game Picker! \n")
print("This program will help you choose a game to play. \n")

games = ["Call of Duty", "Fortnite", "Minecraft", "Among Us", "Valorant", "League of Legends", "Apex Legends", "Overwatch", "Rocket League", "Rainbow Six Siege", "Genshin Impact", "Cyberpunk 2077", "The Witcher 3", "Red Dead Redemption 2", "Grand Theft Auto V", "Assassin's Creed Valhalla", "The Last of Us Part II", "Ghost of Tsushima", "Final Fantasy VII Remake", "Demon's Souls"]

random_game = random.choice(games)

print("You should play: " + random_game + "\n")

print("Enjoy your game! \n")
