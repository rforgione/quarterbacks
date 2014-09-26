import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def scrub_data(url):
	""" Takes NFL combine data from www.nflcombineresults.com and turns it into a 
	pandas dataframe. """
	
	url = urllib2.urlopen(url)
	page = url.read()
	soup = BeautifulSoup(page)

	elems = [i.text for i in soup.tbody.find_all("div", {'align': 'center'})]

	dataset = []

	vec = np.array(elems)

	mat = vec.reshape(-1, 13)

	return pd.DataFrame(mat, columns=['Year', 'Name', 'College', 'POS', 'Height.in', 'Weight.lbs', 
									  'Wonderlic', '40yd', 'Bench', 'Vert', 'BroadJump', 'Shuttle', '3cone'])