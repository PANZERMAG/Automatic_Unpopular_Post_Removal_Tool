
<div align="center">
  
  [![License](https://img.shields.io/badge/License-MIT-blue)](#license "Go to license section")
  [![Made with Python](https://img.shields.io/badge/Python->=3.7-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
</div>

<div align="center">
  
  [![PANZERMAG - Automatic_Unpopular_Post_Removal_Tool](https://img.shields.io/static/v1?label=PANZERMAG&message=Automatic_Unpopular_Post_Removal_Tool&color=blue&logo=github)](https://github.com/PANZERMAG/Automatic_Unpopular_Post_Removal_Tool)
  [![stars - badge-generator](https://img.shields.io/github/stars/PANZERMAG/Automatic_Unpopular_Post_Removal_Tool?style=social)](https://github.com/PANZERMAG/Automatic_Unpopular_Post_Removal_Tool)
  [![forks - badge-generator](https://img.shields.io/github/forks/PANZERMAG/Automatic_Unpopular_Post_Removal_Tool?style=social)](https://github.com/PANZERMAG/Automatic_Unpopular_Post_Removal_Tool)
</div>

# Automatic delete unpopular posts from Facebook
In Facebook groups and groups on social networks sometimes posts don't have an expected count of likes. And this app completely solves this problem.



## For whom is this app?

For media influencers who want to have good statistics, for small businesses who want to delete irrelevant posts for subscribers, and for owners of big groups to filter posts.
## Installation

Install this project with git

```bash
  git clone https://github.com/PANZERMAG/Automatic_Unpopular_Post_Removal_Tool.git
```
```bash
  cd your_project_folder/Automatic_Unpopular_Post_Removal_Tool
```
    
## Deployment

Firstly, you need to create a virtual environment

```bash
  python -m venv venv
```

After that, you need to activate the virtual environment.

**For Windows:**
```bash
  venv/Scripst/activate.bat
```
**For Linux:**
```bash
  source venv/Scripts/activate
```

And install the requirement library.

```bash
  pip install -r requirements.txt
```


## Environment Variables

To run this project, you will need to add the following environment variables to your **parametrs.json** file

`email`

`password`

`groups_link`

`likes` - minimal likes at post


## NOTE!
Do not remember to add your web driver to the folder with a project and change the **PATH** in the *main.py* (10 line)
## Run
After all manipulating you can run the *main.py*

**For Windows**
```bash
    python main.py
```

**For Linux**
```bash
    python3 main.py
```
