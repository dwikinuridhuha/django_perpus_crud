from django.contrib import admin
from purpustakaan.models import Buku, Kelompok

# Register your models here.
class BukuAmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis', 'penerbit', 'kelompok_id', 'jumlah']
    search_fields = ['judul', 'penulis', 'penerbit']
    list_filter = ['kelompok_id']
    list_per_page = 4

admin.site.register(Buku, BukuAmin)
admin.site.register(Kelompok)

