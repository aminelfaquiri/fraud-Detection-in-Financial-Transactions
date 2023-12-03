import requests

def get_data_api(api_url) :

    try:
        # Make a GET request :
        response = requests.get(api_url)

        # Check if the request was successful :
        if response.status_code == 200:

            return response.json()

        else:
            # error message if the request was not successful :
            print(f"Error: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        print(f"Error: {e}")