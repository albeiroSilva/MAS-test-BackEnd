import requests
import json
BASE_API = 'http://masglobaltestapi.azurewebsites.net/api/'
def get_empoyees():
    #curl -X GET --header 'Accept: application/json' 'http://masglobaltestapi.azurewebsites.net/api/Employees'
    end_point = BASE_API+'Employees'
    response = requests.get(end_point)

    response = json.loads(response.text)
    print(response)

    
    

get_empoyees()


