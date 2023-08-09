# CAPSTONE - TTRPG Manager

## Description
This project aims to serve as a workflow for creating a system-agnostic management tracker system for tabletop role-playing game s(TTRPGs). The goal is to provide a set of models and tools that makes games and characters easier to mange, using Django for back-end and JavaScript for front-end interactions. The current project primarily focuses on adapting the Dungeons and Dragons 5e system, as it has the complexity enough to be a suitable capstone proyect and it's the one I'm more familiar with.

## Distinctiveness and Complexity
I believe the project meets the requirements for distinctiveness and complexity because it goes deeper into the usage of Django and JavaScript that we've learned throughout the course.

On the Django side, it involves data cleaning and importing large databases into existing models to populate the items and skills sections. It also uses through-intermediary models. The project relies on the exchange of various data types between HTML, Python, and JavaScript.

In terms of JavaScript, it includes the parsing of diverse data types onto the webpage and delivering the collected data in various ways. For instance, the character page features interconnected fields that update the database via editable fields without requiring a page reload. Another example is the dynamic reallocation of skills based on a recommendation chart integrated within Python.

I chose Dungeons and Dragons for this project due to its familiarity and the complexity of its cross-data structures. As the project's scope is focused on creating a workflow for TTRPG systems, I havent' fully adapted the entire set of D&D rules into the project, as it would impact the scale but not the complexity of it.

## File Structure

### Back-end
* **/rpg:** The root of the current project
    - **/settings.py:** app route and import/export functionalities 
* **/sheet:** The app for this project
    - **/static and /templates:** folders to hold the front-end
    - **/admin.py:** handles the functionality of the main models.
    - **/data.py:** stores the data that results interesting to manage and control different aspects of the character and databases.
    - **/forms.py:** creates the forms for the character creation.
    - **/login.py:** manages the *login* process of the user
    - **/models.py:** defines *User*, *Character*, *Item*, *CharacterItem* and *Spells* models.
    - **/urls.py:** stores and defines the app's urlpatterns.
    - **/views.py:** defines the view handling for the pages *index*, *databases*, *create_character* and *character_page*. It also handles the stat generator and passes all the data inside **data.py**.

### Front-end
For the purpose of having a cleaner code, I've decided to split the JavaScript and CSS into the different pages.
* **register.html:** 

Where an user can register a new account.

* **login.html:** 

Where an user can login with an account.

* **layout.html:**

The place wherer the BootStrap navbar stays, and where the main JavaScript and CSS files will be loaded

Related files: **styles.cc** and **script.js**.

* **index.html:**

The main page of the platform. The user, after login, can see a display of their current characters and basic info of all of them. Attached to this template there's a series of images that represent the class of each character.

Related files: **index.css** and the folder **/images/**.

* **databases.html:**

A place where a logged-in user can look through all the spells and items contained on the project's database. The search engine displays the reslults dinamically via JavaScript queries.

Related files: **databases.css** and **databases.js**.

* **create_character.html:**

A place where an user can create a character. It's the main purpose of the app, alongisde the character page itself. It's designede to be movile-responsive and to make the character creation a clean, smooth and quick process. All stats are automatically generated and reallocated according to the user's class choice, as well as the character starting equipment.

Related files: **character.css** and **character.js**.

* **character.html:**

A place where a player or a GM can manage their character. Almost all labels are editable and responsive, updating the character's data every time the user leaves the editable field. The items and spells section include a shortened version of the databse search engine limited to 5 results. The modularity of the page also allows for easy editing in case the template needs to be modified.

Related files: **create.css** and **create.js**.

## Installation and usage
1. Clone this repository
2. Run your first migrations: 

`python manage.py makemigrations`

`python manage.py migrate`

3. Run the server:

`python manage.py runserver`

4. Create an user account 


## License
The present project uses [OGL](https://company.wizards.com/en/legal/fancontentpolicy) license to showcase and display Dungeons and Dragons materials educational purposes.