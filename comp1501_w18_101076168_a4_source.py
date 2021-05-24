#15. A relationship simulator where the player, a celebrity, 
#must find a partner and become the most popular couple in the city.
import random



class Room:
	def __init__(self, roomType):
		self.up = None
		self.left = None
		self.down = None
		self.right = None
		self.type = roomType
		self.desc = ""
		self.lookDesc = ""
		self.items = [] #takable
		self.chars = [] #characters

	def __str__(self):
		return self.desc
	def __repr__(self):
		return self.desc
		
class Item:
	def __init__(self, title, inventory, world):
		self.name = title
		self.desc = inventory
		self.worldDesc = world  

	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
		
class Character:
	def __init__(self, firstName, lastName, maxdmg, defense, alliance, description, attack):
		self.fName = firstName
		self.lName = lastName
		self.dmg = maxdmg
		self.defen = defense
		self.type = alliance
		self.desc = description
		self.health = 10
		self.fame = 0
		self.attackLine = attack
		self.room = None
		self.direction = 0
		self.quest_3_line = None #used for Partner when finished quest 3
		
		#move character to next room
	def moveRooms(self):
		#print("move" + self.fName)
		moved = False
		while (not moved):
		#check left 
			#print("left")
			#print(self.room)
			if (self.direction == 0 and self.room.left != None and self.room.left.type == "path"):
				self.room.chars.remove(self)
				self.room = self.room.left
				self.room.chars.append(self)
				moved = True
				break
		#check up
			#print("up")
			if (self.direction == 1 and self.room.up != None and self.room.up.type == "path"):
				self.room.chars.remove(self)
				self.room = self.room.up
				self.room.chars.append(self)
				moved = True
				break
		#check right 
			#print("right")
			if (self.direction == 2 and self.room.right != None and self.room.right.type == "path"):
				self.room.chars.remove(self)
				self.room = self.room.right
				self.room.chars.append(self)
				moved = True
				break
		#check down	
			#print("down")
			if (self.direction == 3 and self.room.down != None and self.room.down.type == "path"):
				self.room.chars.remove(self)
				self.room = self.room.down
				self.room.chars.append(self)
				moved = True
				break
			
			 #set next direction
			if self.direction == 0:
				self.direction = 1
			elif self.direction == 1:
				self.direction = 2
			elif self.direction == 2:
				self.direction = 3
			elif self.direction == 3:
				self.direction = 0
			
		
		
	def __str__(self):
		return self.fName + " " + self.lName
	def __repr__(self):
		return self.fName + " " + self.lName

		
		

	
def check_input(enter):
	#quit
	if enter.upper() == "QUIT":
		return (True, None, None, None)

	
			
	words = enter.split()
	one_word = False
	if len(words) < 2:
		one_word = True
	else:
		word_two = words[1].lower()
	
	#make sure a word was entered
	if len(words) > 0:
		word_one = words[0].lower()	
		nouns = {"cd1": CD1,
				"cd2": CD2,
				"cd3": CD3,
				"greggoris": painting1,
				"lightmoon": painting2,
				"flambda": painting3,
				"binder": tenants,
				"tenants": tenants,
				"tuner": tuner,
				"gravy": gravy,
				"container": gravy,
				"package": cheese,
				"cheese": cheese,
				"curds": cheese,
				"fries": fries,
				"treats": treats,
				"jen": singer,
				"tebra": singer,
				"singer": singer,
				"tanya": drummer,
				"zanders": drummer,
				"drummer": drummer,
				"christina": guitarist,
				"eldriss": guitarist,
				"guitarist": guitarist,
				"newspaper": news,
				"news": news,
				"paper": news,
				"pick": pick,
				"money": money,
				"stash": money,
				"officer": "guard",
				"guard": "guard",
				"policeman": "guard",
				"lever": "lever",
				"piano": piano,
				"stage": "stage"
				}
			
		verbs = {"down": playerRoom.down, 
				"left": playerRoom.left, 
				"right": playerRoom.right, 
				"up": playerRoom.up,
				"north": playerRoom.up,
				"east": playerRoom.right,
				"south": playerRoom.down,
				"west": playerRoom.left,
				"look": None,
				"take": None,
				"drop": None,
				"inventory": None,
				"examine": None,
				"push": None,
				"use": None,
				"play": None,
				"talk": None,
				"view": None,
				"help": None
				}
		
		if word_one in verbs:
			#if movement verb found
			if (word_one == "up" or word_one == "left" 
			or word_one == "right" or word_one == "down"
			or word_one == "north" or word_one == "east"
			or word_one == "south" or word_one == "west"):
				if verbs.get(word_one) != None:
					return (False, verbs.get(word_one), word_one, None)
				else:
					print("There is no room there.")
					return(False, None, None, None)
					
			#take or drop		
			if word_one == "take" or word_one == "drop": 
				if not one_word and word_two in nouns:
					if word_one == "take":
						return(False, None, word_one, nouns.get(word_two))
					if word_one == "drop":
						return(False, None, word_one, nouns.get(word_two))

				if word_one == "take":
					print("Take what?")
				if word_one == "drop":
					print("Drop what?")
				return(False, None, None, None)
				
			#inventory	
			if word_one == "inventory":
				return (False, None, word_one, None)
				
			#examine
			if word_one == "examine": 
				if not one_word and word_two in nouns:
					return (False, None, word_one, nouns.get(word_two))
				print("Examine what?")
				return(False, None, None, None)
			
			#look
			if word_one == "look":
				return(False, None, word_one, None)
				
			#push(for piano puzzle and lever puzzle)
			if word_one == "push":
				if not one_word and word_two == "piano":
					return(False, None, word_one, piano)
				if not one_word and word_two == "lever":
					return(False, None, word_one, "lever")
			
				print("Push what?")
				return(False, None, None, None)
				
			#use
			if word_one == "use":
				if nouns.get(word_two) in inventory and not one_word:
					return(False, None, word_one, nouns.get(word_two))
				
				print("Use what?")
				return(False, None, None, None)
				
			#play
			if word_one == "play":
				if not one_word and word_two == "piano":
					return(False, None, word_one, piano)
				elif not one_word and word_two == "stage":
					return(False, None, word_one, word_two)

				print("Play what?")
				return(False, None, None, None)
			
			#talk
			if word_one == "talk":
				if not one_word and word_two in nouns:
					return(False, None, word_one, nouns.get(word_two))
				print("Talk with who?")
				return(False, None, None, None)
			
			#help
			if word_one == "help":
				return(False, None, word_one, None)
			
			#view
			if word_one == "view":
				return(False, None, word_one, None)
				
						
				
			

	print("I didn't understand that.")
	return(False, None, None, None)		
		
		
