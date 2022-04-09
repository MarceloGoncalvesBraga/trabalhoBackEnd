class Noticia:

    def __init__(self, id, titulo, conteudo, estado, data, likes, img, visto):
        self.__id = id
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__estado = estado
        self.__data = data
        self.__likes = likes
        self.__img = img
        self.__visto = visto
        
    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_estado(self):
        return self.__estado

    def get_data(self):
        return self.__data
    
    def get_likes(self):
        return self.__likes
    
    def get_img(self):
        return self.__img
    
    def get_visto(self):
        return self.__visto