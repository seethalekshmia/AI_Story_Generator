# AI Story Generator

An interactive Streamlit application that generates unique short stories based on user-provided themes, genres, and preferences using AI.

## Features

- Generate stories from custom themes
- Multiple genre options
- Adjustable story length
- User-friendly interface
- Real-time story generation

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On Unix or MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Enter a theme or main idea for your story
2. Select your preferred genre
3. Choose the desired story length
4. Click "Generate Story" to create your unique story

## Requirements

- Python 3.7+
- OpenAI API key
- Required packages listed in requirements.txt
