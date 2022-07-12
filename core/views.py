from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView

from .models import Anel
from carrinho.models import Carrinho , CarrinhoAneis

# Class based View
class IndexView(TemplateView):
    template_name: str = 'index.html'


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['aneis'] = Anel.objects.all()
        return context


class AneisDetailView(DetailView):
    template_name: str = 'aneis.html'

    queryset = Anel.objects.all()


    def get_object(self):
        obj = super().get_object()
        return obj



    def post(self, request, *args, **kwargs):
        postData = request.POST
        print(postData)
        carrinho_id =  Carrinho.objects.get(id=5)        # postData.get('carrinho_id')
        print(carrinho_id)
        anel_id = Anel.objects.get(id=(postData.get('anel_id')))
        print(anel_id)
        quantidade = postData.get('quantidade')

        carrinho_anel = CarrinhoAneis(carrinho_id=carrinho_id,
                            anel_id=anel_id,
                            quantidade=quantidade)
        
        print(carrinho_anel.anel_id)

        carrinho_anel.register()
        return redirect('/')




#  carrinho_anel = CarrinhoAneis(5, carrinho.id, anel.id, quantidade=3)


"""
'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
  '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 
  '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', 
  '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together',
   '_check_indexes', '_check_local_fields', '_check_long_column_names',
    '_check_m2m_through_same_relationship', '_check_managers', '_check_model',
     '_check_model_name_db_lookup_clashes', '_check_ordering', 
     '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key',
      '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display',
       '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', 
       '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks',
        '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 
        'anel_id', 'anel_id_id', 'carrinho_id', 'carrinho_id_id', 'check', 'clean', 'clean_fields',
         'date_error_message', 'delete', 'from_db', 'full_clean', 'get_deferred_fields', 'id',
          'objects', 'pk', 'prepare_database_save', 'quantidade', 'refresh_from_db', 'register', 
          'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_unique']

"""