def talkSinger(playerPartner, playerRoom, activeCharacters, singer):
	print("You approach Jen.")
	print('"I know that face, how\'s it going Zack Bondan? What brings you here, comin\' to talk to me?"')
	say = input("\nAction: ")
	say = say.lower()
	while (say != "leave" and say != "exit"):
		if say == "ask partner" or say == "ask date" or say == "ask girlfriend":
			if playerPartner == None:
				print("\nYou ask Jen to be your girlfriend.")
				print('"Ah, want to ride the List of Fame do yah? Well I gotta couple o\' questions for you then."')
				print('"If you can answer them correctly then you might be in luck."')
				print('"Alright, first. You gotta know what type of singer I am, what genre do I sing?"')
				say = input("\nAnswer: ")
				say = say.lower()
				if say == "country":
					print('"\nThat\'s right! That was an easy one though."')
					print('"Alright next question. How old am I?"')
					say = input("\nAnswer: ")
					say = say.lower()
					if say == "25":
						print('\n"Right again! I guess you\'re fit for the test."')
						print("Jen Tebra is now your girlfriend!")
						playerPartner = singer
						singer.room = None
						playerRoom.chars.remove(singer)
						activeCharacters.remove(singer)
						return playerPartner
						
					else:
						print('\n"There\'s no runner-up reward. Come again."')
					
				else:
					print('"\nYa don\'t even know what I sing? There\'s no way I\'ll be your girlfriend!"')
			else:
				print("\nYou already have a partner!")
		elif say == "ask city" or say == "ask town" or say == "ask tromack":
			print("\nYou ask Jen about Tromack City.")
			print('"Ah, yes Tromack City. I\'ve lived here since I was a young girl. It ain\'t all')
			print('rolling hills as it used to be though. Now this place is overrun with musicians, like')
			print('that one city that had all those classical musicians back in the day. It\'s a small city')
			print('but has a lot of adventures."')
		elif say == "ask list" or say == "ask fame":
			print("\nYou ask Jen about the List of Fame.")
			print('"Doesn\'t surprise me you know about the monument of the town. I\'ve been here long enough')
			print('to know that it works. the couples at the top of that list are worldwide stars.')
			print('Oh what I would do to be up there..."')
		elif say == "look" or say == "examine":
			print("\nYou look at Jen.")
			print("Jen is wearing ripped jeans and a red and white checkered shirt. She has")
			print("flowing red hair and a smile that seeps into your heart.")
			print('"What, are ya just goin\' to stare at me?"')
		elif say == "help":
			printHelp()
		else:
			print("\nYou stutter with your words.")
			print('"You alright there, pal?" Jen wonders.')
		
		say = input("\nAction: ")
		say = say.lower()
	
	if playerPartner != singer: #if not partner
		print('"See ya around."')
	return playerPartner

def talkDrummer(playerPartner, playerRoom, activeCharacters, inventory, drummer):
	print("You approach Tanya.")
	print('"Hey, punk. What do you want?"')
	say = input("\nAction: ")
	say = say.lower()
	while (say != "leave" and say != "exit"):
		if say == "ask partner" or say == "ask date" or say == "ask girlfriend":
			if playerPartner == None:
				print("\nYou ask Tanya to be your girlfriend.")
				print('"You want me to be your girlfriend, huh? I\'m not cheap. You got any money for me?"')
				say = input("\nAnswer: ")
				say = say.lower()
				if (say == "yes" and money in inventory):
					print("\nYou give Tanya the stash of money you found.")
					print('"Hmm, I guess this will cut it for now."')
					print("Tanya is now your girlfriend!")
					playerPartner = drummer
					drummer.room = None
					playerRoom.chars.remove(drummer)
					activeCharacters.remove(drummer)
					inventory.remove(money)
					return playerPartner
					
				elif say == "yes":
					print("\nAll your money is in the bank!")
					print('"I only take real money, none of that fake bank stuff," Tanya says.')
				else:
					print('"Yeah, I didn\'t think I was your type."')
			else:
				print("\nYou already have a partner!")
				
		elif say == "ask city" or say == "ask town" or say == "ask tromack":
			print("\nYou ask Tanya about Tromack City.")
			print('"This place is a dump. Collection of famous wannabes here. You\'ll fit right in."')
		elif say == "ask list" or say == "ask fame":
			print("\nYou ask Tanya about the List of Fame.")
			print('"The list? I\'ve been up and down it, with one guy or another. Couples on there')
			print('are not happy with eachother. They all do it for the money, put on their cute')
			print('couple faces and please the cameras then yell at eachother behind the scenes."')
		elif say == "look" or say == "examine":
			print("\nYou look at Tanya.")
			print("She is wearing full black. She has black mascara smeared under her eyes and luscious red lipstick.")
			print("Her hair is also black and is let down past her hips.")
			print('"Keep looking, freak," She says rudely.')
		elif say == "help":
			printHelp()
		else:
			print("\nYou stutter with your words.")
			print('"What\'re you, stupid?" Tanya mocks you.')
		
		say = input("\nAction: ")
		say = say.lower()
	
	if playerPartner != drummer: #if not partner
		print('"Have fun invading someone else\'s bubble," Tanya sneers as you walk away.')
	return playerPartner
	
def talkGuitarist(playerPartner, playerRoom, activeCharacters, inventory, guitarist):
	print("You approach Christina.")
	print('"What\'s up?"')
	say = input("\nAction: ")
	say = say.lower()
	while (say != "leave" and say != "exit"):
		if say == "ask partner" or say == "ask date" or say == "ask girlfriend":
			if playerPartner == None:
				print("\nYou ask Christina to be your girlfriend.")
				print('"It\'s a nice thought, but I don\'t think I can ever be happy again without my specialized')
				print('guitar pick..." her voice trails off.')
				if pick in inventory:
					say = input("\nGive her pick back? ")
					say = say.lower()
					if say == "yes" or say == "give":
						print("\nYou slowly pull out the golden guitar pick you found.")
						print('"My pick!" Christina nearly shouts as she grabs the pick right out of your hands.')
						print('She then unexpectedly hugs you tightly and says "Ready to be my boyfriend?"')
						print("Christina is now your girlfriend!")
						playerPartner = guitarist
						guitarist.room = None
						playerRoom.chars.remove(guitarist)
						activeCharacters.remove(guitarist)
						inventory.remove(pick)
						return playerPartner
					else:
						print("\nMaybe another day.")
			else:
				print("\nYou already have a partner!")
		elif say == "ask city" or say == "ask town" or say == "ask tromack":
			print("\nYou ask Christina about Tromack City.")
			print('"I just got here recently. The city is pretty fascinating. It\'s a small quaint place')
			print('with all the necessities one needs. Most of the people are highly respected artists')
			print('like myself, so it really takes off the pressure of worrying about crazy fans. I like it here."')
		elif say == "ask list" or say == "ask fame":
			print("\nYou ask Christina about the List of Fame.")
			print('"It\'s quite the attraction. I cannot see myself ever getting on that list since I haven\'t')
			print('ever been in a relationship myself."')
		elif say == "look" or say == "examine":
			print("\nYou look at Christina.")
			print("She is wearing a plain white T-shirt along with a pair of leather pants. her right arm has")
			print("a tattoo of an angel, while her left arm has a small tattoo of a rose. She has golden hair")
			print("which is flowing steadily in the wind.")
			print("Christina watches you curiously as you investigate her.") 
		elif say == "help":
			printHelp()
		else:
			print("\nYou stutter on your words.")
			print('Christina smiles slightly at you.')
		
		say = input("\nAction: ")
		say = say.lower()
	
	if playerPartner != guitarist: #if not partner
		print('"It was nice to meet you."')
	return playerPartner
	
