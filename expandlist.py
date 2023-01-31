
import requests
from bs4 import BeautifulSoup


def expandlist(list_input):
    # Initialize a 2-dimensional list
    two_dee: list_input[list_input[str]] = []

    # Create a 2-dimensional list where each sublist contains one item from the input list
    for j in range(len(list_input)):
        two_dee.append([list_input[j]])

    # For each item in the input list, retrieve synonyms from thesaurus.com and add to the 2-dimensional list
    for i in range(len(list_input)):
        # Set the word we want to get synonyms for
        word = two_dee[i][0]

        # Make a request to thesaurus.com
        url = f"https://www.thesaurus.com/browse/{word}"
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the element that contains the synonyms
        synonyms_element = soup.find("ul", {"class": "e1ccqdb60"})

        # Get the synonyms from the element
        synonyms = synonyms_element.text.split(", ")

        # Split the synonyms string into a list
        synonyms = synonyms[0].split()

        # add the synonyms to the two dimensional list
        for j in range(len(synonyms)):
            two_dee[i].append( synonyms[j])

    # Initialize a list to store the expanded list of words
    biglist = list_input.copy()

    # Counter variables to keep track of the current position in the 2-dimensional list
    i = 0
    j = 1

    # Expand the list by adding synonyms to it
    while len(biglist) < 1000:
        if j >= len(two_dee[i]):
            i += 1
            j = 1
        if i >= len(two_dee):
            break
        biglist.append(two_dee[i][j])
        j += 1

    # Remove duplicates from the list
    bigset = set(biglist)
    biglist = list(bigset)

    return biglist

# User input loop to get a list of words
list_input = []
a = 'null'
while(a != 'stop'):
    a = input('give me a word or tell me to stop')
    list_input.append(a)
    print(list_input)

# Call the function to get the expanded list of words
print(expandlist(list_input))
