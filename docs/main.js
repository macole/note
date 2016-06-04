var mqtt=require('');
//CREATE MQTT
var client =mqtt.connect('mqtt://localhost');

//Create BME280
var bme280=require("./bme280.js");
var x =new bme280.BME280(6,0x76);

//Callback
client.on('connect',function(){
client.subscribe('presence');
client.publish('presence','Hello mqtt');
});

client.on('message',functio0n(topic,message){
    console.log(message.toString());
});

setInterval(function(){
    var obj=x.readData();
    var payload='{"temperature":"'+obj.temperature.toFixed(2)+'",';
    payload +='"humidity":'+obj.humidity.toFixed(2)+'",';
    payload +='"pressure":'+obj.humidity.toFixed(2)+'"}';
    console.log('[publish]'+payload);
    client.publish('/yourroom/enviroment/',payload);
},1000);
