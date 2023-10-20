import requests


your_name = input("Please enter your name: ")



# Make a GET request to the Random User API
response = requests.get(f'http://127.0.0.1:5000/hello/{your_name}', verify=False)

good = 200 
if response.status_code == good:
    # Parse the JSON response to extract the user data
    greet = response.json()


    print(greet['message'])
else:
    # The request failed
    print('Error: {}'.format(response.status_code))