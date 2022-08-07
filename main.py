# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorer_0 = player_0 + ' ' + str(goal_0)
scorer_1 = player_1 + ' ' + str(goal_1)

scorers = scorer_0 + ', ' + scorer_1
print(scorers)

report = f'{player_0} scored in the {goal_0}nd minute\n' + f'{player_1} scored in the {goal_1}th minute'
print(report)        

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
