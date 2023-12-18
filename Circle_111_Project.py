## Plotting with Matplotlib in Python 
'''
Data visualization is an essential skill for all data analysts and Matplotlib is one of the most popular libraries for creating visualizations. Matplotlib is a powerful and very popular library used for creating static, interactive, and publication-quality visualizations. 

It provides a wide range of plotting tools to generate graphs, charts, histograms, and more, making it a versatile tool for data visualization in various fields like data analysis, scientific computing, and machine learning. With Matplotlib, you can customize your plots extensively to suit your needs and create professional-looking visuals for presentations, reports, or analysis purposes.
'''

### Types of Matplotlib

'''
Matplotlib comes with a wide variety of plots. Plots help to understand trends, and patterns, and to make correlations. They’re typically instruments for reasoning about quantitative information. Some of the sample plots are covered here.

- Matplotlib Line Plot
- Matplotlib Bar Plotx
- Matplotlib Histograms Plot
- Matplotlib Scatter Plot
- Matplotlib Pie Charts
- Matplotlib Area Plot
'''

### Loading Matplotlib

'''We will load the pyplot submodule of Matplotlib so that we can draw our plots. The pyplot module contains all of the relevant methods we will need to create plots and style them. We will use the conventional alias plt. We will also load in pandas, and numpy for future parts of this project.'''

#We will be working with matplotlib

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib as mpl

### The Dataset

'''Matplotlib is designed to work with NumPy arrays and pandas dataframes. The library makes it easy to make graphs from tabular data. For this project, we will load in the csv file, named fifa.csv using the pandas library and view the first rows using the .head() method.'''

file = 'fifa.csv'

df = pd.read_csv(file, index_col = 'Name')




df.head()

### Subsetting the Dataframe

'''Using only a few columns of the dataframe for the visualization.'''

top10_df= df[['Acceleration', 'Agility', 'Balance', 'Overall', 'Age']].iloc[0:10]

top10_df

### Scatter Plots

'''Scatterplots are very useful for identifying relationships between 2 numeric variables. This can give you a sense of what to expect in a variable when the other variable changes and can also be very informative in your decision to use different modeling techniques.

A scatter plot can be created using plt.scatter() where the first argument is the x-axis variable and the second argument is the y-axis variable. In this project, we will look at the relationship between the acceleration and balance rating of the fifa dataset.'''


##### Here's an example of creating a Scatter Plot:

# Extracting columns
acceleration = top10_df['Acceleration']
balance = top10_df['Balance']

# Example: Scatter plot of Balance vs Acceleration in the top five fifa players
plt.figure(figsize=(14, 6))
plt.scatter(acceleration, balance, label = 'Players')
plt.xlabel('Acceleration')
plt.ylabel('Balance')
plt.title('Acceleration vs Balance for the top five players by FIFA')
#for i, player_name in enumerate(player_names):
#    plt.text(acceleration[i], balance[i], player_name, fontsize=8, ha='right', va='bottom')
for player_name, acc, bal in zip(top10_df.index, acceleration, balance):
    plt.text(acc, bal, player_name, fontsize=8, ha='right', va='bottom')

plt.gca().set_aspect('equal', adjustable='box')




plt.legend()
plt.show()






### Line Plots

'''Line plots are a very important plot type as they do a great job of displaying time series data. It is often important to visualize change over time to understand patterns in data that can be actioned on.

We can create a line plot in matplotlib using the plt.plot() method where the first argument is the x variable and the second argument is the y variable in our line plot. Whenever we create a plot, we need to make sure to call plt.show() to ensure we see the graph we have created.'''

##### Here's an example of creating a Line Chart:

x = np.array([1,4, 5])
y = np.array([6,10, 9])

plt.plot(x, y)
plt.show()














# importing the data (csv file)
stats = pd.read_csv('fifa.csv')

# checking the data
stats.head()


# creating a df for the relevant columns needed for my bar chart
top5_players= stats[['Name','Acceleration', 'Aggression', 'Agility', 'Balance', 'Overall']].iloc[0:5]
top5_players

# Changed the datatype to int to enable plotting because some columns had object dataype. 
top5_players['Acceleration'] = top5_players['Acceleration'].astype(str).astype(int)
top5_players['Aggression'] = top5_players['Aggression'].astype(str).astype(int)
top5_players['Agility'] = top5_players['Agility'].astype(str).astype(int)
top5_players['Balance'] = top5_players['Balance'].astype(str).astype(int)

# confirm the datatype has changed
print(top5_players.dtypes)

### Bar Chart

'''A barplot is one of the most common types of graphic, it is a type of data visualization used to represent data in the form of rectangular bars. Bar chart shows the relationship between a numeric and a categoric variable.'''



