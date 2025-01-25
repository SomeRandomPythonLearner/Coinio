import sys
import random
import time
coins = 10
print("Welcome to Coinio, a crypto currency that was created for fun. please do not close this window/tab as your progress will not be saved. You will start with 10 coins. Type 'view' to see how much coin you have, type mine to try and mine. 100 mines cost 1 coin as it is based on probability. If you run out of coin, you can still mine, but if your coins go negative, the proggrame will stop, forcing you to restart. Or just close and reopen this tab/window to restart manually. You can NOT trade coins for real money, please treat this just as a game, no real money is involved. The mining is done by picking 3 random numbers between 0 and 10, and if they all match, you get a coin. Please use responsibly, and remember NO REAL MONEY IS OR SHOULD BE INVOLVED")
while True:
	action = input()
	if action == "view":
		print(coins, "coins")
	elif action == "mine":
		n = int(input("How many minings do you want to do (make sure you type in a positive integer)? "))
		spent = n/100
		print("That will be", spent, "coins. Type proceed to proceed")
		proceed = input() 
		if proceed == "proceed":
				coins -= spent
				i = n
				gained = 0
				while i > 0:
					a = random.randint(0,10)
					b = random.randint(0,10)
					c = random.randint(0,10)
					if a == b and b == c:
						coins += 1
						gained += 1
					i -= 1
				print("mining...")
				time.sleep(spent+2)
				if coins < 0:
					sys.exit("You went Bankrupt! Close and reopen this tab to start again.")
				print("You spent", spent, "coins and gained", gained, "coins. Overall, your total profit was", gained - spent, "coins.")
