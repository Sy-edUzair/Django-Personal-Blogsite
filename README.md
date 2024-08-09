
# Personal Blog Site
![image](https://github.com/user-attachments/assets/11db4c82-c642-4a1a-896c-ffce646ac6e6)
View the site here: https://syeduzair59.pythonanywhere.com/


## Overview

This is a personal blog website developed using Django, a powerful and flexible Python web framework. The project covers all primary backend concepts in Django, serving as both a personal blog and a demonstration of learned skills.

## Features

- **CRUD Functionality**: Create, Read, Update, and Delete blog posts.
- **Comment System**: Users can leave comments on blog posts.
- **Pagination**: Blog posts are paginated for easier navigation.
- **Admin Panel**: Django’s built-in admin panel for managing the blog posts, users, and comments.

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default for Django)
- **Version Control**: Git
- **Deployment**: PythonAnywhere.com

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the site:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` to manage posts, users, and comments.
- **Commenting**: Engage with blog posts by leaving comments.

## Learning Highlights

Throughout the development of this project, the following Django backend concepts were covered:

- **Models and Migrations**: Designing database schemas and managing changes.
- **Views and Templates**: Implementing logic and rendering HTML templates.
- **Forms and Validation**: Creating and validating forms for user input.
- **Authentication and Authorization**: Handling user sessions, login, and permissions.
- **Django ORM**: Interacting with the database using Django's Object-Relational Mapping system.
- **Middlewares**: Utilizing Django’s middleware for various tasks like security.
- **Static and Media Files**: Managing static assets and user-uploaded content.
- **Deployment**: Deploying the Django application to a live server.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Django community for providing comprehensive documentation and tutorials.
