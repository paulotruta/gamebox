
# Gamebox

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

Go-to self-host app for game archivists! Organize your games library, archive and play retro games using online emulators!

__NOTE: This is a very early stage application and is currently under active development. The current app state as it is available in this repository is not guaranteed to work or be fully safe to use.__


## Features

- Organize your console / games collection
- Automatically pull game metadata from known source websites
- Upload your digitally preserved ROMs
- Play retro games using only your browser! ( _*Limited to supported platforms_ )

  
## Demo

A test deployment is not available at this time ;)

  
## Documentation

The entire project documentation is available in this repository, in the [/docs](/docs) folder. Additions are welcome via PR.



  
## Run Locally

Clone the project

```bash
  git clone https://github.com/paulotruta/gamebox
```

Go to the project directory

```bash
  cd gamebox
```

Start environment

```bash
pipenv shell
  
```

Run migrations

```bash
  python3 manage.py migrate
  
```


Start the server

```bash
  python3 manage.py runserver
```

  
## Running Tests

TODO

  
## Tech Stack

This app uses Wagtail as its building block. Wagtail is based on the Django framework, which itself is created using the Python programming language.

  
## Support

This application is very early stage in its development state, therefore no proper support can be provided. You are welcome to open an issue on this repository and report a problem using the appropriate issue template. Please answer as many questions and provide as most detailed information as possible. I will do my best to get back and help if possible.
  