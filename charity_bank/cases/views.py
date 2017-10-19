from django.views.generic import DetailView, ListView, TemplateView

from .models import Case, GalleryItem, ContentItem


class CaseDetailView(DetailView):

    model = Case
    slug_field = 'id'

    def get_content_item_gallery(self, content_item):
        gallery = GalleryItem.objects.filter(content_item=content_item)
        return gallery

    def get_content_items(self, case):
        qs = ContentItem.objects.filter(case=case)

        [setattr(i, 'gallery', self.get_content_item_gallery(i)) for i in qs]
        # for i, item in enumerate(qs):
        #     #content_items[item] = self.get_content_item_gallery(item)
        #     content_items[i] = item
        # print(content_items)
        # return content_items
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_items'] = self.get_content_items(case=self.object)
        return context


class CaseListView(ListView):

    model = Case
    slug_field = 'id'
    context_object_name = 'case_list'

    def get_context_data(self, **kwargs):
        context = super(CaseListView, self).get_context_data(**kwargs)
        # Get all case list of a fund or All case list
        return context



