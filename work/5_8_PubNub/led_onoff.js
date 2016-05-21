var publishKey = 'pub-c-93d56a31-bf8d-4f8d-8f85-babc40968f2f';
var subscribeKey = 'sub-c-8be5544a-1840-11e6-b700-0619f8945a4f';
var channel = "led-onoff";	//Channel Name setup
var raspi = require('raspi-io');
var five = require("johnny-five");
var board = new five.Board({
	io:new raspi()
});
board.on("ready",funcion(){
	var led = new five.Led('P1-7');
	//PubNub init}var pubnub =require("pubnub")({
	var pubnub = require("pubnub")({
		ssl:true,
		publish_key:publishKey,
		subscribe_key:subscribeKey
	});
	//channel
	pubnub.subscribe({
		channel : channel,
		callback:function(message){
			console.log('>',message);
			if(message.action==='on'){
				led.on()
			}else{
				led.off();
			}
		}
	});
});



