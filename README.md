# Click Boilerplate
Boilerplate project for a the Python Click library. This code can serve as a starting point for your project.
To use it, rename the `cli_app` module to the name of your project and update the `setup.py` to reflect these 
changes.

## Using this boilerplate

In order to use this boilerplate, I recommend doing the following:

- Change the name of the `cli_app` module to something that is relevant to your project
- Update the `setup.py` file, pointing the `console_scripts` option to the updated module name
- Update the `setup.py` file with other values relevant to your project
- Remove the `hello` command and start replacing with commands for your project

## Installing your CLI program

### Development

While developing your CLI program you will want to install it via `setup.py` using the following method:

```
$ python setup.py develop
```

Afterwards, your CLI program will be installed.
If you have installed the default hello command,
a new CLI program called `cli_app` will be available.
Here's how you run it:

```
$ cli_app hello Name
> Hello Name!
```

The main benefit with this method is not having to reinstall everytime a change is made.

### Productions (a.k.a. "for-realsies")

Follow the regular method to install your CLI program into a virtual environment or system Python:

```
$ python setup.py install
```

## Adding more commands

In order to add more commands, 
I recommend adding them to the `cli_app.commands` module as separate files.
Adding them to this directory and as separate files will help keep your project neat and organized.

### But how do I do it?

Great question! Let's say I wanted to add a new command called `weather` that would fetch the current weather
forecast for a city, I would do the following:

1. Create a new file called `weather.py` underneath the `cli_app/commands` directory
2. Put the following code in that file:
```python
import click

@click.command()
@click.argument('city', nargs=-1)
def weather(city):
    """
    Command that retrieves the weather for a given city
    """
    click.echo('75 and SUNNY!!!')
```
3. Let's create a shortcut so it's easier to reference this module later by inserting the following in `cli_app/commands/__init__.py`
```python
# This line should already exist
from .hello import hello
# New entry
from .weather import weather
```
4. Now the final step. Add the following near the bottom of `cli_app/__init__.py`
```python
# All the boilerplate stuff is up here...

# Add Commands
# This line was already here
cli.add_command(commands.hello)
# New entry
cli.add_command(commands.weather)
```

If you have installed the CLI program using the "development" method from above,
you should now be able to run your new sub command:
```
$ cli_app weather Toronto Canada
> 75 and SUNNY!!!
```

## Check out the slides
Here are the slides that accompany this repository:

- [https://docs.google.com/presentation/d/1mNJVFcyuNCSGMgMurWyFeGZWLuOPN6dLWvz279d_P8o/edit?usp=sharing](https://docs.google.com/presentation/d/1mNJVFcyuNCSGMgMurWyFeGZWLuOPN6dLWvz279d_P8o/edit?usp=sharing)
