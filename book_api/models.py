from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
    
class Pembeli(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.nama
    
class Pembelian(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='buku')
    pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE,related_name='pembelian_pembeli')
    jumlah = models.PositiveIntegerField()
    tanggal_beli = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.book