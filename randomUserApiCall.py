import requests

# Make a GET request to the Random User API
response = requests.get('https://randomuser.me/api/', verify=False)

good = 200 
if response.status_code == good:
    # Parse the JSON response to extract the user data
    user_data = response.json()


    print(user_data)
else:
    # The request failed
    print('Error: {}'.format(response.status_code))