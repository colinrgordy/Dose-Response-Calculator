# HTS Dose-Response Calculator

An interactive web application designed to streamline the preparation of serial dilutions and calculate final well concentrations for high-throughput screening (HTS).

## Key Features
* **Dynamic Dilution Math:** Instantly calculates stock plate requirements and final assay concentrations based on user-defined dilution factors.
* **Real-Time Summary:** Provides a physical transfer dilution ratio readout to verify lab protocol accuracy.
* **Excel Export:** Generates standardized `.xlsx` files of dose-response tables for seamless integration with liquid handlers and electronic lab notebooks.
* **Automated Scaling:** Adjusts calculations for varying number of points, transfer volumes (nL), and assay volumes (µL).

## Technical Stack
* **Language:** Python 3.9
* **Framework:** Shiny for Python
* **Data Handling:** Pandas & OpenPyXL
* **Deployment:** shinyapps.io

## Background
Developed to eliminate manual calculation errors in drug titration workflows, ensuring high precision in dose-response curve generation within translational research environments.

---
*Made by Colin Gordy*
