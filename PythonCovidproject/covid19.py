import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

state_count=pd.read_csv('/Users/abhinavchoudhary/Documents/Pythongit/PythonCovidproject/covid_19_india.csv')

def statesdata(states_name):
    state_data = state_count.groupby('StateName')
    states = state_data.get_group(states_name)
    plt.figure(figsize=(20,10))
    plt.plot(states.Date,states.Confirmed,'r',label = "Total Confirmed")
    plt.plot(states.Date,states.Cured,'g',label = "Total Recovered")
    plt.plot(states.Date,states.Deaths,'k',label = "Total Deceased")
    plt.plot(states.Date,(states.Confirmed-(states.Cured+states.Deaths)),'b',label = "Total Active")
    plt.xticks(np.arange(0,states.shape[0],10))
    plt.xticks(rotation = 45)
    plt.xlabel('Date')
    plt.ylabel('Total No.')
    plt.title('Total No. of COVID-19 (Confirmed Cases, Recovered Cases, Deceased Case and Active Cases)')
    plt.legend()
    plt.grid()
    plt.show()

statesdata('Delhi')

def statecompare(state_name1,state_name2):
    state_data = state_count.groupby('StateName')
    state1 = state_data.get_group(state_name1)
    state2 = state_data.get_group(state_name2)
    plt.figure(figsize=(20,10))
    plt.plot(state2.Date,state2.Confirmed,'r',label = state_name2+' confirmed')
    plt.plot(state2.Date,state2.Cured,'g',label = state_name2+' recoverd')
    plt.plot(state2.Date,state2.Deaths,'k',label = state_name2+' deceased')
    plt.plot(state2.Date,(state2.Confirmed-(state2.Cured+state2.Deaths)),'b',label = state_name2+' active')
    plt.plot(state1.Date+(state2.shape[0]-state1.shape[0]),state1.Confirmed,'p',label = state_name1+' confirmed')
    plt.plot(state1.Date+(state2.shape[0]-state1.shape[0]),state1.Cured,'y',label = state_name1+' recoverd')
    plt.plot(state1.Date+(state2.shape[0]-state1.shape[0]),state1.Deaths,'q',label = state_name1+' deceased')
    plt.plot(state1.Date+(state2.shape[0]-state1.shape[0]),(state1.Confirmed-(state1.Cured+state1.Deaths)),'bw',label = state_name1+' active')
    plt.xticks(np.arange(0,state2.shape[0],10))
    plt.xticks(rotation = 45)
    plt.xlabel('Date')
    plt.ylabel('Total No.')
    plt.title('Total No. of COVID-19 (Confirmed Cases, Recovered Cases, Deceased Case and Active Cases)')
    plt.legend()
    plt.grid()
    plt.show()

    
  


def indiacount():
    country_data = state_count.groupby('Date').sum(['Confirmed','Cured','Deaths'])
    # country_data = state_count.groupby("Date")
    # country_data.info()
    # country_data.astype({"Date":'datetime64[D]'})
    print(country_data.get("Date"))
    # plt.figure(figsize=(20,10))s
    # plt.plot(country_data.Date,country_data.Confirmed,'r',label = "Total Confirmed")
    # plt.plot(country_data.Date,country_data.Cured,'g',label = "Total Recovered")
    # plt.plot(country_data.Date,country_data.Deaths,'k',label = "Total Deceased")
    # plt.plot(country_data.Date,(country_data.Confirmed-(country_data.Cured+country_data.Deaths)),'b',label = "Total Active")
    # plt.xticks(np.arange(0,country_data.shape[0],10))
    # plt.xticks(rotation = 45)
    # plt.xlabel('Date')
    # plt.ylabel('Total No.')
    # plt.title('Total No. of COVID-19 (Confirmed Cases, Recovered Cases, Deceased Case and Active Cases)')
    # plt.legend()
    # plt.grid()
    # plt.show()   

def statecurrent():
    state_current = state_count.groupby('StateName').last()
    plt.figure(figsize=(20,20))
    bw = 0.2
    statecount = np.arange(46)
    plt.bar(statecount,state_current.Confirmed,width=bw,color='m',label='Confirmed Cases')
    plt.bar(statecount+bw,state_current.Cured,width=bw,color='g',label='Cured Cases')
    plt.bar(statecount+bw+bw,state_current.Deaths,width=bw,color='m',label='Deceased Cases')
    plt.grid()
    plt.show()


