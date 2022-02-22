from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
en_label_dict = {
        "lang" : "English", "title" : "Dashboard"
}

fn_label_dict = {
    "lang" : "Finnish", "title" : "Kojelauta"
}


def setLang(request):
    if request.COOKIES.get('language'):
        lang = request.COOKIES['language']
    else:
        lang = "en"

    if lang == "fn":
        label_dict = fn_label_dict
    else:
        label_dict = en_label_dict
    return label_dict

@login_required
def dashboard(request):
    label_dict = setLang(request)
    return render(request, 'rootapp\dashboard.html', {"label" : label_dict})