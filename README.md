## About
This project is a data visualization of over 3,000 anime entries sourced from MyAnimeList, created using the t-SNE algorithm. My goal was for this to serve as a personal challenge to learn more about data visualization using scikit-learn and pandas.

## How to Use
- Hover: Hovering over any data point reveals the anime's title and a synopsis.
- Search and Focus: A built-in search function allows you to find anime by their English names. Selecting an anime and clicking "Focus Plot" adjusts the graph boundaries to center on that data point, making it easy to examine its nearest neighbors.

## Technologies Used
The visualization and application were built using the following libraries and tools:
- Pandas - Utilized for data manipulation and creating the primary DataFrame used to power the scatter plot.
- Plotly - Used for generating, customizing, and handling the interactivity of the scatter plot.
- Scikit-learn - Key for data preprocessing, specifically for one-hot encoding categorical features and applying the t-SNE dimensionality reduction algorithm.
- Streamlit - Used to build the user interface and host the web application.
- Jikan API - The data source used to fetch the initial anime information that was subsequently transformed and analyzed.

## Installation
1. Clone the repository
```bash
git clone https://github.com/jaxsonsprinkles/anime-visualization
```
2. Install the dependencies
``` bash
pip install -r requirements.txt
```
3. Start the Streamlit server
```bash
streamlit run main.py
```