
class Meses:
    def __init__(self):
        self.__1 = "janeiro"
        self.__2 = "Fevereiro"
        self.__3 = "Marco"
        self.__4 = "Abril"
        self.__5 = "Maio"
        self.__6 = "Junho"
        self.__7 = "Julho"
        self.__8 = "Agosto"
        self.__9 = "Setembro"
        self.__10 = "Outubro"
        self.__11 = "Novembro"
        self.__12 = "Dezembro"
        
    def get_mes(num):
        #num = int(num)
        meses = {1: 'janeiro', 2: 'Fevereiro', 3: 'Marco', 4: 'Abril', 5: 'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro',10: 'Outubro', 11: 'novembro', 12: 'Dezembro'}
        return meses[num]

#a = Meses
#numero = 3
#print(a.get_mes(6))
