# simple car game using python in cmd

command = ''
started = False   # check if car is already started or not

while True:
	command = input(">> ").lower()
	if command == 'start':
		if started:
			print("Car is already started.")
		else:
			print("Car is starting.")
			started = True
		
	elif command == 'stop':
		if started:
			print("Car is stopping")
			started = False
		else:
			print("Car is already stopped.")
		
	elif command == 'help':
		print('''
		start - to start a car
		stop - to stop  a car
		quit - to end process
		''')
	elif command == 'quit':
		break   # exit while loop
	else:
		print("Invalid command.")


print("That was quite a fun.")