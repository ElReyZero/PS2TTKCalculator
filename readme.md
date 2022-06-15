# Planetside 2 TTK Calculator

This is a tool to help you calculate the theroretical time to kill (TTK) for a given weapon. It is based on the aspects of the [BWAE Battle Bot](https://github.com/ElReyZero/BWAEBattleBot). There will be both a python script as well as a web app in this repo.

Features of the tool (to include or not active in current version):
[X] Variable Weapon  
[X] Variable Distance  
[ ] Where bullets land (Headshots/Bodyshots)  
[X] Heavy Overshield   
[ ] Soft Point Ammo and Hard Velocity Ammo  

### Requirements:
- This project relies on [python dependencies](#python-dependencies).
- A [discord bot application and channels](#discord-bot-component) have to be created.
- To retrieve Planetside2 information a [Daybreak Census ID](#census-id) has to be provided.

### Python dependencies:
- Python 3.8 or above is required to run the project.
- Alternatively, the dependencies are also listed in the `requirements.txt` file (compatible with [venv](https://docs.python.org/3/library/venv.html))

### Census ID
Communication with the Daybreak Census API is required to retrieve weapon information, therefore you have to supply a Service ID.
You can apply for one at the [Daybreak Census](http://census.daybreakgames.com/#service-id) website.
Once you obtained an ID, add it the configuration as `api_key`:
```
[General]
api_key = Daybreak_Registered_Service_ID
```

## Web version of the tool:
This project uses the Django framework to implement its web version, in order for it to work, you need to set up a django token on the config file:
```
[Django]
django_key=Generated_Django_Secret_Key
```

### Database
This project uses a PostgreSQL database to store and query the weapon information used to calculate the TTK.

```
[Database]
host= Database Host
name= Database Name
user= Database User
password= Database Password
```

### *TODO*
Run the web server with the following commands:

Windows:
```
python manage.py runserver
```

Linux:
```
python3 manage.py runserver
```