/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)
//Load bme280 module
var bme280 =require('./bme280.js');

//I2C Port :6 Device's Address:0x76
var x=new bme280.BME280(6,0x76);


var sqlite3=require('sqlite3').verbose();
var db = new sqlite3.Database('/home/root/database/roomenv.db');

require('date-utils');

setInterval(function(){
    var dt =new Date();
    var formatted=dt.toFormat("YYYY-MM-DD HH24:MI:SS");
    var obj=x.readData();
    
    var sql='INSERT INTO ROOM VALUES(?,?,?,?)';
    db.run(sql,formatted,obj.temperature,obj.humidity,obj.pressure);
    
    console.log('Insert into Database!');
},5000);
    
var http=require('http');
http.createServer(function(req,res){
    console.log('Receive Request!!');
    var obj=x.readData();
    res.writeHead(200,{'Content-Type':'text/html'});

    var html='<table border="1">'+
    '<tr>'+
    '<th>time</th>'+
    '<th>temp[degC]</th>'+
    '<th>hum[%]</th>'+
    '<th>pres[hPa]</th>'+
    '</tr>';
    
    //Execute SQL Query & return HTTP Response
    var sql='SELECT *FROM ROOM;';
    db.all(sql,function(err,rows){
        if(!err){
            for(var i in rows){
                html+='<tr>'+
                '<td>'+rows[i].time+'</td>'+
                '<td>'+rows[i].temperature.toFixed(2)+'</td>'+
                '<td>'+rows[i].humidity.toFixed(2)+'</td>'+
                '<td>'+rows[i].pressure.toFixed(2)+'</td>'+
                '</tr>'
            }
        html +='</table>';
        res.end(html);
        }
    }); 
}).listen(3000,'192.168.179.13');