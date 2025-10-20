from django.shortcuts import render, redirect
from .models import PYQ
from .forms import PYQUploadForm
from django.contrib.auth.decorators import login_required

def home(request):
    q = request.GET.get('q', '')
    pyqs = PYQ.objects.all().order_by('-created_at')
    if q:
        pyqs = pyqs.filter(subject__icontains=q) | pyqs.filter(title__icontains=q)
    return render(request, 'pyq/home.html', {'pyqs': pyqs, 'q': q})

@login_required
def upload_pyq(request):
    if request.method == 'POST':
        form = PYQUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pyq = form.save(commit=False)
            pyq.uploaded_by = request.user
            pyq.save()
            return redirect('home')
    else:
        form = PYQUploadForm()
    return render(request, 'pyq/upload.html', {'form': form})