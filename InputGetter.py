import requests
 

def GetInput(day):
    url = 'https://adventofcode.com/2019/day/' + str(day) + '/input'
    print("Loading input from AoC: " + url)

    f = open("sessioncookie.txt", "r")
    aocsession = {'session' : f.read().splitlines()[0]}
    f.close()    
    
    response = requests.get(url, cookies = aocsession)
    if response.status_code == 200:
        input = response.text.split('\n')
        input.pop()

        return input
    else:
        print("Web request failed! Check if session cookie is valid")
        print(response.status_code)
        print(response.text)

        return ""
    