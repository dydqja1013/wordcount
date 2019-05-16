from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    sorted_dictionary = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)
    dic_max = max(sorted_dictionary,key=lambda x: x[1])
    dic_max = dic_max[1]

    return render(request, 'result.html',{'full':text, 'total' : len(words),'dic_max' :dic_max,'dictionary' :sorted_dictionary})
    