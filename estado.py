class Estado:   

    def __init__(self, id, nome, uf):
        self.__id = id
        self.__nome = nome
        self.__uf = uf
    
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_uf(self):
        return self.__uf

    def get_noticia_lista(self):
        return self.__noticia_lista
    
    def set_noticia_lista(self, noticia_lista):
        self.__noticia_lista = noticia_lista

