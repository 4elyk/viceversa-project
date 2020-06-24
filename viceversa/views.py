from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	rev_text = request.GET['usertext']
	reversed_text = rev_text[::-1]
	return render(request, 'reverse.html', {'usertext':rev_text, 'reversedtext':reversed_text})