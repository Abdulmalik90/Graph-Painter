# 📈 Graph Painter

Graph Painter is a desktop graphical user interface (GUI) application built with Python. This was my first real Python project, designed to make data visualization simple and accessible without needing to write code every time. Using `tkinter` for the interface and `matplotlib` for rendering, it allows users to create various types of graphs either by entering data manually or by importing it from Excel files.

## ✨ Features

The application features a main hub (Home Window) that navigates to four distinct graphing modules:

*   **Graph Painter:** Manually input X and Y values to generate customizable line plots and bar charts[cite: 1]. You can customize titles, axis labels, line colors, and grid visibility[cite: 1].
*   **Excel Graph:** Import `.xlsx` or `.xls` files directly into the app[cite: 1]. Simply specify the sheet name and the X/Y columns to instantly generate bar charts or line plots from your spreadsheet data[cite: 1].
*   **Circle Graph (Pie Charts):** Create dynamic pie charts by adding custom labels and percentages[cite: 1]. It includes options to toggle 3D-like shadows and wedge borders[cite: 1].
*   **Comparison Chart:** A dual-input interface designed to let you input multiple datasets to visualize and compare them side-by-side[cite: 1].

## 🖼️ Screenshots

Here is a look at the application's interface:

### Home Screen
![Home Screen](image_de9f7b.png)

### Standard Graph Painter
![Graph Painter](image_de9c91.png)

### Excel Graph Maker
![Excel Graph](image_de9c6f.png)

### Circle (Pie) Graph
![Circle Graph](image_de9f5c.png)

### Comparison Graph
![Comparison Graph](image_de9cb2.png)

## 🛠️ Prerequisites & Dependencies

To run this project locally, you need Python installed on your machine along with the following libraries:

*   `tkinter` (Usually comes pre-installed with standard Python distributions)[cite: 1]
*   `matplotlib` - For generating the plots and charts[cite: 1]
*   `pandas` - For reading and handling Excel files[cite: 1]
*   `Pillow` (PIL) - For rendering images and icons in the UI[cite: 1]

You can install the required external libraries using pip:

```
pip install matplotlib pandas Pillow openpyxl
```
(Note: openpyxl is required by pandas to read modern .xlsx files).

🚀 How to Run
1. Clone this repository to your local machine:
```
git clone [https://github.com/YourUsername/Graph-Painter.git](https://github.com/YourUsername/Graph-Painter.git)

```

2. Navigate to the project directory.

3. Make sure your image and icon paths in the code match your local directory structure (or update them to relative paths).

4. Run the main Python script:
```
python main.py
```

💡 Notes on this Project
As my first major Python project in 2022, building this application taught me the fundamentals of object-oriented programming, state management in GUIs, and handling user inputs. It serves as a great milestone in my programming journey!
