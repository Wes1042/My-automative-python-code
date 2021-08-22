#An assertion is a sanity check to make sure your code isn’t doing something obviously wrong.

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open' , 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I cant do that.'
assert podBayDoorStatus == 'open' , 'The pod bay dorrs need to be "open".'
#In plain English, an assert statement says, “I assert that this condition holds
#true, and if not, there is a bug somewhere in the program.