#       #States Trend
#       conti = (input('Do you want to continue after this yes or no?')).lower()
#       plt.figure(figsize=(20,20))
#       bw=0.2
#       #bw is bar width
#       x_axis= np.arange(36)
#       plt.bar(x_axis,states_confirmed,width=bw,color='m',label='Confirmed Cases')
#       plt.bar(x_axis+bw,states_recovered,width=bw,color='g',label='Recovered')
#       plt.bar(x_axis+bw+bw,states_deaths,width=bw,color='blue',label='Deceased')
#       plt.xticks(x_axis+bw, states)
#       plt.xticks(rotation= 90)
#       plt.yticks(np.arange(0,1698199,40000),('0','40K','80K','120K','160K','200K','240K','280K','320K','360K','400K','440K','480K','520K','560K','600K','640K','680K','720K','760K','800K','840K','880K','920K','960K','1000K','1040K','1080K','1120K','1160K','1200K','1240K','1280K','1320K','1360K','1400K','1440K','1480K','1520K','1560K','1600K','1640K','1680K' ))
#       plt.legend(loc='upper right',ncol=3)
#       plt.title('Statewise Confirmed Cases, Recoveries \n & Deceased')
#       plt.grid()
#       plt.show()



# print('COVID-19')
# print("This part of the code helps in the comparison of the graphs we have made in some of the many parameters like daily and total cases, deaths, recoveries of different countries. These countries being India, Nepal, Pakistan, Brazil and the USA. This is a menu driven user based program in which the user gets to choose which countries' Covid-19 data do they want to compare and the output will be based on that choice")#about the project
# conti = 'yes'
# while conti == 'yes':
#   print('COVID-19 trends around the world-','\n','1) Covid trends in India.','\n','2) Comparing trend of diffrent countries.','\n','3) Sources')
#   menu1= int(input('Enter the no. corresponding to the required menu'))
#   if menu1 == 1:
#     #Covid trends in India
#     print('Covid trends in India','\n','1)Total No. of COVID-19 (Confirmed Cases, Recovered Cases, Deceased Cases and Active Cases)','\n','2)Daily No. of COVID-19 (Confirmed Cases, Recovered Cases and Deceased Cases)','\n','3)Confirmed Only','\n','4)Recovered Only','\n','5)Deceased Only','\n','6)States Trends')
#     menu2 = int(input('Enter the no. corresponding to the required menu'))
#     if menu2 == 1:
#       #Total No. of COVID-19 (Confirmed Cases, Recovered Cases, Deceased Case and Active Case)
#       conti = (input('Do you want to continue after this yes or no?')).lower()
#       plt.figure(figsize=(20,10))
#       plt.plot(date,total_confirmed,'r',label = "Total Confirmed")
#       plt.plot(date,total_recovered,'g',label = "Total Recovered")
#       plt.plot(date,total_deceased,'k',label = "Total Deceased")
#       plt.plot(date,(total_confirmed-(total_recovered+total_deceased)),'b',label = "Total Active")
#       plt.xticks(np.arange(0,275,10))
#       plt.xticks(rotation = 45)
#       plt.yticks(np.arange(0,8183317,1000000),('0','10L','20L','30L','40L','50L','60L','70L','80L'))
#       plt.xlabel('Date')
#       plt.ylabel('Total No.')
#       plt.title('Total No. of COVID-19 (Confirmed Cases, Recovered Cases, Deceased Case and Active Cases)')
#       plt.legend()
#       plt.grid()
#       plt.show()
#       print('The Line chart represents the total daily impact of Covid-19 on India with the gaps of 10 days each. The red line represents total confirmed cases which peaked at the latter stages of October when it crossed the 80 Lakhs mark. It took us upto about 18th July to hit our first 10 Lakh cases. The exponential growth of the graph shows how fast the pandemic spread throughout the nation. The green line shows the amount of recoveries made from this pandemic. The confirmed cases peaked near the end of October. We made our first 10 Lakh recoveries on 28th of July. Total active cases are represented by the dark blue line, these peaked at around the 16th September. The black line represents the total deceased throughout India. All data used in the chart above is recorded until the 31st of October.')
#     elif menu2 == 2:
#       #Daily No. of COVID-19 (Confirmed Cases, Recovered Cases and Deceased Case)
#       conti = (input('Do you want to continue after this yes or no?')).lower()
#       plt.figure(figsize=(20,10))
#       plt.plot(date,daily_confirmed,'m-.',label = "Daily Confirmed")
#       plt.plot(date,daily_recovered,'g-.',label = "Daily Recovered")
#       plt.plot(date,daily_deceased,'b-.',label = "Daily Deceased") 
#       plt.xticks(np.arange(0,275,10))
#       plt.xticks(rotation = 45) 
#       plt.xlabel('Date') 
#       plt.ylabel('Daily Cases') 
#       plt.title('Daily Impact Of Covid 19(Daily Cases, Daily Recoveries & Daily Deceased') 
#       plt.legend() 
#       plt.grid() 
#       plt.show()
#       print('The line chart above depicts daily impact of Covid-19 with a gap of 10 days each. The magenta dotted line represents reported daily confirmed cases. The maximum spike in the confirmed cases was on 16th September when the cases hit nearly 96000 plus cases. The green line depicts the daily recoveries made around India. The recoveries topped in the 10 day span between 16th and 26th September when they hit 110000+. The blue line represents number of deaths reported daily throughout India. All data used in the chart above is recorded until the 31st of October.')
#     elif menu2 == 3:
#       #Confirmed Only
#       conti = (input('Do you want to continue after this yes or no?')).lower()
#       plt.figure(figsize=(20,10))
#       axis1= plt.subplot()
#       axis2= axis1.twinx()
#       d_confirmed = axis1.plot(date,daily_confirmed,'r-.',label = 'Daily')
#       t_confirmed = axis2.plot(date,total_confirmed,'r', label = 'Total')
#       plt.xticks(np.arange(0,275,20))
#       plt.xticks(rotation = 45)
#       plt.yticks(np.arange(0,8183317,1000000),('0','10L','20L','30L','40L','50L','60L','70L','80L'))
#       axis1.set_xlabel('Date')
#       axis1.set_ylabel('Daily No.')
#       axis2.set_ylabel('Total No.')
#       axis1.set_title('Confirmed')
#       confirmed_leg = d_confirmed + t_confirmed
#       lab1 = [l.get_label() for l in confirmed_leg ]
#       axis1.legend(confirmed_leg,lab1)
#       plt.show()
#       print('This line graph shows confirmed cases throughout India at the gaps of 10 days each. The dotted lines show the daily confirmed cases in India where the y-axis on the left helps depict the numerical value of the graph. The daily confirmed cases peaked in the month of September, from the 6th to 26th after which the graph went downhill which is a pleasant change. The continuous line depicts the total number of confirmed cases reported till that date. The y-axis on the right is the one associated with the daily confirmed cases. The total confirmed cases have obviously kept on growing.  All data used in the chart above is recorded until the 31st of October.')
#     elif menu2 == 4:
#       #Recovered Only
#       conti = (input('Do you want to continue after this yes or no?')).lower()
#       plt.figure(figsize=(20,10))
#       axis1= plt.subplot()
#       axis2= axis1.twinx()
#       d_recovered = axis1.plot(date,daily_recovered,'g-.',label = 'Daily')
#       t_recovered = axis2.plot(date,total_recovered,'g', label = 'Total')
#       plt.xticks(np.arange(0,275,20))
#       plt.xticks(rotation = 45)
#       plt.yticks(np.arange(0,8183317,1000000),('0','10L','20L','30L','40L','50L','60L','70L','80L'))
#       axis1.set_xlabel('Date')
#       axis1.set_ylabel('Daily No.')
#       axis2.set_ylabel('Total No.')
#       axis1.set_title('Recovered')
#       recovered_leg = d_recovered + t_recovered
#       lab2 = [l.get_label() for l in recovered_leg ]
#       axis1.legend(recovered_leg,lab2)
#       plt.show()
#       print('The line chart above depicts the data of recoveries made in India. The daily recovery is represented by the dotted line and it is associated with the y-axis on the left side. The total recovery is represented by the solid line and it is associated with the y-axis on the right side.The daily recovery reached its max in the month of September when the cases were also at its highest. All data used in the chart above is recorded until the 31st of October.')
#     elif menu2 == 5:
#       #Deceased Only
#       conti = (input('Do you want to continue after this yes or no?')).lower()
#       plt.figure(figsize=(20,10))
#       axis1= plt.subplot()
#       axis2= axis1.twinx()
#       d_deceased = axis1.plot(date,daily_deceased,'k-.',label = 'Daily')
#       t_deceased = axis2.plot(date,total_deceased,'k', label = 'Total')
#       plt.xticks(np.arange(0,275,20))
#       plt.xticks(rotation = 45)
#       axis1.set_xlabel('Date')
#       axis1.set_ylabel('Daily No.')
#       axis2.set_ylabel('Total No.')
#       axis1.set_title('Deceased')
#       deceased_leg = d_deceased + t_deceased
#       lab3 = [l.get_label() for l in deceased_leg ]
#       axis1.legend(deceased_leg,lab3)
#       plt.show()
#       print('The line chart above shows the number of deaths reported in India with a gap of 10 days each. The dotted line represents the daily amount of deaths reported. The y-axis on the left is associated with this line. This number peaked at around 19th June when it touched 2000+ deaths. Thankfully this graph came down after the end of October. The continuous black line represents the total amount of deaths to that day. The y-axis on the rights is the one associated with the total number of deceased. This number crossed more than 120000 by the end of October. All data used in the chart above is recorded until the 31st of October.')
#     elif menu2 == 6:
#       #States Trend
#       conti = (input('Do you want to continue after this yes or no?')).lower()
#       plt.figure(figsize=(20,20))
#       bw=0.2
#       #bw is bar width
#       x_axis= np.arange(36)
#       plt.bar(x_axis,states_confirmed,width=bw,color='m',label='Confirmed Cases')
#       plt.bar(x_axis+bw,states_recovered,width=bw,color='g',label='Recovered')
#       plt.bar(x_axis+bw+bw,states_deaths,width=bw,color='blue',label='Deceased')
#       plt.xticks(x_axis+bw, states)
#       plt.xticks(rotation= 90)
#       plt.yticks(np.arange(0,1698199,40000),('0','40K','80K','120K','160K','200K','240K','280K','320K','360K','400K','440K','480K','520K','560K','600K','640K','680K','720K','760K','800K','840K','880K','920K','960K','1000K','1040K','1080K','1120K','1160K','1200K','1240K','1280K','1320K','1360K','1400K','1440K','1480K','1520K','1560K','1600K','1640K','1680K' ))
#       plt.legend(loc='upper right',ncol=3)
#       plt.title('Statewise Confirmed Cases, Recoveries \n & Deceased')
#       plt.grid()
#       plt.show()
#       print('The given bar chart shows the statewise confirmed, recovered & deceased cases. We can see that Maharashtra has been leading the race in the cases reported, and hence in it is also leading in recoveries. Both being around 17 lakhs and 15.3 lakhs respectively. Lakshadweep Islands on the other hand managed to keep themselves Covid-19 free due to proper management and precautions throughout these challenging times. This shows how prevention is better than cure. In small states like Sikkim & Dadra and Nagar Haveli and Daman and Diu have an almost same amount of recoveries as they have confirmed cases.')
#     else :
#       print('Please enter a valid option!')
#   elif menu1 == 2:
#     #Comparing trend of different countries
#     conti = (input('Do you want to continue after this yes or no?')).lower()
#     print('The World','\n','1)Total Cases','\n','2)Daily Cases')
#     menu3 = int(input('Enter the no. corresponding to the required menu'))
#     if menu3 == 1:
#       ch_diff = 'no'
#       while ch_diff == 'no':
#         choice1 = (input('Pease enter the first country of your choice from the the given 5 options- 1) new zealand 2) pakistan 3) USA 4) India 5) Brazil')).lower()
#         choice2 = (input('Pease enter the second country of your choice from the the given 5 options- 1) new zealand 2) pakistan 3) USA 4) India 5) Brazil')).lower()
#         if choice1 == choice2:
#           ch_diff = 'no'
#         else:
#           ch_diff = 'yes'
#       total = countries.total_cases
#       dates = countries.date
#       dates = dates.iloc[0:309]
#       new_zealand = total.iloc[35470:35779]
#       pakistan = total.iloc[37389:37698]
#       usa = total.iloc[51319:51628]
#       india = total.iloc[22844:23153]
#       brazil = total.iloc[6981:7290]
#       plt.figure(figsize=(20,10))
#       if choice1 == 'india':
#         plt.plot(dates,india,'m',label = 'India')
#       elif choice1 == 'usa':
#         plt.plot(dates,usa,'b',label = 'USA')
#       elif choice1 == 'new zealand':
#         plt.plot(dates,new_zealand,'c',label = 'new zealand')
#       elif choice1 == 'pakistan':
#         plt.plot(dates,pakistan,'g',label = 'pakistan')
#       elif choice1 == 'brazil':
#         plt.plot(dates,brazil,'k',label = 'Brazil')
#       else :
#         print('sorry we did not get the first choice')
#       if choice2 == 'india':
#         plt.plot(dates,india,'m',label = 'India')
#       elif choice2 == 'usa':
#         plt.plot(dates,usa,'b',label = 'USA')
#       elif choice2 == 'new zealand':
#         plt.plot(dates,new_zealand,'c',label = 'new zealand')
#       elif choice2 == 'pakistan':
#         plt.plot(dates,pakistan,'g',label = 'pakistan')
#       elif choice2 == 'brazil':
#         plt.plot(dates,brazil,'k',label = 'Brazil')
#       else:
#         print('Sorry we did not got the second choice')
#       if choice1 == 'usa' or choice2 == 'usa':
#         plt.yticks(np.arange(0,9383979,1000000),('0','10L','20L','30L','40L','50L','60L','70L','80L','90L'))
#       elif choice1 == 'india' or choice2 == 'india':
#         plt.yticks(np.arange(0,8313876,1000000),('0','10L','20L','30L','40L','50L','60L','70L','80L'))
#       elif choice1 == 'brazil' or choice2 == 'brazil':
#         plt.yticks(np.arange(0,5566049,1000000),('0','10L','20L','30L','40L','50L'))
#       plt.xticks(np.arange(0,309,7))
#       plt.xticks(rotation = 90)
#       plt.xlabel('Dates')
#       plt.ylabel('Total No. Cases')
#       plt.title('Covid-19 in'+' '+choice1+' and '+choice2)
#       plt.grid()
#       plt.legend()
#       plt.show()
#     elif menu3 == 2:
#       ch_diff = 'no'
#       while ch_diff == 'no':
#         choice1 = (input('Pease enter the first country of your choice from the the given 5 options- 1) New Zealand 2) Pakistan 3) USA 4) India 5) Brazil ')).lower()
#         choice2 = (input('Pease enter the second country of your choice from the the given 5 options- 1) New Zealand 2) Pakistan 3) USA 4) India 5) Brazil ')).lower()
#         if choice1 == choice2:
#           ch_diff = 'no'
#         else:
#           ch_diff = 'yes'
#       daily = countries.new_cases
#       dates = countries.date
#       dates = dates.iloc[0:309]
#       new_zealand = daily.iloc[35470:35779]
#       pakistan = daily.iloc[37389:37698]
#       usa = daily.iloc[51319:51628]
#       india = daily.iloc[22844:23153]
#       brazil = daily.iloc[6981:7290]
#       plt.figure(figsize=(20,10))
#       if choice1 == 'india':
#         plt.plot(dates,india,'m',label = 'India')
#       elif choice1 == 'usa':
#         plt.plot(dates,usa,'b',label = 'USA')
#       elif choice1 == 'new zealand':
#         plt.plot(dates,new_zealand,'c',label = 'New Zealand')
#       elif choice1 == 'pakistan':
#         plt.plot(dates,pakistan,'g',label = 'Pakistan')
#       elif choice1 == 'brazil':
#         plt.plot(dates,brazil,'k',label = 'Brazil')
#       else :
#         print('Sorry we did not got the first choice')
#       if choice2 == 'india':
#         plt.plot(dates,india,'m',label = 'India')
#       elif choice2 == 'usa':
#         plt.plot(dates,usa,'b',label = 'USA')
#       elif choice2 == 'new zealand':
#         plt.plot(dates,new_zealand,'c',label = 'New Zealand')
#       elif choice2 == 'pakistan':
#         plt.plot(dates,pakistan,'g',label = 'Pakistan')
#       elif choice2 == 'brazil':
#         plt.plot(dates,brazil,'k',label = 'Brazil')
#       else:
#         print('Sorry we did not got the second choice')
#       plt.xticks(np.arange(0,309,7))
#       plt.xticks(rotation = 90)
#       plt.xlabel('Dates')
#       plt.ylabel('Daily No. Cases')
#       plt.title('Covid-19 in'+' '+choice1+' and '+choice2)
#       plt.grid()
#       plt.legend()
#       plt.show()
#     else:
#       print('Please enter a valid option!')
#   elif menu1 == 3:
#     #Sources
#     print('The Sources for the given data are-','\n','India- https://www.covid19india.org/','\n','World- https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
#     conti = (input('Do you want to continue yes or no')).lower()
#   else :
#     print('Please enter a valid option!')
# print('thank you')