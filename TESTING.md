# Testing

The Westhill Fitness Shred website has been tested using the following methods:
- [Code Validation](#code-validation)
    - [W3C HTML Validator](#w3c-html-validator) 
    - [W3C CSS Validator](#w3c-css-validator)
    - [JSHINT Javascript Code Quality Tool](#jshint-javascript-code-quality-tool)
    - [Python Validation using Gitpod](python-validation-using-gitpod)
- [Wave Webaim Accessibility Checker](#wave-webaim-accessibility-checker)
- [Lighthouse](#lighthouse)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Testing User Stories](#testing-user-stories)
    - [First Time User](#first-time-user)
    - [Returning User](#returning-user)
    - [Business Owner](#business-owner)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [Peer Review](#peer-review)
- [Bugs](#bugs)
    - [Resolved](#resolved)
    - [Unresolved](#unresolved)

# Code Validation

## W3C HTML Validator

- The Westhill Fitness website passed all tests using the [W3C HTML](https://validator.w3.org/) Validator tool, any errors that were thrown were due to the jinja language and were in themselves not errors.

- Minor errors such as missing closing tags were shown, these were all updated accordingly.

## W3C CSS Validator

- The Westhill Fitness website passed all tests using the [W3C CSS](https://jigsaw.w3.org/css-validator/) Validator tool, any errors that were thrown up were due to vendor extensions and were in themselves not errors.

## JSHINT Javascript Code Quality Tool

- The Westhill Fitness website passed all tests using the [JSHint](https://jshint.com/) Validator tool

## Python Validation using Gitpod

- Errors and warnings highlighted by Gitpod included:
   
   - Only minor errors relating to line length and indentation were shown however these do not affect the running of the python app in any way.

# Wave Webaim Accessibility Checker

- The index page was tested using the [Wave Webaim](https://wave.webaim.org/) accessibility checker and no serious issues were found. 

# Lighthouse

I used the Lighthouse reports in Google Developer Tools to examine the pages of the website for the following
- Performace
- Accessibility
- Best Practices 
- SEO

- The website scored well in all areas on mobile and desktop screens.

# Browser Compatibility

The site was tested in Microsoft Edge and Mozilla Firefox on desktop.

The site was tested in Microsoft Edge and Safari on mobile and tablet.

No issues arose during browser testing.

# Responsiveness

Responsivity tests were carried out using Google Chrome DevTools. Device screen sizes covered include:
- iPhone SE
- iPhone XR
- iPhone 12 Pro
- Pixel 5
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- iPad Mini
- iPad Air
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/71
- Nest Hub
- Nest Hub Max

I also personally tested the website on Android 13 mobile phone and Microsoft Surface Tablet.

# Testing User Stories

### First-time Users

- As a first-time user, I want the landing page of the website to explain the purpose of the website and allow me to preview the content.

    - The landing page of the website features an eye-grabbing jumbatron with an image and tag line which gives a feel and overview of the website. There is also a 'Three-across' section which explains the features in more detail.
    - The website footer also features the website's name and social media links.

* As a first-time user, I want to be able to register for an account.
     - There is a sign up page. These can be accessed from the nav bar and also from a button on the homepage when not logged in.
     - There is also a link on the log in page.

* As a first-time user, I want the website to work on any device.

    - The website is fully responsive and works on any device size. This was tested on developer tools as well as several devices.

### Returning Users

* As a returning user, I want to be able to log in to my account.
    - There is a log in page. This can accessed from the nav bar. There is also a link at the bottom of the sign up page.

* As a returning user, I want to be able to create/ view/ edit/ delete my own recipes.
    - Users can create recipes via the Recipe page when logged in
    - Users can edit their own recipes via the Edit Recipe button shown on each of their own recipe cards
    - Users can delete their own recipes via the Delete Recipe button shown on each of their own recipe cards
    - Users can only edit and delete their own recipes.

* As a returning user, I want to be able to view other user’s recipes.
    - Logged in users can access the Find Recipes page, which shows all user's recipes and recipes that are in the current shred meal plan.

* As a returning user, I want recipes to include useful information such as a title, ingredient list, instructions broken down into steps, prep and cooking time, recipe category, serving sizee, calories per serving and a link to a URL and an image.
    - These features are included on the recipe page

* As a returning user, I want to be able to get a quick overview of a recipe

    - The user can use the Quick-View feature to quickly see more about a recipe.
    - The user can choose to View the Recipe to get the recipe presently clearly on its own page.

* As a returning user, I want to be able to search for recipes, to make it quicker to find recipes with a certain word in their name or by recipe category
    - The user can use the search function on the Find Recipes page.

* As a returning user, I want to be able to access and use the website on any device.
    - The website is functional on any screen size.

### Buisness Owner

* As a business owner, I want only logged in users to be able to see and contribute to the recipes. I want user to only be able to edit and delete their own recipes, but not those of any other user.
    - There are permissions in place, so users must be logged in to access certain pages, and users can only edit and delete their own recipes.

* As a business owner, I want the adding, editing and deleting of recipe categories to be limited to admin only
    - There are permissions in place, so users must be admins to access the manage categories page, and admins can only edit and delete these

* As a business owner, I want it to be as easy as possible for users to submit recipes, e.g. they can copy and paste an ingredients list in.
    - There are text-area inputs so that users can copy and paste recipes in. The recipe ingredients and instructions are easily edited if needed.

* As a business owner, I want the website to function and look good on any device.
    - The website functions and looks good on any device size.

# Manual Testing

## Nav Bar

* The main navigation buttons have been tested and work correctly
* User permissions have been tested and work correctly

## Footer

* Social links in the footer have been tested and work correctly, opening in a seperate tab.

## Flash Messages

* Flash messages show and disappear appropriately with every website function

## Index Page

* Buttons have been tested and all work correctly
* User permissions showing the correct buttons have been tested and work correctly

## Register/ Log In Pages

* Buttons, forms and links have been tested and work correctly
* I've tested using a non-unique username. The appropriate flash message is displayed warning the user that the username is taken.
* I've tested logging in with incorrect details. The appropriate flash message is displayed warning the user that the details are incorrect.

## Find Recipes

* The search and reset buttons were tested and work correctly.
* Search has been tested and works correctly, both with a valid and invalid item.

## Submit/ Edit Recipe

* Buttons and forms have been tested and all work correctly.
* I have tested editing a recipe - the existing recipe is pre-populated correctly and can be edited with ease. Saving the update correctly updates the correct information.

## Delete Recipe

* Buttons and forms have been tested and work correctly.
* I have tested deleting a recipe created by myself - the recipe is removed successfully and a flash message is displayed confirming this.
* I have tested deleting recipes that were created by another user - the option is not available therefore this functions correctly.

## Manage Recipe Categories

* Buttons have been tested and work correctly.
* Recipe categories can be added, edited and deleted appropriately, by only admin login.


# Peer Review

I asked family members to test the website, ensuring they accessed each function and page of the website, thoroughly testing every available option.

- Feedback included:
    - Main font used on the index page did not stand out sufficiently and was sometimes difficult to read. I changed the font to a more readable font for some parts of the website. I was also told the jumbotron text needed splitting up, therefore I added a hr.
    
# Bugs

No major bugs were highlighted through peer testing as well as my own testing. Any feedback received was taken into account and acted upon accordingly, as mentioned.

Back to [README.md](/README.md#testing)