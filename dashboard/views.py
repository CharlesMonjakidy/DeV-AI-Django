from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .ml import predict
from .models import Analysis
from accounts.models import Profile
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    if not request.user.is_authenticated:
        return render(request, "landing.html")
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if profile.status != "approved" and not request.user.is_staff:
        return render(request, "pending.html", {"profile": profile})
    data = pd.read_csv(BASE_DIR / "data" / "etudiants.csv")
    last = Analysis.objects.filter(user=request.user).first()
    context = {
        "nombre_etudiants": len(data),
        "moyenne_note": round(data["note_precedente"].mean(), 1),
        "moyenne_revision": round(data["heures_revision"].mean(), 1),
        "last": last,
    }
    return render(request, "index.html", context)

@login_required
def predire(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if profile.status != "approved" and not request.user.is_staff:
        messages.warning(request, "Ton compte doit être approuvé avant d'utiliser l'analyse IA.")
        return redirect("home")
    if request.method != "POST":
        return redirect("home")
    try:
        vals = {
            "heures_revision": float(request.POST["heures_revision"]),
            "exercices": float(request.POST["exercices"]),
            "absence": float(request.POST["absence"]),
            "note_precedente": float(request.POST["note_precedente"]),
        }
    except (KeyError, ValueError):
        messages.error(request, "Vérifie les valeurs saisies.")
        return redirect("home")

    result = predict(**vals)
    if result == 1:
        resultat = "Profil favorable"
        conseil = "Continue tes révisions et garde une bonne régularité."
    else:
        resultat = "Attention"
        conseil = "Augmente progressivement ton temps de révision et pratique davantage."

    Analysis.objects.create(user=request.user, resultat=resultat, conseil=conseil, **vals)
    return render(request, "result.html", {"resultat": resultat, "conseil": conseil, **vals})

def installation(request):
    return render(request, "installation.html")
