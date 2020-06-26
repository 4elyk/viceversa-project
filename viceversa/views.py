from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	rev_text = request.GET['usertext']
	words = 1
	for i in range(0,len(rev_text)-1):
		if rev_text[i] == " ":
			words =words +1
		print(words)
	reversed_text = rev_text[::-1]
	return render(request, 'reverse.html', {'usertext':rev_text, 'reversedtext':reversed_text, 'sum_words':words})