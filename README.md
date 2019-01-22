# Word-Analyzer
### written using Python 3.7
## Goal: 
1. Cross Check two files for english text
2. Sort Words found by frequency
3. Filter out the stopwords (For example: a, and, or, but, so)
4. Filter out words less than 3 letters.
5. Output Top 50-100 common english words between the two documents to a new file
6. Use output to generate graphs and visuals
7. Autosearch web for word definition
8. Pair words with their definitions
9. Sort Words and definitions alphabetically
10. Autogenerate a glossary with the word definitions to a new html file


## Todo:
- [x] scan html for english words
- [x] create ordered word frequency list 
- [x] Filtering stopwords

- [ ] Add functions to scan .pdf files and other doctypes
- [ ] Build gui for file/url input
- [ ] Automatically Search web for word definitions
- [ ] pairing words with definition
- [ ] sorting words alphabetically
- [ ] Generate glossery in html with helpful linking 

## How to run:
  1. Install the dependencies:
  
    1. Beautiful Soup 4
    2. nltk
    3. urllib
    
  2. Try running the example file
    1. May need to uncomment the nltk download lines
    2.  python3 test.py
