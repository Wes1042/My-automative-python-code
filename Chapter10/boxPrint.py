def boxPrint(symbol, width, height):
    #Note : This will serve as a valid checker
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <=2:
        raise Exception('Height must be greater than 2.')
# this will loop it 
    print(symbol * width)

    for i in range(height -2 ):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol * width)

# the numbers we are using to calculate
for sym,w,h in (('*',4,4) ,('0',20,5), ('x',1,3), ('ZZ',3,3)):
    try:
        boxPrint(sym,w,h)           # we are calling the function
    except Exception as err:        # we are creting a blockage in the name of err
            print('An exception happened: ' + str(err))