from django.shortcuts import render
from PyDictionary import PyDictionary



def homeView(request):
    return render(request, 'dictionary/index.html')

def searchView(request):
    word = request.GET.get('search')
    dictionary = PyDictionary()
    meanings = dictionary.meaning(word)
    context = {
            'word': word,
            'meanings':meanings,
        }
    return render(request, 'dictionary/search.html', context)


