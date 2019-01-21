import quickurl
import wordFilter
import wordFreqSort
import genFile

url = "http://www.wikipedia.com"
html1=quickurl.urlopen(url)
html2 = quickurl.grabtext(html1).lower()
del html1
filtered1 = wordFilter.filterStopWords(html2)
del html2
filtered2 = wordFilter.filterSpellCheckedWords(filtered1)
del filtered1
filtered3 = wordFilter.filterNonAlphaChars(filtered2)
del filtered2
filtered4 = wordFilter.filterSmallWords(filtered3)
del filtered3
dic1 = wordFreqSort.wordListToFreqDict(filtered4)
del filtered4
dic2 = wordFreqSort.sortFreqDict(dic1)
del dic1
f = genFile.genFile("sitewords.txt")
for s in dic2: genFile.writeFile(f, str(s)+'\n')
