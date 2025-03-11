# AI-blog_Generator
# AI Blog Generator


An AI-powered blog generator built using Django that generates high-quality blog posts based on given topics using AI.

## 🚀 Features
- 🔹 AI-powered content generation
- 🔹 Supports multiple topics
- 🔹 User-friendly UI with Django templates
- 🔹 Media file handling (supports audio file input)
- 🔹 REST API for seamless integration
- 🔹 Secure authentication & user management

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **AI Integration:** OpenAI/GPT
- **Database:** SQLite / PostgreSQL
- **Frontend:** Django Templates, Bootstrap
- **Deployment:** AWS / Render / Heroku

## 📦 Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/ai-blog-generator.git
   cd ai-blog-generator
   ```

2. **Create a virtual environment** (Recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```sh
   python manage.py migrate
   ```

5. **Start the development server**
   ```sh
   python manage.py runserver
   ```

## 🔥 Usage
- Navigate to the homepage and enter a topic.
- The AI will generate a well-structured blog post.
- Users can edit and save the content for later use.
- API endpoints are available for programmatic access.

## 📌 API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/generate-blog/` | POST | Generate a blog post based on input |
| `/api/blogs/` | GET | Retrieve all generated blogs |
| `/api/blogs/<id>/` | GET | Retrieve a specific blog |

## 🚀 Deployment
1. Set up environment variables for secrets and API keys.
2. Use **Gunicorn** for production.
   ```sh
   gunicorn ai_blog_generator.wsgi:application --bind 0.0.0.0:8000
   ```
3. Configure a **PostgreSQL** database for production.
4. Deploy on **AWS, Render, or Heroku**.

## 🤝 Contributing
Feel free to fork this repo and submit a PR with improvements!

## 📜 License
This project is licensed under the MIT License.

---
🚀 Developed by [Your Name](https://github.com/your-username)