def talkGuard(playerPartner):
	print("You approach the guard.")
	print('"What is your business here?" he says sternly.')
	say = input("\nAction: ")
	say = say.lower()
	while (say != "leave" and say != "exit"):
		if say == "ask partner" or say == "ask date" or say == "ask boyfriend":
			print("You ask the guard to be your boyfriend.")
			print('"Sorry, I\'m not gay."')
		elif say == "ask list" or say == "ask fame" or say == "ask town" or say == "ask city" or say == "ask tromack":
			print('"I don\'t know about that stuff."')
		elif (say == "ask piano" or say == "ask music" or say == "ask play") and playerPartner == None:
			print("\nYou ask if there is a piano to play in this room.")
			print('"No, not unless you brought your own. Well, there is this one guy who always leaves')
			print('his piano here in the front, maybe come back at a later time."')
		elif (say == "ask piano" or say == "ask music" or say == "ask play"):
			print('\n"There is a piano in the front of the station right now, perhaps if you could get it in')
			print('here you would be able to play it."')
		elif say == "ask crime" or say == "ask police" or say == "ask city":
			print("\nYou ask about crime in the city.")
			print('"This place does not have much crime. A lot of the crimes that happen are by people who')
			print('try and get too close to the artists around here."')
		elif say == "look" or say == "examine":
			print("You attempt to examine the guard.")
			print('"Stop it with that suspicious eying." he tells you.')
		elif say == "help":
			printHelp()
		else:
			print("\nYou try to think of a good question, but could not.")
		say = input("\nAction: ")
		say = say.lower()
	print('"You stay out of trouble now," the guard warns.')	
	
def battle(player, fame, enemy):
	print("\n" + enemy.fName + " and " + enemy.lName + " force you into a performance battle! A small crowd gathers.")
	while player.health > 0 and enemy.health > 0: #while player and enemy still alive
		input("\nPress enter to roll.")
		playerRoll = random.randint(1, player.dmg) #roll dice up to max damage
		print("\n" + player.attackLine)
		if playerRoll > enemy.defen: #if attack greater than opposing defense
			print("The opposing couple loses " + str(playerRoll - enemy.defen) + " confidence point(s).")
			enemy.health -= (playerRoll - enemy.defen)
		else: #no damage dealt
			print("You and " + player.fName + " are out of sync! You have no affect on the opposing couple.")
		if enemy.health <= 0:
			break
		
		enemyRoll = random.randint(1, enemy.dmg)
		print("\n" + enemy.attackLine)
		if enemyRoll > player.defen: #hit
			print("You and " + player.fName + " lose " + str(enemyRoll - player.defen) + " confidence point(s).")
			player.health -= (enemyRoll - player.defen)
		else: #miss
			print(enemy.fName + " and " + enemy.lName + " are out of key with eachother! They have no affect on you.")
		
	
		
	if player.health <= 0: #player lost
		print("\nYou and " + player.fName + " run out of confidence and flee the performance.")
		if fame > 3:
			print("You lose 4 fame!")
			fame -= 4
		else: #Intentionally don't take away fame if less than 4
			print("You don't have enough fame to lose!") 
			
	else: #opponent lost
		print("\n" + enemy.fName + " and " + enemy.lName + ' admit defeat to your skills. "Don\'t think this is the \nend though! We shall return!" They say while leaving you in the crowd.')
		print("You gain 4 fame!")
		fame += 4
		
	#reset values
	player.health = 10
	enemy.health = 10	
		
	return fame
	
	
	
			#print all verbs
def printHelp():
	print("\nWelcome to the help page! Here ALL verbs are listed alongside with what you can do with them.")
	print("'down' or 'south': Used to enter room south")
	print("'left' or 'west': Used to enter room to the west")
	print("'up' or 'north': Used to enter room north")
	print("'right' or 'east': Used to enter room east")
	print("'look': Give an additional description of the current area.")
	print("'take': Add item specified after take to your inventory if in the room you're in.")
	print("'drop': Remove item specified after drop from inventory. Adds to current room.")
	print("'inventory': Displays name of all items currently in inventory.")
	print("'examine': Gives a description of an item specified after examine. Item has to be in inventory or current room.")
	print("'push': Used to push an object specified after push.")
	print("'use': Attempt to use item specified after 'use' in the current room. Item has to be in inventory.")
	print("'play': Attempt to play object specified after play.")
	print("'view': Used to view the List of Fame when in the room of the List of Fame.")
	print("'talk': Talk with character specified after talk. Character must be in the same room.")
	print("'quit': Used to exit the game.")
	print("ADDITIONAL TALK VERBS")
	print("'ask': Ask about the word specified after ask to character.")
	print("'look' or 'examine': Look at features of the character.")
	print("'leave' or 'exit': Leave the conversation.")
	
			
		

			
#Make rooms
start_room = Room("start")
start_room.desc = "You are inside the Tromack airport. People are rushing to and fro, many who\nseem to be tourists. To the East is the exit to Tromack."
start_room.lookDesc = "There is nothing else to see in the airport. The normal description will be displayed.\n" + start_room.desc

path_1 = Room("path")
path_1.desc = "You stand outside the fence of a public school. Kids are outside playing, \nthrowing and kicking balls back and forth. To the East is the entrance to MallMart. \nTo the South is a casino. To the West is the Tromack airport."
path_1.lookDesc = "As you look at the kids, some of them come running up to the fence and start \nyelling at you and asking you to come play with them. The teacher comes out and \ntells them to get away from the fence. To the East is the entrance to MallMart. \nTo the South is a casino. To the West is the Tromack airport."

path_2 = Room("path")
path_2.desc = "You are at the entrance to MallMart, the local supermarket. It doesn't seem too busy \nright now. Enter MallMart by heading North. To the East is an intersection. \nTo the West is a public school."
path_2.lookDesc =  "As you look around, you see a homeless man at the side begging for money. \nYou can hear a baby crying somewhere in the store and someone's car alarm will not stop going off.\nEnter MallMart by heading North. To the East is an intersection. \nTo the West is a public school."

path_3 = Room("path")
path_3.desc = "You are standing at an intersection. To the East is the Northern section of downtown. \nTo the South is the Western section of downtown. To the West is the entrance to MallMart."
path_3.lookDesc =  "At the corner of the intersection, there is an old lady selling flowers. A little \nred car drives by with a dog sticking its head out the window and its tongue lolling.\nTo the East is the Northern section of downtown. \nTo the South is the Western section of downtown. To the West is the entrance to MallMart."

path_4 = Room("path")
path_4.desc = "You are in the Northern section of downtown. To the North is an art gallery. \nTo the East taxis are parked alongside a sidewalk. To the South is \nthe List of Fame. To the West is an intersection."
path_4.lookDesc =  "Many food stands litter this area. People rush back and forth, bumping into you \nwithout saying anything. To the East taxis are parked alongside a sidewalk. To the South is \nthe List of Fame. To the West is an intersection." 

