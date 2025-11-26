# Nexus Inventory Backend

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Production-green.svg)](https://your-live-demo-url.com)

A modern, full-stack IT Asset Management (ITAM) backend solution built with Django REST Framework. Designed to replace manual spreadsheets with a centralized API for tracking hardware and software, ensuring traceability, cost reduction, and accountability auditing.

## 🚀 Live Demo

Check out the API documentation: [Nexus Inventory API Docs](#)

## 🚀 Features

### Core Functionality

- **Authentication**: JWT-based login with secure token management using djangorestframework-simplejwt.
- **API Endpoints**: RESTful APIs for assets, employees, categories, software, and asset history.
- **User Management**: Custom user model with email authentication.
- **Asset Lifecycle**: Track check-in/check-out, maintenance, and disposal with history logging.

### Advanced Features

- **File Uploads**: Image uploads for assets with MIME type validation.
- **Filtering & Search**: Advanced filtering and textual search using django-filter.
- **Pagination**: Efficient pagination for large datasets.
- **CORS Support**: Configured for frontend integration.

### Technical Highlights

- **Complex Data Modeling**: Handles relationships (1:N for categories, N:N for software).
- **Real-time Ready**: Built for integration with frontend for real-time updates.
- **Secure**: Environment-based secrets, permissions, and input validation.
- **Documentation**: Auto-generated API docs with drf-spectacular.

## 🛠 Tech Stack

- **Backend**: Django 5.2, Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (development), PostgreSQL (production)
- **Filtering**: django-filter
- **File Handling**: Pillow, python-magic
- **Deployment**: Docker, Supabase for database
- **Other**: drf-spectacular for docs, corsheaders

## 📦 Getting Started

### Prerequisites

- Python 3.13+
- PDM (Python package manager)
- Backend database (SQLite for dev)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/renato-chagas/nexus-inventory-backend.git
   cd nexus-inventory-backend
   ```

2. Install dependencies:

   ```bash
   pdm install
   ```

3. Set up environment variables:
   Create a `.env` file:

   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=*
   MODE=DEVELOPMENT
   ```

4. Run migrations:

   ```bash
   pdm run python src/manage.py migrate
   ```

5. Create superuser:

   ```bash
   pdm run python src/manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   pdm dev
   ```

7. Build for production:
   ```bash
   pdm run python src/manage.py collectstatic
   ```

## 📱 API Documentation

- Interactive docs: `http://127.0.0.1:8000/api/docs/` (Swagger UI)
- Schema: `http://127.0.0.1:8000/api/schema/`

## 🎯 Usage

### Authentication

Enter email and password to authenticate and receive JWT tokens.

POST `/api/token/` with:
```json
{
  "email": "user@example.com",
  "password": "password"
}
```

### API Endpoints

- **Assets**: `/api/assets/` (CRUD, search, filter)
- **Employees**: `/api/employees/`
- **Categories**: `/api/categories/`
- **Software**: `/api/softwares/`
- **Asset History**: `/api/asset-history/`
- **Users**: `/api/users/`
- **Images**: `/api/images/`

### Managing Assets

- Search and filter assets by name, category, status.
- View detailed specs, software, and history.
- Perform CRUD operations via API.

### Advanced Interactions

- Use filters like `?search=laptop&category=1` for advanced queries.
- Upload images with validation.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions or suggestions, reach out to [renatochagas.m@gmail.com](mailto:renatochagas.m@gmail.com) or open an issue.

---

_Built as a portfolio project to demonstrate backend development skills with Django._