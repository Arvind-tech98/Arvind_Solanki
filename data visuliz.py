import pandas as pd
import  matplotlib.pyplot as plt
import pandas_profiling
from pandas_profiling import ProfileReport
#from matplotlib import dates as mpl_dates

#plt.style.use('seaborn')

data = pd.read_csv('March-April.2020.csv')

profile= ProfileReport(data)
profile
#data.DATE = pd.to_datetime(data['DATE'])  #to sort the date format
#data.sort_values('DATE', inplace = True)

#data
#Raipur = data[data.DISTRICT == 'Raipur']

#Raipur = data[data.DISTRICT == 'Raipur']
#plt.plot(Raipur.DATE, Raipur.TOTAL_CASES)


#plt.plot(data.DATE, data.TOTAL_CASES, linestyle= 'solid')
#plt.plot(data.DATE, data.RECOVERED_CASES)
#plt.plot(data.DATE, data.DECRESED_CASES, linestyle = 'dotted')

#plt.gcf().autofmt_xdate()  #to tilt the date format make easiler to read


#plt.plot(Raipur.Date, Raipur.Tested)

#plt.xlabel("DATE")
#plt.title("Covid_Cases")
#plt.ylabel("CASES")

#plt.tight_layout()

#plt.legend(["Confirmed cases", "Recovered cases", "Decreased cases"])
#plt.show()