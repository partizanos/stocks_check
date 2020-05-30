from django.shortcuts import render

# Create your views here.

import json
import requests
def get_price(product = 'IBM'):
      data_r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ product +'&interval=5min&apikey=demo')
      data_json = data_r.json()
      return data_json

from django.http import HttpResponse, Http404

def home(request):
    
    return HttpResponse("""
       

       <button type="button" class="btn">Click me!</button>
        <p class="text">Replace me!!</p>
        <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script>
        $('.btn').click(function() {
          
          $('.text').text('loading . . .');
          
          $.ajax({
            type:"GET",
            url:"https://api.meetup.com/2/cities",
            success: function(data) {
              $('.text').text(JSON.stringify(data));
            },
            dataType: 'jsonp',
          });
          
        });
        </script>
    """)

def view_article(request, id_product):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    # if id_article > 100:
    #     raise Http404
    json_response = get_price(product = 'IBM')
    return HttpResponse('<h1>Mon product ici</h1>' +json.dumps(json_response) )

def ModelViewSet(request):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'article n° {0} !".format(id_article)    
    )