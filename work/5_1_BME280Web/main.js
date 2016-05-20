/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)
//Load bme280 module
var bme280 =require('./bme280.js');

//I2C Port :6 Device's Address:0x76
var x=new bme280.BME280(6,0x76);

var http=require('http');
http.createServer(function(req,res){
    console.log('Receive Request!!');
    var obj=x.readData();
    res.writeHead(200,{'Content-Type':'text/html'});
    var html='<table border="1">'+
    '<tr>'+
    '<td>temp[degC]</td>'+
    '<td>'+obj.temperature.toFixed(2)+'</td>'+
    '</tr>'+
    '<tr>'+
    '<td>hum[%]</td>'+
    '<td>'+obj.humidity.toFixed(2)+'</td>'+
    '</tr>'+
    '<tr>'+
    '<td>pres[hPa]</td>'+
    '<td>'+obj.pressure.toFixed(2)+'</td>'+
    '</tr>'+
    '</table>';
    res.end(html);
}).listen(3000,'192.168.179.13');
