# 📦 Nexus Inventory Backend

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PDM](https://img.shields.io/badge/PDM-Package%20Manager-blue?style=for-the-badge&logo=python&logoColor=white)](https://pdm-project.org/)

O **Nexus Inventory Backend** é uma API REST robusta para Gerenciamento de Ativos de TI (ITAM). Centraliza o controle de hardware, categorias, funcionários, softwares instalados e histórico de movimentações de ativos.

---

## ✨ Funcionalidades Core

### 🔐 Autenticação e Segurança
- Autenticação baseada em JWT (JSON Web Tokens)
- Custom User Model com autenticação por email
- Permissões granulares por endpoint
- Refresh token automático

### 📊 Gestão de Ativos
- CRUD completo de ativos com status (Disponível, Em uso, Manutenção, Descartado)
- Rastreamento de histórico de movimentações
- Associação de ativos com funcionários responsáveis
- Gerenciamento de categorias e softwares instalados

### 📋 Recursos Adicionais
- Documentação automática via Swagger UI e ReDoc
- Paginação de resultados
- Filtros e busca por recursos
- Upload de imagens para ativos

---

## 🛠 Tech Stack

| Ferramenta | Versão | Propósito |
|-----------|--------|----------|
| Django | 5.2.8 | Framework web principal |
| Django REST Framework | - | API REST |
| Python | 3.13+ | Linguagem base |
| PDM | - | Gerenciador de dependências |
| SQLite | - | Banco de dados (desenvolvimento) |
| JWT (djangorestframework-simplejwt) | - | Autenticação |
| drf-spectacular | - | Documentação (Swagger/ReDoc) |
| CORS Headers | - | Suporte CORS para frontend |

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.13+
- PDM instalado
- Git

### Passo a Passo

#### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/nexus-inventory-backend.git
cd nexus-inventory-backend
```

#### 2️⃣ Instale as dependências
```bash
pdm install
```

#### 3️⃣ Ative o ambiente virtual
```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Mac/Linux
source .venv/bin/activate
```

#### 4️⃣ Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=*
MODE=dev
```

#### 5️⃣ Execute as migrações
```bash
python src/manage.py migrate
```

#### 6️⃣ Crie um superusuário (admin)
```bash
python src/manage.py createsuperuser
```

#### 7️⃣ (Opcional) Popule o banco com dados de teste
```bash
python populate_db.py
```

#### 8️⃣ Inicie o servidor
```bash
pdm dev
```

Ou sem PDM:
```bash
python src/manage.py runserver
```

✅ O servidor estará rodando em: **http://127.0.0.1:8000**

---

## 📖 Documentação da API

Após iniciar o servidor, acesse:

- 🛠 **Swagger UI (Interativo):** [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- 📄 **ReDoc:** [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- 🔑 **Admin Django:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Estrutura Principal

```
Nexus-Inventory-backend/
├── src/
│   ├── config/              # Configurações do Django
│   │   ├── settings.py      # Settings principais
│   │   ├── urls.py          # Rotas principais
│   │   └── router.py        # Rotas da API
│   ├── core/                # Apps do projeto
│   │   ├── nexus_inventory/ # App principal (Ativos, Histórico, Categorias)
│   │   ├── user/            # App de usuários
│   │   └── uploader/        # App de upload de imagens
│   ├── manage.py            # Gerenciador Django
│   └── db.sqlite3           # Banco de dados
├── populate_db.py           # Script para popular com dados
├── pyproject.toml           # Dependências PDM
└── README.md                # Este arquivo
```

---

## 🔑 Endpoints Principais

### Autenticação
- `POST /api/token/` - Obter tokens (access + refresh)
- `POST /api/token/refresh/` - Renovar access token
- `GET /api/users/me/` - Dados do usuário logado

### Ativos
- `GET /api/assets/` - Listar todos os ativos
- `POST /api/assets/` - Criar novo ativo
- `GET /api/assets/{id}/` - Detalhes de um ativo
- `PUT /api/assets/{id}/` - Atualizar ativo
- `DELETE /api/assets/{id}/` - Deletar ativo

### Histórico
- `GET /api/asset-history/` - Listar histórico
- `POST /api/asset-history/` - Criar registro de histórico
- `GET /api/asset-history/{id}/` - Detalhes de um histórico

### Outras Rotas
- `GET /api/employees/` - Listar funcionários
- `GET /api/categories/` - Listar categorias
- `GET /api/softwares/` - Listar softwares

---

## 🧪 Testes

```bash
python src/manage.py test
```

---

## 📝 Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `SECRET_KEY` | Chave secreta do Django | Obrigatória |
| `DEBUG` | Modo debug | `False` |
| `ALLOWED_HOSTS` | Hosts permitidos | `*` |
| `MODE` | Modo de execução (dev/prod) | `dev` |

---

## 🐛 Solução de Problemas

### Erro: "No such column"
Execute as migrações novamente:
```bash
python src/manage.py migrate
```

### Erro: "Permission Denied" em populate_db.py
Certifique-se de estar no diretório da raiz do projeto e com permissões adequadas.

### Erro: "ModuleNotFoundError"
Reinstale as dependências:
```bash
pdm install
```

---

## 👨‍💻 Desenvolvido por
**Renato Chagas**

---

## 📜 Licença
MIT License
