# Fruitipedia-App
Workshop: Fruitipedia App from Software University

Project Description: Fruitipedia App

The Fruitipedia App is a Django-based web application developed as part of the Python ORM course at Software University. The app serves as an interactive encyclopedia for fruits, allowing users to explore information about various fruits, create new fruit entries, and manage fruit categories. Below are key components and features of the Fruitipedia App:

Skeleton:
The project provides HTML pages, images, and CSS files, offering a ready-to-use foundation for the development.

Configurations:

Templates and Static Files:

HTML templates are organized and placed in the appropriate templates folder.
Static files (images and styles) are added and configured in the settings.py file.
URLs (Paths):

URL patterns are established for each app to load templates.
The main project urls.py file includes these patterns using the include() function.
Database:
Two models are defined for the database: Category Model and Fruit Model.

Fields: name, image_url, description, nutrition.

Views:
Views are implemented in Django, representing Python functions or classes that handle HTTP requests, process data, and return HTTP responses. They follow the Model-Template-View (MTV) architectural pattern.

Fruits App URLs:
URL patterns are defined in the urls.py file within the fruits app to direct requests to the appropriate views.

Template Inheritance:
Common parts of templates (head, header, footer) are extracted into a base.html template for better code organization.

Navigation bar with links to "Create Category," "Create Fruit," and "Dashboard."
Dashboard Page:

Displays all created fruits.
If no fruits exist, shows a message.
Create Category Page:

Form for creating a new category.
Create Fruit Page:

Form for creating a new fruit.
Fruit Details Page:

Displays detailed information about a specific fruit.
Includes "Edit" and "Delete" buttons.
Edit Fruit Page:

Form pre-filled with existing fruit information for editing.
Delete Fruit Page:

Form for confirming the deletion of a fruit.

The Fruitipedia App provides a user-friendly interface to manage and explore information about fruits, supporting CRUD (Create, Read, Update, Delete) operations with a well-structured Django application architecture.

![image](https://github.com/IvanVakov/Fruitipedia-App/assets/119103300/9402999a-5c55-4bee-ab91-8bc39bc2f214)

![image](https://github.com/IvanVakov/Fruitipedia-App/assets/119103300/71f28409-d3e6-432f-b490-d60a40c1d2cf)

![image](https://github.com/IvanVakov/Fruitipedia-App/assets/119103300/443eb479-4fe6-4661-932f-1f85fc8c0ba5)


