import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([5, 10, 15, 20, 7])
# plt.plot(x,y,c = 'r',ms= '20', ls = '-.')
# plt.show()


"""
1] labels:
    - gives additional information about axis in the graph
    
    - syntax = 
                plt.xlable("String")
                plt.ylable("String")
                fontdict= font
                
                
                
                
2] Position the Title

    -You can use the loc parameter in title() to position the title.

   - Legal values are: 'left', 'right', and 'center'. 
   
   - Default value is 'center'.
   
   - syntax = 
                loc='left/right/center'
                
                
3] grid()
    - With Pyplot, you can use the grid() function to add grid lines to the plot.
    - syntax=
                plt.grid()
                
    - for particular axis:
    - default value is both
                plt.grid(axis='x/y/both')
    
4] width
        - syntax:
            width= value                

"""

b = [1, 5, 3, 9, 4, 8, 2]
b.reverse()
a = [1, 5, 3, 9, 4, 8, 2]
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
plt.title("Detailed analysis of production and average income", c='r', fontdict=font1, loc='left')
plt.xlabel("production")
plt.ylabel("average income")
plt.plot(a, b, linestyle=':',linewidth='5')
plt.grid(axis='y', linestyle='--', linewidth='1')
plt.show()
