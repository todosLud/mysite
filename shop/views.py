from .models import Categorie, Prodotti
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm

# Create your views here.

def lista_prodotti(request, categoria_slug=None):
    categoria = None
    categorie = Categorie.objects.all()
    prodotti = Prodotti.objects.filter(pubblicato=True)
    #Se viene passata uno slug di categoria facio i filtri
    if categoria_slug:
        categoria = get_object_or_404(Categorie, slug=categoria_slug)
        prodotti = Prodotti.objects.filter(categoria=categoria).filter(pubblicato=True)
        
    return render(request,'shop/lista_prodotti.html', {'categorie':categorie, 'prodotti':prodotti, 'categoria':categoria})



def dettaglio_prodotto(request, id, slug):
    prodotto = get_object_or_404(Prodotti, id=id, slug=slug, pubblicato=True) 
    prodotti_correlati = Prodotti.objects.filter(categoria=prodotto.categoria).filter(pubblicato=True).exclude(id=prodotto.id)
    cart_prodotto_form = CartAddProductForm()
    return render(request, 'shop/dettaglio_prodotto.html', {'prodotto': prodotto, 
                                                            'prodotti_correlati':prodotti_correlati, 
                                                            'cart_prodotto_form':cart_prodotto_form,
                                                            'max_buy': range(1,prodotto.quantita+1)})