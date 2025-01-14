#from rest_framework import serializers
#from book_api.models import Book

#class Bookserializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    title = serializers.CharField()
#    number_of_pages = serializers.IntegerField()
#    publish_date = serializers.DateField()
#    quantity = serializers.IntegerField()

#    def create(self, data):
#        return Book.objects.create(**data)
    
#    def update(self, instance, data):
#        instance.title = data.get('title', instance.title)
#        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
#        instance.publish_date = data.get('publish_date', instance.publish_date)
#        instance.quantity = data.get('quantity', instance.quantity)

#        instance.save()
#        return instance



from rest_framework import serializers
from book_api.models import Book
from .models import Pembeli
from .models import Pembelian
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("No diet coke please")
        return value
    
    def validate(self, data):
        if data["number_of_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("Kalau ga boleh jangan maksa ")
        return data
    

    def get_description(self, data):
        return "buku ini berjudul " + data.title + " dan " + str(data.number_of_pages) + " halaman. "
    
class PembeliSerializer(serializers.ModelSerializer):
    pembelian_pembeli = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pembelian-detail'
    )
    class Meta:
        model = Pembeli
        fields = ["id", "nama", "alamat", "email", 'pembelian_pembeli']

class PembelianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembelian
        fields = ["id", "book", "pembeli", "jumlah", "tanggal_beli"]