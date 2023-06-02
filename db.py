from requests_html import HTMLSession
import sqlite3


class Conn:
    def __init__(self, nome_db):
        self.conn = sqlite3.connect(f"{nome_db}.db")
        self.cur = self.conn.cursor()
        self.create_table()
        

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tutoriais(
            titulo TEXT,
            link TEXT
        )
        """
        self.cur.execute(query)
        self.conn.commit()

    def insert(self, titulo, link):
        query = f"""
        INSERT OR IGNORE INTO tutoriais VALUES
        (?, ?)
        """
        self.cur.execute(query, (titulo, link))
        self.conn.commit()

    def select(self, condicao=""):
        resultado = []
        for linha in self.cur.execute(f"SELECT * FROM tutoriais {condicao}"):
            resultado.append(linha)

        return resultado


def srapping():
    session = HTMLSession()
    web_page = 'https://edisciplinas.usp.br/mod/glossary/view.php?id=197645&mode&hook=ALL&sortkey&sortorder&fullsearch=0&page=-1'
    respone = session.get(web_page)
    page_html = respone.html
    element = page_html.find('source')
    data = []

    for sources in element:

        link = sources.attrs['src']
        titulo = sources.attrs['src'].split("_")[3]


        try:
            for n in range(4, 6):
                if sources.attrs['src'].split("_")[n] != "STREAM.mp4":
                    titulo = titulo + " " + sources.attrs['src'].split("_")[n]
        except:
            pass

        if "-" in titulo :
            titulo = titulo.split("-")[0] + " " + titulo.split("-")[1]
            

        mydict = {"titulo": titulo, "link": link}
        data.append(mydict)

    return data



def store_data_db(conn):
    for data_scraped in srapping():

        titulo = data_scraped['titulo']
        link = data_scraped['link']

        conn.insert(titulo, link)

if __name__ == '__main__':
    conn = Conn("libras")
    store_data_db(conn)
    print("banco de dados criado com sucesso.")
    #print(conn.select())
    #titulo = "album de foto"
    #print(conn.select(f"WHERE titulo = '{titulo}' OR titulo LIKE '%{titulo}%'"))