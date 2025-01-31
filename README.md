## Overview

The FAQ Project is a Django application designed to manage frequently asked questions (FAQs) with multi-language support. It integrates a WYSIWYG editor for formatting answers, provides a REST API for easy access, and implements caching for improved performance.

## Features

- Multi-language support for FAQs (English, Hindi, Bengali).
- WYSIWYG editor integration using `django-ckeditor`.
- REST API for managing FAQs.
- Caching mechanism using Redis for efficient translation retrieval.
- Automatic translation using Google Translate API.
- User-friendly Django admin interface for managing FAQs.

## Prerequisites

- Python 3.9 or higher
- Redis server running locally

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/anubhavanand1516/BharatFD_assigement.git
   cd BharatFD_assigement
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the Redis server (ensure it's running):
   ```bash
   # If you have Redis installed, you can start it using:
   redis-server
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```


### Django Admin

Access the admin interface at `http://localhost:8000/admin/` and log in using the superuser credentials you created.

you can manually run the commands inside the Django shell:
```bash
from faq_app.models import FAQ  # Replace 'faqs' with your actual app name

FAQ.objects.create(
    question="What is Django?",
    answer="Django is a high-level Python web framework.",
    question_hi="डिजैंगो क्या है?",
    question_bn="ডিজ্যাঙ্গো কি?"
)

FAQ.objects.create(
    question="How do I install Django?",
    answer="You can install Django using pip: `pip install django`.",
    question_hi="मैं डिजैंगो कैसे इंस्टॉल करूं?",
    question_bn="আমি কীভাবে ডিজ্যাঙ্গো ইনস্টল করব?"
)

print("FAQs added successfully!")

```





## API Usage

### Fetch FAQs

#### Fetch FAQs in English (default)
```bash
curl http://localhost:8000/api/faqs/
```
![Screenshot 2025-02-01 at 3 47 47 AM](https://github.com/user-attachments/assets/ad34ceb0-35b4-4283-bf0e-13c7cc0715b8)


#### Fetch FAQs in Hindi
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```
<img width="1440" alt="Screenshot 2025-02-01 at 3 48 51 AM" src="https://github.com/user-attachments/assets/99d7a044-22fe-4782-8ee1-572d7e45ec90" />

#### Fetch FAQs in Bengali
```bash
curl http://localhost:8000/api/faqs/?lang=bn
```
<img width="1440" alt="Screenshot 2025-02-01 at 3 49 23 AM" src="https://github.com/user-attachments/assets/97ff443f-2ee2-4c11-a364-d5ae295af0d4" />


## Running Tests

To run the unit tests, use the following command:
```bash
python manage.py test
```


## Acknowledgments

- [Django](https://www.djangoproject.com/) for the web framework.
- [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) for WYSIWYG editor support.
- [Redis](https://redis.io/) for caching.
- [Google Translate API](https://cloud.google.com/translate/docs) for translation services.
