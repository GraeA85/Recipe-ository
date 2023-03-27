# Westhill Fitness - Two Week Shred Website

## Milestone Project 3 - Backend Development

<h2 align="center"><img src="./static/images/amiresponsive.jpg"></h2>

* The Westhill Fitnes Shred website is designed to accompany a two-week fitness programme used by a local fitness company. The website allows users to access shopping lists, food plans and recipes, as well as contribute recipes for future shreds. It allows the user full CRUD functionality - users can create new recipes, which are stored in a backend database (mongodb), search and retrieve recipes on the website, edit/update their contributed recipes and also delete them if necessary.

* I got the idea for the website from a local fitness company that I have used to participate in a health shred. A health shred is designed to give you meal plans and exercises that should be used over a two week period. It is designed to help users lose weight. The local company which I have based the idea currently use paper plans/paper recipe books which are given to members. I decided this would
be a good basis for a website, allowing users to access their shopping list and meal plans on their mobile phones or computers - making it much easier to follow recipes in their kitchen or access shopping lists in the supermarket.


* This is my Milestone Project 3 submission for Code Institute's Diploma in Web Application Development course. My website uses a backend database, features full CRUD functionality and is built using technologies that I have learnt including HTML, CSS, JavaScript, Python, Flask and PyMongo.

## Live Project

