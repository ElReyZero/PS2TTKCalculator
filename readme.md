# Planetside 2 TTK Calculator

This is a tool to help you calculate the theroretical time to kill (TTK) for a given weapon. It is based on the aspects of the [BWAE Battle Bot](https://github.com/ElReyZero/BWAEBattleBot). There will be both a discord bot and a well as a web app in this repo.

Features of the tool (to include or not active in current version):
[ ] Variable Weapon
[ ] Variable Distance
[ ] Where bullets land (Headshots/Bodyshots)
[ ] Heavy Overshield 
[ ] Soft Point Ammo and Hard Point

## Discord bot version of the tool:

### Requirements:
- This project relies on [python dependencies](#python-dependencies).
- A [discord bot application and channels](#discord-bot-component) have to be created.
- To retrieve Planetside2 information a [Daybreak Census ID](#census-id) has to be provided.

### Python dependencies:
- Python 3.8 or above is required to run the project.
- Alternatively, the dependencies are also listed in the `requirements.txt` file (compatible with [venv](https://docs.python.org/3/library/venv.html))

### Discord Bot Component
Create a bot application following the [discord.py documentation](https://discordpy.readthedocs.io/en/latest/discord.html).
The client-secret retrieved at this manual has to put into the configuration file:
```buildoutcfg
[General]
token = RetrievedDiscordApiBotToken
```

### Census ID
Communication with the Daybreak Census API is required to retrieve weapon information, therefore you have to supply a Service ID.
You can apply for one at the [Daybreak Census](http://census.daybreakgames.com/#service-id) website.
Once you obtained an ID, add it the configuration as `api_key`:
```
[General]
api_key = Daybreak_Registered_Service_ID
```

## Web version of the tool (not yet implemented)):

### *TODO*