path_5 = Room("path")
path_5.desc = "You are on the sidewalk next to many large business buildings. Taxis are \nlined up alongside the sidewalk waiting to give people rides. To the East is the \nentrance to the Jesse Pub. To the South is the Eastern section of downtown. \nTo the West is the Northern section of downtown."
path_5.lookDesc =  "A lot of the taxis are just going down the street and dropping people \noff at the concert hall. To the East is the entrance to the Jesse Pub. To the South \nis the Eastern section of downtown. To the West is the Northern section of downtown."

path_6 = Room("path")
path_6.desc = "You are outside the Jesse Pub. Enter the pub by heading North. To the East is a large \napartment building. To the West are taxis parked alongside a sidewalk."
path_6.lookDesc =  "A couple of people who appear to be drunk are coming out of the pub, \nwobbling back and forth. They walk to their pickup truck. Looks like they're going to be driving drunk!\nTo the East is a large apartment building. To the West are taxis parked alongside a sidewalk."

path_7 = Room("path")
path_7.desc = "A large apartment building looms before you. Enter the building by heading East. \nTo the South is a dark alleyway. To the West is the entrance to the Jesse Pub."
path_7.lookDesc =  'You look up and see someone high up washing windows. A banner is at the top of \nthe apartment building, which reads "Goswood Apartments". Enter the building by heading East. \nTo the South is a dark alleyway. To the West is the entrance to the Jesse Pub.'

path_8 = Room("path")
path_8.desc = "You enter a casino. You see people playing roulette, poker, and other games. \nTo the North is a public school. To the South is a science lab."
path_8.lookDesc = "You take a look to the side and see that there is also a buffet here. \nLooks like a great place to spend a lot of money. \nTo the North is a public school. To the South is a science lab."

path_9 = Room("path")
path_9.desc = "You are in the Western section of downtown. To the North is an intersection. \nTo the East is the List of Fame. To the South is a library."
path_9.lookDesc =  "There is a small crowd gathered around 3 guitarists who are just playing \nsongs that the crowd requests. A guitar case lays open before them filled with tips. \nTo the East is the List of Fame. To the South is a library."

path_10 = Room("path")
path_10.desc = "You are in the Eastern section of downtown. To the North are taxis parked alongside \na sidewalk. To the South is a church. To the West is the List of Fame."
path_10.lookDesc =  "There is a river flowing nearby. It looks mucky and dirtied and you cannot spot \nanything living down below.  To the North are taxis parked alongside a sidewalk. To the South \nis a church. To the West is the List of Fame."

path_11 = Room("path")
path_11.desc = "You are in an alleyway behind an apartment building. You can see a raccoon \ndigging through some trash. To the North is the front of the apartment building. \nTo the South is a police station."
path_11.lookDesc =  "Many dumpsters line the alleyway. There is a garbage shoot connected to the \napartment building which is shooting out garbage every 30 seconds. To the North is the front of the apartment building. \nTo the South is a police station."

path_12 = Room("path")
path_12.desc = "You enter a science laboratory where multiple scientists in white vests are writing \nnotes on clipboards and performing tests. To head deeper into the lab, go West. \nTo the North is a casino. To the East are fast food restaurants."
path_12.lookDesc =  "You look around and see various experiments contained behind glass. Looks like \nthere is a huge section set to work on the cure for cancer. To head deeper into the \nlab, go West. To the North is a casino. To the East are fast food restaurants."

path_13 = Room("path")
path_13.desc = "There are multiple fast food restaurants here. One catches your eye, Poutine Queen. \nHead South to enter Poutine Queen. To the East is a library. To the West is a science lab."
path_13.lookDesc =  'You look at some of the other restaurants. Some of the names are "John\'s Pizzaria", \n"DokBurger" and "Thai Valley". Head South to enter Poutine Queen. To the East is a \nlibrary. To the West is a science lab.'

path_14 = Room("path")
path_14.desc = "You enter a library, where a small collection of people are quietly reading and \nusing their devices. To the North is the Western section of downtown. To the East is the \nSouthern section of downtown. To the West are fast food restaurants."
path_14.lookDesc =  "The library is split into different sections for kids and adults, but the few people \nhere seem to be adults with their children over in the kids' section. \nTo the North is the Western section of downtown. To the East is the Southern \nsection of downtown. To the West are fast food restaurants."

path_15 = Room("path")
path_15.desc = "You are in the Southern section of downtown. To the North is the List of Fame. \nTo the East is a church. To the South is a train station. To the West is a library."
path_15.lookDesc =  'There is a small park named "Featherstone Park" here. Looks like a nice place to relax. \nTo the North is the List of Fame. To the East is a church. To the South is a train \nstation. To the West is a library.'

path_16 = Room("path")
path_16.desc = "There is a large church here. To the North is Eastern downtown. To the East is a \nparking lot for a large concert hall. To the West is Southern downtown."
path_16.lookDesc =  'A giant cross is at the top of the church. There is a sign set up which says, \n"All are welcome!" To the North is Eastern downtown. To the East is a \nparking lot for a large concert hall. To the West is Southern downtown.'

path_17 = Room("path")
path_17.desc = "You are in an enormous parking lot for the Blain concert hall. Enter the concert hall by \nheading South. To the East is a police station. To the West is a church."
path_17.lookDesc =  "The parking lot is filled so there must be a show going on. You expect that to be \ntypical in this town. Enter the concert hall by heading South. \nTo the East is a police station. To the West is a church."

path_18 = Room("path")
path_18.desc = "You are at the front of a police station. There are jail cells inside holding people. \nView the jail cells by heading East. To the North is a dark alleyway. \nTo the West is a parking lot for a large concert hall."
path_18.lookDesc =  "Nobody is at the front desk. There are multiple desks and computers lined up out back. \nWith most of the seats occupied. View the jail cells by heading East. To the North is a \ndark alleyway. To the West is a parking lot for a large concert hall."

quest_1 = Room("quest")
quest_1.desc = "You enter MallMart and marvel at the size. You imagine you could find anything in this place. \nYou can see multiple cashiers lined up serving customers. You also take note of the \nold music playing on the speaker system. The MallMart manager is grumpily walking past. \nTo exit the store, head South."
quest_1.lookDesc = 'While looking at all the cashiers, you notice the MallMart manager grumbling, \n"Get better music... too old... not cool enough..." To exit the store, head South.'

quest_2 = Room("quest")
quest_2.desc = "The art gallery has many magnificent works. However you notice one section of the gallery \nthat is missing three adjacent paintings. In their place is a note - 'if paintings found, \nplease return'. To exit the gallery, head South."
quest_2.lookDesc = "After thoroughly inspecting the art gallery, you come to the conclusion that the missing \npaintings are not IN the art gallery. To exit the gallery, head South."

quest_3 = Room("quest")
quest_3.desc = "The pub is lively with people drinking, laughing and just enjoying themselves. You notice an \nempty stage with a wide range of instruments setup. To exit the pub, head South."
quest_3.lookDesc = "The stage has a piano, a guitar, a microphone, and a drumset. What a great setup! To exit the pub, head South."

quest_4 = Room("quest")
quest_4.desc = "The apartment building is the home to most of the citizens of Tromack. There are 9 floors in \nthe building. On the main floor you can see the head office. To exit the building, head West."
quest_4.lookDesc = 'As you look around more thoroughly, you overhear a lady in the office shouting,\n"We are missing half of all the tenants information! This is not good." \nTo exit the building, head West.'

