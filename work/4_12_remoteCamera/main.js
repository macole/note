/*jslint node:true, vars:true, bitwise:true, unparam:true */
/*jshint unused:true */
// Leave the above lines for propper jshinting
//Type Node.js Here :)

var exec=require('child_process').exec,capture;
capture =exec('fswebcam /home/root/test.jpg',function(error,stdout,stderr){
    console.log('stdout; '+stdout);
    console.log('stderr: '+stderr);
    if(error !==null){
        console.log('exec error; '+error);
    }
});