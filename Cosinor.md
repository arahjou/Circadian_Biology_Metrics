Below is a Python code that fits a cosinor model to data consisting of date-time and signal values. The cosinor model is commonly used to analyze periodic (e.g., circadian) rhythms in biological data.

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

Certainly! Let’s break down the mathematics behind the **cosinor model** and the Python code step by step.

---

### **What is a Cosinor Model?**

The **cosinor model** is a mathematical way to describe periodic (cyclical) data, such as rhythms that repeat over a specific period (e.g., daily, monthly, yearly). It uses a cosine wave to model the data.

#### **The Mathematical Formula**

\[
y(t) = M + A \cdot \cos(\omega \cdot t + \phi)
\]

Where:
- **\( y(t) \)**: The signal value at time \( t \).
- **\( M \) (Mesor)**: The mean level around which the oscillation occurs (baseline or midline).
- **\( A \) (Amplitude)**: The height of the wave, or how much the signal deviates from the mean level \( M \).
- **\( \omega \) (Angular Frequency)**: Controls the period (how long it takes to complete one cycle). It's related to the period (\( P \)) as:
  \[
  \omega = \frac{2\pi}{P}
  \]
  For example, if the rhythm repeats every 24 hours (circadian rhythm), \( \omega = \frac{2\pi}{24} \).
- **\( \phi \) (Acrophase)**: The phase shift, which determines when the peak (or trough) occurs within a cycle.

---

### **Steps in the Code**

#### 1. **Define the Cosinor Function**
This step implements the mathematical formula:
```python
def cosinor(t, M, A, omega, phi):
    return M + A * np.cos(omega * t + phi)
```
Here, `t` is the time variable, and \( M, A, \omega, \phi \) are the parameters we want to estimate.

---

#### 2. **Prepare the Data**
To fit the model, we need:
- **Time as a numerical variable (`t`)**:
  - Convert the `datetime` column into elapsed time in hours from the start.
  - Example: If the first timestamp is 08:00, then 09:00 is `1 hour`, 10:00 is `2 hours`, and so on.
- **Signal values (`y`)**: The measured values you want to model.

This is done here:
```python
data['t'] = (data['datetime'] - t0).dt.total_seconds() / 3600.0  # Time in hours
t = data['t'].values
y = data['signal'].values
```

---

#### 3. **Initial Guesses for Parameters**
Fitting the model requires good starting guesses for the parameters:
- **\( M \):** Use the mean of the signal values as an initial guess.
- **\( A \):** Use half the range of the signal values (\( \frac{\text{max} - \text{min}}{2} \)).
- **\( \omega \):** Use \( \frac{2\pi}{P} \), where \( P \) is the expected period. For example, for a daily rhythm, \( P = 24 \), so \( \omega = \frac{2\pi}{24} \).
- **\( \phi \):** Start with 0 (no phase shift).

```python
M0 = np.mean(y)
A0 = (np.max(y) - np.min(y)) / 2.0
omega0 = 2 * np.pi / 24  # Assuming a 24-hour period
phi0 = 0.0
initial_guess = [M0, A0, omega0, phi0]
```

---

#### 4. **Fit the Model**
The `curve_fit` function from `scipy.optimize` estimates the best-fit parameters by minimizing the difference between the observed data (`y`) and the model’s predicted values:
```python
params, covariance = curve_fit(cosinor, t, y, p0=initial_guess, bounds=(lower_bounds, upper_bounds))
```
- **`params`** contains the estimated values for \( M, A, \omega, \phi \).
- **`covariance`** gives the uncertainties of these estimates.

---

#### 5. **Interpret the Results**
Extract the fitted parameters:
```python
M_fit, A_fit, omega_fit, phi_fit = params
```
- Compute the period:
  \[
  P = \frac{2\pi}{\omega}
  \]
  This tells you how long the cycle takes to complete one oscillation.

---

#### 6. **Generate the Fitted Curve**
To visualize the fit, create a smooth curve using the fitted parameters:
```python
t_fit = np.linspace(np.min(t), np.max(t), 1000)
y_fit = cosinor(t_fit, M_fit, A_fit, omega_fit, phi_fit)
```
This generates model predictions over a range of time values.

---

#### 7. **Plot the Results**
Finally, plot the original data and the fitted curve to see how well the model matches the data:
```python
plt.scatter(t, y, label='Data', color='blue')
plt.plot(t_fit, y_fit, label='Cosinor Fit', color='red')
```

---

### **Mathematical Understanding of the Fitted Parameters**
1. **Mesor (\( M \))**:
   - Represents the average value of the oscillating signal.

2. **Amplitude (\( A \))**:
   - Indicates the strength or magnitude of the oscillation. Larger \( A \) means the signal fluctuates more significantly around the mesor.

3. **Angular Frequency (\( \omega \))**:
   - Tells you how quickly the oscillation repeats. For a 24-hour rhythm:
     \[
     \omega = \frac{2\pi}{24}
     \]

4. **Acrophase (\( \phi \))**:
   - Determines the timing of the peak within a cycle. A positive \( \phi \) shifts the peak to the right; a negative \( \phi \) shifts it to the left.

---

### **Summary**

1. The **cosinor model** fits a cosine wave to periodic data using the formula \( y(t) = M + A \cdot \cos(\omega \cdot t + \phi) \).
2. The parameters (\( M, A, \omega, \phi \)) are estimated by minimizing the difference between the model and the observed data.
3. The code prepares the data, provides initial parameter guesses, fits the model using `curve_fit`, and visualizes the results.
4. The fitted parameters give insights into the rhythm:
   - **Mesor (\( M \))**: Average level.
   - **Amplitude (\( A \))**: Strength of oscillation.
   - **Frequency (\( \omega \))**: Speed of oscillation.
   - **Acrophase (\( \phi \))**: Timing of the peak.

This is a practical and mathematical way to study rhythms like daily (circadian) patterns.
