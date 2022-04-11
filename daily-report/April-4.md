* check in  -9:30 am
* checkout - 6:00 pm

## Work in progress - 
* program developed for the integrating the bim model is complete. currently developed code using the HTML(for testing purpose). But here I am facing a problem - Using the xeokit , we can use multiple formats like .ifc, .xkt etc. But here our model is very big file so not working properly and take too much time to load. But I tested the logic with some smaller file but that  was working perfectly and the performance was also ok. 
* So, Next option is to convert the IFC to XKT and then test it . Found one converter tool from the xeokit website and tested it. But that also not working with our model. But the smaller files are working fine and it is converted from ifc to .xkt file 
Developed a program for viewing the .xkt file in the browser.
Found other two similar modules like xeokit - BIMdata.io, IFC.js 
* BIMdata.io - here the problem is , the .ifc file first need to upload in their cloud   and then we need to call the ifc file in our program  . They will give some parameter like cloudid,project id , ifcid etc for the api call - https://developers.bimdata.io/viewer/getting_started.html#installation
IFC.js - didn't checked by writing the code but in there website one simulator was given there I checked by uploading our model but didn't worked , but smaller file are working fine - website link - https://ifcjs.github.io/info/
## Pending job for tomorrow
* Try to develop a program to convert the ifc to xkt by following the procedure given in the xeokit website and then test the logic
* Try to test the BIMdata.io - bim viewer module - already logic written in vue.js  - but need to check how to upload the ifc file to their cloud server  - procedure given here  - https://developers.bimdata.io/api/introduction/quick_start.html#create-an-application - (need permission to upload the model in their cloud )