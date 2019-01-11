# trustometer

<img src="https://img.shields.io/badge/version-0.4.0-green.svg" />

Fake news verifier Chrome extension using AWS Comprehend and News API

The Chrome extension is based on a [Node.js](https://nodejs.org/) server. It scrap the title of the desired webpage using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/doc) library and search for similar news with the [News API](https://newsapi.org). Then, it uses [AWS Comprehend](https://aws.amazon.com/es/comprehend/) to analize every title for them comparing it to the title of the main new.

## Authors:
This prototype app was made by us while participating in the [HackUPC 2018 Edition](https://hackupc.com). They made a great job to make the hackathon possible!
* [Kevin Rosales](https://github.com/kevindx98) 
* [Adrián Lorenzo](https://github.com/AdrianLorenzoDev) 
* [Borja Zarco](https://github.com/BorjaZarco) 
* [Héctor Henríquez](https://github.com/hectorhc2014) 

## Install:

### Server

After cloning the repository, at the directory, use this command to install dependencies:

```
npm install
```

For python dependencies, install:

```
pip install bs4 requests awscli json --update
```

Before running, make sure your AWS credentials at *env.cred.json* editing the file:

```
"AWS_USER":""
"AWS_CREDENTIALS":""
```

Also, remember to add the News API key if you want to make it working properly

To start the server, just use the npm command that enables it:

```
npm run dev
```

### Extension

1. At Chrome, go to ```chrome://extensions```. Then **enable the Developer Mode**.
2. Then, press **load unpacked**.
3. Finally, select your project folder.
