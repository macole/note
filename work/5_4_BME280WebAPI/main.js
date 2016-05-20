/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)

//http://192.168.179.13:3000/api/yourroom/latest

var bme280=require('./bme280.js');

//
var x=new bme280.BME280(6,0x76);

//Database
var sqlite3=require('sqlite3').verbose();

//date-util
var db=new sqlite3.Database('/home/root/database/roomenv.db');
require('date-utils');

//Insert data to database
setInterval(function(){
    var dt=new Date();
    var formatted=dt.toFormat("YYY-MM--DD HH24:MI:SS");
    var obj=x.readData();
    
    var sql='INSERT INTO ROOM VALUES(?,?,?,?)';
    db.run(sql,formatted,obj.temperature,obj.humidity,obj.pressure);
    console.log('Insert into Database!');
},5000);

//Express
var express=require('express');
var app=express();

app.get('/api/yourroom/latest',function(req,res){
    var obj=x.readData();
    var json='{"temperature":'+obj.temperature+','+'"humidity":'+obj.humidity+','+'"pressure":'+obj.pressure+'}';
    res.send(json);
});

app.get('/api/yourroom/latest/temperature',function(req,res){
    var obj=x.readData();
    var json='{"temperature":'+obj.temperature+'}';
    res.send(json);
});

app.get('/api/yourroom/latest/humidity',function(req,res){
    var obj=x.readData();
    var json='{"humidity":'+obj.humidity+'}';
    res.send(json);
});

app.get('/api/yourroom/latest/pressure',function(req,res){
    var obj=x.readData();
    var json='{"pressure":'+obj.pressure+'}';
    res.send(json);
});

var server=app.listen(3000,function(){
    var host=server.address().address;
    var port=server.address().port;
    
    console.log('Example app listening at http://%s:%s',host,port);
});