quest_5 = Room("quest")
quest_5.desc = 'You are outside many jail cells. As you walk by one of the jail cells, a man calls out, \n"Is that you Zack Bondan? It is! Oh what I would do to hear one of your piano pieces live." \nTo head back to the police station, head West.'
quest_5.lookDesc = "You see a guard skeptically watching your movements. Perhaps you could talk to him. \nThe man who called out is very slim and is wearing tattered orange jailer overalls.\nTo head back to the police station, head West."

quest_6 = Room("quest")
quest_6.desc = "You enter the concert hall to see an opposing couple on stage, Mandy Jamerson singing \nand Burt Bradds playing the piano for the half-full room. something doesn't seem right though, \nyou can tell the piano is out of tune and the crowd is booing because if it. \nTo exit back to the parking lot, head North."
quest_6.lookDesc = "There doesn't seem to be anything else of interest in the room. To exit back to the \nparking lot, head North."

quest_7 = Room("quest")
quest_7.desc = "The train station is overcrowded and the train does not seem to be moving. The conductor \nis a young man and seems to be new to this. He does not know why the train won't move. \nTo exit the train station head North."
quest_7.lookDesc = "It is quite the predicament, but you don't think you can do anything here alone. \nTo exit the train station head North."

quest_8 = Room("quest")
quest_8.desc = 'The Poutine Queen is empty. No one is here to buy food. You walk up to the counter and \na lady walks out of the back room sporting the Poutine Queen employee shirt. "Sorry, we \ncannot make poutine right now, we are all out of cheese, gravy and fries," she says. \nTo exit the Poutine Queen, head North.'
quest_8.lookDesc = "This place is really dull without any people to give it an atmosphere. With all the seats \nempty, this place feels like an abandoned fast food place. Maybe because it is.\nTo exit the Poutine Queen, head North." 

quest_9 = Room("quest")
quest_9.desc = "Deep in the lab you approach a strange sight. There are a bunch of scientists locked up \nin a room! They are frantically looking at you and pointing at a cat sitting on a \nbutton on the floor. To exit back to the lab, Head East."
quest_9.lookDesc = "The cat looks vicious, approaching it is not a good idea. To exit back to the lab, Head East."

quest_10 = Room("quest")
quest_10.desc = "You are confronted by the List of Fame. Or maybe you're the one confronting the list? \nIt doesn't really matter if you're not on the top of it. You may 'view' the list here. \nTo the North is Northern downtown. To the East is Eastern downtown. \nTo the South is Southern... you're in the centre of downtown."
quest_10.lookDesc = "Yet again, \n" + quest_10.desc


#join rooms together
start_room.right = path_1
path_1.left = start_room
path_1.right = path_2
path_1.down = path_8
path_2.left = path_1
path_2.up = quest_1
path_2.right = path_3
path_3.left = path_2
path_3.down = path_9
path_3.right = path_4
path_4.left = path_3
path_4.up = quest_2
path_4.right = path_5
path_4.down = quest_10
path_5.left = path_4
path_5.right = path_6
path_5.down = path_10
path_6.left = path_5
path_6.up = quest_3
path_6.right = path_7
path_7.left = path_6
path_7.right = quest_4
path_7.down = path_11
path_8.up = path_1
path_8.down = path_12
path_9.up = path_3
path_9.right = quest_10
path_9.down = path_14
path_10.up = path_5
path_10.down = path_16
path_10.left = quest_10
path_11.up = path_7
path_11.down = path_18
path_12.up = path_8
path_12.left = quest_9
path_12.right = path_13
path_13.left = path_12
path_13.right = path_14
path_13.down = quest_8
path_14.left = path_13
path_14.up = path_9
path_14.right = path_15
path_15.left = path_14
path_15.right = path_16
path_15.down = quest_7
path_15.up = quest_10
path_16.left = path_15
path_16.up = path_10
path_16.right = path_17
path_17.left = path_16
path_17.down = quest_6
path_17.right = path_18
path_18.left = path_17
path_18.up = path_11
path_18.right = quest_5
quest_1.down = path_2
quest_2.down = path_4
quest_3.down = path_6
quest_4.left = path_7
quest_5.left = path_18
quest_6.up = path_17
quest_7.up = path_15
quest_8.up = path_13
quest_9.right = path_12
quest_10.up = path_4
quest_10.left = path_9
quest_10.down = path_15
quest_10.right = path_10

#make Items (Not all get placed in rooms, some after finding a partner)
CD1 = Item("CD1", "You recognize this as one of your albums, the first of three parts. You weren't very creative with the name.", "A CD named 'CD1' lies on the ground closed within a case.")
CD2 = Item("CD2", "You recognize this as one of your albums, the second of three parts.", "A CD named 'CD2' is outside of its case and rests on the ground.")
CD3 = Item("CD3", "You recognize this as one of your albums, the third of three parts.", "A small box containing a CD named 'CD3' is nearby.")
painting1 = Item("Greggoris", "The painting belongs to an art gallery. It's a painting of a viking named Greggoris the Great.", "The painting 'Greggoris' is here.")
painting2 = Item("Lightmoon", "The painting belongs to an art gallery. It's a painting of light being reflected off of a crescent moon.", "The painting 'Lightmoon' is here.")
painting3 = Item("Flambda", "The painting belongs to an art gallery. It's a painting of the Greek symbol lambda, engulfed in flames.", "The painting 'Flambda' is here.")
tenants = Item("binder", "This binder seems to contain information on tenants living in an apartment building.", "A binder rests nearby.")
tuner =  Item("tuner", "A tuner, used with instruments to make sure notes sound right. You know how to use this with pianos.", "A tuner sits on the ground.")
gravy = Item("gravy", "Gravy, one of the key ingredients in making poutine.", "A container of gravy rests here.")
cheese = Item("cheese curds", "Cheese curds, one of the key ingredients in making poutine.", "A package of cheese curds is here.")
fries = Item("fries", "Fries, one of the key ingredients in making poutine.", "A plastic bag containing a large amount of fries is here.")
treats = Item("cat treats", "Cats can't resist these tasty snacks, they'll do anything for them.", "a bag of cat treats is on the ground.")
piano = Item("piano", "this shouldn't be in your inventory.", "There is a piano in this room.")

news = Item("newspaper", 'The newspaper is 2 years old and says, "Jen Tebra, famous country singer, helps the disabled: \nThis 23 year-old has been donating a lot of money to..." the rest is illegible.', "A newspaper rests nearby.") 
money = Item("money", "It's just a large stack of money.", "You spot a pile of money hidden in a corner.")
pick = Item("guitar pick", "A golden guitar pick, with the letters CE engraved into it.", "A shiny guitar pick is laying on the ground.")

#Place items needed for dates
quest_3.items.append(news)
path_8.items.append(money)
path_17.items.append(pick)


#set player Stuff
playerRoom = start_room
playerFame = 0
playerPartner = None
inventory = []

