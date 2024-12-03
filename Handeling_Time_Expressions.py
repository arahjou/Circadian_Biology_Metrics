import numpy as np
from datetime import datetime, timedelta

def convert_time(time_value, from_type, to_types, period=24):
    """
    Convert time between different representations.

    Parameters:
    - time_value: The input time value(s) to convert. Can be a single value or a list of values.
    - from_type: The representation of the input time ('linear', 'clock', 'decimal', 'fractional', 'radial', 'hour_angle', 'phase').
    - to_types: A list of desired output representations.
    - period: The period of the cycle (default is 24 for daily rhythms).

    Returns:
    - A dictionary with keys as requested to_types and values as converted time values.
    """
    # Ensure time_value is a list for uniform processing
    single_value = False
    if not isinstance(time_value, list):
        time_value = [time_value]
        single_value = True

    # Initialize dictionary to store conversions
    conversions = {t: [] for t in to_types}

    # Conversion factors
    omega = 2 * np.pi / period  # Angular frequency

    for t in time_value:
        # Step 1: Convert from from_type to linear time in hours
        if from_type == 'linear':
            linear_time = t
        elif from_type == 'decimal':
            linear_time = t
        elif from_type == 'clock':
            if isinstance(t, str):
                dt = datetime.strptime(t, '%H:%M:%S')
                linear_time = dt.hour + dt.minute / 60 + dt.second / 3600
            elif isinstance(t, datetime):
                linear_time = t.hour + t.minute / 60 + t.second / 3600
            else:
                raise ValueError("Invalid time format for 'clock' type.")
        elif from_type == 'fractional':
            linear_time = t * period
        elif from_type == 'radial':
            linear_time = (t / (2 * np.pi)) * period
        elif from_type == 'hour_angle':
            linear_time = (t / 360) * period
        elif from_type == 'phase':
            linear_time = (t / omega) % period
        else:
            raise ValueError(f"Unsupported from_type: {from_type}")

        # Step 2: Convert linear_time to desired to_types
        for to_type in to_types:
            if to_type == 'linear':
                value = linear_time
            elif to_type == 'decimal':
                value = linear_time
            elif to_type == 'clock':
                hours = int(linear_time) % 24
                minutes = int((linear_time - hours) * 60)
                seconds = int(((linear_time - hours) * 60 - minutes) * 60)
                value = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            elif to_type == 'fractional':
                value = linear_time / period
            elif to_type == 'radial':
                value = (2 * np.pi * linear_time) / period
            elif to_type == 'hour_angle':
                value = (360 * linear_time) / period
            elif to_type == 'phase':
                value = (omega * linear_time) % (2 * np.pi)
            else:
                raise ValueError(f"Unsupported to_type: {to_type}")
            conversions[to_type].append(value)

    # If single input value, return single outputs
    if single_value:
        for key in conversions:
            conversions[key] = conversions[key][0]

    return conversions


"""
Example 1:
# Convert '18:45:30' from clock time to other representations
time_input = '18:45:30'
from_type = 'clock'
to_types = ['decimal', 'fractional', 'radial', 'hour_angle', 'phase']

conversions = convert_time(time_input, from_type, to_types)
print(conversions)
"""

"""
Example 2:
# Convert 12.5 (12:30 PM) from decimal time to clock time and radial time
time_input = 12.5
from_type = 'decimal'
to_types = ['clock', 'radial']

conversions = convert_time(time_input, from_type, to_types)
print(conversions)
"""

"""
Example 3:
# Convert 0.25 (a quarter through the period) to clock time and phase
time_input = 0.25
from_type = 'fractional'
to_types = ['clock', 'phase']

conversions = convert_time(time_input, from_type, to_types)
print(conversions)
"""
