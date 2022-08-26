const { response } = require('express');
const express = require('express');
const getOntology = express.Router();
var fs = require('fs')
var path = require('path') 

getOntology.route('/onto').get((req,res,next) =>{
         filePath = path.join("C:/Users/ARUN/OneDrive/Desktop/ontologyfolder/"+"tet" + ".ttl");
         res.sendFile(filePath)
       
})

module.exports = getOntology

