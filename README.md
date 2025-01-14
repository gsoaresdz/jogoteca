<h1 align="center">Jogoteca</h1>
<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/gsoaresdz/jogoteca?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/gsoaresdz/jogoteca?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/gsoaresdz/jogoteca?color=56BEB8">
  <!--<img alt="License" src="https://img.shields.io/github/license/user/jogoteca?color=56BEB8">-->
</p>
<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-execution">Execution</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/gsoaresdz" target="_blank">Author</a>
</p>
<br>

## **:dart: About**

This project is a web application called Jogoteca, which allows users to register, view, and manage information about games. The application uses the Flask framework for web development and includes features such as user authentication, image uploads, and database management.

## **:memo: Project Structure**

The project structure is organized as follows:

- **config.py:** Application configurations.
- **helpers.py:** Auxiliary functions.
- **jogoteca.py:** Main application file.
- **models.py:** Database model definitions.
- **prepara_banco.py:** Script to prepare the database.
- **static:** Static files (CSS, JS, images).
- **templates:** HTML templates.
- **uploads:** Directory for image uploads.
- **views_game.py:** Views related to games.
- **views_user.py:** Views related to users.

## **:sparkles: Features**

:heavy_check_mark: **Feature 1**: User registration and authentication.

:heavy_check_mark: **Feature 2**: Game registration, viewing, and management.

:heavy_check_mark: **Feature 3**: Image uploads for games.

:heavy_check_mark: **Feature 4**: User-friendly interface using HTML templates.

## **:rocket: Technologies**

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [SQLite](https://www.sqlite.org/)
- [Jinja2](https://pypi.org/project/Jinja2/)
- [Werkzeug](https://pypi.org/project/Werkzeug/)

## **:white_check_mark: Requirements**

Before starting :checkered_flag:, make sure you have [Git](https://git-scm.com/) and [Python](https://www.python.org/) installed.

## **:checkered_flag: Execution**

```bash
# Clone the project
$ git clone https://github.com/gsoaresdz/jogoteca.git

# Navigate to the project directory
$ cd jogoteca

# Create a virtual environment
$ python -m venv venv

# Activate the virtual environment
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
$ pip install -r requirements.txt

# Prepare the database
$ python prepara_banco.py

# Run the application
$ flask run

# The application will be available at http://127.0.0.1:5000

```

## **:memo: License**

This project is under the MIT license. For more details, see the [LICENSE](LICENSE) file.

Made with :heart: by <a href="https://github.com/gsoaresdz" target="_blank">gsoaresdz</a>

<a href="#top">Back to top</a>
