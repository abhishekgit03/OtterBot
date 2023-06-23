# OtterBot

OtterBot is an OpenAI-powered chatbot with MongoDB integration and Streamlit for the frontend. It is designed to provide a seamless conversational experience for users by leveraging the power of OpenAI's language model and storing data in a MongoDB database.

## Features

- Natural language processing powered by OpenAI.
- MongoDB integration for storing and retrieving chatbot data.
- User-friendly frontend interface built with Streamlit.
- Easy setup and deployment.

## Prerequisites

- Python 3.7 or higher
- MongoDB
- OpenAI API key
- Streamlit

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/OtterBot.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure MongoDB:

   - Start MongoDB service on your local machine or use a remote MongoDB instance.
   - Update the MongoDB connection details in the `config.py` file.

4. Set up OpenAI API:

   - Sign up for an API key at the [OpenAI website](https://openai.com/).
   - Set your OpenAI API key as an environment variable:
   
     ```bash
     export OPENAI_API_KEY=your-api-key
     ```

5. Run the application:

   ```bash
   streamlit run app.py
   ```

6. Access the OtterBot interface in your browser:

   ```
   http://localhost:8501
   ```

## Usage

1. Open the OtterBot interface in your browser.
2. Type your message in the input field.
3. Press Enter or click on the Send button to send your message to the chatbot.
4. The chatbot will generate a response based on the input using OpenAI's language model.
5. The conversation history and bot responses will be stored in MongoDB for future reference.

## Contributing

Contributions are welcome! Here's how you can contribute to OtterBot:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.


## Acknowledgements

- [OpenAI](https://openai.com/) for providing the powerful language model.
- [MongoDB](https://www.mongodb.com/) for the database integration.
- [Streamlit](https://streamlit.io/) for the user-friendly frontend framework.

## Contact

If you have any questions or suggestions, feel free to reach out to me:

- Email: abhishek20dgp@gmail.com
