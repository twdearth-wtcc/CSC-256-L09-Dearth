import requests

url = 'https://duckduckgo.com/?q=presidents+of+the+united+states&format=json'


# Returns DuckDuckGo results related to the search "presidents of the united
#   states"
def get_pres_names():
    response = requests.get(url)
    resp_json = response.json()
    related_results = []
    for topic in resp_json['RelatedTopics']:
        related_results.append(topic['Text'])
    return related_results


# Runs get_pres_names(), returns search results
if __name__ == '__main__':
    results = get_pres_names()
    for result in results:
        print(result)
