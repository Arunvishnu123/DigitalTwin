const { response } = require('express');
const express = require('express');
const getKG = express.Router();
var fs = require('fs')
var path = require('path') 

const tes = express.Router();

getKG.route('/:ifcClass/:ifcGuid').get((req,res,next) =>{
         let  ifcClass = req.params.ifcClass
         let ifcGuid  = req.params.ifcGuid
         filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/finaltest", ifcClass , ifcGuid + ".ttl");
         res.sendFile(filePath)
       
})

getKG.route('/:ifcClass/:ifcGuid/:sensorType').get((req,res,next) =>{
    let  ifcClass = req.params.ifcClass
    let ifcGuid  = req.params.ifcGuid
    let sensorType  = req.params.sensorType
    filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/ThingDirectory", ifcClass , ifcGuid, sensorType + ".ttl");
    res.sendFile(filePath)
  
})


getKG.route('/:ifcClass/:ifcGuid/employee/:firstName').get((req,res,next) =>{
    let  ifcClass = req.params.ifcClass
    let ifcGuid  = req.params.ifcGuid
    let firstName  = req.params.firstName
    fileEmployee = path.join("C:/Users/ARUN/OneDrive/Desktop/employeeDirectory", ifcGuid, firstName + ".ttl");
    res.sendFile(fileEmployee)
  
})
getKG.route('/:ifcClass').get((req,res,next) =>{
    let  ifcClass = req.params.ifcClass
    filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/finaltest", ifcClass +  ".ttl");
    res.sendFile(filePath)
  
})

getKG.route('/update').get((req,res , next) =>{
    let          
})

getKG.route('/ifcClass').get((req,res,next) =>{
    filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/finaltest/ifcClass.ttl");
    res.sendFile(filePath)  
})

getKG.route('/fayol/mines/ontology/test').post((req, res, next) => {
    console.log(req.body)
    ontologyPath = path.join("C:/Users/ARUN/OneDrive/Desktop/ontologyfolder","tet.ttl");
    res.sendFile(ontologyPath) 
     

});

module.exports = getKG

