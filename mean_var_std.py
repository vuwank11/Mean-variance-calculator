import numpy as np

def calculate(list):
  original_array= np.array(list)
  reshaped_array= original_array.reshape(3,3)
  calculations ={
    'mean':[],
    'variance':[],
    'standard deviation':[],
    'max':[],
    'min':[],
    'sum':[]
  }
#Mean calculation
  #axis=0
  mean1 = reshaped_array.sum(axis=0)/3
  #axis=1
  mean2 = reshaped_array.sum(axis=1)/3
  #flattened
  mean3=  original_array.sum(axis=0)/9
  
  calculations['mean']= [mean1,mean2,mean3]
  
#variance and standard deviation calculations
  var1=[]
  std1=[]
  for column in range(0,3):
    sum=0
    for row in range(0,3):
      diff= reshaped_array[row][column]-mean1[column]
      sum= sum + diff**2
    var1.append(sum/3)
    std1.append((sum/3)**(1/2))

  var2=[]
  std2=[]
  for row in range(0,3):
    sum=0
    for column in range(0,3):
      diff= reshaped_array[row][column]-mean2[row]
      sum= sum+ diff**2
    var2.append(sum/3)
    std2.append((sum/3)**(1/2))
    
  sum=0
  for item in original_array:
    diff= item - mean3
    sum= sum + diff**2
  var3= sum/9
  std3= var3**(1/2)
  
  calculations['variance']= [var1, var2, var3]
  calculations['standard deviation']=[std1, std2, std3]

  #max calculations
  max1= reshaped_array.max(axis=0)
  max2= reshaped_array.max(axis=1)
  max3= original_array.max(axis=0)
  calculations['max']=[max1,max2,max3]

  #min calculations
  min1= reshaped_array.min(axis=0)
  min2= reshaped_array.min(axis=1)
  min3= original_array.min(axis=0)
  calculations['min']=[min1,min2,min3]

  #sum calculations
  sum1= reshaped_array.sum(axis=0)
  sum2= reshaped_array.sum(axis=1)
  sum3= original_array.sum(axis=0)

  calculations['sum']=[sum1, sum2, sum3]

  
  return calculations