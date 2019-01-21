def wordListToFreqDict(wordlist):
    wordfreq=[wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))

def sortFreqDict(freqdict):
    aux=[(freqdict[key],key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
