# Full Stack Skeleton
Full stack bare bones: front end in Reactjs, server, database, REST API in flask

### Environment Setup

Install node and npm:
Install create-react-app
Install react via npm
navigate to client folder, install package.json
```
npm install
```
Start front end
```
npm start
```
Install python3:
```
> brew upgrade python3
```

Install and configure virtualenv:
```
> pip install virtualenv
> mkdir ~/Python_envs
> cd ~/Python_envs
> virtualenv -p /usr/local/Cellar/python3/3.6.2/bin/python3 reactflask
```

# Using and Updating the Environment:
Anytime you want to activate this environment:
```
> source ~/Python_envs/reactflask/bin/activate
```

You will know if you have the environment activated or not from your
command line prompt:
```
(reactflask) >
```

All the required python packages are defined in the
requirements.txt file in the server folder. Use the `pip` command to install or
upgrade. Remember you need to do this each time someone adds a required
package to the project.
```
(reactflask) > pip3 install -r requirements.txt
```

To add a required package to the project, use the `pip freeze` command:
```
(reactflask) > pip3 freeze > requirements.txt
```

Run instructions
install mysql
make database called reactflask
export environment variables from .env file:
```
(reactflask) > source reactflask.env

```
then install mysql, create a database called reactflask 

```
brew install mysql
mysql -u root -p
mysql -u username -p
CREATE DATABASE reactflask;
```
Once database has been created, now you can go to the your virtual environment
and go into the server folder
```
(reactflask) > python3 manage.py db upgrade
(reactflask) > python3 manage.py seed
(reactflask) > python3 run.py
```
