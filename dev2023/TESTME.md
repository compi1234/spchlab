#  TEST including figures



##### Purpose

How to consistently embed figures in Markdown ?????????

##### Test1 - markdown and figure in same or sub directories

simple markdown
![](PetersonBarney_1952_fig8.jpg)

##### Test2 - HTML and figure in same or sub directories
simple   HTML

<img src="PetersonBarney_1952_fig8.jpg">


HTML without backslash before end />   

<img src="./PetersonBarney_1952_fig8.jpg">


HTML with backslash
<img src="./PetersonBarney_1952_fig8.jpg" alt="PB fig8"/>

##### Test3 - relative paths including ..

referencing to relative directory higher in the tree   
<img src="../figures/Fletcher_Munson.jpg">