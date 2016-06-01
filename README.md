# friendly-drink
We all want a friendly drink

## Requirements to compile and run
- Make sure to run using Python 2
- Make sure to install NLTK packages
    - Not needed yet, but will at some point soon
- Install RDFLib
    - `pip install rdflib` (use `sudo` if needed)
- Install Wikipedia (Github repo used for Wikipedia interfacing)
    - `pip install wikipedia` (use `sudo` if needed)

# Python File Goals:
* To achieve:
    1. Alternate entries
        * Asking for time
        * Asking birthday
    1. Intelligent suggestions
        * For page names
            * e.g. `Barack Obama` from `brack Obama`
        * For resource names
            * e.g. `dbo:headquarter` from `headquarters`
            * LATER `dbo:parent` from `parent company`
    1. NLTK to get information about learning a concept
        * Find appropriate YouTube video/Wikipedia page
        * "I want to learn about integration"
    2. Do NLTK on page to get information from Wikipedia page
        * E.g. DOB, gender
        * "What is the DOB of Kanye West?""

# Accepted Commands:
`Time in` + "Name of Major City"
* Looks up time in city

`flip` [or synonyms] + `coin` (order insignificant)
* Alternately, `heads or tails` or `tails or heads` can be used
* Flips a coin for the user, returning the result and a corresponding ASCII image

`when was` + `<firstName>` + `<secondName>` + `born` + (optional) `?`
* Searches wikipedia for birthdate of queried individual


# References
[Parts of Speech (POS) Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) - Used for NLTK
