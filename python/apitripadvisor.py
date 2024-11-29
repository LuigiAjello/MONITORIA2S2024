import requests

url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchLocation"

querystring = {"query":"brasilia"}

headers = {
	"x-rapidapi-key": "1f0d9fbb8dmsh2c8d877ff0ec528p191bdajsn22efae3037d4",
	"x-rapidapi-host": "tripadvisor16.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response.json()["data"]