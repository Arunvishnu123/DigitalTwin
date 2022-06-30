const { response } = require('express');
const express = require('express');
const getOntology = express.Router();
var fs = require('fs')
var path = require('path') 

getOntology.route('/:ifcClass/:ifcGuid').get((req,res,next) =>{
         let  ifcClass = req.params.ifcClass
         let ifcGuid  = req.params.ifcGuid
         filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/New folder (31)" + ".ttl");
         res.sendFile(filePath)
       
})



module.exports = getOntology

