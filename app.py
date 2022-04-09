
from asyncio.windows_events import NULL
from distutils.log import debug
import imp
from flask import Flask, redirect,render_template, url_for
from meses import Meses
from lista_estados import Estados
from estado import Estado
from noticia import Noticia
from ordem import bubbleSort

app = Flask(__name__)

estado_rio = Estado(1, "Rio de Janeiro", "RJ")

estado_minas = Estado(2, "Minas Gerais", "MG")

estado_espirito = Estado(3, "Espirito Santo", "ES")

estado_bahia = Estado(4, "Bahia", "BA")

noticia_minas_lista = [
    Noticia(1, "Com recordes diários, janeiro de 2022 será o mês com maior número de casos da Covid em Minas", "Janeiro será o mês com mais contaminados pelo coronavírus em Minas. O recorde do pico de casos pode ocorrer já neste sábado devido à disparada de infecções provocadas pela variante Ômicron. Mesmo defendido por alguns especialistas, um recuo nas flexibilizações não está na pauta de governo do Estado.Dados da Secretaria de Estado de Saúde (SES-MG) indicam março de 2021 com o mês com mais doentes desde o início da pandemia. Foram 245 mil testes positivos. Porém, apenas nos 21 dias de 2022 já são 239 mil. Desde terça-feira, 20 mil novos casos são registrados a cada 24 horas.<br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a> ", estado_minas,"01/02/2022",3457,"r01.jpg","7846"),
    Noticia(2, "Minas Gerais registra 3.922 casos confirmados nas últimas 24 horas", "De acordo com o Informe Epidemiológico do coronavírus desta quinta-feira (24 de março de 2022), até o momento, foram notificados 3.310.675 casos confirmados de infecção humana pela Covid-19, em Minas Gerais, com registro oficial de 60.687 óbitos confirmados. Estão em acompanhamento 60.932 casos e são 3.189.056 casos recuperados. Nas últimas 24 horas, foram 3.922 casos e 49 óbitos confirmados <br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a>", estado_minas,"24/03/2022",11452,"r02.jpeg","16478")
]

noticia_rio_lista = [
    Noticia(3, "Mapa de Risco da Covid-19: estado do Rio de Janeiro retorna para a bandeira amarela", "A 68ª edição do Mapa de Risco da Covid-19, divulgada nesta sexta-feira (11.02) pela Secretaria de Estado de Saúde (SES), mostra que o estado do Rio de Janeiro voltou para a bandeira amarela, de baixo risco para Covid-19. A análise faz a comparação da quinta semana epidemiológica (SE) deste ano, a SE 05 (30 de janeiro a 05 de fevereiro), com a terceira, a SE 03 (16 a 22 de janeiro). O mapa desta semana apresenta uma melhora nas regiões Metropolitana I, que saiu da bandeira laranja (risco moderado) para bandeira amarela (baixo risco) e Serrana, que estava em bandeira vermelha (risco alto) e agora aparece em bandeira laranja (risco moderado)<br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a>", estado_rio,"09/02/2022",3142,"r03.jpeg","4125")
]

noticia_espirito_lista = [
    Noticia(5, "Governo do Espírito Santo divulga 97º Mapa de Risco Covid-19 ", "O Governo do Estado anunciou, nesta sexta-feira (04), o 97º Mapa de Risco Covid-19, que terá vigência desta segunda-feira (07) até o próximo domingo (13). Dos 78 municípios capixabas, 68 estão classificados em Risco Baixo e dez municípios ficarão em Risco Moderado. Não há municípios classificados em Risco Alto <br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a>", estado_espirito,"04/03/2022",1071,"r05.jpg","1478")
]
noticia_bahia_lista = [
    Noticia(6, "Prefeitura de Salvador oferta vacina contra a Covid-19 para residentes da Bahia nesta terça-feira (15)", "A vacinação contra Covid-19 acontece nesta terça-feira (15) com a estratégia “Liberou Geral” para aplicação da 1ª dose em pessoas com 12 anos ou mais, além da 2ª e 3ª dose para indivíduos com 18 anos ou mais, independentemente de ser residente do município, ou seja, mesmo não morando em Salvador ou não tendo tomado as doses aqui, o cidadão será contemplado. O único requisito é ter o cartão SUS vinculado a algum município do estado da Bahia.<br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a>", estado_bahia,"14/02/2022",212,"r06.jpg","789"),
    Noticia(7, "Governo libera limite de público em eventos na Bahia", "Está publicada no Diário Oficial do Estado, edição deste sábado (19), a autorização para a realização de eventos sem limite de público em todo o território baiano. Isso inclui atividades como cerimônias de casamento, eventos urbanos e rurais em logradouros públicos ou privados, eventos exclusivamente científicos e profissionais, circos, parques de exposições, solenidades de formatura, feiras, passeatas, parques de diversões, espaços culturais, teatros, cinemas, museus, espaços congêneres e afins. O decreto entra em vigor a partir da data de sua publicação.<br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a>", estado_bahia,"19/03/2022",375,"r07.jpg","487")
]
estado_rio.set_noticia_lista(noticia_rio_lista)
estado_minas.set_noticia_lista(noticia_minas_lista)
estado_espirito.set_noticia_lista(noticia_espirito_lista)
estado_bahia.set_noticia_lista(noticia_bahia_lista)

#noticias_lista = [noticia_espirito_lista, noticia_minas_lista, noticia_rio_lista]



estado_lista = [
    estado_rio,
    estado_minas,
    estado_espirito,
    estado_bahia
]

debug(True)

 # rota da pagina principal
@app.route("/")
@app.route("/home")
def home():
    template_name = 'home.html'

    return render_template(template_name,
        menus = estado_lista,
        estados=estado_lista
    )

@app.route("/estado/<string:uf>")
def noticias_do_estado(uf):
    for estado in estado_lista:
        if estado.get_uf() == uf:
            return render_template("exibir-noticias-do-estado.html", 
                                   noticias = bubbleSort(estado.get_noticia_lista())
,
                                    menus = estado_lista,
                                    estado = estado.get_uf()
                                   )
    return render_template("home.html", noticias=estado_lista)



@app.route("/noticia/<int:id>")
def exibir_noticia(id):
    for estado in estado_lista:
        for a in  estado.get_noticia_lista(): 
            if a.get_id() == id:
                return render_template("exibir-noticia.html",
                    noticia=a,
                     menus = estado_lista
                    )
            
    return render_template("home.html", noticias=estado_lista)





#if __name__ == '__main__':
    #app.run(debug=True) 
