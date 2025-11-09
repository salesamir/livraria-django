from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return self.descricao
        
class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()
    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    nome = models.CharField(max_length=255)    
    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32, blank=True) 
    """ 
    nao vou usar o: null=True pois é possivel que um livro nao tenha ISBN
    O null=true > Afeta o nível do banco de dados.
    Permite que o valor do campo seja NULL (ausência total de valor, não uma string).
    É útil para tipos numéricos, data/hora ou chave estrangeira, onde NULL tem um significado diferente de 0 ou "".
    Exemplo:
    Um DateField(null=True) indica que a data pode ser desconhecida.
    Um CharField(null=True) é tecnicamente possível, mas o Django recomenda usar apenas blank=True para texto.
    """
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')
    
    def __str__(self):
        return "%s (%s)" %(self.titulo, self.editora)    

class Compra(models.Model):
        class StatusCompra(models.IntegerChoices):
            CARRINHO = 1, 'Carrinho'
            REALIZADO = 2, 'Realizado'
            PAGO = 3, 'Pago'
            CANCELADA = 4, 'Entregue'
        user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='compras')
        status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    
class ItensCompra(models.Model):
        compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
        livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
        quantidade = models.IntegerField()
        