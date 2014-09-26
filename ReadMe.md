### Quarterback Success Predictions

This project aims to take data on college performance and NFL combine metrics from college quarterbacks, and use them to predict success at the NFL level. 

As of now, I will be using data from the following sources:
* http://www.nflcombineresults.com
* http://www.sports-reference.com/cfb/players/

I am using Python along with Pandas, NumPy, BeautifulSoup, and urllib2.

The planned approach is as follows:
1. Collect data
2. Perform exploratory data analysis and vizualization
3. Encode dataset into a numerical data matrix that can be processed algorithmically
4. Train a classification algorithm on this data where the combine data and college
statistics are the features, and the output is some measure of success at the NFL level
(right now I am considering using Pro Bowl selections)

