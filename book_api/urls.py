from django.urls import path
from book_api.views import BookCreate, BookList, BookDetail
from book_api.views import Pembeli, PembeliList, PembeliSerializer
from book_api.views import Pembelian, PembelianList, PembelianSerializer

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', BookDetail.as_view()),
    path('pembeli/', PembeliList.as_view(), name='pembeli-list'),
    path('pembelian/', PembelianList.as_view(), name='pembelian-list'),
]
