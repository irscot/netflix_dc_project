---

# README

## Netflix 1990s Movie Analysis

This project analyzes a Netflix dataset to answer three questions:

1. **Which movies were released in the 1990s?**  
2. **What is the most common movie duration among 1990s films?**  
3. **How many short action movies (< 90 minutes) from the 1990s are available?**

The analysis uses **pandas**, **NumPy**, and **matplotlib** to filter data, visualize movie durations, and count specific subsets of films.

---

## Requirements

- Python 3  
- pandas  
- numpy  
- matplotlib  

Install dependencies:

```bash
pip install pandas numpy matplotlib
```

---

## How the Script Works

### **1. Load and Filter 1990s Movies**
The script reads `netflix_data.csv` into a pandas DataFrame and uses a NumPy boolean mask to select movies released between **1990 and 1999**.

### **2. Identify the Most Frequent Duration**
A histogram of movie durations is plotted to visualize the distribution.  
From the plot, **100 minutes** appears as the most common duration.

### **3. Count Short 1990s Action Movies**
The script filters for:

- release years 1990–1999  
- genre = "Action"  
- duration < 90 minutes  

A loop counts how many movies meet these criteria and prints the result.

---

## Output

- A histogram showing the distribution of 1990s movie durations  
- A printed statement such as:
```
There are X 90s action films on Netflix.
```
