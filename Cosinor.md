Certainly! Below is a Python code that fits a cosinor model to data consisting of date-time and signal values. The cosinor model is commonly used to analyze periodic (e.g., circadian) rhythms in biological data.

```python
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Function to define the cosinor model
def cosinor(t, M, A, omega, phi):
    """
    Cosinor model function.

    Parameters:
    - t: Time variable
    - M: Mesor (midline estimating statistic of rhythm)
    - A: Amplitude
    - omega: Angular frequency
    - phi: Acrophase (phase shift)

    Returns:
    - Model value at time t
    """
    return M + A * np.cos(omega * t + phi)

# Load your data into a pandas DataFrame
# Assuming your CSV file has columns 'datetime' and 'signal'
data = pd.read_csv('data.csv')

# Convert 'datetime' column to pandas datetime objects
data['datetime'] = pd.to_datetime(data['datetime'])

# Convert datetime to a numerical time variable (e.g., hours since start)
t0 = data['datetime'].iloc[0]
data['t'] = (data['datetime'] - t0).dt.total_seconds() / 3600.0  # Time in hours

# Extract time and signal values
t = data['t'].values
y = data['signal'].values

# Initial parameter guesses
M0 = np.mean(y)
A0 = (np.max(y) - np.min(y)) / 2.0
omega0 = 2 * np.pi / 24  # Assuming a 24-hour period
phi0 = 0.0
initial_guess = [M0, A0, omega0, phi0]

# Parameter bounds to ensure meaningful values
lower_bounds = [-np.inf, 0, 0, -np.inf]  # A >= 0, omega >= 0
upper_bounds = [np.inf, np.inf, np.inf, np.inf]

# Fit the cosinor model to the data
params, covariance = curve_fit(
    cosinor, t, y, p0=initial_guess, bounds=(lower_bounds, upper_bounds)
)

# Extract fitted parameters
M_fit, A_fit, omega_fit, phi_fit = params

# Calculate the period from the fitted angular frequency
period_fit = 2 * np.pi / omega_fit

# Print the fitted parameters
print(f"Mesor (M): {M_fit}")
print(f"Amplitude (A): {A_fit}")
print(f"Angular frequency (omega): {omega_fit}")
print(f"Fitted Period: {period_fit} hours")
print(f"Acrophase (phi): {phi_fit} radians")

# Generate fitted values for plotting
t_fit = np.linspace(np.min(t), np.max(t), 1000)
y_fit = cosinor(t_fit, M_fit, A_fit, omega_fit, phi_fit)

# Plot the original data and the fitted cosinor curve
plt.figure(figsize=(10, 6))
plt.scatter(t, y, label='Data', color='blue')
plt.plot(t_fit, y_fit, label='Cosinor Fit', color='red')
plt.xlabel('Time (hours since start)')
plt.ylabel('Signal')
plt.title('Cosinor Model Fit')
plt.legend()
plt.show()
```

**Instructions:**

1. **Data Preparation:**
   - Ensure your data is in a CSV file named `'data.csv'` with columns `'datetime'` and `'signal'`.
   - The `'datetime'` column should contain date-time strings, and `'signal'` should contain numerical signal values.

2. **Model Explanation:**
   - **Mesor (M):** The mean level around which the oscillation occurs.
   - **Amplitude (A):** The extent of oscillation (peak deviation from the mesor).
   - **Angular Frequency (omega):** Related to the period (`omega = 2π / period`).
   - **Acrophase (phi):** The time point of the peak of the rhythm within the period.

3. **Adjusting the Period:**
   - If you have a different expected period (e.g., 12 hours), adjust the initial guess for `omega0` accordingly:
     ```python
     omega0 = 2 * np.pi / expected_period_in_hours
     ```

4. **Visualization:**
   - The plotted graph will show your data points and the fitted cosinor curve, helping you visualize how well the model fits your data.

5. **Dependencies:**
   - Make sure you have the necessary libraries installed:
     ```bash
     pip install numpy pandas scipy matplotlib
     ```

**Note:** This code fits the cosinor model by estimating all parameters, including the angular frequency (`omega`). If you prefer to fix the period (and thus `omega`), you can modify the `cosinor` function and remove `omega` from the parameters to be estimated.

---

This script should provide a solid foundation for fitting a cosinor model to your date-time and signal data in Python. Adjust the initial guesses and bounds as necessary for your specific dataset.
