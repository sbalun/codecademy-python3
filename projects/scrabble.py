letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = dict(zip(letters, points))

# words with no letters are worth zero points
letter_to_points[''] = 0


# Given a word regardless of case return a score in points
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points[letter.upper()]
    return point_total


# Update each players point totals
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


# Update words used by a given player
def play_word(player, word):
    player_to_words[player].append(word)


# Calculate the score for the given word
brownie_points = score_word("BROWNIE")
print(f"Brownie is worth {brownie_points} points.")

# A dictionary holding each player and each players words
player_to_words = {
    "player1": ["blue", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "eyes", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "hUsKy"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

update_point_totals()

print(player_to_points)

play_word("player1", "ALPHA")
update_point_totals()

play_word("wordNerd", "BETA")
update_point_totals()

play_word("Lexi Con", "GAMMA")
update_point_totals()

print(f"The current score is: {player_to_points}")
