from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Resident, Blotter, Certificate
from .forms import ResidentForm, BlotterForm, CertificateForm

# LOGIN
def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# =========================
# RESIDENT MANAGEMENT
# =========================
@login_required
def resident_list(request):
    residents = Resident.objects.all()
    return render(request, 'residents/list.html', {'residents': residents})


@login_required
def add_resident(request):
    form = ResidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resident_list')
    return render(request, 'residents/form.html', {'form': form})


# =========================
# BLOTTER MANAGEMENT
# =========================
@login_required
def blotter_list(request):
    blotters = Blotter.objects.all()
    return render(request, 'blotter/list.html', {'blotters': blotters})


@login_required
def add_blotter(request):
    form = BlotterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blotter_list')
    return render(request, 'blotter/form.html', {'form': form})


# =========================
# CERTIFICATE ISSUANCE
# =========================
@login_required
def issue_certificate(request):
    form = CertificateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'certificates/form.html', {'form': form})


# =========================
# REPORTS
# =========================
@login_required
def reports(request):
    residents = Resident.objects.count()
    blotters = Blotter.objects.count()
    return render(request, 'reports/report.html', {
        'residents': residents,
        'blotters': blotters
    })


# =========================
# SYSTEM SETTINGS
# =========================
@login_required
def settings(request):
    return render(request, 'settings/settings.html')