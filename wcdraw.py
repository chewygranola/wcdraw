import random, copy

def round_generator(groups, team_selection, round):
  group_new_round = copy.deepcopy(groups)
  team_subset = dict((k, team_selection[k]) for k in range(round*8-7,round*8+1) if k in team_selection)
  for letter in range(0,8):
    flat_list = [sublist[1] for sublist in group_new_round[chr(65+letter)]]
    keys_remaining = list(filter(lambda x: x <= round*8, team_subset.keys()))
    #groups['GROUP-'+chr(65+letter)] = [[letter+1, x.pop(letter+1, None)]]
    while True:
      rand_choice = random.choice(keys_remaining)
      if team_subset[rand_choice] not in flat_list:
        group_new_round[chr(65+letter)] += [[rand_choice, team_subset.pop(rand_choice, None)]]
        break
      if set(team_subset.values()).issubset(flat_list):
        print("Fail")
        return False
  for letter in range(0,8):
    groups[chr(65+letter)] = group_new_round[chr(65+letter)]
  return True

def main():
  snake = False
  players = input("Enter # of players: ")
  print("players = "+str(players))
  print("snake draft? = "+str(snake))
  x = {}
  for rank in range(0,32):
    #even = forward, odd = backward
    if rank+1 > 32/players*players:
      x[rank+1] = 'Z'
    else:
	  if snake:
		  snake_rank = chr(rank%players+65) if rank/players%2 == 0 else chr(players-rank%players+65-1)
		  x[rank+1] = snake_rank
	  else:
		  x[rank+1] = chr(rank%players+65)
		
  groups = {}
  #form groups
  for letter in range(0,8):
    groups[chr(65+letter)] = [[letter+1, x.pop(letter+1, None)]]

  for round in [2,3,4]:
    while not round_generator(groups, x, round):
      continue

  for letter in range(0,8):
    print(','.join([str(team[0]) for team in groups[chr(65+letter)]]))

if __name__ == "__main__":
  main()
