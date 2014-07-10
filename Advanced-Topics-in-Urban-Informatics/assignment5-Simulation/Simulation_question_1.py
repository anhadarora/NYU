import random
import numpy as np
from random import expovariate
import pandas as pd
import matplotlib.pyplot as plt
from math import log10, log
from scipy.stats import johnsonsb, gamma
import scipy.stats as ss

def simulation(time, rate, mean, k):
    arrival_time = 0 
    arrival_time_list = [0]
    arrival_headway_list = [0]
    service_time = (mean-0.25)+ round(np.random.random()*0.5, 2) # generate the first service time
    service_time_list = [service_time]
    departure_time = service_time
    departure_time_list = [departure_time]
    delay_time = service_time
    delay_time_list = [delay_time]
    for i in range(0, 1000):
        if arrival_time <time:
            arrival_headway = round(random.expovariate(rate), 2) # generate arrival time interval
            arrival_headway_list.append(arrival_headway)
            arrival_time += arrival_headway
            arrival_time_list.append(arrival_time)
            service_time = (mean-0.25)+ round(np.random.random()*0.5,2) # generate service time
            service_time_list.append(service_time)
            if arrival_time>= departure_time: # determine the departure time
                departure_time = arrival_time + service_time
                delay_time = service_time
                departure_time_list.append(departure_time)
                delay_time_list.append(delay_time)
            else: 
                departure_time = departure_time + service_time
                delay_time = departure_time - arrival_time
                departure_time_list.append(departure_time)
                delay_time_list.append(delay_time)
    index = np.arange(len(arrival_headway_list))+1
    departure_list = []
    for i in range(0, len(arrival_headway_list)):
        if departure_time_list[i] <1000:
            departure_list.append(departure_time_list[i])
            n = i
    index_2 = np.arange(n+1)
    ax = plt.subplot(111)
    ar, = plt.plot(arrival_time_list, index)
    de, = plt.plot(departure_list, index_2)
    plt.title("Arrivals and Departures")
    plt.legend([ar, de], ["Arrivals", "Departures"], loc = 2)
    ax.set_xlim(-0.5, 1000.5)
    plt.show()
    average_delay = (np.array(delay_time_list)).sum()/len(delay_time_list)
    output = pd.DataFrame({'CUSTOMER':index,'ARRIVAL HEADWAY':arrival_headway_list, 'ARRIVAL TIME':arrival_time_list, 'SERVICE TIME':service_time_list, 'DEPARTURE TIME':departure_time_list, 'DELAY TIME': delay_time_list})
    output.to_csv('Outputxxx1.txt',"\t", index = False, header = True,cols = ["CUSTOMER", "ARRIVAL HEADWAY", "ARRIVAL TIME", "SERVICE TIME", "DEPARTURE TIME", "DELAY TIME"] )
    np.save('delay_list', delay_time_list)
    np.save('arrival_list', arrival_time_list)
    return (average_delay, len(arrival_time_list), np.std(np.array(delay_time_list)), (np.array(delay_time_list)).min() )

if __name__ == '__main__':
    total_delay = 0
    total_times = 0
    delay_list = []
    all_list = []
    n = 1 # times of simulation
    time = 1000 # time period of the simulation
    rate = 0.495 # arrival rate
    mean = 1 # service time mean
    total_std = 0
    av_mini = 0
    for i in range(0, n):
        delay, times, std, mini = simulation( time, rate, mean, i)
        delay_list.append(delay)
        total_delay += delay
        total_std += std
        total_times += times
        delay_list.append(delay)
        av_mini += mini
    average_delay = total_delay/n
    total_std =float(total_std)/n
    print "Average of delays: " + str(average_delay)
    print "Average of Stardard deviation: "+ str(total_std)
    print "Average of Mini delay: "+ str(float(av_mini/n))
  #  np.save('delay1', delay_list)
    delay_list = np.load('delay_list.npy')
  #  print stats.kstest(np.array(delay_list), 'norm')
    
 #   a, b , c = ss.gamma.fit(delay_list)
 #   d, e = ss.exponweib.fit(delay_list)
    arrival_list = np.load('arrival_list.npy')
    t = []
    n = 1
    for x in range(0, len(arrival_list)):
        if n < 11:
            if arrival_list[x]< 100*n:
                t.append(delay_list[x])
            else:
                print (np.array(t)).min()
                t = []
                t.append(delay_list[x])
                n += 1


    

    
    

 #   min = delay_list.min()
 #   max = delay_list.max()
 #   mean = float((np.array(delay_list)).sum())/len(delay_list)
  #  print mean
 #   delay_list.sort()
 #   median = delay_list[2500]
 #   variance = (np.std(delay_list))**2
 #   cv = np.std(delay_list)/mean
 #   lexus = float(variance)/mean
 #   sum = 0
 #   sumlog = 0
 #   for x in range (0, 10000):
  #      sum += (delay_list[x]-mean)**3
   #     sumlog += log(delay_list[x])
 #   skewness = sum/(10000*((variance)**(1.5)))
   # t = log(mean)-float(sumlog)/10000
  #  t = 1/t
  #  b = mean/3.859
#    print min, max,mean,  median, variance, cv, lexus, skewness
 #   print t, b
 ###   output = pd.DataFrame({'delay':delay_list})
   # output.to_csv('out1.txt', index = False)
#    n = 10000
#    nn = 1 + 3.322*log10(n)
#    print int( nn)
 #   plt.hist(delay_list , bins= nn )
#    mm, nn = np.histogram(delay_list, bins = nn)
#    print mm
#    print nn
#    plt.title("Average delay distribution")
 #   plt.legend([delay], ["Average delay"], loc = 2)
 #   ax.set_xlim(-0.5, 100.5)
 #   plt.show()    
    
