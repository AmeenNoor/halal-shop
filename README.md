
# 

## Author

Ameen Noor

## Introduction





## Table of Contents

- [EireBnb](#eirebnb)
  - [Author](#author)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Agile Process](#agile-process)
    - [Project Goals](#project-goals)
    - [Initial User Stories](#initial-user-stories)
    - [Agile Methodology](#agile-methodology)
  - [User Experience (UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)
  - [Information Architecture](#information-architecture)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Database Choice](#database-choice)
    - [Data Models](#data-models)
      - [Accommodation Data Model](#accommodation-data-model)
      - [Booking Data Model](#booking-data-model)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Tools, Libraries and Programs Used](#frameworks-tools-libraries-and-programs-used)
  - [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
    - [Manual Testing](#manual-testing)
    - [Fixing Bugs](#fixing-bugs)
  - [Deployment](#deployment)
    - [Local deployment](#local-deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Mentor](#mentor)


## Agile Process
### Project Goals


### Initial User Stories



### Agile Methodology



## User Experience (UX)

### Target Audience



### Design Choices
- #### Colors

  
- #### Typography

  

### Wireframes
- #### Desktop


- #### Tablet


- #### Mobile




## Information Architecture
### Entity Relationship Diagram



### Database Choice


### Data Models



## Features
### Implemented Features



### Future Features


## Technologies Used
### Languages Used


   
### Frameworks, Tools, Libraries and Programs Used






## Testing
### Validation Testing


1. #### admin.py



### Compatibility and Responsive Testing



### Manual Testing


### Fixing Bugs


## Deployment
### Local deployment
To deploy the site using Visual Studio Code, follow these steps:

1. **Clone the Repository:**
    * Open VS Code.
    * Use the command palette and run "Git: Clone".
    * Enter the GitHub repository URL and choose a local directory.
    * Open the cloned project in VS Code.

2. **Install Dependencies:**
    * Navigate to the project directory in the terminal & run the following:
    **pip3 install -r requirements.txt**

3. **Set Environment Variables:**
    * Create a .env file in the project root.
    * Copy the contents of env.py into the .env file.

4. **Apply Migrations:**
    * Run the following commands to apply migrations:
    **python3 manage.py migrate**

5. **Create Superuser :**
    * Create an admin superuser for accessing the Django admin panel:
    **python3 manage.py createsuperuser**

6. **Run the Server:**
    * Start the Django server:
    **python3 manage.py runserver**

### Heroku



## Credits
### Code



### Content


   
### Media


   
### Mentor

