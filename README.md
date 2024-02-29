
# EzTasklist

This project contains a simple tasklist. It is designed to quickly and easily manage your tasks with a few button clicks.


## Features

- An input field to add new tasks
- An area to display all current tasks
- A checkbox for each task to delete a task

More features are comming soon.
## Tech Stack

**Client:** React, Axios, TailwindCSS

**Server:** FastAPI (Python)

## Demo
LIVE DEMO: https://croco-dev.xyz/tasklist/
-> Please note that this is only a preview. All data will be deleted from the database every 2 minutes.

Preview:<br />
![demo](https://i.ibb.co/YLR8Whn/Screenshot-2024-02-29-200309.png) <br />


## Clone
1. Clone this repo
2. Go to the client folder
3. Run: 
```bash
npm install -D tailwindcss postcss autoprefixer axios
```
4. In client/src/App.jsx insert your IP or URL where your API runs
5. Go to the server folder
6. Run: 
```bash
pip install -r requirements.txt
```
7. Rename the .example-env to .env and insert your MySQL data there
8. Create a new MySQL Database called "ez_tasklist"
9. Inside there create a new table called "tasks. There should be the Values id(int, AUTO_INCREMENT) and task(LONGTEXT)


To start the application:
1. Go to the client folder and run: 
```bash
npm run dev
```
2. Go to the server folder and run: 
```bash
python main.py
```
## Authors

- [@crocosnipe](https://www.github.com/crocosnipe)