[View the live project here.](https://recipe-ository.herokuapp.com/)

## Repository

[Find the project repository here.](https://github.com/GraeA85/Recipe-ository)

# Table of Contents

## Contents
- [User experience](#user-experience)
  * [User Stories](#user-stories)
    + [First-time Users](#first-time-users)
    + [Returning Users](#returning-users)
    + [Business Owner](#business-owner)
- [Design](#design)
  + [Overview](#overview)
  + [Colour Scheme](#colour-scheme)
  + [Typography](#typography)
  + [Imagery and Aesthetics](#imagery-and-aesthetics)
  + [Icons](#icons)
  + [Cards](#cards)
- [Wireframes](#wireframes)
- [Features](#features)
  + [All Pages Features](#all-pages-features)
  + [Index (Landing Page) Features](#index-landing-page-features)
  + [Register/ Log In Pages Features](#-register-log-in-pages-features)
  + [Find Recipes Page Features](#find-recipes-page-features)
  + [View Recipe Page Features](#view-recipe-page-features)
  + [Recipe page features](#recipes-page-features)
  + [Error Handling](#error-handling)
- [Future Features](#future-features)
  + [User Experience Features](#user-experience-features)
  + [Development Features](#development-features)
- [Data Model](#data-model)
- [Technologies used](#technologies-used)
  + [Languages Used](#languages-used)
  + [Frameworks Libraries and Programs](#frameworks-libraries-and-programs)
- [Testing](#testing)
- [Deployment](#deployment)
  + [Creating a Gitpod Workspace](#creating-a-gitpod-workspace)
  + [GitHub Pages](#github-pages)
  + [Forking the GitHub Repository](#forking-the-github-repository)
  + [Making a Local Clone](#making-a-local-clone)
  + [Creating an application with Heroku](#creating-an-application-with-heroku)
- [Credits](#credits)
  + [Code](#code)
  + [Media](#media)
  + [Content](#content)
  + [Acknowledgements](#acknowledgements)

# User Experience

## User stoires

### First-time Users

* As a first-time user, I want the landing page of the website to explain the purpose of the website and allow me to preview the content.

* As a first-time user, I want to be able to register for an account.

* As a first-time user, I want the website to work on any device.

### Returning Users

* As a returning user, I want to be able to log in to my account.

* As a returning user, I want to be able to create/ view/ edit/ delete my own recipes.

* As a returning user, I want to be able to view recipes that are used in the two-week shred

* As a returning user, I want to be able to access my shopping lists and meal plans to plan accordingly for the two-week shred

* As a returning user, I want recipes to include useful information such as a title, ingredient list, instructions broken down into steps, time to make, calorie count and an image of the food.

* As a returning user, I want to be able to search for recipes, to make it quicker to find recipes with a certain word in their name, or by recipe category (breakfast, snack or lunch/dinner)
 
* As a returning user, I want to be able to search for recipes, to make it quicker to find recipes with a certain word in their name or category (breakfast/snack/lunch/dinner).

* As a returning user, I want to be able to access and use the website on any device.

### Buisness Owner

* As a business owner, I want users to be able to create, edit and delete their own recipes, but not those of any other user.

* As a business owner, I want the adding, editing and deleting of recipe categories to be limited to admin or those with permission. 

* As a business owner, I want it to be as easy as possible for users to submit recipes, e.g. they can copy and paste an ingredients list in, but it will display in a formatted and easy to read list on the recipe page.

* As a business owner, I want the website to function and look good on any device.

## Design

### Overview

- The website design is simple, colourful and youthful. I looked at the design of cookbooks and similar recipe websites for inspiration. The Shred website's aesthetic is simple yet full of character, inviting and easy to use.

### Colour
<h2 align="center"><img src="./static/images/colorpal.jpg"></h2>
<br>

- The Shred website uses a simple colour scheme of black, white, light grey and dark grey with turquoises, yellow and browns. The background is white, with a Westhill Signature turqouise chosen for the navbar and a two-tone grey footer. I have used cards with a white background for areas of dense text for improved legibility. The website brand, social media icons and anchor links are in the website’s footer in antique white. Buttons are either in brown or greens and reds.

### Typography

- Headings and recipes are in 'Poiret One' with cursive as a fallback font. Other texts are presented with the 'Edu NSW ACT Foundation' font as it stands out on all devices and gives that "notebook" feel as the website is updated frequently to account for new shreds every season of the year.

### Imagery 

- I have not used much imagery on the website, as users can post an image URL for the recipes they upload. There is a splash image on the landing page to set the tone of the website (healthy foods only!) - I have set the image as transparent for appropriate styling of the website.

### Icons

- Font awesome icons are used throughout the website, mainly sticking with the food/fitness theme. 

### Cards

- I have used Materialize CSS card components for displaying recipes and forms. This makes the content stand out from the website background. It also neatly presents the various recipes, which can be easily accessed on a desktop PC or mobile phone.

# Wireframes

- [View my homepage wireframe in PDF form here](./static/images/westhill-home.pdf)
- [View my recipe page wireframe in PDF form here](./static/images/westhill-recipe.pdf)


# Features

## All Pages Features

### Nav Bar

<h2 align="center"><img src="./static/images/westhill-loggedout.jpg"></h2>
<h2 align="center"><img src="./static/images/westhill-adminlogin.jpg"></h2>
<h2 align="center"><img src="./static/images/westhill-loginuser.jpg"></h2>
<h2 align="left"><img src="./static/images/westhill-nav-mobile.jpg"></h2>
<h2 align="left"><img src="./static/images/westhill-mobile-nav.jpg"></h2>

- The nav bar presents different options whether the user is logged in or logged out or an administrator.

- The links change colour on hover, to signal to the user which link they have the mouse over.

- The logo links back to the main landing page.

- The nav bar turns into a slide-out menu on smaller screen sizes

### Footer 

<h2 align="center"><img src="./static/images/westhill-footer.jpg"></h2>

- The footer includes the website’s name and location. 

- It also features icons with external links to social media. These windows open in a new tab. The icons feature ARIA labels for accessibility best practices.

### Flash Messages

<h2 align="center"><img src="./static/images/westhill-welcomeflash.jpg"></h2>

- Flash messages appear to confirm when a user has completed an action, namely logging in, logging out, editing a recipe and deleting a recipe.

- The styling of the flash messages is inkeeping with the rest of the site and colour scheme. They alert the user when required but not enough to cause alert fatigue.

## Index (Landing Page) Features

<h2 align="center"><img src="./static/images/westhill-homelogin.jpg"></h2>

- The purpose of the Westhill Fitness Shred Homepage is to explain the purpose of the website. It does this with an eye-catching jumbatron, short explanation and a 'three-across' explainer section with icons, allowing the user to access their shopping lists, recipes and meal plans. These cards are only accessible once the user is registered and logged in, if not logged in the user is drawn to the GET STARTED button as part of the jumbotron. 

- Once a users are logged in, the navbar buttons on the landing page change. This means that the page is still useful for a returning user, as it directs them to different pages within the website.

## Register/ Log In Pages Features

<h2 align="center"><img src="./static/images/westhill-register.jpg"></h2>

<h2 align="center"><img src="./static/images/westhill-login.jpg"></h2>

- The Register and Log in pages both feature forms, a large submit button, and a link to the login page in case a user misclicks.

- The Register form features input fields for Username and Password. All fields are required.

- The Log in form features input fields for Username and Password. All fields are required.

- The User's password is hashed for security.

<h2 align="center"><img src="./static/images/westhill-exists.jpg"></h2>

- Each Username must be unique, If it already exists, a flash message informs the user to try another username.

<h2 align="center"><img src="./static/images/westhill-incorrect.jpg"></h2>

- If incorrect log in details are provided, a flash message informs the user that the Username and/or password is incorrect.

<br>


## Recipes Page Features

<h2 align="center"><img src="./static/images/westhill-adminrecipes.jpg"></h2>

- The purpose of this page is to show the users all recipes. This includes their own recipes and those recipes added as part of the shred mealplan.

- From this page, users can search recipes, quick-view recipes, edit and delete recipes (only recipes that the user has added).

- The user's own recipes appear in the same way as those added as part of the meal plan. I chose to do this to keep the format neat. The delete and edit buttons are only viewable for the user that added them, and admin.

### Search Recipes

- The search feature uses a MongoDB's index. This returns search results based on the recipe name and recipe category.

<h2 align="center"><img src="./static/images/westhill-noresults.jpg"></h2>

- If no results are found, then a message appears to inform the user.
<br><br>
## Quick View Recipes

<h2 align="center"><img src="./static/images/westhill-recipecard.jpg"></h2>
<h2 align="center"><img src="./static/images/westhill-recipeopen.jpg"></h2>

- The quick-view expands the information on the card, that the user can scroll through without navigating away from the page. 

- The quick-view is accessed by pressing the button with an  eye icon. There is a tooltip that appears when the button is hovered over and an Aria Label for screenreaders.

- I included this feature to help keep the recipe cards neat and consistent. The intital information that the user can see is the recipe image (if provided) and title.

- To see the full details of the recipe (ingredients and instructions list) the user simply clicks the eye icon, and the cross button to return to the recipe card.


## Add Recipe feature

- The website allows users to add their own recipes as well as edit and delete. The main reason for this is to encourage users to look for healthy recipes - if they submit them to the website they may be used in the next seasons shred, which rewards those whos recipes get chosen.

<h2 align="center"><img src="./static/images/westhill-addrecipe.jpg"></h2>

- The add recipe feature takes the user to a form to input the recipe. They must select a category (breakfast/snack/lunch/dinner), recipe name (minimum 5 characters), ingredients list (user is prompted to add each ingredient to a new line), instructions (new line for each instruction), prep and cooking time, calories per serving and how many people served. There is an option to add a URL of an image - this is designed to be held externally (i.e. free images/images with permission). The url must end in the appropriate image format to display correctly.

<h2 align="center"><img src="./static/images/westhill-success.jpg"></h2>

- Once a recipe is successfully created, the user is taken back to the recipe page and a flash message shown to confirm addition of recipe.

## Edit Recipe Page Features

<h2 align="center"><img src="./static/images/westhill-edit.jpg"></h2>

- If a user wishes to edit their recipe they will be taken back to the add recipe page with the form fields pre-populated with their previous entries. Once the editing is finished the user clicks the button to confirm. If no changes are required the user can click cancel editing to return to the recipe page.

<h2 align="center"><img src="./static/images/westhill-editflash.jpg"></h2>

- Once the changes are confirmed a flash message will display to the user back on the recipe page.
<br><br>
### Recipe form considerations
<br>

- It was quite challenging to get the right balance between user friendliness, and making sure the recipes were well presented on the website correctly.

- I experimented with storing the ingredients and instructions in an array rather than a string on mongoDB, however this proved too difficult when it came to editing a recipe and displaying correctly.

- Using information on slack and stack overflow, i found that it would be easier to store the instructions and ingredients as one string like the other fields, each on their own line. Using a method available within jinja, i used the .splitlines function which stores the recipe ingredients in a single string within mongoDB whilst also showing a user-friendly list when the user wanted to edit their recipe (each ingredient and instruction displays on a seperate line for easy editing).

- Through testing I have found no issues with copy and pasting of ingredient lists and instructions which is a massive positive for user-friendliness on the site.

<br>

## Manage Recipe Categories Page Features

<h2 align="center"><img src="./static/images/westhill-categories.jpg"></h2>

- This page is available to admin accounts only. It allows admin to add/edit the recipe categories that are available for the recipes to be stored under. Similar to the adding and editing of recipes, flash messages will confirm to the admin when categories have been successfully added or edited.

## Error Handling

- In most instances if there is an error, e.g. the recipe id in the page URL is changed, then the user will be redirected back to the Find Recipes page. Logged-out-users will be directed to the log in page, as they cannot access the Find Recipes page.

- If the user's session cookie deleted, they will also be logged out and unable to access logged-in features.

# Future Features

## User Experience Features 
<br>

### Current day of Shred Recipes on Home page

- It would be good for the user experience to display each days recipes on the homepage underneath the current navigation cards. This would be coded to change the recipes on each day of the shred to allow the users quicker access to the appropriate recipes.

### Seperate recipe pages for current shred recipes and user submitted

- Currently, all recipes are stored on the same page. In the future it would be good for the user submitted recipes and the current meal plan recipes to be shown on different pages so users have less information to look at when it is not required.

### Favourite Recipes

- A future feature would allow users to 'favourite' recipes they like to use outside of the shred. These would be stored on a "my favourites" page or on their profile page.

### Confirm delete of items

- A confirm deletion button to prevent users accidently deleting recipes

### Profile Page - weights

- The profile page is present, however it is currently marked with a coming soon. This page would allow the user to store their weights and measurements (which users typically record before and after the shred). It would record their weights before the shred began, after week one and at the end. This could then be used (with permission) to show a leaderboard of which users have lost the most weight during the shred.

### Profile page - images

- The ability for the users to upload and store their before and after body pictures, which is encouraged at each shred (the members are asked to take before and after photos to allow them to see the difference in their body shapes after the shred).

### Add edit/ delete user account functionality including reset password

- This would allow the user to edit their username or password, or delete their account.

### Add an authentication code when registering

- The Shred is a paid-for service in Westhill Fitness. To be able to register an account the user must have an authentication code that they would recieve from the owners once they had paid for the shred. Without this code the user wouldn't be able to register for an account and access the content available. 

- Alternitavely, add a feature that allows the website to take payment before being able to register for an account.

### Contact admin button

- I could add a contact admin button, to notify admin if there is an error out of hours.

### Food Shopping Links

- Links to external supermarket websites for the shopping lists, which automatically put all required items in your shopping basket instantly, allowing the user to have the food delivered if desired.

### Links to Recipes from Meal Plan Site

- Users to be able to click through directly from the meal plan to each specified recipe.

### Automated Testing

- I would like to add more automated tests for my Python and Javascript files. This would mean that developers who work on the website in the future can add new features and be sure they are not breaking the code.

# Data Model

- [View my Database structure in PDF form here](./static/images/Recipe-Store-Westhill-Fitness.pdf).

# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- [PyMongo](https://pymongo.readthedocs.io/en/stable/)

## Frameworks Libraries and Programs

- [Heroku](https://id.heroku.com/login)
  - Heroku is the deployment source I used for this project. I'm also using it for the Postgres relational database

- [MongoDB](https://www.mongodb.com/)
    - I'm using MongoDB for my non-relational database.

- [Flask](https://flask.palletsprojects.com/en/2.2.x/templating/)
  - Templating language I've used with Python to add logic to my html templates.

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
  - Templating language I've used with Python to add logic to my html templates.

- [Materialize CSS](https://materializecss.com/)
  - Front-end library with HTML, CSS and Javascript based components. I used Nav bar, Cards, Buttons and Forms.

- [Google Fonts](https://fonts.google.com/)
  - Two fonts are imported from google fonts.
  
- [Font awesome](https://fontawesome.com/)
  - I used icons from font awesome on buttons.

- [Github](https://github.com/)
  - Github was used to create and store the project repository.

- [Gitpod](https://gitpod.io/)
  - Gitpod was used to create my files and where I wrote the code.

- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to create Wireframes for the project during the initial planning stage.

- [Techsini](https://techsini.com/multi-mockup/)
  - Techsini was used to help check responsiveness and take screenshots of the page at different screen sizes.

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
  - Google Chrome's Dev Tools were used while building the project to test responsiveness and for debugging.

- [dbdiagram](https://dbdiagram.io/)
  - Tool used to mock up database structure diagram.

# Testing

- Please refer [here](TESTING.md) for more information on testing carried out

# Deployment

## Creating a Gitpod Workspace

The project was created in Gitpod using the Code Institute Gitpod Full Template using these steps:

1. Log in to GitHub and go to the [Code Institute student template for Gitpod](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this Template' next to the Green Gitpod button.
3. Add a repository name and click 'Create reposiory from template'.
4. This will create a copy of the template in your own repository. Now you can click the green 'Gitpod' button to open a workspace in Gitpod.

## Forking the GitHub Repository

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the GitHub Repository
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

You will now have a fork of the repository, but you don't have the files in that repository locally on your computer.

To make a local clone:

1. Log in to GitHub and go to the GitHub Repository
2. Above the list of files, click  Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the 'Copy' icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the 'Copy' icon. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the 'Copy' icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub AE username instead of YOUR-USERNAME:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `website`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

## Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a requirements.txt file by typing ``` pip3 freeze --local > requirements.txt ``` into the Gitpod CLI. Ensure this is added to your .gitignore file.
2. Create a Procfile by typing ```echo web: python app.py > Procfile```. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
3. Add and commit these files to Github.
4. Go to [Heroku](https://dashboard.heroku.com/apps). Log in or create an account
5. Click the 'New' button and click 'Create new app'.
6. Enter a unique name for your project with no capital letters or spaces and select your region. Click 'Create App'.
7. Inside your project, go to the Resources tab and create a Heroku Postgres Database
8. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
9. Add in the following variables
  - IP : 0.0.0.0
  - PORT : 5000
  - MONGO_DBNAME : Your MongoDB database name
  - MONGO_URI : This can be found on MongoDB by going to Clusters, Connect, Connect to your application
  - SECRET_KEY : Your secret key
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. To connect your Heroku database, go to 'More' in the top right and select run console. Enter ```python3``` to access the python intepreter.
13. Then type ```From recipe-ository import db```. Then type ```db.create_all()```. You can then exit the console.

# Credits

## Code

- Materalize CSS: I used this library throughout the project. Particularly for the nav bar, cards, forms and buttons.

- Code Institute: Task Manager walkthrough product was used as the basis of this website with further added functionality and custom CSS styling throughout.

- Stack Overflow: I referred to Stack Overflow articles throughout the project. Mainly used for the storage of the recipe ingredients and instructions - jinja function.

- Slack: Many users ran into similar issues during their projects and the information proved invaluable during the creation of my project.

- Documentation:  [Python](https://docs.python.org/3/library/exceptions.html), [Jest](https://jestjs.io/docs/getting-started), [MongoDB](https://www.mongodb.com/docs/manual/reference/method/ObjectId.valueOf/), [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)

## Content

East Coast Fitness Shred Cookbook for recipes, meal plans and shopping lists were used for the bulk of the website content.


## Acknowledgements

Thank you to all my users who tested the website and highlighted any issues/bugs to me. 

Please note this is a personal project. This website is purely for the sake of the developer's portfolio and not for public consumption.

