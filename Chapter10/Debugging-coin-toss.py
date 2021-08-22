import random, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of program')
guess = ''

#logging.info('The program is not working %s' % (guess))

while guess not in ('heads', 'tails'):
    logging.info('The program is working %s' % (guess))
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.info('Start of the coin toss')
toss = random.randint(0,1) # 0 is tails and 1 is heards
print(toss)

if toss == 0 :
    toss = 'tails'
    print(toss)
if toss == 1:
    toss = 'heads'
    
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
if toss == guess:
    print('You got it!')
else:
    print('Nope. You are really bad at this game.')