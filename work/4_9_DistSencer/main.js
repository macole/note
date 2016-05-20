/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)


//Load Modules
var mraa=require('mraa');
var sleep=require('sleep');
var us =require('microseconds');

console.log('MRAA Vesrion:'+mraa.getVersion());

//GPIO trigger pin:second trigger signal
var trigPin=new mraa.Gpio(8);
trigPin.dir(mraa.DIR_OUT);

//echo pin:recieve echo from module
var echoPin=new mraa.Gpio(7);
echoPin.dir(mraa.DIR_IN);

var LOW=0;
var HIGH=1;

//convert from microsec to inch
function microsecondsToInches(microsec){
    return microsec / 73.746 /2.0;
}

//convert from microsecto centi
function microsecondsToCentimeters(microsec){
    return microsec / 29.034 /2.0;
}

setInterval(function(){
    var pulseOn,pulseOff;
    var duration;
    
    //Send Trigger Signal to Module
    trigPin.write(LOW);
    sleep.usleep(2);
    trigPin.write(HIGH);
    sleep.usleep(5);
    trigPin.write(LOW);
    
    //Measure duration of echo pulse
    while(echoPin.read()==0){
        pulseOn=us.now();
    }
    while(echoPin.read()==1){
        pulseOff=us.now();
    }
    //duration[microsec]
    duration=pulseOff-pluseOn;
    
    //Caluculate Distance from dulation
    var inch=microsecondsToInches(duration);
    var centi=microsecondsToCentimeters(duration);
    
    //Show the distance on the console
    console.log("in;"+inchi+",centi:"+centi);
},1000);