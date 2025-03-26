from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

# Aqui srá feito a classe para manipular as requisições
class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        #rotas
        if self.path == '/':
            self.path = '/templates/index.html'

            return SimpleHTTPRequestHandler.do_GET(self)

#configurando o endereço ip e a porta para rodar
host = 'localhost'
port = 8000

#config do servidor com o diretório raiz e o manipulador raiz
server_address = (host, port)
httpd = HTTPServer(server_address, CustomHandler)

#Iniciar o server
httpd.serve_forever()
