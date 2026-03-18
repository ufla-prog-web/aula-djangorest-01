from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cliente, Produto
from .serializers import ClienteSerializer, ProdutoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """
    # API de Clientes

    Esta API permite gerenciar clientes cadastrados no sistema.

    ## Operações disponíveis

    - **GET /clientes/** → lista todos os clientes
    - **POST /clientes/** → cria um novo cliente
    - **GET /clientes/{id}/** → retorna um cliente específico
    - **PUT /clientes/{id}/** → atualiza um cliente
    - **DELETE /clientes/{id}/** → remove um cliente

    ## Exemplo de JSON

    ```json
    {
        "nome": "João",
        "endereco": "Rua A, 123",
        "idade": 30
    }
    ```
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['idade']

    #filter_backends = [filters.SearchFilter]
    #search_fields = ['nome', 'idade']

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer