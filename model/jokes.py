import random

joke_list = [
    "What day is it today? Friday.",
    "You should go touch grass.",
    "Guess what?",
    "今天是星期五！！！",
    "Chicken Butt.",
    "You should love yourself NOW.",
    "Your life has ALL PURPOSE.",
    "🐥",
    "🐧",
    "Gabriel Zebra One?",
    "Sunroof..."
]
# Return all jokes from jokes_data
def getJokes():
    return(joke_list)

# Joke getter
def getJoke(id):
    return(joke_list[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(joke_list))
# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(joke_list)

# Test Joke Model
if __name__ == "__main__": 
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))