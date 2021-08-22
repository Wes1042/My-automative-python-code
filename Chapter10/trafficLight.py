# ns = nort to south      ew = east to west 
market_2nd= {'ns':'green', 'ew': 'red'}
mission_16th = {'ns':'red', 'ew': 'green'}

# TODO: creating a function that will change the color values
# this will loop continously since they will turn upon change
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key]== 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] == 'red'
        elif stoplight[key] == 'red':
            stoplight[key] == 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)


