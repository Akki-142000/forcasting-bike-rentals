# Forcasting Bike Rentals
*The objective of the project is - using historical usage patterns and weather data, forecast(predict) bike rental demand number of bike users on hourly basis.
*We use the provided “Bikes Rental” data set to predict the bike demand bike users count  using various best possible models (ML algorithms).
and report the model that performs best, fine-tune the same model using one of the model fine-tuning techniques.
and report the best possible combination of hyperparameters for the selected model.
*Lastly, use the selected model to make final predictions and compare the predicted values with the actual values.
*Below are the details of the features list for the given Bikes data set:
*instant: record index
*dteday : date
*season: season (1: springer, 2: summer, 3: fall, 4: winter)
*yr: year (0: 2011, 1:2012)
*mnth: month (1 to 12)
*hr: hour (0 to 23)
*holiday: whether the day is a holiday or not
*weekday: day of the week
*workingday: if day is neither weekend nor holiday is 1, otherwise is 0.
*weathersit:
*1: Clear, Few clouds, Partly cloudy, Partly cloudy
*2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
*3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
*4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
*temp: Normalized temperature in Celsius.
*atemp: Normalized feeling temperature in Celsius.
*hum: Normalized humidity. The values are divided to 100 (max)
*windspeed: Normalized wind speed. The values are divided to 67 (max)
*casual: count of casual users
*registered: count of registered users
*cnt: count of total rental bikes including both casual and registered users

*We will be following the below steps to solve this problem:
*Importing the libraries
*Using some pre-defined utility functions
*Loading the data
*Cleaning the data
*Dividing the dataset into training and test dataset
*using train_test_split in the ratio 70:30
*Training several models and analyzing their performance to select a model
*Fine-tuning the model by finding the best hyper-parameters and features
*Evaluating selected model using test dataset


