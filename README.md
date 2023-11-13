# Text Classification Web App

### Overview:

This Flask web application is designed for text classification, specifically categorizing titles into predefined categories. The app uses a pre-trained Skip-gram Word2Vec model and a classifier model trained on the Word2Vec vectors to make predictions.

### Dependencies:

- Python 3.7 or higher
- Flask
- Gensim
- Spacy
- Numpy

### Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/christianduhp/api_classificador_artigo
   cd your_repo
   ```

2. Install the required dependencies:

   ```bash
   pip install Flask Gensim spacy numpy
   ```

3. Download the pre-trained models:

   - Skip-gram Word2Vec model: [skipgram_model.txt](models/skipgram_model.txt)
   - Classifier model: [rl_sg.pkl](models/rl_sg.pkl)

4. Run the application:

   ```bash
   python app.py
   ```

### Usage:

1. Access the application through your web browser at [http://localhost:5000/](http://localhost:5000/).

2. Enter a title in the provided input field.

3. Click the "Predict" button.

4. The application will classify the title into a category and display the result.

### Code Structure:

- **app.py**: Flask application script containing the main functionality for loading models and handling web requests.
- **utils.py**: Utility functions for text tokenization and vector combination.

- **templates**: Folder containing HTML templates for rendering the web interface.

- **static**: Directory for static files used by the web application, including CSS and JavaScript.

- **notebooks**: Directory for Jupyter notebooks, potentially used for data exploration and model development.

- **data**: Directory containing CSV files for training and testing the models.

- **models**: Directory storing pre-trained Word2Vec models and the classifier model.

### Models:

- **Word2Vec Model (Skip-gram)**: Trained on a large corpus, this model generates word embeddings used to represent words in a vector space.

- **Classifier Model**: A machine learning model, trained using the Word2Vec vectors, for classifying titles into predefined categories.

### Additional Notes:

- The application uses the Flask web framework for creating the web interface.
- Text tokenization is performed using spaCy, and the resulting tokens are used to create a vector representation through Word2Vec.

- The application runs in debug mode, which is suitable for development purposes. Consider disabling debug mode in a production environment.

### License:

This project is licensed under the [MIT License](LICENSE).
