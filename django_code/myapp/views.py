from django.shortcuts import render

# Create your views here.
API_KEY='BJYMCEG40R2V26VL'
import json
import requests
def get_price(product = 'IBM'):
      data_r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ product +'&interval=5min&apikey='+API_KEY)
      data_json = data_r.json()
      return data_json

def get_symbol(SYMBOL_SEARCH='AS'):
  data_r = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + SYMBOL_SEARCH +'&apikey=BJYMCEG40R2V26VL')
  data_json = data_r.json()
  return data_json

from django.http import HttpResponse, Http404, JsonResponse

def home(request):
    return HttpResponse("""
       

       <button type="button" class="btn">search!</button>
        <p class="text">Replace me!!</p>
        <input id="input"/>
        <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script>
        $('.btn').click(function() {
          
          $('.text').text('loading . . .');
          fetch("/search_stocks/"+document.querySelector('#input').value)
          .then(response => response.json())
          .then(data => $('.text').text(JSON.stringify(data)));
          /*
          # $.ajax({
          #   type:"GET",
          #   url:"/search_stocks/"+document.querySelector('#input').value,
          #   success: function(data) {
          #     $('.text').text(JSON.stringify(data));
          #   },
          #   dataType: 'jsonp',
          # });
          */
          
        });
        </script>
    """)

def view_article(request, id_product):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    # if id_article > 100:
    #     raise Http404
    
    json_response = get_price(product = id_product)
    
    return HttpResponse('<h1>Mon product ici</h1>' +json.dumps(json_response) )
    
import time
def search_stocks(request, queue_word):
    json_response = get_symbol(
      SYMBOL_SEARCH=queue_word)
    print(search_stocks)
    print(time.ctime())
    return JsonResponse(json_response)

def ModelViewSet(request):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )