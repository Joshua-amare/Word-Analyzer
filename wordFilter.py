def filterStopWords(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    return [w for w in word_tokens if not w in stop_words]

def filterSpellCheckedWords(text):
    #import enchant
    import nltk
    from nltk.corpus import wordnet
    nltk.download('wordnet')
    #d = enchant.Dict("en_US")
    return [w for w in text if wordnet.synsets(w)]
def filterSmallWords(text):
    return [w for w in text if len(w)>3]
def filterNonAlphaChars(text):
    import re
    return re.compile(r'[^a-zA-Z]+',re.UNICODE).split(str(text))
