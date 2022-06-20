const { response } = require('express');
const express = require('express');
const getKG = express.Router();
var fs = require('fs')
var path = require('path') 

getKG.route('/:ifcClass/:ifcGuid').get((req,res,next) =>{
         let  ifcClass = req.params.ifcClass
         let ifcGuid  = req.params.ifcGuid
         filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/New folder (31)", ifcClass , ifcGuid + ".ttl");
         res.sendFile(filePath)
       
})

getKG.route('/:ifcClass').get((req,res,next) =>{
    let  ifcClass = req.params.ifcClass
    filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/New folder (31)", ifcClass +  ".ttl");
    res.sendFile(filePath)
  
})

module.exports = getKG

