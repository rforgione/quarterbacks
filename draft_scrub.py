import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def scrub_data(url):
	""" Takes NFL combine data from www.nflcombineresults.com and turns it into a 
	pandas dataframe. The script was built with the following URL in mind:
	http://nflcombineresults.com/nflcombinedata.php?year=all&pos=&college= """
	
	url = urllib2.urlopen(url)
	page = url.read()
	soup = BeautifulSoup(page, 'html5lib')

	vec = np.array([i.text for i in soup.tbody.find_all('div', {'align': 'center'})]).reshape(-1,13)

	return pd.DataFrame(vec, columns=['Year', 'Name', 'College', 'POS', 'Height.in', 'Weight.lbs', 
			   					      'Wonderlic', '40yd', 'Bench', 'Vert', 'BroadJump', 'Shuttle', '3cone'])


def forty_yd_list(g):
	g = [float(i) for i in [i for i in list(g['40yd']) if i != '' and '*' not in i]]

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.hist(g, 100, color='green', alpha=0.8)
	ax.set_xlim(4, 6)
	ax.set_xlabel('Time (s)')
	ax.set_ylabel('Frequency')
	ax.set_title("40-yard Dash Times - All Positions (NFL Combine)")
	plt.xticks(np.arange(4,6,.15))
	plt.show()
