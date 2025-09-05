# Personal Portfolio Website

This is my personal website built with **Django**, showcasing my resume, projects, and other information.  

The site includes:
- **Home Page** – Introduction and welcome.
- **Resume Page** – My professional experience and skills.
- **Projects Page** – Overview of projects with GitHub links.


## Tech Stack

- **Backend:** Django 5.1
- **Database:** PostgreSQL (deployed on Render)
- **Web Server:** Gunicorn
- **Deployment:** Render (free tier)
- **Static Files:** Collected using Django’s `collectstatic`


## Live Demo

Visit the live site here: https://kwanelemyeza.onrender.com


## Setup Instructions (Local Development)

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000 in your browser.