#make characters
singer = Character("Jen", "Tebra", 5, 2, "friend", "A woman you recognize is here, the singer Jen Tebra.", "Jen sings while you play the piano.")
singer.room = globals()["path_" + str(random.randint(1, 18))] #cast string to object
singer.room.chars.append(singer)
singer.quest_3_line = "on the microphone"
drummer = Character("Tanya", "Zanders", 8, 1, "friend", "A woman with tattered jeans who you recognize as the drummer Tanya Zanders is here.", "Tanya drums a beat to your piano song.")
drummer.room = globals()["path_" + str(random.randint(1, 18))]
drummer.room.chars.append(drummer)
drummer.quest_3_line = "who begins hammering on the drums"
guitarist = Character("Christina", "Eldriss", 4, 3, "friend", "A woman walking around with her guitar is nearby. Her guitar has a name tag which reads 'Christina Eldriss'.", "Christina plays along with you on the piano.")
guitarist.room = globals()["path_" + str(random.randint(1, 18))]
guitarist.room.chars.append(guitarist)
guitarist.quest_3_line = "who calmly plays along on her guitar"

enemy_1 = Character("Mandy Jamerson", "Burt Bradds", 4, 2, "enemy", "The couple Mandy Jamerson and Burt Bradds are here with their piano!", "Mandy sings to Burt's piano playing.")
enemy_1.fame = 10
enemy_1.room = globals()["path_" + str(random.randint(1, 18))]
enemy_2 = Character("Becky Marsh", "Jimmy White", 5, 1, "enemy", "The couple Becky Marsh and Jimmy White are here with their guitars!", "Becky and Jimmy play their guitars in sync.")
enemy_2.fame = 24
enemy_2.room = globals()["path_" + str(random.randint(1, 18))]
enemy_3 = Character("Amanda Small", "Brandon Long", 7, 0, "enemy", "The couple Amanda Small and Brandon Long are here with their brass instruments!", "Amanda plays her Trumpet alongside Brandon's Tuba.")
enemy_3.fame = 36
enemy_4 = Character("Mandy Homes", "John Smith", 6, 2, "enemy", "The couple Mandy Homes and John Smith are here with their flute and harmonica!", "Mandy leads on her flute while John follows on the harmonica.")
enemy_4.fame = 49


 
activeCharacters = [singer, drummer, guitarist]
enemyQueue = [enemy_3, enemy_4]

listOfFame = ["LIST OF FAME", "Couple\t\t\t\t\tFame", "Mandy Homes and John Smith\t\t49 fame", "Amanda Small and Brandon Long\t\t36 fame", "Becky Marsh and Jimmy White\t\t24 fame", "Mandy Jamerson and Burt Bradds\t\t10 fame"]


#intro
print("\nWelcome to the city of Tromack! Your name is Zack Bondan and you are a famous")
print("musician known for your talented piano compositions. Tromack is a small town")
print("known for the many popular artists who reside here. You came here because you")
print("were getting quite lonely and wanted to find the 'girl of your dreams'. Not only")
print("that, but Tromack has a list of all the famous couples, found in the center of town.")
print("The list is renowned worldwide. Finding a girlfriend isn't enough for you,")
print("you want to reach the top of the List of Fame so that people will remember")
print("your name forever.")

#how to play
print("\nTo move around the city type the commands 'North', 'East', 'South', or 'West'. Some")
print("other helpful commands are 'look' which will give you a better description of the area")
print("you are currently in. 'take' and 'drop' may be used on objects in the world or in")
print("your inventory, respectively. 'inventory' will show the names of items in your")
print("inventory. 'examine' can be used on interactive objects in the current location or in")
print("your inventory. 'use' can be used on items in your inventory, typically for solving")
print("puzzles in a room. You can 'talk' to some people in the same area as you. Don't be afraid")
print("to 'ask' about their opinion on the city or the List of Fame.")
print("You can type 'help' for a list of all action words and what they do.")
print("Only the first 2 words that you type are evaluated (Even when talking).")

input("\nPress enter to continue.")

print("\nYou arrive in the Tromack airport expecting to turn every corner and see an artist you")
print("know. You do not see anyone of the sorts here and feel it is time to head into town")
print("and explore. The exit of the airport is to the East.")

#variable used after new Items initalized when player gets a partner
placed_new_items = False

#variable used to check if quest 3 was completed
quest_3_complete = False

#variable used to check if quest 7 was completed
quest_7_complete = False

#boolean used so other characters move every second player move
move = False

#boolean used to give help before first battle
first_battle = True

closed_flag = False

