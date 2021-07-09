# Learning Deploying a Python Flask Example Application Using Heroku

<p align="center">
    <a href="#" alt=""><img src="https://img.shields.io/github/last-commit/Arseni1919/Learnig_Deploy_Flask_to_Heroku" /></a>
    <a href="#" alt=""><img src="https://img.shields.io/github/repo-size/Arseni1919/Learnig_Deploy_Flask_to_Heroku" /></a>
    <a href="#" alt=""><img src="https://img.shields.io/github/license/Arseni1919/Learnig_Deploy_Flask_to_Heroku" /></a>
    <a href="#" alt=""><img src="https://img.shields.io/github/languages/top/Arseni1919/Learnig_Deploy_Flask_to_Heroku" /></a>
    <a href="https://github.com/Arseni1919" alt="Follow"><img src="https://img.shields.io/github/followers/Arseni1919?label=Follow&style=social" /></a>
</p>

## About

Heroku makes building and deploying applications really friendly for developers.
It removes much of the burden related to building and running web applications,
taking care of most infrastructure details and letting you focus on creating and improving the app.
Some of the details handled by Heroku include:

- Provisioning HTTPS certificates
- Managing DNS records
- Running and maintaining servers


## Process

### [Creating the Python Flask Example Application](https://realpython.com/flask-by-example-part-1-project-setup/#creating-the-python-flask-example-application)

- Initializing the Project
- Installing Dependencies
- Freeze Dependencies

```shell
$ python3 -m pip freeze > requirements.txt
```
You’ll use `requirements.txt` when deploying the project to tell Heroku
which packages must be installed to run your application code.

- Writing the Application Code
- Running the Python Flask Example Locally

### [Deploying the Application to Heroku](https://realpython.com/flask-by-example-part-1-project-setup/#deploying-the-application-to-heroku)

- Heroku Account Setup
- Heroku Command-Line Interface (CLI)

The Heroku command-line interface (CLI) is a tool that allows you to create and
manage Heroku applications from the terminal.

Installation:
```shell
$ curl https://cli-assets.heroku.com/install.sh | sh
```

Login:
```shell
$ heroku login
```

- Application Deployment to Heroku

The first step is to create a file named Procfile in the project’s root directory.
This file tells Heroku how to run the app. You can create it by running the following command:
```shell
$ echo "web: gunicorn app:app" > Procfile
```

Note that this filename must start with a capital letter.
This file tells Heroku to serve your application using [Gunicorn](https://gunicorn.org/),
a Python Web Server Gateway Interface (WSGI) HTTP server compatible with various web frameworks,
including Flask. Make sure to install Gunicorn and update the requirements.txt file using pip:
```shell
$ python3 -m pip install gunicorn==20.0.4
$ python3 -m pip freeze > requirements.txt
```

Don't forget to commit all the changes to the Git.

You can create the application in Heroku by running the following command:
```shell
$ heroku create your-unique-name-app
```

Running the above command initializes the Heroku application, creating a Git remote named heroku.
Next, you can push the Git repository to this remote to trigger the building and deployment process:
```shell
$ git push heroku master
```

*Congratulations, the app is now online!*
The output shows the building process, including the installation of dependencies and the deployment.
On line 39, you’ll find the URL for your application.
In this case, it’s https://your-unique-name-app.herokuapp.com/.
You can also use the following Heroku CLI command to open your app’s URL:
```shell
$ heroku open
```


## Redeploy The App

Now let’s make a small change to the app and see how you can redeploy it. Edit `app.py` and modify the string a bit.


## Credits

- [Bootstrap](https://getbootstrap.com/)
- [Bootstrap - Docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Deploying a Python Flask Example Application Using Heroku | Real Python](https://realpython.com/flask-by-example-part-1-project-setup/)
- [Mac: Cmd+Shift+R - hard refresh](https://stackoverflow.com/questions/41144565/flask-does-not-see-change-in-js-file)















