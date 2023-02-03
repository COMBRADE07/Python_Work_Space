import matplotlib.pyplot as plt
import numpy as np

x_point = np.array([0, 8])
y_point = np.array([0, 250])

# plt.plot(x_point, y_point)
# plt.show()


# 2] multiple points
x_point1 = [1, 2, 6, 10]
y_point1 = [3, 8, 1, 5]
# plt.plot(x_point1,y_point1)
# plt.show()


"""

3] Markers

        - You can use the keyword argument marker to emphasize each point with a specified marker:
        - syntax
                plt.plot(marker='values')
            values = [h,p,+,*,o] etc
"""
y_point2 = np.array([3, 5, 1, 9, 7, 3])
# plt.plot(y_point2, marker="h")  # also we can set marker as [o,+,*,P,d,h,H,D,p,1,2,3] etc. which has some mean
# plt.show()


"""3.1] lines
        syntax = i] linestyle / ls

        '-' 	Solid line
        ':' 	Dotted line
        '--' 	Dashed line
        '-.' 	Dashed/dotted line


    3.2] colour / syntax = i] 'mec'/ 'markeredgecolor ' === for marker edge
                          ii] 'markerfacecolor' / 'mfc'   ===  change colour of the faces
                          iii] color/c
        'r' 	Red
        'g' 	Green
        'b' 	Blue
        'c' 	Cyan
        'm' 	Magenta
        'y' 	Yellow
        'k' 	Black
        'w' 	White

    3.3] marker size / syntax = 'ms'

"""

# plt.plot([1, 3, 4, 6, 8, 3], [8, 1, 4, 7, 2, 7], 'p--y', ms='10', mec='b', markerfacecolor= 'm')  # yellow == line        edge = black        marker size = 20
# plt.show()


# plt.plot([1, 3, 4, 6, 8, 3], [8, 1, 4, 7, 2, 7], linestyle = ':', color = 'y')           # this will print dotted line
# plt.show()



"""
4] multiple line on single graph
    - syntax:   plt.plot(x1)
                plt.plot(x2)
                plt.plot(x3)

    - simply calling plot function repeatedly



5] marker size / ms
    - change marker size
    - maximum size as per documentation is 20
    - syntax =
                ms= '20'

"""
x1 = np.array([3,1,3,1,7,8])
x2 = np.array([8,1,7,2,8])
x3 = np.array([2,8,5,9,3])
plt.plot(x1)
plt.plot(x2)
plt.plot(x3,x2)
# plt.show()


"""
6] subplot():

    - it takes three argument as input
        -i] row
        -ii] column
        -iii] index

    -syntaxt:
            plt.subplot(row, column, index)

    - if you want 3 column in one row then you must have set column value as 4. similarly
"""
# plot 1:
m = np.array([0, 1, 2, 3])
n = np.array([3, 8, 1, 10])
plt.subplot(2,4,1)
plt.plot(m,n)


# plot 2:
m1 = np.array([3, 8, 1, 10])
n1 = np.array([0, 1, 2, 3])
plt.subplot(2,4,2)
plt.plot(m1,n1)


# plot 3:
m4 = np.array([3, 8, 1, 10])
plt.subplot(2,4,3)
plt.plot(m4)

# plot 4:
m2 = np.array([5, 2, 6, 2])
n2 = np.array([3, 8, 1, 10])
plt.subplot(2,4,4)
plt.suptitle("Scatter")
# plt.plot(m2,n2)
plt.scatter(m2,n2)
plt.colorbar()
plt.show()






"""
7] Color Each Dot

    - You can even set a specific color for each dot by using an array of colors as value for the c argument:
    - c=colors_value
    - colors_value =[value1, value2, value3,... ]

"""


xx = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
yy = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.title("Changing the color of the dots")
plt.scatter(xx, yy, c=colors)
plt.colorbar()
plt.show()



xy = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
yx = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(xy, yx, s=sizes)
plt.show()



"""
8] bar()
    - With Pyplot, you can use the bar() function to draw bar graphs:
    - it takes two parameter as input such as x and y axis value

    - The bar() and barh() takes the keyword argument color to set the color of the bars

    - barh():
            it display bars in horizontal view



    8.1] bar width
            - The bar() takes the keyword argument width to set the width of the bars:
            - syntax:
                    plt.bar(width= value)

            - Note: For horizontal bars, use height instead of width.


    8.2] color
        plt.bar(x,y,color='orange')

"""
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x,y,color='orange',width=0.1)
plt.show()
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()



""""
9] Histogram:
            - A histogram is a graph showing frequency distributions.

            - It is a graph showing the number of observations within each given interval.

   9.1] Create Histogram

        - In Matplotlib, we use the hist() function to create histograms.
        - the array is sent into the function as an argument.
        - simple program for histogram as follows:

          ==>
            import matplotlib.pyplot as plt
            import numpy as np
            x = np.random.normal(170, 10, 250)
            plt.hist(x)
            plt.show()



10] pie():

    - With Pyplot, you can use the pie() function to draw pie charts
    - syntax
            plt.pie(parameter)

            #:parameter is array of numbers which sum is always = 100

     ===========================================================

11]     parameter of pie() as follows

        11.1]   start angle()
                - by deafault it start from x-axis 
                - default angle is 0
                - syntax:
                            plt.pie(startangle = 90/180) # also we can specify value
        
        11.2]   label
                - label gives extra information about pie diagram
                - syntax:
                            plt.pie(lable= values)
                            
                        #Note: values of the label is size of parameter are passed to it.
                        
        11.3]   Explode
                
                - if you want to take some part of your pie chart out then you can do with explode keyword
                - syntax:
                        plt.pie(explode= value)
                        
                        # here we have to set value which we have to explodeed from pie chart 
                        #value variable contain list as paramter with how much we have to take out in it
                        
                        e.g.    hello= [0.2, 0.2, 0.2, 0.4]         # consider here is 4 value in pie charth
                                plt.pie(exploade = hello)
                        
        11.4]   shadow
                - shadow will show some shadow of pie charth
                - syntax:
                            plt.pie(shadow= True)
                            
                                # here we have to set shadow as true if we want the shadow
                                
        11.5    color
                - this parameter will set the color of pie charth
                - this one take list of color as value
                - syntax:
                        value = [c1,c2,c3,....]
                        plt.pie(color=value)
                        

"""
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
colorx = ['green','red','b','yellow']
explode_list = [0.2,0.2,0.2,0.5]
plt.pie(y, labels = mylabels, colors=colorx, startangle=180, explode= explode_list, shadow= True)
plt.show()
"""
        function=>
        
        legend():
                    - this function gives detailed information about pie value/slices
                    - syntax:
                            plt.legend()
                            plt.legend(title= 'mytitle')    #this one set some title to our information
                                                            list which is returned by legend() function.

"""


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title="hello fruits guy")
plt.show()