from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from purpustakaan.models import Buku
from purpustakaan.forms import FormBuku

# Create your views here.
def signup(req):
    if(req.POST):
        form = UserCreationForm(req.POST)
        if(form.is_valid()):
            form.save()
            messages.success(req, "User berhasil di buat")
            return redirect('signup')
        else:
            messages.error(req, "Terjadi kesalahan")
            return redirect('signup')
    else:
        form = UserCreationForm()
        kontext = {
            'form': form
        }
        return render(req, 'signup.html', kontext)

@login_required(login_url=settings.LOGIN_URL)
def hapusBuku(req, idBuku):
    buku = Buku.objects.filter(id = idBuku)
    buku.delete()
    messages.success(req, "Data berhasil untuk di hapus")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def ubahBuku(req, idBuku):
    buku = Buku.objects.get(id = idBuku)
    template = 'ubah-buku.html'
    if req.POST:
        formData = FormBuku(req.POST, req.FILES,instance=buku)
        if formData.is_valid():
            formData.save()
            messages.success(req, "data berhasil diperbarui")
            return redirect('ubah_buku', idBuku = idBuku)
    else:
        formData = FormBuku(instance=buku)
        kontext = {
            'formBuku': formData,
            'buku': buku,
        }
    return render(req, template, kontext)

@login_required(login_url=settings.LOGIN_URL)
def buku(req):
    buku = Buku.objects.all()

    konteks = {
        'bukuBanyak': buku
    }

    return render(req, 'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(req):
    return render(req, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambahBuku(req):
    if req.POST:
        formData = FormBuku(req.POST, req.FILES)
        if formData.is_valid():
            formData.save()
            formData = FormBuku()
            pesan = "Data berhasil di simpan"

            kontext = {
                'formBuku': formData,
                'pesan': pesan
            }
            return render(req, 'tambah-buku.html', kontext)
    else:
        form = FormBuku()
        kontext = {
            'formBuku': form
        }

    return render(req, 'tambah-buku.html', kontext)