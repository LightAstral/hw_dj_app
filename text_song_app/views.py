from django.shortcuts import render

# Create your views here.

from django.utils.translation import activate, gettext_lazy as _


def default_text_song(request):
    text_of_song = _("We are the champions, my friends. And we'll keep on fighting till the end...\n"
                     "Queen, We are the champions")
    return render(request, "text_song_app/text_song.html", {'text_of_song': text_of_song})


def text_song_language(request, language):
    activate(language)

    if language == 'fr':
        text_of_song = _("Nous sommes les champions, mes amis. Et nous continuerons à nous battre jusqu'à la fin...\n"
                         "Queen, We are the champions")
    elif language == 'de':
        text_of_song = _("Wir sind die Champions, meine Freunde. Und wir werden bis zum Ende kämpfen...\n"
                         "Queen, We are the champions")
    elif language == 'es':
        text_of_song = _("Somos los campeones, mis amigos. Y seguiremos luchando hasta el final...\n"
                         "Queen, We are the champions")
    else:
        text_of_song = _("We are the champions, my friends. And we'll keep on fighting till the end...\n"
                         "Queen, We are the champions")

    return render(request, "text_song_app/text_song.html", {'text_of_song': text_of_song})
