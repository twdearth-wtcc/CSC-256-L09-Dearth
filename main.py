import requests

url = 'https://duckduckgo.com/?q=presidents+of+the+united+states&format=json'


# Returns DuckDuckGo results for names of the US presidents
def get_pres_names():
    response = requests.get(url)
    resp_json = response.json()
    related_results = []
    for topic in resp_json['RelatedTopics']:
        related_results.append(topic['Text'])
    return related_results


# Runs the main script
if __name__ == '__main__':
    names = get_pres_names()
    # print(type(names[0]))
    for pres_name in names:
        print(pres_name.find("Abraham Lincoln"), pres_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
