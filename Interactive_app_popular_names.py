# Import essential libraries 
import pandas as pd # data manipulation
import matplotlib.pyplot as plt # data visualization
import os # interacting with the operating system, such as file paths
import requests # making HTTP requests to download files from the internet
import io # byte stream handling when dealing with binary data like files from a request
import zipfile # extracting files from ZIP archives
from unidecode import unidecode # normalizing unicode characters in strings to their ASCII counterparts
import dash # building interactive web applications
from dash import html, dcc # HTML components for building the layout and interactive components
import plotly.express as px # for high-level, easy-to-use plotting functions
from dash.dependencies import Input, Output # managing callbacks for interactive components

# Define the URL for the Social Security Administration (SSA) baby names dataset.
url_SSA = "https://www.ssa.gov/oact/babynames/names.zip"  

# Use requests to download the ZIP file from the SSA URL.
# The response content is a ZIP file containing yearly name data.
response = requests.get(url_SSA)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))

# Initialize a DataFrame to hold the data for all years included in the SSA dataset
all_years_ssa_data = pd.DataFrame()

# Loop through each file within the zip archive, which contains names data for individual years
for filename in zip_file.namelist():
    if filename.endswith('.txt'):
        # Open the current file and read its content into a DataFrame
        with zip_file.open(filename) as file:
            year_data = pd.read_csv(file, names=['name', 'gender', 'count'])

        # Extract the year from the filename and add the year as a new column
        year = int(filename[3:7])  # Extract year from file name (e.g., 'yob2023.txt')
        year_data['year'] = year

        # Append the data from the current year to the all_years_ssa_data DataFrame
        all_years_ssa_data = pd.concat([all_years_ssa_data, year_data], ignore_index=True)

# Initialize a Dash app to create an interactive web dashboard
app = dash.Dash(__name__)

# Set up dropdowns for selecting years and genders, and a graph component for displaying name trends
years = all_years_ssa_data['year'].unique()
genders = all_years_ssa_data['gender'].unique()

app.layout = html.Div([
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in sorted(years)],
        value=years[0]  # Default selection is the first year available.
    ),
    dcc.Dropdown(
        id='gender-dropdown',
        options=[{'label': gender, 'value': gender} for gender in genders],
        value=genders[0]  # Default selection is the first gender available.
    ),
    dcc.Graph(id='name-trends-graph')
])

# Define callback functions to update the graph based on user input from dropdown menus
@app.callback(
    Output('name-trends-graph', 'figure'),
    Input('year-dropdown', 'value'),
    Input('gender-dropdown', 'value')
)
def update_graph(selected_year, selected_gender):
    # Filter data based on the selected year and gender
    filtered_data = all_years_ssa_data[(all_years_ssa_data['year'] == selected_year) & 
                                       (all_years_ssa_data['gender'] == selected_gender)]
    # Aggregate and select the top 10 names for the selected category
    top_names = filtered_data.groupby('name').sum().nlargest(10, 'count')
    # Create a bar chart for the top names
    fig = px.bar(top_names, x=top_names.index, y='count', title=f'Top 10 Names in {selected_year} for {selected_gender}',
                 color_discrete_sequence=['#317773' if selected_gender == 'F' else '#E2D1F9'])
    
    # plot layout
    fig.update_layout(
        plot_bgcolor='white',  # Set background color to white for readability
        paper_bgcolor='white'
    )
    return fig

# Run the server with debugging enabled
if __name__ == '__main__':
    app.run_server(debug=True)