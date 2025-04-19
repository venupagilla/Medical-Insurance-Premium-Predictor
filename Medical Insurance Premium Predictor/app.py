from flask import Flask, render_template, request
from model import predict_premium, FEATURES, MSE, R2, SUMMARY_STATS, MAE, RMSE, DISTRIBUTION_PLOTS, UNIQUE_FEATURE_VALUES

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    input_values = {}

    if request.method == "POST":
        try:
            form_data = request.form
            input_values = {}
            for feature in FEATURES:
                if UNIQUE_FEATURE_VALUES.get(feature) == [0, 1]:
                    input_values[feature] = int(form_data[feature])
                else:
                    input_values[feature] = float(form_data[feature])
            prediction = round(predict_premium(list(input_values.values())), 2)
        except ValueError:
            error = "Please enter valid numeric values for all fields."

    return render_template(
        "index.html",
        features=FEATURES,
        prediction=prediction,
        error=error,
        mse=round(MSE, 2),
        r2=round(R2, 2),
        mae=round(MAE, 2),
        rmse=round(RMSE, 2),
        summary_stats=SUMMARY_STATS,
        input_values=input_values,
        distribution_plots=DISTRIBUTION_PLOTS,
        unique_feature_values=UNIQUE_FEATURE_VALUES
    )

if __name__ == "__main__":
    app.run(debug=True)