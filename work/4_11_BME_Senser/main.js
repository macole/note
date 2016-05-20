/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)

//Load bme280 module
var bme280=require("./bme280.js")
//I2C Port :6
//Device's Address;0x76
var x= new bme280.BME280(6,0x76);

//Excecute Periodic Process
setInterval(function(){
    //Read Data from Device
    var obj=x.readData();
    console.log('-------------------------');
    console.log('temp: '+obj.temperature.toFixed(2)+' degC');
    console.log('hum : '+obj.humidity.toFixed(2)+' per');
    console.log('pres: '+obj.pressure.toFixed(2)+' hPa');
},1000);

                