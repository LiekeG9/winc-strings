# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when, according to the format:
# <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorer_0 = player_0 + ' ' + str(goal_0)
scorer_1 = player_1 + ' ' + str(goal_1)

# The result should be stored in a variable scorers
scorers = scorer_0 + ', ' + scorer_1
print(scorers)

# Use f-strings or the +-operator to create a single string with information about who scored when in the format:
# <scorer_name> scored in the <when_they_scored>nd minute
report = f'{player_0} scored in the {goal_0}nd minute\n' + f'{player_1} scored in the {goal_1}th minute'
print(report)        
# The result should be stored in a variable report.

# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute

# 1 Choose a player that played in the soccer match and store his name as a string in the variable player.
# 2 first_name: use slicing and the find-method (help) to isolate and store the player's first name.
# 3 last_name_len: use find, slicing and len to isolate and store the length of their last name.
# 4 name_short: isolate and store the player's name in this format:
# G. von Examplestein

player = 'Hans van Breukelen'

x = player.find(' ')
first_name = player[:x]
last_name = player[x+1:]
last_name_len = len(last_name)
name_short = first_name[:1] + '. ' + last_name
chant = (first_name + '! ') * len(first_name)
chant = chant[:-1]
good_chant = chant[:-1] != ' '

print(first_name)      
print(last_name)   
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)




