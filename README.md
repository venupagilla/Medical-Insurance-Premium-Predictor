# Medical-Insurance-Premium-Predictor

This web application predicts medical insurance premiums based on user-provided input features. It utilizes a Linear Regression model trained on a dataset. The application provides an interactive user interface to input patient details, view the predicted premium, and assess the model's performance through various visualizations and statistical summaries.

## Features

* **Interactive Input Form:** Allows users to enter patient details for prediction. The form dynamically adapts to binary features (0 or 1) by displaying a "Yes/No" dropdown.
* **Premium Prediction:** Displays the predicted medical insurance premium in Indian Rupees (₹).
* **Model Performance Metrics:** Shows key performance indicators of the Linear Regression model, including:
    * Mean Squared Error (MSE)
    * Root Mean Squared Error (RMSE)
    * Mean Absolute Error (MAE)
    * R² Score
* **Data Visualizations:** Provides a selection of informative graphs to understand the data and model behavior:
    * **Correlation Matrix:** Visualizes the pairwise correlations between features.
    * **Residual Plot:** Displays the residuals (the difference between actual and predicted values) against the predicted values to check for patterns.
    * **Actual vs Predicted Plot:** Shows the relationship between the actual and predicted premium prices.
    * **Distribution Plots:** Displays the distribution of each input feature.
* **Summary Statistics:** Presents a table of descriptive statistics for the dataset.
* **Responsive Layout:** The user interface is built with Bootstrap, ensuring it adapts well to different screen sizes.

## Implementation Details

The application is built using the following technologies:

* **Python:** The backend logic, including the machine learning model and Flask web framework, is implemented in Python.
* **scikit-learn:** Used for training the Linear Regression model and calculating performance metrics.
* **pandas:** Employed for data manipulation and loading the dataset.
* **seaborn & matplotlib:** Utilized for generating various data visualizations.
* **Flask:** A lightweight Python web framework used to build the web application and serve the HTML templates and static files.
* **HTML:** Structures the web pages.
* **CSS (Bootstrap):** Provides styling and responsiveness to the user interface.

The application consists of the following main files:

* **`model.py`:** Contains the machine learning model definition, data loading, preprocessing, training process, prediction function (`predict_premium`), calculation of performance metrics (MSE, RMSE, MAE, R²), generation of summary statistics, and the code to automatically generate the visualization files (saved in the `static` directory).
* **`app.py`:** The Flask application that handles user requests, renders the HTML templates, receives user input from the form, calls the `predict_premium` function, and passes the prediction results, performance metrics, summary statistics, and list of available graphs to the HTML template.
* **`index.html`:** The main HTML template responsible for rendering the user interface. It includes the input form, displays the prediction results, model performance metrics, the graph selector, and the summary statistics table. It uses Jinja templating to dynamically display data passed from the Flask application.
* **`Medicalpremium.csv`:** (Assumed) The dataset used to train the medical insurance premium prediction model. This file should be in the same directory as `model.py`.
* **`static/` directory:** Contains the generated image files for the visualizations (e.g., `heatmap.png`, `residuals.png`, `actual_vs_predicted.png`, `distribution_*.png`).

## How to Run the Application

1.  **Ensure Dependencies are Installed:**
    Navigate to the project directory in your terminal and install the necessary Python libraries using pip:
    ```bash
    pip install pandas scikit-learn seaborn matplotlib Flask
    ```

2.  **Place the Dataset:**
    Make sure the `Medicalpremium.csv` file is in the same directory as `model.py` and `app.py`.

3.  **Run the Flask Application:**
    In your terminal, within the project directory, run the Flask application:
    ```bash
    python app.py
    ```
    This will start the Flask development server. You will likely see an output similar to:
    ```
    * Serving Flask app 'app'
    * Debug mode: on
    * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
    * Press Ctrl+C to quit
    ```

4.  **Open in Your Browser:**
    Open your web browser and navigate to the address provided (usually `http://127.0.0.1:5000`).

5.  **Interact with the Application:**
    * Enter the required patient details in the form on the left.
    * Click the "Predict Premium" button to get the predicted premium. The result and model performance metrics will be displayed in the right column.
    * Use the dropdown menu in the right column to select and view different data visualizations.
    * The summary statistics for the dataset are displayed below.

## Notes

* This application assumes the presence of a `Medicalpremium.csv` file with features that the Linear Regression model was trained on.
* The accuracy of the predictions depends on the quality and representativeness of the training data.
* The visualizations provide insights into the data and model performance, which can be helpful for understanding the predictions.
