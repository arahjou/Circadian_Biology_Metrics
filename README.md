# Circadian_Biology_Metrics
Circadian Biology Metrics (CBM) is a repository designed to consolidate essential functions for calculating various metrics needed to investigate circadian rhythm perturbations using Python. Additionally, I plan to develop tools that can be utilized by users or agents (e.g., LLMs) to generate recommendations.

## Handeling time
1) Importing
2) Converting

## Metics

### Most Active 10 Hours - M10
The average activity level during the most active 10 hours of the day, reflecting overall activity and possibly light exposure.

### Lowest 5 Hours - L5
The average activity level during the least active 5 hours of the day, typically a measure of rest or sleep quality.

### Composite Phase Deviation - CPD
"Based on a single time series, our Composite Phase Deviation method unveils distinct, subject- and schedule-specific geometries (‘islands and pancakes’) that illustrate how modern work times interfere with sleep [Reference](https://www.nature.com/articles/srep38601)".

### Interdaily Stability - IS
A measure of the stability of an individual's circadian rhythm from day to day [Reference](https://irispublishers.com/ann/fulltext/rest-activity-circadian-rhythm-and-light-exposure-using-wrist-actigraphy-in-icu-patients.ID.000787.php).

### Intradaily Variability - IV
A measure of the fragmentation of the circadian rhythm within a single day [Reference](https://irispublishers.com/ann/fulltext/rest-activity-circadian-rhythm-and-light-exposure-using-wrist-actigraphy-in-icu-patients.ID.000787.php).

### Circadian Rhythm Index - CRI
The metric calculated from IV and IS in circadian biology is called the Circadian Rhythm Index (CRI).

CRI is a composite measure of circadian rhythmicity that combines information from interdaily stability (IS) and intradaily variability (IV). These two parameters are derived from actigraphy data, which measures activity patterns over time.

IS represents the stability or regularity of the sleep-wake cycle from day to day. Higher IS indicates a more consistent sleep schedule.   
IV reflects the fragmentation of activity and rest within a 24-hour period. Higher IV suggests more fragmented activity patterns, with frequent transitions between rest and activity.   
CRI is calculated as follows:

CRI = IS / IV

A higher CRI indicates a stronger and more robust circadian rhythm, characterized by both a stable sleep-wake schedule and consolidated periods of activity and rest. A lower CRI suggests a weaker or more disrupted circadian rhythm, with either an irregular sleep-wake pattern or fragmented activity throughout the day.

CRI is a useful tool for assessing circadian rhythm health and identifying individuals who may be at risk for circadian rhythm disorders. It can also be used to track the effectiveness of interventions aimed at improving circadian rhythmicity.

### SRI
A measure of the regularity of social rhythms, which can influence circadian rhythms and overall health.

### Cosinor
"Historically, the single cosinor was developed to analyze short and sparse data series [2, 30–32]. Periodograms and classical spectra originally used in chronobiology [33, 34] required the data to be equidistant and to cover more than a single cycle. Whereas some spectral analysis techniques are now available to analyze non-equidistant data [35–37], algorithms available in most software packages remain limited to the case of equidistant data".
[Reference](https://tbiomed.biomedcentral.com/articles/10.1186/1742-4682-11-16)

### Relative Amplitude - RA
A measure of the difference between the most and least active periods, indicating the robustness of the circadian rhythm
[Reference](https://irispublishers.com/ann/fulltext/rest-activity-circadian-rhythm-and-light-exposure-using-wrist-actigraphy-in-icu-patients.ID.000787.php).

### Self-similarity paramerter - SSP

### Activity Balance Index - ABI
