# Use a imagem oficial do Python como base
FROM python:3.9

# Instale o Apache e o módulo mod_wsgi
RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi-py3

# Copie os arquivos da aplicação para o diretório apropriado
COPY ./app /var/www/flask_app
COPY ./requirements.txt /var/www/flask_app/requirements.txt

# Defina o diretório de trabalho
WORKDIR /var/www/flask_app

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Configure o Apache para rodar a aplicação Flask
RUN echo "<VirtualHost *:80>\n\
    ServerName localhost\n\
    WSGIDaemonProcess flask_app threads=5\n\
    WSGIScriptAlias / /var/www/flask_app/flask_app.wsgi\n\
    <Directory /var/www/flask_app>\n\
        WSGIProcessGroup flask_app\n\
        WSGIApplicationGroup %{GLOBAL}\n\
        Require all granted\n\
    </Directory>\n\
</VirtualHost>" > /etc/apache2/sites-available/000-default.conf

# Crie o arquivo WSGI para rodar a aplicação Flask
RUN echo "import sys\n\
sys.path.insert(0, '/var/www/flask_app')\n\
from app import app as application" > /var/www/flask_app/flask_app.wsgi

# Exponha a porta 80
EXPOSE 80

# Inicie o Apache em primeiro plano
CMD ["apachectl", "-D", "FOREGROUND"]
