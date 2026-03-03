# 📦 Nexus Inventory Backend

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![PDM](https://img.shields.io/badge/PDM-6D50ED?style=for-the-badge&logo=pdm&logoColor=white)](https://pdm-project.org/)

O **Nexus Inventory Backend** é uma solução robusta de Gerenciamento de Ativos de TI (ITAM) desenvolvida com **Django REST Framework**. Projetado para substituir planilhas manuais, oferece uma API centralizada para rastreamento de hardware, licenças de software e histórico completo de movimentações.

---

## ✨ Principais Funcionalidades

### 🔐 Segurança e Autenticação
- **JWT (JSON Web Tokens):** Autenticação segura com `djangorestframework-simplejwt`.
- **Custom User Model:** Login baseado em e-mail em vez de username.
- **Permissions:** Proteção de rotas com base no nível de acesso do usuário.

### ⚙️ Gestão de Ativos (Lifecycle)
- **Rastreabilidade Total:** Registro automático de histórico (`AssetHistory`) em cada movimentação (Check-in/Check-out/Manutenção).
- **Relacionamentos Complexos:** Gerenciamento de categorias (1:N) e softwares instalados (N:N).
- **Validação de Mídia:** Upload de imagens de ativos com validação rigorosa de MIME type.

### 🔍 Performance e UX da API
- **Advanced Filtering:** Busca textual e filtros por categoria/status via `django-filter`.
- **Pagination:** Respostas otimizadas para grandes volumes de dados.
- **Auto-Docs:** Documentação interativa via **Swagger UI** (drf-spectacular).

---

## 🛠 Tech Stack

- **Linguagem:** Python 3.13+
- **Framework:** Django 5.2 & Django REST Framework
- **Gerenciador de Pacotes:** PDM
- **Banco de Dados:** SQLite (Dev) | PostgreSQL (Prod/Supabase)
- **Documentação:** Swagger (drf-spectacular)
- **Qualidade de Código:** Identificação de tipos de arquivo com `python-magic`