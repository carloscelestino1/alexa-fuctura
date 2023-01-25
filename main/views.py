from django.shortcuts import render, get_object_or_404, redirect
from .models import Agenda
from .forms import EventoForm
from django.contrib import messages
from django.core.paginator import Paginator
from  django.contrib.auth.decorators import login_required
import datetime
#api
from rest_framework import viewsets
from .serializers import EventoSerializer


@login_required
def eventoList(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    eventosDoneRecently = Agenda.objects.filter(updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    eventosDoing = Agenda.objects.filter(user=request.user).count()
    
    


    eventos_list = Agenda.objects.all().order_by('-created_at')
    paginator = Paginator(eventos_list, 5)

    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    
    return render(request, 'main/list.html', 
        {'eventos':tasks, 'eventosrecently': eventosDoneRecently,  'eventosdoing': eventosDoing })

@login_required
def eventoView(request, id):
    evento = get_object_or_404(Agenda, pk=id)
    return render(request, 'main/evento.html', {'evento': evento})

@login_required
def newEvento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            evento.save()
            return redirect('/')
    else:
        form = EventoForm()
    return render(request, 'main/add_evento.html', {'form': form})

@login_required
def editEvento(request, id):
    evento = get_object_or_404(Agenda, pk=id)
    form = EventoForm(instance=evento)

    if(request.method == 'POST'):
        form = EventoForm(request.POST, instance=evento)

        if(form.is_valid()):
            evento.save()
            return redirect('/')
        else:
            return render(request, 'main/edit_evento.html', {'form': form, 'evento': evento})
    else:
        return render(request, 'main/edit_evento.html', {'form': form, 'evento': evento})

@login_required
def deleteEvento(request, id):
    evento = get_object_or_404(Agenda, pk=id)
    evento.delete()
    messages.info(request,'evento deletado com sucesso.')
    return redirect('/')



#api

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = EventoSerializer