#### Vertical Bar chart

'''We will start by creating a bar chart with vertical bars. This can be done using the plt.bar() method with the first argument being the x-axis variable (Name) and the height parameter being the y-axis (acceleration, aggression, agility, balance).  We then want to make sure to call plt.show() to show our plot.'''

##### Here's an example of creating a vertical Bar Chart:

#set the plot style
plt.style.use('ggplot')

# plotting a vertical barchart to compare the players' skills
top5_players.plot(x="Name", y=["Acceleration", "Aggression", "Agility", "Balance"],
        kind="bar", ylabel='Skills', title="Comparing the Players' skills", figsize=(10, 5))
plt.show()

#### A Verical Bar chart showing names and acceleration of players

namee = top5_players['Name']
acceleration = (top5_players['Acceleration'])
plt.figure(figsize=(14, 6))
plt.bar(namee, agility, color='skyblue')
plt.xlabel('Player Names')
plt.ylabel('Acceleration')
plt.title('Player SPeed in FIFA')
plt.xticks(rotation=90)
plt.show()


#### Horizontal Bar chart

'''It is sometimes easier to interpret bar charts and read the labels when we make the bar plot with horizontal bars. We can do this by setting the kind parameter to barh.  '''

##### Here's an example of creating a horizontal Bar Chart:

# plotting a horizontal barchart to compare the players' skills and stacking their skills using the stacked parameter
 
top5_players.plot(x="Name", y=["Acceleration", "Aggression", "Agility", "Balance"],
        kind="barh", ylabel='Names', xlabel='Skills', title="Comparing the Players' skills", figsize=(10, 5), stacked=True)
plt.show()


### Histogram

'''Histogram is a fundamental tool in data visualization, providing a graphical representation of the distribution of data. They are particularly useful for exploring continuous data, such as numerical measurements or sensor readings.

Histogram can be by created using the plt.hist() function of matplotlib and pass in the data along with the number of bins and a few optional parameters like color, hist type, label.'''

##### Here's an example of creating a Histogram:

#Histogram of Player Ages
plt.figure(figsize=(10, 6))
plt.hist(top10_df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Player Ages in FIFA')
plt.xlabel('Age')
plt.ylabel('Number of Players')
plt.show()



### Box Plot

'''A Box Plot is created to display the summary of the set of data values having properties like minimum, first quartile, median, third quartile and maximum and also to identify outliers within a dataset. 

In the box plot, a box is created from the first quartile to the third quartile, a vertical line is also there which goes through the box at the median. Here x-axis denotes the data to be plotted while the y-axis shows the frequency distribution.

A box plot can be created by using the plt.boxplot() method and passing a number of parameters to it.'''

##### Here's an example of creating a Box Plot:





### Pie Chart

'''A Pie Chart is a circular statistical plot that can display only one series of data. The area of the chart is the total percentage of the given data. The area of slices of the pie represents the percentage of the parts of the data. The slices of pie are called wedges. The area of the wedge is determined by the length of the arc of the wedge. The area of a wedge represents the relative percentage of that part with respect to whole data. Pie charts are commonly used in business presentations like sales, operations, survey results, resources, etc as they provide a quick summary.

plt.pie() function is used to create a pie chart using matplotlib in Python, this function takes values and labels as inputs to generate a pie chart representing proportions and percentages.'''

##### Here's an example of creating a Pie Chart:



# Combine player names and speeds for the labels
labels = [f'{name} ({speed})' for name, speed in zip(namee, agility)]

# Plotting the pie chart
plt.figure(figsize=(10, 10))
plt.pie(agility, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribution of Player Names and Acceleration in FIFA')
plt.show()



### Heatmap

'''A heatmap in matplotlib is a great way to visualize data using colors to represent values in 2D array. Matplotlib provides functionalities to create heatmaps using the imshow() function.'''

##### Here's an example of creating a Heatmap:





### 3D Plot

'''Creating 3D plots using Matplotlib allows you to visualize data in three dimensions, which can be particularly useful for understanding complex relationships or surfaces in scientific or engineering contexts.

Mplot3d toolkit is used in creating a 3D plot in matplotlib, which allows the generation of various types of 3D plots like surface plot, scatter plot, wireframe plot, and more.'''


##### Here's an example of creating a 3D plot:





### Annotation and Text

'''Annotations and text can be added to plots to highlight specific points, provide additional information, or label certain features within the plot. 

In Matplotlib, annotation and text can be added using the plt.text() function for general text and the plt.annotate() function for annotated text with arrows pointing to specific data points.'''


##### Here's an example demonstrating how to add annotations and text to a plot:











