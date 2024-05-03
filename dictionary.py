import requests

def get_word_definition(word, api_key):
    url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]['shortdef']
        else:
            return ['No definition found.']
    else:
        return ['Failed to retrieve definition.']

def main():
    api_key = '6f88d673-a0c5-46cd-aabc-01d1fb8aecb0'
    word = input("Enter a word to get its definition: ")
    definitions = get_word_definition(word, api_key)
    for definition in definitions:
        print(definition)

if __name__ == "__main__":
    main()