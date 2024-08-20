# Fashion Review Web Application

## Overview

The **Fashion Review Web Application** is a full-stack web application that serves as a mockup for a professional fashion review blog site.

### Features

- **Frontend**: 
  - Built with React.js.
  - Modern, responsive design.
- **Backend**:
  - Built with Django and Django REST Framework.
  - Provides RESTful API endpoints.

### Installation

### 1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/fashion-review-web-application.git

   cd fashion-review-web-application
```

### 2. Setting up the Backend

   ```bash
   cd fashion_review_backend
   ```
   #### Create a virtual environment
   ```bash
   python -m venv env
   ```
   #### Activate the virtual environment
   
   ##### On Linux/Mac
   ```bash
   source env/bin/activate
  ```
   
   ##### On Windows
   ```bash
   .\env\Scripts\activate
  ```


  a. Install Backend Dependencies
  ```bash
     pip install -r requirements.txt
```

  b. Apply Migrations
  ```bash
     python manage.py migrate
```

  c. Run the Development Server
  ```bash
    python manage.py runserver
```
    
### 3. Setting up Frontend
   a. Navigate to the frontend directory
   ```bash
     cd ../fashion-review-site
```
   
   b. Install frontend dependencies
   ```bash
     npm install
```

   c. Run the frontend development server
   ```bash
     npm start
```

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

License
This project is open-source and available under the MIT License.


