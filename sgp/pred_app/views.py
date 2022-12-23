from django.shortcuts import render, redirect
from pred_app.lstm_prediction import *

# --------------- MAIN WEB PAGES -----------------------------
def redirect_root(request):
    return redirect('/pred_app/index')

def index(request):
	return render(request, 'pred_app/index.html') 

def pred(request):
    return render(request, 'pred_app/prediction.html')

def contact(request):
	return render(request, 'pred_app/contact.html')

def news(request):
	import requests
	import json
	
	# News API
	api_request = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=28dfc0e50f654c6fa419f53fc41cde2d')
	
	# BASIC - Stock News API
	#api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=general&items=50&token=</your_api_key>')
	
	# PREMIUM - Stock News API
	#api_request = requests.get('https://stocknewsapi.com/api/v1/category?section=alltickers&items=50&token=</your_api_key>')
	api = json.loads(api_request.content)
	#return render(request, 'news.html', {'api': api})
	return render(request, 'pred_app/news.html',{'api': api} )

def search(request, se, stock_symbol):
	import json
	predicted_result_df = lstm_prediction(se, stock_symbol)
	return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df})
# -----------------------------------------------------------