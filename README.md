# Fake News Detection
A fake news detection Ai model created while interfacing it to an Electron app

### How To Setup This Project
1) Git clone the entire repository using the following command
```sh 
$ git clone https://github.com/Hecker-Squad/Fake-News-Detection.git
```

2) To install the libraries for `FakeNews-FrontEnd`, run the following command:
```sh
$ pip install -r requirements.txt
```

3) To install the libraries for `FakeNews-BackEnd`, run the following command:
```sh
$ npm i
```

### How To Run This Project

1) Setup the ML flask server by typing the following command:
```sh
$ python flask_app.py
```

2) Run the Electron app by typing the following command:
```sh
$ npm run dev
```

### How To Use This Project

Type the news headlines in the text box and press submit and you will get a simple pop up which will show whether the news is `FAKE` or `REAL`