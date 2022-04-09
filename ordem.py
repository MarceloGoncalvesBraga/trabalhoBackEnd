from noticia import Noticia

def bubbleSort(lista_noticia):
    algumAlterado = True
    while algumAlterado:
        algumAlterado = False
        nova_lista = []
        noticia_anterior = None
        for noticia in lista_noticia:
            if not noticia_anterior:
                print('Sem notícia anterior!')
                noticia_anterior = noticia
                nova_lista.append(noticia)
                continue
            elif noticia.get_likes() < noticia_anterior.get_likes():
                print(f'{noticia.get_titulo} < {noticia_anterior.get_titulo}')
                algumAlterado = True
                nova_lista.pop()
                nova_lista.append(noticia)
                nova_lista.append(noticia_anterior)
            else:
                print(f'Adicionando a notícia {noticia.get_titulo}')
                nova_lista.append(noticia)
            noticia_anterior = noticia
        lista_noticia = nova_lista
    return lista_noticia
