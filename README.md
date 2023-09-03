## Project Planning Tool
Welcome to the Project Planning Tool, a powerful suite of APIs built using Django Rest Framework.

## Introduction
The Project Planning Tool is a web application built using Django and the Django REST framework. It serves as a comprehensive tool for managing team projects, user accounts, teams, and project boards along with their tasks. The tool provides a RESTful API for seamless integration and efficient project management.

## Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/project-planning-tool.git
cd project-planning-tool
Install project dependencies using pip:

Copy code
pip install -r requirements.txt
Run database migrations:

Copy code
python manage.py migrate
Start the development server:

Copy code
python manage.py runserver
Access the application through your browser at http://127.0.0.1:8000.

## Features
User Management: Create, update, and delete user accounts.
Team Management: Form teams, assign administrators, and manage team members.
Project Board: Create project boards with tasks, assign tasks to team members, and track task status.
RESTful API: Provides endpoints for all features, enabling easy integration and automation.
API Reference
The API endpoints are as follows:

## Users

GET /users/: Retrieve a list of all users.
GET /users/<int:pk>/: Retrieve details of a specific user.
Teams

GET /teams/: Retrieve a list of all teams.
GET /teams/<int:pk>/: Retrieve details of a specific team.
Project Boards

GET /project/: Retrieve a list of all project boards.
GET /project/<int:pk>/: Retrieve details of a specific project board.
For more detailed information, refer to the API Documentation.

## Usage
User Management: Use the API to create, update, and delete user accounts. Authenticate users for secure access.

Team Management: Form teams, set administrators, and add team members. Manage team-related operations through API calls.

Project Boards: Create project boards, add tasks, assign tasks to team members, and track task progress.

API Integration: Integrate the provided RESTful API with external tools, applications, or scripts for seamless project management.