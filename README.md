# Fashion Review Web Application
Overview
The Fashion Review Web Application is a full-stack web application that serves as a mockup for a professional fashion review blog site. It features a modern-looking frontend built with React and a backend powered by Django, providing a seamless experience for viewing and managing fashion reviews.

Features
Frontend:

Built with React.js.
Modern, responsive design with a focus on fashion reviews.
Dynamic pages for viewing detailed reviews.
Backend:

Built with Django and Django REST Framework.
Provides RESTful API endpoints for managing fashion reviews.
Includes CORS handling with django-cors-headers for secure frontend-backend communication.
Prerequisites
Node.js (for the frontend)
Python 3.x (for the backend)
Pip (Python package installer)
Git (for cloning the repository)
Installation

1. git clone https://github.com/yourusername/fashion-review-web-application.git
   cd fashion-review-web-application

2. Setting up Backend
   cd fashion_review_backend
   python -m venv env
   source env/bin/activate  # On Linux/Mac
  .\env\Scripts\activate  # On Windows

  a. Install Backend Dependencies
     pip install -r requirements.txt

  b. Apply Migrations
     python manage.py migrate

  c. Run the Development Server
    python manage.py runserver
    
3. Setting up Frontend
   a. Navigate to the frontend directory
     cd ../fashion-review-site
   
   b. Install frontend dependencies
     npm install

   c. Run the frontend development server
     npm start

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

License
This project is open-source and available under the MIT License.


