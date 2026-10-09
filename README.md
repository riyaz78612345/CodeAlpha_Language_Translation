# CodeAlpha Language Translation Tool

Task 1 of my Artificial Intelligence internship at CodeAlpha.

A translation website built with Flask, HTML, CSS and JavaScript.
It uses the MyMemory API to translate short text between selected languages.

## Features

- Source and target language selection
- Text translation
- Copy translated text
- Swap languages
- Clear input and output
- Input validation and error messages
- Responsive webpage

## Technologies

Python, Flask, Requests, HTML, CSS, JavaScript and MyMemory API.

## Project Structure

```text
CodeAlpha_Language_Translation/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Open PowerShell in the project folder:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000 in your browser.
Keep the terminal running while using the website.
Press Ctrl+C in the terminal to stop the server.

## How It Works

1. The user enters text and selects two languages.
2. JavaScript sends the request to the Flask backend.
3. Flask validates the input and calls the MyMemory API.
4. The webpage displays the translated text.

## Limitations

- Internet access is required.
- Each request is limited to 500 UTF-8 bytes.
- The external API has usage limits.
- Translation accuracy and service availability may vary.
- Entered text is sent to MyMemory for translation.

This project integrates an existing translation service.
It does not train a translation model.