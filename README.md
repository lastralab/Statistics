# Gender and the environment in Mexico

Capstone Project for <a href="https://www.coursera.org/specializations/python">Coursera Specialization</a>: "Retrieving, Processing, and Visualizing Data with Python".
<br>
<img src="https://user-images.githubusercontent.com/22894897/31048907-89598960-a5fe-11e7-881e-c2081dd9edd8.png" width="100%"/>
<br>

I downloaded data files from http://www.inegi.org.mx/ and I wrote Python programs to read, extract, analyze and visualize that data, in a way that anyone can use them for their own purposes, by entering the name of their own files:

The main **INSTRUCTIONS** for all of them are very simple:

- Select file.
- Select column header.
- Select alpha (if applies).
- Enter 'ya' to quit.
- etc.

**_All the programs have the same structure so you can use the same keywords to start/proceed/quit._**  

- <a href="https://github.com/lastralab/Statistics/blob/master/MoCT.py"><b>MoCT.py</b></a><br>
  - Measures of Central Tendency:
  - N, mean, standard deviation, standard error, etc.
  - Sampling distribution graph
  - z-value and p-value from z-table
  - z-score
  - One tailed T-test
  - Confidence Interval
  - Acceptance/Rejection of the null hypothesis.
   <br><br>
<img src="https://user-images.githubusercontent.com/22894897/30722723-2ffa7ec0-9f09-11e7-8fb4-38d9f12c1061.png" width=50%/><img src="https://user-images.githubusercontent.com/22894897/30881591-b63e3a86-a2dc-11e7-863f-26fe1a2a848e.png" width=50%/><br>
  <br>
  
- <a href="https://github.com/lastralab/Statistics/blob/master/DepT-test.py"><b>DepT-test</b></a><br>
  - Two tailed T-test
  - Column behavior graph
  - Differences of means graph
  - T-statistic
  - Cohen's D
  - Acceptance/rejection of the null hypothesis
  - Confidence Interval
   <br><br>
<img src="https://user-images.githubusercontent.com/22894897/30747470-c444ecbc-9f83-11e7-8d5f-272e473878e3.png" width=50%/><img src="https://user-images.githubusercontent.com/22894897/30747472-c662db76-9f83-11e7-8892-4f998ad1710a.png" width=50%/><br>
  <br>
  
- <a href="https://github.com/lastralab/Statistics/blob/master/ConverS.py"><b>ConverS.py</b></a><br>
  - Value replacement
  - You need to modify this code in order to convert your own data

- <a href="https://github.com/lastralab/Statistics/blob/master/RangeR.py"><b>RangeR.py</b></a><br>
  - Values assignment to Intervals
  - Returns minimum and maximum
  - Returns factors for that range
  - New file with data split by intervals
<br><br>
<img src="https://user-images.githubusercontent.com/22894897/30775730-ddb76822-a06f-11e7-907a-4b892353f880.png" height=350px/><img src="https://user-images.githubusercontent.com/22894897/30775757-7f0a2d18-a070-11e7-93d8-eae1feef4574.png" height=350px/><br><br>  

- <a href="https://github.com/lastralab/Statistics/blob/master/SkewU.py"><b>SkewU.py</b></a><br>
  - Skewness calculation
  - Returns skewness representation graph
<br><br>
<img src="https://user-images.githubusercontent.com/22894897/30722630-b2205c22-9f08-11e7-88b1-0afc91895027.png" width=50%/><img src="https://user-images.githubusercontent.com/22894897/30722629-b1ecea86-9f08-11e7-87af-f995280449e4.png" width=50%/><br>
  <br>
- <a href="https://github.com/lastralab/Statistics/blob/master/Boxy.py"><b>Boxy.py</b></a><br>
  - BoxCox transformation to reduce skewness
  - Original skewed data histogram
  - Un-skewed data using sqrt histogram
  - Un-skewed data using BoxCox histogram
  - Create file with new data (using BoxCox or sqrt), optional
     <br><br>
<img src="https://user-images.githubusercontent.com/22894897/30747462-c15cc358-9f83-11e7-9abc-2665662b8fb2.png" width=100%/><br>
  <br>
 
- <a href="https://github.com/lastralab/Statistics/blob/master/Stan.py"><b>Stan.py</b></a><br>
  - Standardization of data
  - Comparison graphs
  - Creates new file with standardized data
 <br><br>
<img src="https://user-images.githubusercontent.com/22894897/30747475-c8ece6ac-9f83-11e7-8ec1-f1abbfd6e67c.png" width=50%/><img src="https://user-images.githubusercontent.com/22894897/30747478-c9e3e7a4-9f83-11e7-893f-a8706f519880.png" width=50%/><br>
  <br>
  
- <a href="https://github.com/lastralab/Statistics/blob/master/PeaR.py"><b>PeaR.py</b></a><br>
  - Pearson correlation coefficient
  - p-value
  - Returns graph of correlation relationship
<br><br>
<img src="https://user-images.githubusercontent.com/22894897/30765204-d0e38848-9fc4-11e7-9dd0-20916fc8a484.png" width=50%/><img src="https://user-images.githubusercontent.com/22894897/30722727-303258f4-9f09-11e7-8b9a-3041fa9e7a24.png" width=50%/><br>

- <a href="https://github.com/lastralab/Statistics/blob/master/SpeaR.py"><b>SpeaR.py</b></a><br>
  - Spearman correlation coefficient
  - p-value
  - Returns graph of correlation relationship
  <br><br>
<img src="https://user-images.githubusercontent.com/22894897/30762494-94002e6a-9fb8-11e7-833c-cde847c021d3.png" width=50%/><img src="https://user-images.githubusercontent.com/22894897/30762497-964f8ba2-9fb8-11e7-9b08-122380dc0beb.png" width=50%/><br>
<br>

- <a href="https://github.com/lastralab/Statistics/blob/master/ANowoa.py"><b>Anowoa.py</b></a><br><br>
  - Analysis of Variance (ANOVA), one or two ways <br> 
  - Returns Analysis of Variance between two or more group means <br>
  - Returns Degrees of Freedom, Sum of Squares, Mean Square <br>
  - Returns F-value and p-value <br>
  - Returns Eta squared and Omega squared for effect size  <br>
  - Returns ANOVA table and variables scatter graph
  <br><br>
<img src="https://user-images.githubusercontent.com/22894897/31048484-34411fba-a5f4-11e7-8dca-d15228664176.png" height="300px"/><img src="https://user-images.githubusercontent.com/22894897/31048485-35bf2116-a5f4-11e7-8239-a48707fc0e46.png" height="400px"/><br>
<br><br>
<br><br>
More data visualization coming soon...
<br>
<br>
<p><b>How to Python:</b></p>
<a href="https://www.python.org/downloads/">Downloads here!</a><br><br>
- <a href="https://docs.python.org/3/using/mac.html">Macintosh</a>.<br>
- <a href="https://docs.python.org/3/using/unix.html">Unix</a>.<br>
- <a href="https://docs.python.org/3/using/windows.html">Windows</a>:<br>
~ <a href="https://www.youtube.com/watch?v=BArhFr06nPM">Tutorial for Windows installation</a>.<br>
~ <a href="https://www.youtube.com/watch?v=ZO1SKpL8Jxk">Easy Way to run Python Programs on Windows</a>.<br>

<br>
<br>
<p align="center"><a href="https://lastralab.github.io/website/index.html" target="_blank"><br><button><img src="http://i.imgur.com/ERyS5Xn.png" alt="l'astra lab icon" width="50px" background="transparent" opacity="0.5" padding="0;"/></button></a></p><br><br>
