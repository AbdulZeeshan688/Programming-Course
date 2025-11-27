import pandas as pd
import matplotlib.pyplot as plt


data = {
    'temperature': [23, 23, 21, 20, 19, 15, 12, 23, 25, 30],
    'movement': [1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)
print(df)



plt.figure(figsize=(10, 8)) # Set the overall figure size


plt.subplot(2, 1, 1) 
plt.plot(df['temperature'], label="Temperature", color='blue')
plt.title('Temperature Over Time') 
plt.ylabel('Temperature')        
plt.legend()                      


plt.subplot(2, 1, 2)
plt.plot(df['movement'], label="Movement", color='green')
plt.title('Movement Over Time')  
plt.xlabel('Time')                
plt.ylabel('Movement')            
plt.legend()                      


plt.tight_layout()


plt.show()