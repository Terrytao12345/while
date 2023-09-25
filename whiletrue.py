while True :
	mode = input('enter the game mode : ')
	if mode == 'q' :
		print('gam mode q')
		#break #(enter q will break only')
	elif mode == '1' :
		print('game mode 1')
	elif mode == '2' :
		print('game mode 2')
	else :
		print('please enter q/1/2 type only')
	break #(break any mode)
print('break working')