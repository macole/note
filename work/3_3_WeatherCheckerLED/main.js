/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)

var mraa=require('mraa');
console.log('MRAA Version: ' + mraa.getVersion());

var fine=0;
var cloud=0;
var rain=0;

var fineLed=new mraa.Gpio(11);
fineLed.dir(mraa.DIR_OUT);
var cloudLed=new mraa.Gpio(10);
cloudLed.dir(mraa.DIR_OUT);
var rainLed=new mraa.Gpio(9);
rainLed.dir(mraa.DIR_OUT);

ledActivity();

function ledActivity()
{
    fineLed.write(fine?0:1);
    fine=!fine;
    cloudLed.write(cloud?0:1);
    cloud=!cloud;
    rainLed.write(rain?0:1);
    rain=!rain;
    
    setTimeout(ledActivity,1000);
}
