import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import os

# Load dataset
df = pd.read_csv("Medicalpremium.csv")

X = df.drop("PremiumPrice", axis=1)
y = df["PremiumPrice"]
FEATURES = X.columns.tolist()

# Get unique values for each feature (for UI enhancement)
UNIQUE_FEATURE_VALUES = {feature: sorted(df[feature].unique().tolist()) for feature in FEATURES}

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
R2 = r2_score(y_test, y_pred)
MAE = mean_absolute_error(y_test, y_pred)
RMSE = MSE**0.5

# Summary stats for display
SUMMARY_STATS = df.describe().round(2).to_html(classes="table table-striped", border=0)

# Create graphs directory if not exists
os.makedirs("static", exist_ok=True)

# Auto-generate Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("static/heatmap.png")
plt.close()

# Auto-generate Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
sns.residplot(x=y_pred, y=residuals, lowess=True, color="purple", line_kws={"color": "red"})
plt.xlabel("Predicted Premium Price")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.tight_layout()
plt.savefig("static/residuals.png")
plt.close()

# Auto-generate Actual vs Predicted Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, color="teal")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Premium Price")
plt.ylabel("Predicted Premium Price")
plt.title("Actual vs Predicted")
plt.tight_layout()
plt.savefig("static/actual_vs_predicted.png")
plt.close()

# Auto-generate Distribution Plots
for feature in FEATURES:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[feature], kde=True)
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"static/distribution_{feature}.png")
    plt.close()

def predict_premium(input_list):
    return model.predict([input_list])[0]

DISTRIBUTION_PLOTS = [f"distribution_{feature}.png" for feature in FEATURES]