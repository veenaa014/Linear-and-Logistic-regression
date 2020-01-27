Simple Linear Regression is a statistical method to find relationship between two continuous variables, where one is independent variable 
and the other is dependent variable. 

The basic assumption for the linear regression model is that a linear relationship exists between the independent variable (X) 
and dependent variable (y).

* Import the dataset and perform Data pre-processing.
* Fit the dataset into Simple Linear Regression model.
* Visualising the correlation in the dataset.

Correlation Coefficient: r
* r has values between -1 and 1.
* It measures the linear relationship between two quantitative variables with respect to 
direction and strength.

Coefficient of determination: r**2
* r**2 has values between 0 and 1.
* It is a measure of how close each data point fits to the regression line.
* It tells us how well the regression line predicts actual values.
* r**2 close to 1 tells us that the predicted values and the actual values are close together.
* r**2 close to 0 tells us that the regression line doesn't fit the data so well, there is 
large amount of distance between the actual and predicted values.

R-squared is the percentage of variation in 'y' that is accounted for by its regression
on 'x'. 

For example, in house price prediction, if y-axis is price and x-axis is the square foot size.
Say r=0.94, r**2 = 0.94*0.94 = 0.88. This tells that 88% of the variation in house price is accounted for by its regression on square foot size.
