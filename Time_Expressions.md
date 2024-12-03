### **Decimal Time**

**Decimal time** expresses time as a fractional number, where hours, minutes, and seconds are converted into a single decimal representation of the day. It is another way to represent time in a continuous and linear format.

---

### **How Decimal Time Works**

#### **Conversion Formula**
Decimal time is calculated as:
\[
\text{Decimal Time} = \text{Hour} + \frac{\text{Minutes}}{60} + \frac{\text{Seconds}}{3600}
\]
This expresses the time of day as a single number in terms of hours, with fractions representing minutes and seconds.

#### **Examples**
| Clock Time | Decimal Time |
|------------|--------------|
| 00:00:00   | 0.00         |
| 06:00:00   | 6.00         |
| 12:30:00   | 12.50        |
| 18:45:30   | 18.7583      |
| 23:59:59   | 23.9997      |

---

### **Why Use Decimal Time?**

1. **Simplified Calculations:**
   - Decimal time is easier to use for mathematical computations because it eliminates the need to handle separate units (hours, minutes, seconds).
   
2. **Continuous Representation:**
   - Decimal time provides a continuous value, which is particularly useful in models like the cosinor model or other periodic analyses.

3. **Direct Mapping to Linear or Radial Time:**
   - Decimal time can be directly mapped to **linear time** (hours since a reference) or converted to **radial time** (e.g., radians).

---

### **Decimal Time and Periodic Data**

#### **Relation to the Cosinor Model**
In the cosinor model:
- Decimal time can be used as the \( t \) variable directly if the rhythm is measured over a day (24-hour cycle).
- To calculate the radial time:
  \[
  \text{Radial Time (in radians)} = \frac{2\pi \cdot \text{Decimal Time}}{24}
  \]

#### **Relation to Fractional Time**
Decimal time can also be normalized to a fraction of the period (e.g., a 24-hour day):
\[
\text{Fractional Time} = \frac{\text{Decimal Time}}{\text{Total Period}}
\]
For a 24-hour period, this simplifies to:
\[
\text{Fractional Time} = \frac{\text{Decimal Time}}{24}
\]

---

### **How to Calculate Decimal Time in Python**

Here’s how you can compute decimal time from a `datetime` object in Python:

```python
import pandas as pd

# Example: Create a DataFrame with timestamps
data = pd.DataFrame({
    'datetime': [
        '2024-11-30 00:00:00', '2024-11-30 06:00:00',
        '2024-11-30 12:30:00', '2024-11-30 18:45:30',
        '2024-11-30 23:59:59'
    ]
})

# Convert to datetime format
data['datetime'] = pd.to_datetime(data['datetime'])

# Extract Decimal Time
data['decimal_time'] = data['datetime'].dt.hour + \
                       data['datetime'].dt.minute / 60 + \
                       data['datetime'].dt.second / 3600

# Display the result
print(data)
```

#### Output:
```
             datetime  decimal_time
0 2024-11-30 00:00:00      0.000000
1 2024-11-30 06:00:00      6.000000
2 2024-11-30 12:30:00     12.500000
3 2024-11-30 18:45:30     18.758333
4 2024-11-30 23:59:59     23.999722
```

---

### **Comparison of Decimal Time to Other Representations**

| Representation   | Example for 18:45:30         | Formula                                              |
|-------------------|------------------------------|-----------------------------------------------------|
| **Decimal Time**  | \( 18.7583 \) hours         | \( 18 + \frac{45}{60} + \frac{30}{3600} \)          |
| **Radial Time**   | \( 4.91 \) radians          | \( \frac{2\pi \cdot 18.7583}{24} \)                |
| **Hour Angle**    | \( 281.37^\circ \)          | \( \frac{360 \cdot 18.7583}{24} \)                 |
| **Fractional Time** | \( 0.7816 \) (normalized) | \( \frac{18.7583}{24} \)                           |

---

### **When to Use Decimal Time**

- **Cosinor Modeling:** Decimal time is ideal for \( t \) in periodic models, as it represents continuous linear time.
- **Time-Duration Analysis:** Decimal time simplifies calculations involving durations or intervals.
- **Clock-Time Conversion:** It provides a simple way to represent clock time as a numerical variable.

In summary, **decimal time** is a practical and flexible way to express time for many scientific and mathematical analyses, especially when dealing with periodic data like circadian rhythms.
