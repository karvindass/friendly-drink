# friendly-drink
We all want a friendly drink

## Requirements to compile and run
- Make sure to run using Python 2
- Make sure to install NLTK packages
    - Not needed yet, but will at some point soon
- Install RDFLib
    - `pip install rdflib` (use `sudo` if needed)

# Python File Goals:
* To achieve:
    1. Toss a coin
        * "heads or tails" as possible input
    2. NLTK to get information about learning a concept
        * Find appropriate YouTube video/Wikipedia page
        * "I want to learn about integration"
    3. Do NLTK on page to get information from Wikipedia page
        * E.g. DOB, gender
        * "What is the DOB of Kanye West?""

# Accepted Commands:
`Time in` + "Name of Major City"
* Looks up time in city

`flip` [or synonyms] + `coin` (order insignificant)
* Flips a coin for the user, returning the result and a corresponding ASCII image

# References
[Parts of Speech (POS) Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) - Used for NLTK
