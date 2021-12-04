# hungry_geese_game
---
This repository contains the the models and code that I used for my submission in the hungry geese kaggle [competition](https://www.kaggle.com/c/hungry-geese). Which I ranked 20th for.

I have built a pygame application that allows you to play against two versions of my model and a hard coded agent.

## 1.Running executable in Windows
---

To run the game in Windows open power shell and change the directory to the path where you have downloaded the repository.

```
cd <your/saved/path>/hungry_geese_game
```

Since the size of the files in the executable were to large for git, you will need to download the [dist_windows.zip](https://drive.google.com/drive/folders/1cDl3fCa8Z1opo0D88E5YCO4ZWhyC_Tjw?usp=sharing) file, save it within the repository folder and extract it.


Once you have done this run the following command to launch the executable. This will launch the pygame application and you can start playing the game.
```
.\dist_windows\hungry_geese_game\hungry_geese_game.exe
```

## 2.Running executable in Linux
---

To run the game in Linux open a terminal and change the directory to the path where you have downloaded the repository.

```
cd <your/saved/path>/hungry_geese_game
```

Since the size of the files in the executable were to large for git, you will need to download the [dist_linux.zip](https://drive.google.com/drive/folders/1cDl3fCa8Z1opo0D88E5YCO4ZWhyC_Tjw?usp=sharing) file, save it within the repository folder and extract it.


Once you have done this run the following command to launch the executable. This will launch the pygame application and you can start playing the game.
```
dist_linux/hungry_geese_game/hungry_geese_game
```

## 3. Running from python

To run from python, install the dependencies and run the following command in the terminal.
```
# Move into directory
cd <your/saved/path>/hungry_geese_game

# install dependencies
pip install -r requirements.txt

# Run game
python hungry_geese_game.py
```
