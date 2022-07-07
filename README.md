# Server-Monitoring-Plotly-Dash
Creates a line chart using Plotly in Dash that reads up to the second updates from a json file. Initially created to read a CPU usage json file created in another project.



1. Install the Plotly and Dash libraries before use.


2. There are simple customizable settings at the top which are:

  #If there are any datapoints at or above this threshold then those datapoints will turn red along with turning the whole line chart red.
  caution_threshold = 90

  #This must match the number of items in the list within the json file.
  num_of_datapoints = 30

  #How often the dash reads the json file.
  interval_seconds = 2

  #json file name.
  json_file = 'ListJson.json'


3. There are additional user customizable settings for the Plotly chart such as colors, text size, and titles.

![image](https://user-images.githubusercontent.com/66573737/177826679-5fde31c3-584e-4c29-8523-f4644562755f.png)

