from django.views.generic import DetailView, ListView
from .models import Page, ContentCard
from .forms import PageFilterForm

class PageListView(ListView):
    model = ContentCard
    template_name = 'app2/page_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        form = PageFilterForm(self.request.GET)
        
        if form.is_valid():
            if form.cleaned_data['search']:
                queryset = queryset.filter(
                    title__icontains=form.cleaned_data['search']) | \
                    queryset.filter(description__icontains=form.cleaned_data['search'])
            
            if form.cleaned_data['sort_by']:
                queryset = queryset.order_by(form.cleaned_data['sort_by'])
        
        return queryset.select_related('page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PageFilterForm(self.request.GET)
        return context

class PageDetailView(DetailView):
    model = Page
    template_name = 'app2/page_detail.html'
    context_object_name = 'page'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.object
        
        if page.slug == 'program-management':
            context['supervisor'] = getattr(page, 'supervisor', None)
            context['managers'] = page.managers.all()
        elif page.slug == 'my-classmates':
            context['classmates'] = page.classmates.all()
        
        return context