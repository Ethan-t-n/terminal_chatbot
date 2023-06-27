# terminal_chatbot

This is a simple chatbot project built using OpenAI's ChatGPT.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Gitignore](#gitignore)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The chatbot project utilizes OpenAI's ChatGPT to provide interactive conversations. It takes user input and generates responses based on the trained model.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip3 install openai pyyaml` in your project's virtual environment.
3. Ensure you have an OpenAI API key. If you don't have one, visit the OpenAI website to sign up and obtain an API key.
4. Create a `config.yml` file in the project directory and add your OpenAI API key in the following format:

   ```yaml
   bot_api: YOUR_API_KEY
   ```
## Usage
1. Run the ```chatbot.py``` script using the command ```python3 chatbot.py``` in your terminal.
2. The chatbot will start and prompt you to enter your input.
3. Enter your text as a user input, and the chatbot will generate a response.
4. The conversation continues, with each user input followed by a chatbot response.

### Configuration
The project uses a configuration file (config.yml) to store the OpenAI API key. This helps keep the key hidden and separate from the codebase. The config.yml file should be in the following format:

```yaml
bot_api: YOUR_API_KEY
```
Ensure that the ```config.yml``` file is present in the project directory with the correct API key.

## Gitignore
The project includes a ```.gitignore``` file to prevent sensitive data from being committed to the repository. The following entries are included in the ```.gitignore``` file:

```arduino
config.yml
data/
```
This ensures that the ```config.yml``` file and the ```data/``` directory are not included in the version control, protecting sensitive information and preventing accidental commits.


