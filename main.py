import os

translations = {"colada": "lavagem (comida)", "plachan": "passar ferro", "empiezan": "começam", "sencillas": "simples", "retendrá": "irá reter",
                "muletillas": "é uma palavra ou frase que é repetida muito pelo hábito", "pelea": "lutar", "Infografía": "Infográfico: é um conteúdo explicativo que une informações verbais e visuais",
                "patalla táctil": "tela sensivel ao toque", "lentilla": "tela lente", "gafas": "óculos", "inalámbrico": "sem fio", "ojalá": "tomara que...", "salgas": "sair", "abuelo": "vovô",
                "suenan": "tocam (instrumento)", "oídas": "boato", "olvidan": "eles esquecem", "aislamiento": "isolamento", "desarrolloo": "em desenvolvimento", "sencilla": "simples",
                "empezar": "Começar", "leídos": "ler", "pelo": "cabelo", "anduviésimos": "vamos andar", "botellas": "garrafas", "llamaba": "chamado", "la ceja": "sobrancelha", "la barbilla": "o queixo",
                "el cuello": "o pescoço", "la mejilla": "bochecha", "el talón": "calcanhar", "la espalda": "as costas", "el muslo": "a coxa", "la rodilla": "joelho", "la coronilla": "parte da cabeça onde fica o “redemoinho”",
                "vergüenza": "vergonha", "entonces": "então", "diré": "direi", "mira": "olha", "hija": "filha", "agregó": "adicionado", "entonces": "então", "asesina": "assassino", "sacarle": "tirar",
                "señala": "indica (algo)", "sencillo": "simples", "prensa": "imprensa (revista)", "embarazo": "gravidez", "ventas": "vendas", "magacín": "revista", "juguetería": "loja de brinquedo",
                "ragañadientes": "com relutância", "repelerlas": "repeli-los", "sillín": "banco de bicicleta", "pollo": "frango", "tirita": "bandagem", "ahorrando": "salvando", "alquilar": "para alugar",
                "pantalones": "calças", "calcetines": "meias", "pashimina": "lenço para o pescoço", "diseñadores": "desenhistas", "malísimas": "muito ruim", "alabadas": "elogiado", "semillas": "sementes",
                "hubiese": "teria", "enseñaba": "ensinou", "lográbamos": "conseguimos", "palabrota": "palavrão", "mala palabra": "palavrão", "garaboto": "rabisco", "perrito": "cachorro", "niñez": "infância",
                "basándote": "com base em...", "bañador": "roupa de banho (sunga, maiô etc)", "malla": "malha ou rede", "canilla": "toque", "apellidos": "sobrenome", "oreja": "orelha", "película": "filme",
                "villancicos": "canções de natal", "rociadas": "polvilhadas", "pestiños": "pequenos pastéis fritos", "sandía": "melancia", "descargar": "baixar algo em algum dispositivo eletronico",
                "acostarse": "ir dormir", "empiezar": "começar", "pronominales": "pronomes", "olvidan": "esquecem", "ordenador": "computador", "destartalados": "detonado, desmantelado, surrado",
                "aíslan": "isolar", "cepillas": "pincéis", "afeitas": "barbear-se", "maquillas": "maquiar-se", "arreglarte": "arrumar-se", "perilla": "bigode", "sombrero": "chapéu", "ponerse": "colocar",
                "población": "população", "chatarra": "sucata", "sana": "saudável", "Hogares": "casas", "pereja": "casal", "salgo": "vou embora", "pongo": "coloquei", "vengo": "eu venho", "alquiler": "aluguel",
                "coche": "carro", "albañil": "pedreiro", "reseñables": "extraordinário", "empiezan": "começam", "iban": "estavam indo", "tierna": "macio", "pormenores": "detalhes", "lunes": "segunda-feira",
                "quitarse": "descolar", "concierto": "show", "película": "filme", "estorbar": "impedir", "olla": "panela", "resbalar": "escorregar", "olvidarse": "esquecer", "castillo": "castelo",
                "guantes": "luvas", "huir": "fugir", "campesina": "camponês", "paraguas": "guarda-chuva", "anillo": "anel", "jinete": "cavaleiro", "conduje": "dirigiu", "empezado": "começado",
                "sembrar": "semear", "casi": "quase", "ahorrar": "economizar", "meseta": "platô", "morcilla": "chouriço", "jamón": "presunto", "guindilla": "pimenta", "hojaldre": "massa folhada",
                "vainilla": "baunilha", "cuya": "de quem", "regalo": "presente", "calabacín": "abobrinha", "zanahoria": "cenoura", "gamba": "camarão", "pavo": "peru", "pollo": "frango", "llena": "cheio",
                "toma": "levando", "sencillo": "simples", "lejía": "água sanitária", "solamente": "somente", "manglar": "manguezal", "basura": "lixo", "vertedero": "aterro", "iluvia": "chuva", "desarrollo": "em desenvolvimento",
                "labor": "trabalho", "ocio": "lazer", "depuradora": "estação de tratamento", "contenedor": "recipiente", "botellas": "garrafas", "riada": "corrente", "huracán": "furacão", "conserje": "porteiro",
                "tormárselo": "pegue", "tuvo": "ele tinha", "pasillo": "corredor", "cerrillas": "palitos de fósforo", "guay": "frio", "trocito": "pouco", "butacas": "poltronas", "Rojo": "vermelho", "espinita": "espinho", "ilave": "chave inglesa",
                "gorra": "boné", "concepto": "conceito", "campera": "jaqueta", "sucia": "sujo", "acogedora": "aconchegante", "postre": "sobremesa", "senderismo": "caminhada", "galletas": "biscoitos"}
T = []


def appendTranslations():
    for key in translations.keys():
        T.append(key)


def findTranslateByKey(t):
    for key in translations.keys():
        if (t == key):
            find = translations[key]
            return find


appendTranslations()
print("\033[1;32m-------------------------------------------------\033[m")
print("\033[1;32m   BEM VINDOS AO PROJETO ESPANHOL SEM MOAGEM\033[m")
print("\033[1;32m-------------------------------------------------\033[m\n")
while True:
    try:
        scanner = str(input("\033[1;32mBuscador: \033[m")).lower()
    except ValueError:
        print("\033[1;32mAlgo deu errado\033[m")
        continue

    if scanner in T:
        print(
            f"\033[1;32mResultado: \033[m{str(findTranslateByKey(scanner)).capitalize()}\n")
        os.system("pause")
    else:
        print('\033[1;32mPalavra errada\033[m\n')
        os.system("pause")
