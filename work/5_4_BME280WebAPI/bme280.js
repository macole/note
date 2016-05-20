//Call mraa
var mraa = require('mraa');
var version = mraa.getVersion();

if(version>='v0.6.1'){
    console.log('mraa version('+version+')ok');
}
else{
    console.log('mraa version('+version+')is old -this code may not work');
}

//Constructor
exports.BME280=function(port,address){
    this.digT=[];
    this.digP=[];
    this.digH=[];
    this.t_fine=0.0;
    this.m=new mraa.I2c(port);
    this.m.address(address);
    this.init();
};

exports.BME280.prototype={
    //Device initilization
    init:function(){
        this.setup();
        this.getCalibParam();
    },
    setup:function(){
        var osrs_t=1;
        var osrs_p=1;
        var osrs_h=1;
        var mode=3;
        var t_sb=5;
        var filter=0;
        var spi3w_en=0;
        
        var ctrl_meas_reg=(osrs_t<<5)|(osrs_p<<2)|mode;
        var config_reg=(t_sb<<5)|(filter<<2)|spi3w_en;
        var ctrl_hum_reg=osrs_h;
        
        this.m.writeReg(0xF2,ctrl_hum_reg);
        this.m.writeReg(0xF4,ctrl_meas_reg);
        this.m.writeReg(0xF5,config_reg);
    },
    getCalibParam:function(){
        var calib=[];
        for(var i = 0x88;i < 0x88+24;i++){
            calib.push(this.m.readReg(i));
        }
        calib.push(this.m.readReg(0xA1));
        for(var i = 0xE1;i < 0xE1+7;i++){
            calib.push(this.m.readReg(i));
        }
        this.digT.push((calib[1] << 8)|calib[0]);
        this.digT.push((calib[3] << 8)|calib[2]);
        this.digT.push((calib[5] << 8)|calib[4]);
        this.digP.push((calib[7] << 8)|calib[6]);
        this.digP.push((calib[9] << 8)|calib[8]);
        this.digP.push((calib[11] << 8)|calib[10]);
        this.digP.push((calib[13] << 8)|calib[12]);
        this.digP.push((calib[15] << 8)|calib[14]);
        this.digP.push((calib[17] << 8)|calib[16]);
        this.digP.push((calib[19] << 8)|calib[18]);
        this.digP.push((calib[21] << 8)|calib[20]);
        this.digP.push((calib[23] << 8)|calib[22]);
        this.digH.push((calib[24]));
        this.digH.push((calib[26] << 8)|calib[25]);
        this.digH.push((calib[27]));
        this.digH.push((calib[28] << 4)|(0x0F&calib[29]));
        this.digH.push((calib[30] << 4)|((calib[29] >> 4)& 0x0F));
        this.digH.push((calib[31]));
        for(var i=1;i<2;i++){
            if(this.digT[i] & 0x8000)
                this.digT[i]=(-this.digT[i] ^ 0xFFFF)+1;
        }
        for(var i=1;i<8;i++){
            if(this.digP[i] & 0x8000)
                this.digP[i]=(-this.digP[i] ^ 0xFFFF)+1;
        }
        for(var i=0;i<6;i++){
            if(this.digH[i] & 0x8000)
                this.digH[i]=(-this.digH[i] ^ 0xFFFF)+1;
        }
        },
        //Read Data from device
        readData:function(){
            var data=[];
            for(var i = 0xF7;i<0xF7+8;i++){
                data.push(this.m.readReg(i));
            }
            //Caluculate Actual Value
            var pres_raw=(data[0] << 12)|(data[1] << 4)|(data[2] >> 4);
            var temp_raw=(data[3] << 12)|(data[4] << 4)|(data[5] >> 4);
            var hum_raw=(data[6] << 8)|data[7];
            var pres=this.compensateP(pres_raw);
            var temp=this.compensateT(temp_raw);
            var hum=this.compensateP(hum_raw);
            
            return{temperature:temp,pressure:pres,humidity:hum};
        },
    compensateT:function(adcT){
        var temperature=0.0;
        var v1=(adcT /16384.0 - this.digT[0] / 1024.0)*this.digT[1];
        var v2=(adcT /131072.0 - this.digT[0] / 8192.0)*(adcT /131072.0 - this.digT[0] / 8192.0) * this.digT[2];
        this.t_fine=v1+v2;
        temperature=this.t_fine /5120.0;
        return temperature;
    },
    compensateH:function(adcH){
        var humidity=this.t_fine -76800.0;
        if(humidity !=0)
            humidity=(adcH-(this.digH[3]*64.0 + this.digH[4]/16384.0*humidity))*(this.digH[1]/ 65536.0 *(1.0+this.digH[5]/67108864.0*humidity*(1.0+this.digH[2] /67108864.0 *humidity)));
        else
            return 0;
        humidity=humidity*(1.0-this.digH[0]*humidity /524288.0);
        if(humidity>100.0)
            humidity=100.0;
        if(humidity<0.0)
            humidity=0.0;
        return humidity;
    },
    compensateP:function(adcP){
        var pressure=0.0;  
        var v1=(this.t_fine /2.0)-64000.0;
        var v2=(((v1/4.0)*(v1/4.0))/2048)*this.digP[5];
        v2=v2+((v1*this.digP[4])*2.0);
        v2=(v2/4.0)+(this.digP[3]*65536.0);
        v1=(((this.digP[2]*(((v1/4.0)*(v1/4.0))/8192))/8)+((this.digP[1]*v1)/2.0))/262144;
        v1=((32768+v1)*this.digP[0])/32768;
        if(v1==0)
            return 0;
        pressure=((1048576 -adcP)-(v2/4096))*3125;
        if(pressure<0x80000000)
            pressure=(pressure*2.0)/v1;
        else
            pressure=(pressure/v1)*2;
        v1=(this.digP[8]*(((pressure/8.0)*(pressure/8.0))/8192.0))/4096;
        v2=((pressure/4.0)*this.digP[7])/8192.0;
        pressure=pressure+(v1+v2+this.digP[6]/16.0);
        return pressure/100;
        },
};

        
        