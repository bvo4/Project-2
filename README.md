# Project-2

All resource and code displayed here are down primarily to show what resources we, the libraries implemented, the decision tree algorithms we implemented and designed, and data sets we created and used to train our decision trees.  

The web page implementation was done on a separate Git Repo Located Here:  https://github.com/bvo4/bvo4.github.io

To use the decision tree generator, access is located on this link:  https://colab.research.google.com/drive/1Lqleeot7ubQH8LUeD7cxZ0wVi2PEmT90?usp=sharing

To view the full implementation of the Q&A Interface, visit the github page here:  https://bvo4.github.io/CS6903ProjectSite/

Part 1 Documentation Link:  https://docs.google.com/document/d/16IrAHuETq-MkEepGNEEcd8zJ5tZzzAioAa2U2hmgM2Q/edit?usp=sharing

Part 2 Documentation Link:  https://docs.google.com/document/d/1wMexGlowhvlHOqgJQdsEx_neFY_4jyh48NUh-p15AfA/edit?usp=sharing

Presentation Link:  https://docs.google.com/presentation/d/1zV1qWp1qsaZ9clOtOSEmXB_l4ElH07hs9tHqbN3tKPU/edit?usp=sharing

## Prerequisites

1. [Node and npm](https://nodejs.org/en/download/) are installed. Here are the versions I'm using:

    ```shell
    $ node --version
    v8.6.0

    $ npm --version
    8.6.0
    ```
    > Installing npm adds two commands to the system—`npm` and `npx`—both of which I'll be using while making this tutorial.### GitHub
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
This will allow you to see the website at http://localhost:9500/, however this will not work properly until the backend is started in the following steps.


## Viewing the Site
To view the site, navigate to http://localhost:9500/.
    
