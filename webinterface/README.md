## Prerequisites

1. [Node and npm](https://nodejs.org/en/download/) are installed. Here are the versions I'm using:

    ```shell
    $ node --version
    v8.6.0

    $ npm --version
    8.6.0
    ```
    > Installing npm adds two commands to the system—`npm`.### GitHub
You will need to have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your machine and create a GitHub account that you will be able to log into.
### Python
We used [Python](https://www.python.org/downloads/) version 3.9.12 installed on your machine. Check the version with the following command:
```
python --version
```
### Node.js
Ensure that you have [Node.js](https://nodejs.org/en/download/) version 8.6.0 installed on your machine. Check the version with the following command:
```
npm -v
```

## Installation
### Clone the Repository
The first step is to clone the repository from [GitHub](https://github.com/bvo4/Project-2). You can do this manually from the link by downloading the files or you can run the following command:
```
https://github.com/bvo4/Project-2.git
```
### Install Client Dependencies
Next you will need to install the libraries used on the frontend. To do this, navigate to the webinterface folder using:
```
cd Project-2/webinterface
```
Then, install the required files by running the command:
```
npm i
npm i babel-loader
npm i --save-dev css-loader
npm i --save-dev style-loader
npm i react-native
```

## Running the Website
### Client
After the installations are complete, run the following command to launch the frontend:
```
npm start
```
This will allow you to see the website at http://localhost:3000/CS6903ProjectSite, however this will not work properly until the backend is started in the following steps.


## Viewing the Site
To view the site, navigate to http://localhost:3000/CS6903ProjectSite.
