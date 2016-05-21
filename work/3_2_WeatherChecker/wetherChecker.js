/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)

var http=require('http');
//console.log('mraa Version:'+mraa.getVersion());

var url='http://weather.livedoor.com/forecast/webservice/json/v1?city=240010';
var weather='';

http.get(url,function(res){
    var body='';
    res.setEncoding('utf8');
    res.on('data',function(data){
        body+=data;
    });
    res.on('end',function(data){
        var weather_data=JSON.parse(body);
        forecasts=weather_data['forecasts'];
        for(index in forecasts){
            forecast=forecasts[index];
            if(forecast['dateLabel']=='今日'){
                weather=forecast['telop'];
                console.log(weather);
                console.log(forcast);
            }
        }
    });
});
    