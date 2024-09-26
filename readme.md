# Projeto Sua-Diarista

### Instalando o projeto

#### Clonar o projeto aqui no repositório
`git clone https://github.com/devkoyote/suadiarista.git`

#### Instalar dependências 
`pip install -r requeriments.txt`

#### Alterar configurações DB `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_config',
        'HOST': 'ip_config_host',
        'PORT': port_config,
        "USER": 'name_config',
        "PASSWORD": 'passwd_config'
    }
}

```

#### Migrar banco de dados
`python manage.py migrate`

#### Iniciar Servidor 
`python manage.py runserver`


