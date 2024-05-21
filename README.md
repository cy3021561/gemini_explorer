# Gemini_explorer

## Overview

Gemini Explorer Mission is a Streamlit application that leverages Google's Vertex AI Generative Models to provide an interactive chat experience. The application uses a large language model named "Gemini-Pro" to generate responses to user queries in real-time.

## Features

- **Interactive Chat Interface:** Engage in dynamic conversations with the AI model.
- **Persistent Chat History:** Keeps track of the conversation history during the session.
- **Customizable Responses:** The AI can introduce itself and interact in a specific style.

## Requirements

- Python 3.7+
- Streamlit
- Vertex AI Python SDK

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages:**

   ```bash
   pip install streamlit vertexai
   ```

3. **Set up Vertex AI:**

   Ensure you have access to Google Cloud and the Vertex AI API. Initialize Vertex AI with your project ID:

   ```python
   project = "your-gcp-project-id"
   vertexai.init(project=project)
   ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Interacting with the Chat:**

   - Upon launching the app, you will be prompted to enter your name.
   - The AI will introduce itself in a friendly and interactive manner.
   - Use the chat input box to ask questions or make requests. The AI will respond based on the provided input.