while not closed_flag:
	
	
	#####INPUT#####
	enter = input("\nNext action: ")
	(closed_flag, newRoom, keyWord, object) = check_input(enter)
	
	#if QUIT, exit loop
	if closed_flag:
		break
	
	
		
	
	
	
	#####UPDATE#####
	if newRoom != None:
		playerRoom = newRoom
		
	if keyWord == "take":
		if object in playerRoom.items:
			playerRoom.items.remove(object)
			inventory.append(object)
			print("ok.")
		else:
			print("Could not find item in room.")
	
	if keyWord == "drop":
		if object in inventory:
			inventory.remove(object)
			playerRoom.items.append(object)
			print("ok.")
		else:
			print("Could not find item in inventory.")
		
	#place new items / spawn enemy couples
	if playerPartner != None and placed_new_items == False:
		placed_new_items = True
		path_18.items.append(CD3)
		path_11.items.extend((tenants, treats))
		path_8.items.append(CD1)
		path_16.items.append(fries)
		quest_8.items.append(cheese)
		path_9.items.append(CD2)
		path_12.items.append(painting2)
		path_17.items.append(gravy)
		path_7.items.append(tuner)
		quest_10.items.append(painting1)
		path_14.items.append(painting3)
		path_18.items.append(piano)
		quest_7.lookDesc = playerPartner.fName + " notices a lever at the front of the train facing towards you. It seems to be set to 'brake'."
		enemy_1.room.chars.append(enemy_1)
		activeCharacters.append(enemy_1)
		enemy_2.room.chars.append(enemy_2)
		activeCharacters.append(enemy_2)
		
	if keyWord == "talk":
		if object == singer and playerRoom == singer.room:
			playerPartner = talkSinger(playerPartner, playerRoom, activeCharacters, singer)
		elif object == drummer and playerRoom == drummer.room:
			playerPartner = talkDrummer(playerPartner, playerRoom, activeCharacters, inventory, drummer)
		elif object == guitarist and playerRoom == guitarist.room:
			playerPartner = talkGuitarist(playerPartner, playerRoom, activeCharacters, inventory, guitarist)
		elif object == "guard" and playerRoom == quest_5:
			talkGuard(playerPartner)
		else:
			print("Who are you trying to talk to?")
			
	
		#move active characters every second player move
	if newRoom != None:
		if move:
			move = False
			for char in activeCharacters:
				char.moveRooms()
		else:
			move = True
	
			
			
	#update list of fame
	if playerPartner != None:
		if playerPartner == guitarist: #accomadate for long name, remove a tab
			playerLine = ("Zack Bondan and " + playerPartner.fName + " " + playerPartner.lName + "\t" + str(playerFame) + " fame")
		else:
			playerLine = ("Zack Bondan and " + playerPartner.fName + " " + playerPartner.lName + "\t\t" + str(playerFame) + " fame")
		if playerFame > 49:
			listOfFame = ["LIST OF FAME", "Couple\t\t\t\t\tFame", playerLine, "Mandy Homes and John Smith\t\t49 fame", "Amanda Small and Brandon Long\t\t36 fame", "Becky Marsh and Jimmy White\t\t24 fame", "Mandy Jamerson and Burt Bradds\t\t10 fame"]
		elif playerFame > 36:
			listOfFame = ["LIST OF FAME", "Couple\t\t\t\t\tFame", "Mandy Homes and John Smith\t\t49 fame", playerLine, "Amanda Small and Brandon Long\t\t36 fame", "Becky Marsh and Jimmy White\t\t24 fame", "Mandy Jamerson and Burt Bradds\t\t10 fame"]
		elif playerFame > 24:
			listOfFame = ["LIST OF FAME", "Couple\t\t\t\t\tFame", "Mandy Homes and John Smith\t\t49 fame", "Amanda Small and Brandon Long\t\t36 fame", playerLine, "Becky Marsh and Jimmy White\t\t24 fame", "Mandy Jamerson and Burt Bradds\t\t10 fame"]
		elif playerFame > 10:
			listOfFame = ["LIST OF FAME", "Couple\t\t\t\t\tFame", "Mandy Homes and John Smith\t\t49 fame", "Amanda Small and Brandon Long\t\t36 fame", "Becky Marsh and Jimmy White\t\t24 fame", playerLine, "Mandy Jamerson and Burt Bradds\t\t10 fame"]
		else:
			listOfFame = ["LIST OF FAME", "Couple\t\t\t\t\tFame", "Mandy Homes and John Smith\t\t49 fame", "Amanda Small and Brandon Long\t\t36 fame", "Becky Marsh and Jimmy White\t\t24 fame", "Mandy Jamerson and Burt Bradds\t\t10 fame", playerLine]
	
	
	#####RENDER#####
	
	#player enters a new room
	if newRoom != None:
		print(playerRoom.desc)
		if not playerRoom.items:
			pass
		else:
			for i in playerRoom.items:
				print(i.worldDesc)
		if not playerRoom.chars:
			pass
		else:
			for char in playerRoom.chars:
				print(char.desc)
				
	for char in playerRoom.chars: #check for battles
		if char.type == "enemy" and char.room == playerRoom:
			if first_battle:
				first_battle = False
				print("\nYou are about to enter your first performance battle. Your stats for performance battles")
				print("are hidden. Depending on who your partner is, your stats will vary. You roll for how well")
				print("you and your partner play together in your turn. If you play well together the opposing couple")
				print("will lose some confidence. The opposing couple then tries to break your confidence.")
				print("The first couple to lose all their confidence loses.")
				input("\nPress enter to commence!")
				
			playerFame = battle(playerPartner, playerFame, char)
			
			#remove enemy, place new one somewhere
			char.room = None
			playerRoom.chars.remove(char)
			activeCharacters.remove(char)
			enemyQueue.append(char)
			enemyQueue[0].room = globals()["path_" + str(random.randint(1, 18))]
			while enemyQueue[0].room == playerRoom: #if happens to be same room, change it
				enemyQueue[0].room = globals()["path_" + str(random.randint(1, 18))]
			enemyQueue[0].room.chars.append(enemyQueue[0])
			activeCharacters.append(enemyQueue.pop(0))	
	
	#player examines room (print items again)
	if keyWord == "look":
		print(playerRoom.lookDesc)
		if not playerRoom.items:
			pass
		else:
			for i in playerRoom.items:
				print(i.worldDesc)
		if not playerRoom.chars:
			pass
		else:
			for char in playerRoom.chars:
				print(char.desc)
	
	#player examines inventory
	if keyWord == "inventory":
		if not inventory:
			print("Nothing in inventory.")
		else:	
			for item in inventory:
				print(item.name)
	
	#player examines object
	if keyWord == "examine":
		if object in inventory or object in playerRoom.items:
			print(object.desc)
		elif object == "lever" and playerRoom == quest_7 and playerPartner != None:
			print("The lever is sturdy. You imagine you could push it.")
		elif (object == piano or object == "stage") and playerRoom == quest_3 and playerPartner != None:
			print("The stage is open, perhaps for you and " + playerPartner.fName + " to take the stage?")
		else:
			print("Could not find object.")
		
	#get help
	if keyWord == "help":
		printHelp()
	
	#view list of fame
	if keyWord == "view":
		if playerRoom == quest_10:
			for i in listOfFame:
				print(i)
		else:
			print("You are not in the right area to view the List of Fame.")
		
	#player tries to use item from inventory
	if keyWord == "use":
		#QUEST 1
		if object == CD1 or object == CD2 or object == CD3:
			if CD1 in inventory and CD2 in inventory and CD3 in inventory:
				if playerRoom == quest_1:
					playerFame += 10
					inventory.remove(CD1)
					inventory.remove(CD2)
					inventory.remove(CD3)
					print('You approach the MallMart manager and give him the three CD parts to your album.')
					print('"These are for you to play on your speakers," you tell him. He turns to you and recognizes')
					print('who you are. "Mr. Bondan!? I would be honoured to play your music here. Everyone at MallMart')
					print('should know about you two!"')
					print("You and " + playerPartner.fName + " gain 10 fame!")
					quest_1.desc = "You enter MallMart and marvel at the size. You imagine you could find anything in this place. \nYou can see multiple cashiers lined up serving customers. To exit, head South."
					quest_1.lookDesc = "Nothing else to see, here is the normal description.\n" + quest_1.desc
			else:
				print("You can't use the CD here. You may be missing something.")
		#QUEST 2
		elif object == painting1 or object == painting2 or object == painting3:
			if painting1 in inventory and painting2 in inventory and painting3 in inventory: 
				if playerRoom == quest_2:
					playerFame += 10
					inventory.remove(painting1)
					inventory.remove(painting2)
					inventory.remove(painting3)			
					print("You return the 3 lost paintings to the art gallery. For your work, \nthe art gallery adds a notice under the paintings, 'retrieved by Zack Bondan \nand " + playerPartner.fName + " " + playerPartner.lName + "'. You and " + playerPartner.fName + " gain 10 fame!")
					quest_2.desc = "The art gallery has many magnificent works, including the 3 that you retrieved. \n To exit the gallery, head South."
					quest_2.lookDesc = "Nothing else to see, here is the normal description.\n" + quest_2.desc
			else:
				print("You can't use the painting here. You may be missing something.")
		#QUEST 4
		elif object == tenants:
			if playerRoom == quest_4:
				playerFame += 10
				inventory.remove(tenants)
				print("You return the binder with tenants information to the head office.")
				print("The lady in the office is very thankful for yours and " + playerPartner.fName + "'s work.")
				print("You and " + playerPartner.fName + " gain 10 fame!")
				quest_4.lookDesc = "Nothing else to see, here is the normal description.\n" + quest_4.desc
			else:
				print("You can't use the binder here.")
		#QUEST 6
		elif object == tuner:
			if playerRoom == quest_6:
				playerFame += 10
				inventory.remove(tuner)
				print("You hop up on the stage with your beloved " + playerPartner.fName + ".")
				print("You push Burt aside and make quick work in tuning the piano.")
				print("It sounds as good as new! The crowd goes wild! Mandy and Burt eye you")
				print("and " + playerPartner.fName + " evilly. You and " + playerPartner.fName + " gain 10 fame!")
				quest_6.desc = "Mandy and Burt continue the concert as if nothing happened, but now \nthey have a happy crowd. To exit back to the parking lot, head North."
				quest_6.lookDesc = "Nothing else to see, here is the normal description.\n" + quest_6.desc
			else:
				print("You can't use the tuner here.")
		#QUEST 8
		elif object == gravy or object == fries or object == cheese:
			if gravy in inventory and fries in inventory and cheese in inventory:
				if playerRoom == quest_8:
					playerFame += 10
					inventory.remove(gravy)
					inventory.remove(fries)
					inventory.remove(cheese)	
					print("You provide gravy, fries, and cheese for the Poutine Queen to make more poutines today.")
					print("Immediately customers start walking in and recognizing yours and " + playerPartner.fName + "'s generosity.")
					print("You and " + playerPartner.fName + " gain 10 fame!")
					quest_8.desc = "Poutine Queen is packed with customers, all hungry for poutine! Head North to leave."
					quest_8.lookDesc = "Nothing else to see, here is the normal description.\n" + quest_8.desc
			else:
				print("You can't use that ingredient here. You may be missing something.")	
		#QUEST 9
		elif object == treats:
			if playerRoom == quest_9:
				playerFame += 10
				inventory.remove(treats)
				print("You throw some cat treats for the cat away from the button she was standing on.")
				print("The door to the room containing the scientists opens and they come tumbling out.")
				print("They sincerely thank you and " + playerPartner.fName + " for your help, then immediately get back to business.")
				print("You and " + playerPartner.fName + " gain 10 fame!")
				quest_9.desc = "Deep in the lab, a cat is sitting and licking her paws clean after a nice snack. \nTo exit back to the lab, Head East."
				quest_9.lookDesc = "Nothing else to see, here is the normal description.\n" + quest_9.desc
		else:
			print("Could not use item.")
		
				
				
	#player attempts to play (STAGE - QUEST 3, PIANO - QUEST 5)
	if keyWord == "play":
		#QUEST 3;
		if (object == piano or object == "stage") and playerRoom == quest_3 and not quest_3_complete and playerPartner != None:
			quest_3_complete = True
			playerFame += 10
			print("You hop up on the stage and begin playing the piano. You are joined by " + playerPartner.fName)
			print(playerPartner.quest_3_line + '. The pub loves your work as they expressed outwardly')
			print('shouting "You guys are great!" "Finally some atmosphere!" "Did not know there would be a party."')
			print("You and " + playerPartner.fName + " gain 10 fame!")
			quest_3.desc = "The pub is lively with people drinking, laughing and just enjoying themselves. \nOne performance was enough. To exit the pub, head South."
		#QUEST 5
		elif object == piano and piano in quest_5.items and playerRoom == quest_5:
			playerFame += 10
			quest_5.items.remove(piano)
			print("You play one of your sombre songs for the friendly inmate. " + playerPartner.fName + " wipes a tear from her eye.")
			print('"Wow, that was a great piece Zack. I know it might not mean much from me, but thanks a bunch,"')
			print("the man behind bars says. The guard no longer looks worried about you, in fact,")
			print("you hear him spreading the story through his walkie-talkie to his coworkers. The piano strangely breaks down.")
			print("You and " + playerPartner.fName + " gain 10 fame!")
			quest_5.desc = "You are outside many jail cells. Your fan behind bars is sleeping soundly. The guard smiles at you. \nTo head back to the police station, head West."
			quest_5.lookDesc = "You can't help but feel bad for the jailer. At least he has good taste in music."
		elif object == piano and piano in path_18.items and playerRoom == path_18:
			print("You have a feeling that playing the piano in this room will not do anything.")
		else:
			print("could not find what you wanted to play.")
				
	#player pushes piano from police station to jail cells (QUEST 5)
	if keyWord == "push" and object == piano and playerRoom == path_18 and piano in path_18.items:
		quest_5.items.append(piano)
		path_18.items.remove(piano)
		print("You pushed the piano into the room with the jail cells.")
		
	#push lever train room QUEST 7; 	
	if keyWord == "push" and object == "lever" and playerRoom == quest_7 and not quest_7_complete and playerPartner != None:
		quest_7_complete = True
		playerFame += 10
		print("You pushed the lever and the train started working. Everyone in the train station \nincluding the conductor looks at you happily. You and " + playerPartner.fName + " gain 10 fame!")
		quest_7.desc = "The train station is no longer crowded as the train is now moving. \nTo exit the train station, head North."
		quest_7.lookDesc = "Nothing else to see, here is the normal description.\n" + quest_7.desc
		
			
	#ENDGAME
	if playerFame > 49:
		print("\nYou and " + playerPartner.fName + " have triumphantly made it to the top of the List of Fame!")
		input("Press enter to continue.")
		if playerPartner == singer:
			print("When you hear the news about reaching the top of the List of Fame you tell Jen Tebra right away.")
			print("She excitedly jumps for joy then kisses you on the cheek.")
			print("You and Jen become sensations to the world, by creating your own genre of music and")
			print("spreading it called Classical Country. You play classical music pieces on your piano and")
			print("together you two make country lyrics for Jen to sing overtop.")
			print('"It\'s only up from here!" Jen tells you after another great concert.')
			print('"It sure is," you tell yourself in a whisper.')
			print("\nENDING 1")
		elif playerPartner == drummer:
			print("Tanya Zanders hears that you guys are the top couple, but she can't believe it.")
			print('"You know I was only in this for the money, right?" she says, but not with much assurance.')
			print('After you look at her sadly for a little bit she continues, "You\'re not like the other guys')
			print('I\'ve dated though. They were all rock artists, putting all their depression into their songs')
			print('until it got the better of them and they killed themselves. No, you\'re different. You put your')
			print('heart into your music. None of the stuff that drags you down. Ya know, you might not be a punk')
			print('after all." She walks over to you and lightly punches your shoulder. "Hey, c\'mon, we\'ve got a')
			print('crowd to please!" She finishes with a smile.')
			print("\nENDING 2")
		elif playerPartner == guitarist:
			print('Christina Eldriss runs over to you, shouting, "WE DID IT! WE DID IT!"')
			print('You give her a confused look. "We made it to the top of the list silly. We\'re superstars!"')
			print('She gently puts her guitar on the ground then grabs you by the waist and lifts you into the air.')
			print('After a short moment, she puts you back down. "Zack, show some spirit! Isn\'t this what you dreamed of?')
			print('Am I not enough or something?" You finally loosen up and crack a pearly white smile. "Of course it is!"')
			print('you say. You start hugging Christina tightly and she returns the feeling.')
			print('"I hope we can stay like this forever," Christina says with her head covered by your chest.')
			print('You caress her head gently. "Me too," you reply quietly. "Me too..."')
			print("\nENDING 3")
			
			
			
		closed_flag = True
			
			
			

	
	
	
	
	
	
	



