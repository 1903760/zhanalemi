from django.views import generic
from .models import Photo, Album


class IndexView(generic.ListView):
    template_name = 'albome/index.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.all().order_by('date')[:8]
        return context

# def split_subcategories(qs):
#     b = int(len(qs) / 8)
#     c = 0
#     res = []
#     while b >= 0:
#         res.append(qs[c:(c + 8)])
#         b -= 1
#         c += 8m
#     return res


class ProView(generic.ListView):
    template_name = 'albome/detail.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super(ProView, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.all()
        return context


# .order_by('album__year_id')