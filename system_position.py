import random

def win(v, oLoc, options, level, winning_rows):
	condition = True
	for row in winning_rows:
		for element in row:
			position1 = element
			for position2 in row:
				if position1 != position2 and v[position1] == v[position2] == "o":
					row.remove(position1)
					row.remove(position2)

					if v[row[0]] not in options:
						oLoc = row[0]
						condition = False
						break
					else:
						pass
				else:
					continue

	if condition:
		for row in winning_rows:
			for element in row:
				position1 = element
				for position2 in row:
					if position1 != position2 and v[position1] == v[position2] == "x":
						row.remove(position1)
						row.remove(position2)

						if v[row[0]] not in options and level != "e":
							oLoc = row[0]
							condition = True
							break
						else:
							pass
					else:
						continue

	return oLoc

def system_logic_easy(v, options, xLoc, oLoc, i, locations):
	#logic for random move as the game is neutral
	oLoc = random.choice(locations)
	pass
	return oLoc

def system_logic_medium_first(v, options, xLoc, oLoc, i, locations):
	if i==1:
		oLoc = random.choice([5, 1, 3, 7, 9])

	if i==2:
		if v[5] == "o":
			while True:
				system_case_ = [1,3,7,9]
				oLoc = random.choice(system_case_)
				if v[oLoc]=="x":
					continue
				else:
					break

		else:
			while True:
				if v[1]=="o" or v[9]=="o":
					oLoc = random.choice([3,7])
					if v[oLoc]=="x":
						continue
					else:
						break

				if v[3]=="o" or v[7]=="o":
					oLoc = random.choice([1,9])
					if v[oLoc]=="x":
						continue
					else:
						break
		
	#logic for random move as the game is neutral
	if i!=1 and i!=2:
		oLoc = random.choice(locations)
		pass

	return oLoc

def system_logic_medium_second(v, options, xLoc, oLoc, i, locations):
	#logics for special moves leading towards tie
	if i==2:
		while True:
			system_case_ = [2,8,4,6]
			oLoc = random.choice(system_case_)
			if v[oLoc] not in options:
				break 
			else:
				continue
	
	#logic for random move as the game is neutral
	if i!=2:
		oLoc = random.choice(locations)
		pass

	return oLoc

def system_logic_hard_second(v, options, xLoc, oLoc, i, locations):
	#logics for special moves leading towards tie
	if i==1:
		if xLoc == 5:
			oLoc = random.choice([7,3])
		else: 
			oLoc = 5

	if i==2:
		while True:
			if v[7] == "o" or v[3] == "o" :
				_system_case_ = [1,9]
				oLoc = random.choice(_system_case_)
				break

			else:
				system_case_ = [2,8,4,6]
				oLoc = random.choice(system_case_)
				if v[oLoc] not in options:
					break 
				else:
					continue
		
	#logic for random move as the game is neutral
	if i!=1 and i!=2:
		oLoc = random.choice(locations)
		pass
	
	return oLoc

def system_logic_hard_first(v, options, xLoc, oLoc, i, locations):
	#logics for special moves leading towards tie
	if i==1:
		oLoc = random.choice([5, 1, 3, 7, 9])

	if i==2:
		if v[5] == "o":
			while True:
				system_case_ = [1,3,7,9]
				oLoc = random.choice(system_case_)
				if v[oLoc]=="x":
					continue
				else:
					break

		else:
			while True:
				if v[1]=="o" or v[9]=="o":
					oLoc = random.choice([3,7])
					if v[oLoc]=="x":
						continue
					else:
						break

				if v[3]=="o" or v[7]=="o":
					oLoc = random.choice([1,9])
					if v[oLoc]=="x":
						continue
					else:
						break

	if i==3:
		if v[5] == "o":
			while True:
				if v[1]=="o" or v[9] == "o":
					oLoc = random.choice([3,7])
					if v[oLoc]=="x":
							continue
					else:
						break


				if v[3]=="o" or v[7] == "o":
					oLoc = random.choice([1,9])
					if v[oLoc]=="x":
							continue
					else:
						break
		else:
			rows = [1,3,7,9]
			cases = [[1,3], [3,9], [9,7], [7,1]]
			for case in cases:
                                op1 = case.pop()
                                op2 = case.pop()
                                if v[op1]==v[op2]=="o":
                                        rows.remove(op1)
                                        rows.remove(op2)
                                        oLoc = random.choice(rows)
                                        rows.remove(oLoc)
                                        if oLoc not in locations:
                                                oLoc = rows.pop()
                                                break
                                        else:
                                                break
                                else:
                                        continue
	
	#logic for random move as the game is neutral
	if i!=1 and i!=2 and i!=3:
                oLoc = random.choice(locations)
                pass

	return oLoc

def check_win(v, winning_rows2):
	for row in winning_rows2:
                i = row[0]
                j = row[1]
                k = row[2]
                if v[i]==v[j]==v[k]=="o":
                        return 0
			break
		elif v[i]==v[j]==v[k]=="x":
                        return 1
			break
                else:
                        continue
