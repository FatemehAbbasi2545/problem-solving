def main():
    players = []
    games = [
        { 'key': 'PUBG' },
        { 'key': 'Minecraft' },
        { 'key': 'Apex Legends' }
    ]
    for i in range(3):
        name = input("Enter the player's name:")
        dict = { 'name': name }

        for game in games:
            try:
                score = int(input(f'Score of {game['key']}: '))
            except ValueError:
                print('Enter an integer number.')
                score = int(input('Integer number: '))
            finally:
                dict[f'{game['key']}'] = score
                if 'winner' not in game.keys() and 'score' not in game.keys():
                    game['winner'] = name
                    game['score'] = score
                else:
                    if score > game['score']:
                        game['winner'] = name
                        game['score'] = score

        players.append(dict)        

    for game in games:
        print(f'Winner of {game['key']} is: {game['winner']}, {game['score']}')
    
if __name__ == "__main__":
    main()