# Tetromino Falls

Developer: Kristian Colville

[Visit Tetromino Falls](https://tetromino-falls.herokuapp.com/)

(Image of final terminal)

## Table of Contents
* [Project Goals](#project-goals)
    * [User Goals](#user-goals)
    * [Site Owners Goals](#site-owners-goals)
* [User Experience](#user-experience-ux)
    * [Target Audience](#target-audience)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
* [User Stories](#user-stories)
    * [Site User](#site-user)
    * [Site Owner](#site-owner)
* [Design](#design)
    * [Color Scheme](#color-scheme)
    * [Fonts](#color-scheme)
    * [Structure](#color-scheme)
    * [Wireframes](#wireframes)
* [Technologies & Tools](#technologies--tools)
    * [Main Tech](#main-tech)
    * [Python Packages Used](#python-packages-used)
* [Logic](#logic)
    * [Initial Flow](#initial-flow)
    * [Python Logic](#python-logic)
* [Features](#features)
* [Data Model](#data-model)
* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Accessibility](#accessibility)
    * [Performance](#performance)
* [Testing](#testing)
    * [Device Testing](#device-testing)
    * [Testing User Stories](#testing-user-stories)
* [Bugs](#bugs)
* [Deployment](#deployment)
    * [Version Control](#version-control)
    * [Heroku](#heroku)
    * [Local Machine](#local-machine)
    * [Cloning this Repository](#cloning-this-repository)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)


## Project Goals
The goals of this project include:
- Designing an interactive game that takes advantage of a [command line interface](https://en.wikipedia.org/wiki/Command-line_interface).
- It should be highly attractive and visually pleasing to the user of the terminal game. 
- The game is expected to run within a terminal so should be built to take advantage of this scenario.
- The project should be deployed to Heroku.
- The expectation is that the [python language](https://en.wikipedia.org/wiki/Python_(programming_language)) is used throughout.

### User Goals

- To play a terminal based game that is fun and easy to use
- Be able to interact with the game in real time and not stall while waiting for input
### Site Owners Goals

- Create a game that is fun and easy for the user to understand
- Make the terminal game visually attractive to users
- Circumvent waiting for user input within the terminal
- Create the game using python

[Back to Top](#table-of-contents)
## User Experience
### Target Audience
### User Requirements and Expectations
[Back to Top](#table-of-contents)
## User Stories
### Site User
### Site Owner
[Back to Top](#table-of-contents)
## Design
### Color Scheme
### Fonts
### Structure
### Wireframes
[Back to Top](#table-of-contents)
## Technologies & Tools
### Main Tech
### Python Packages Used
[Back to Top](#table-of-contents)
## Logic
### Initial Flow
### Python Logic
[Back to Top](#table-of-contents)
## Features
[Back to Top](#table-of-contents)
## Data Model
[Back to Top](#table-of-contents)
## Validation
### HTML Validation
### CSS Validation
### JavaScript Validation
### Accessibility
### Performance
[Back to Top](#table-of-contents)
## Testing
### Device Testing
### Testing User Stories
[Back to Top](#table-of-contents)
## Bugs
| Bug | Fix |
| --- | --- |
| Curses objects interfering with user input | Tried refactoring code blocks and discovered after trying to make a window class that the issue was because the objects were initialized before trying to get user input, I separated the code structure in run.py and this helped|
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |

[Back to Top](#table-of-contents)
## Deployment
### Local Machine
I used [Ubuntu](https://ubuntu.com/) as my [operating system](https://en.wikipedia.org/wiki/Operating_system) so I could use the non windows version of the python programming language and access the normal [curses module](https://docs.python.org/3/howto/curses.html#the-python-curses-module).

This decision was made to take advantage of the terminal template provided by [Code Institute](https://codeinstitute.net/ie/) for this project.

Please visit the embedded links above for more information.
### Version Control
I used [Visual Studio Code](https://code.visualstudio.com/) as a local repository and IDE & [GitHub](https://github.com/) as a remote repository.

1. Firstly, I needed to create a new repository on Github [tetromino-falls](https://github.com/KristianColville1/tetromino-falls).
2. I opened that repository on my local machine by copying the URL from that repository and cloning it from my IDE for use.
3. Visual Studio Code opened a new workspace for me.
4. I created files and folders to use.
5. To push my newly created files to GitHub I used the terminal by pressing Ctrl + shift + `.
6. A new terminal opened and then I used the below steps.

    - git add (name of the file) *This selects the file for the commit*
    - git commit -m "Commit message: (i.e. Initial commit)" *Allows the developer to assign a specific concise statement to the commit*
    - git push *The final command sends the code to GitHub*

### Heroku
As a deployment solution I chose [Heroku](https://dashboard.heroku.com).

To deploy a project using Heroku follow these steps:

- Log into heroku
- Go to the heroku dashboard
- Create a new app by selecting 'New'
- Give your application a name and select a preferred location
- Click the 'Create app' button
- If you have config variables in your application
    - Click on settings
    - Click 'Reveal config vars'
    - Input your deployment variables

- If you need specific build packs
    - Click on settings
    - Click on build pack
    - Add your packs as needed (Please be aware that the order matters)
    - For Tetromino Falls, Python and then NodeJs was selected.

- Once these steps are completed
    - Go to the deploy section
    - Select your version control system
    - For Tetromino Falls, GitHub was selected

- Connect your version control system
- Add your repository
- Connect the app selecting 'connect'
- Either choose automatic deployment or manual deployment
- Once all these steps are completed and the build is successful
    - You can click the 'view' button
    - It will reveal your deployed app
    
### Cloning this Repository
If you would like to clone this repository please follow the bellow steps.

Instructions:

1. Log into GitHub
2. Navigate to the repository you want to clone
3. Click on the green button labelled 'Code'
4. Copy the URL under the HTTPS option
5. Open an IDE of your choosing that has Git installed
6. Open a new terminal window in your IDE
7. Type this exactly: git clone the-URL-you-copied-from-GitHub
8. Hit Enter

You should have a local copy of the repository to use on your machine.

[Back to Top](#table-of-contents)
## Credits
[Back to Top](#table-of-contents)
## Acknowledgements
[Back to Top](#table-of-contents)