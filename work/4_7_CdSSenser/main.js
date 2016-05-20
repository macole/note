/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)

var mraa=require('mraa');
console.log('MRAA Version:'+mraa.getVersion());

//Analog Input:A0
var analogPin0=new mraa.Aio(0);

//On Board LED:GPIO13
var ledPin=new mraa.Gpio(13);
ledPin.dir(mraa.DIR_OUT);

var threshold=500;

setInterval(function(){
    var analogValue=analogPin0.read();
    console.log(analogValue);
    if(analogValue>threshold)
        ledPin.write(1);
    else
        ledPin.write(0);
},1000);

    