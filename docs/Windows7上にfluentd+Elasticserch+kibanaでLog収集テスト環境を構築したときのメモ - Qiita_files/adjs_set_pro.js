var BigGlobalLib = BigGlobalLib || {};
(function(window, undefined){
  try {
    var AD_REQUEST_JS_URL = (document.location.protocol == 'https:' ? 'https://' : 'http://') + 'dg-ads-proxy.bigmining.com/js/adrequest.js';
    var AD_REQUEST_URL = (document.location.protocol == 'https:' ? 'https://' : 'http://') + 'dg-ads-adserver.bigmining.com/www/delivery/spc.php';
    var DMP_REQUEST_URL = (document.location.protocol == 'https:' ? 'https://' : 'http://') + 'dg-ads-proxy.bigmining.com/log/adevent';
    var ERROR_REPORT_URL = (document.location.protocol == 'https:' ? 'https://' : 'http://') + 'dg-ads-proxy.bigmining.com/log/error';

    var isEmpty = function(obj) {
      return (typeof obj === 'undefined' || obj === null);
    };

    var addEvent = function(event, func, target) {
      if (typeof target === 'undefined') {
        target = window;
      }
      if (target.addEventListener) {
        target.addEventListener(event, func, false);
      } else if (target.attachEvent) {
        target.attachEvent('on' + event, func);
      } else {
        throw new Error('can not add event');
      }
    };

    var removeEvent = function(event, func, target) {
      if (typeof target === 'undefined') {
        target = window;
      }
      if (target.removeEventListener) {
        target.removeEventListener(event, func, false);
      } else if (target.detachEvent) {
        target.detachEvent('on' + event, func);
      } else {
        throw new Error('can not remove event');
      }
    };

    var addEventReady = function(func) {
      if (document.readyState === 'complete' || document.readyState === 'interactive') {
        func();
      } else if (document.addEventListener) {
        document.addEventListener('DOMContentLoaded', func, false);
      } else if (document.attachEvent) {
        document.attachEvent('onreadystatechange', function() {
          if (document.readyState === 'complete') {
            document.detachEvent('onreadystatechange', arguments.callee);
            func();
          }
        });
      } else {
        throw new Error('can not add event');
      }
    };

    var encodeHTMLForm = function(data) {
      var params = [];
      for (var name in data) {
        var value = data[name];
        if (isEmpty(value)) {
          continue;
        }
        var param = encodeURIComponent(name).replace(/%20/g, '+') +
          '=' +
          encodeURIComponent(value).replace(/%20/g, '+');
        params.push(param);
      }
      return params.join('&');
    };

    var sendBeacon = function(endpoint, data) {
      var src = endpoint;
      if (data) src += '?' + encodeHTMLForm(data);
      var img = document.createElement('img');
      img.src = src;
      img.width = 0;
      img.height = 0;
      img.style.display = 'none';
      document.body.appendChild(img);
    };

    var error_report = function(error) {
      try {
        //console.log('ERROR:');
        //console.log(error.stack);
        //TODO send ERROR report
        sendBeacon(ERROR_REPORT_URL, {
          "msg": error.stack
        });
      } catch (e) {
        //console.log('ERROR REPORT FAILED:');
        //console.log(e);
        // no op.
      }
    };

    var tryCatchReport = function(method, arg) {
      try {
        method(arg);
      } catch (e) {
        error_report(e);
      }
    };

    var sendRequest = function(data, method, url, async, success, failure) {
      'use strict';
      var READYSTATE_UNINITIALIZED = 0;
      var READYSTATE_LOADING = 1;
      var READYSTATE_LOADED = 2;
      var READYSTATE_INTERACTIVE = 3;
      var READYSTATE_COMPLETE = 4;
      var HTTP_STATUS_OK = 200;
      var HTTP_STATUS_NOTFOUND = 404;
      var request = false;
      var isIE9 = (navigator.userAgent.indexOf('MSIE 9.') != -1 || navigator.userAgent.indexOf('MSIE 8.') != -1 || navigator.userAgent.indexOf('MSIE 10.') != -1);
      if (isIE9) {
        try {
          request = new window.XDomainRequest();
          void 0;
        } catch (e) {
          request = false;
        }
      } else if (window.XMLHttpRequest) {
        try {
          request = new XMLHttpRequest();
          request.withCredentials = true;
          void 0;
        } catch (e) {
          request = false;
        }
      } else if (window.ActiveXObject) {
        try {
          request = new ActiveXObject('Msxml2.XMLHTTP');
          void 0;
        } catch (e) {
          try {
            request = new ActiveXObject('Microsoft.XMLHTTP');
            void 0;
          } catch (e2) {
            request = false;
          }
        }
      }

      if (request === false) {
        void 0;
        return null;
      }

      if (isIE9) {
        request.ontimeout = function() {};
        request.onprogress = function() {};
        request.onerror = failure;
        request.onload = function() {
          success(request.responseText);
        };
      }

      if (method == 'GET' && data !== "") {
        url = url + '?' + encodeHTMLForm(data);
      }

      request.open(method, url, async);
      if (method == 'POST') {
        try {
          Obj.objReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        } catch (e) {}
      }

      request.onreadystatechange = function() {
        if (this.readyState == READYSTATE_COMPLETE) {
          if (this.status == HTTP_STATUS_OK) {
            success(this.responseText);
          } else {
            failure('ERROR: ' + this.statusText);
          }
        }
      };

      if (isIE9) {
        setTimeout(function() {
          request.send(encodeHTMLForm(data));
        }, 0);
      } else {
        request.send(encodeHTMLForm(data));
      }
    };

    var getImpParams = function(node, html, zoneId) {
      var params = {
        event: 'impression',
        zoneid: zoneId
      };
      if (html.indexOf('bannerid=') != -1 && html.indexOf('campaignid=') != -1) {
        params.bannerid = html.match(/bannerid=([0-9]+)/)[1];
        params.campaignid = html.match(/campaignid=([0-9]+)/)[1];
      }
      return params;
    };

    var getClickParams = function(node, html, zoneId) {
      var params = {
        event: 'click',
        zoneid: zoneId
      };
      if (html.indexOf('bannerid=') != -1 && html.indexOf('campaignid=') != -1) {
        params.bannerid = html.match(/bannerid=([0-9]+)/)[1];
        params.campaignid = html.match(/campaignid=([0-9]+)/)[1];
      }
      return params;
    };

    var setDmpRequest = function(node, adHtml, zoneId) {
      sendBeacon(DMP_REQUEST_URL, getImpParams(node, adHtml, zoneId));
      addEvent("click", function() {
        sendBeacon(DMP_REQUEST_URL, getClickParams(node, adHtml, zoneId));
      }, node);
    };

    // 各ゾーンタグに広告を挿入・表示
    var insertAd = function(zone_id, html) {
      var targets = document.getElementsByClassName('bigmining_zone_' + zone_id);
      if (targets.length <= 0 || !html) return;
      var target = targets[0];
      target.innerHTML = html;
      setDmpRequest(target, html, zone_id);
    };

    var adrequestSuccess = function(response, zone_ids) {
      if (!window.JSON || typeof JSON.parse !== 'function' || !(JSON.parse('{"test": true}').test)) return;
      ////console.log('ad request succeed');

      // 取得したjsを実行し、htmlテキストを変数に入れる
      eval(response);
      // eval内でOA_outputが定義されたことを確認
      if (typeof(OA_output) === 'undefined') return;

      bannersHtml = OA_output;
      for (var zone_id in bannersHtml) {
        insertAd(zone_id, bannersHtml[zone_id]);
      }
    };

    var adrequest = function(segment) {
      var source = init();
      if(zone_ids.length == 0) return;

      var adrequest_url = AD_REQUEST_URL;
      adrequest_url += "?zones=" + escape(zone_ids.join('|'));
      adrequest_url += "&r=" + Math.floor(Math.random() * 99999999);
      adrequest_url += "&block=1";
      adrequest_url += "&source=" + source + segment;
      adrequest_url += (document.charset ? '&charset=' + document.charset : (document.characterSet ? '&charset=' + document.characterSet : ''));
      if (window.location) adrequest_url += "&loc=" + escape(window.location);
      if (document.referrer) adrequest_url += "&referer=" + escape(document.referrer);

      sendRequest("", 'GET', adrequest_url, true,
        function(response) {
          tryCatchReport(adrequestSuccess, response, zone_ids);
        },
        function() {
          error_report("send error");
        }
      );
    };

    BigGlobalLib.proxy_callback = function(segment) {
      addEventReady(function() {
        tryCatchReport(adrequest, segment);
      });
    };

    var script = document.createElement("script");
    script.src = AD_REQUEST_JS_URL + '?r=' + Math.floor(Math.random() * 99999999);
    document.body.appendChild(script);





    var zone_ids = [];
    var init = function() {
      if (navigator.userAgent.indexOf('iPhone') > 0 || navigator.userAgent.indexOf('Android') > 0) return;

      //枠構築
      zone_ids = [16,18,19];

      var ad_frame_right_banner_1 = document.getElementsByClassName("ad_frame_right_banner_1")[0];
      if(ad_frame_right_banner_1){
        var element = document.createElement('div');
        element.className = 'bigmining_zone_16';
        ad_frame_right_banner_1.appendChild(element);
      }

      var ad_frame_header_text = document.getElementsByClassName("ad_frame_header_text")[0];
      if(ad_frame_header_text){
        var element = document.createElement('div');
        element.className = 'bigmining_zone_18';
        ad_frame_header_text.appendChild(element);
      }

      var ad_frame_footer_text = document.getElementsByClassName("ad_frame_footer_text")[0];
      if(ad_frame_footer_text){
        var element = document.createElement('div');
        element.className = 'bigmining_zone_19';
        ad_frame_footer_text.appendChild(element);
      }

      //source属性
      var categories = document.getElementsByClassName("tagIcon_name");
      var params = "";
      if (typeof categories !== "undefined") {
        for (var i = 0; i < categories.length; i++) {
          params += "_cat(" + categories[i].innerHTML + ")";
        }
      }
      return params;
    };







    // banner risize trigger
    var ad = "";
    var endtime_a = 0;
    var intervalSetResize = setInterval(function() {
      var ad_elements = document.getElementsByClassName("bm_ad_text");
      if (typeof ad_elements !== "undefined") {
        if (ad_elements.length > 0) {
          adResize();
          clearInterval(intervalSetResize);
        }
      }
      ++endtime_a;
      if (endtime_a > 50) {
        clearInterval(intervalSetResize);
      }
    }, 100);


    // page render action
    function adResize(){
      function setStyle(elms, sObj) {
        try {
          for(var i = 0, j = elms.length; i < j; i++) {
            for(var c in sObj) {
              elms[i].style[c] = sObj[c];
            }
          }
        } catch (e) {
        }
      }
      function setBefore() {
        try {
          document.getElementById("bm_ad_text_sub").style.display="";
          document.getElementsByClassName("bm_ad_text")[0].style.height="64px";
          document.getElementsByClassName("bm_ad_text")[1].style.height="64px";
          document.getElementById("bm_ad_category").style.display="";
          var t_title = document.getElementsByClassName("bm_ad_title_back");
          setStyle(t_title, {
            display: "",
            margin: "0px 0px 0px 10px",
          });
        } catch (e) {
        }
      }
      try {
        if (window.matchMedia("(max-width:767px)").matches) {
          setBefore();
        } else if (window.matchMedia("(max-width:991px)").matches) {
          document.getElementsByClassName("bm_ad_text")[0].style.height="96px";
          document.getElementsByClassName("bm_ad_text")[1].style.height="96px";
          //document.getElementById("bm_ad_subtitle").style.display="none";
          document.getElementById("bm_ad_text_sub").style.display="none";
          document.getElementById("bm_ad_category").style.display="none";
          var t_title = document.getElementsByClassName("bm_ad_title_back");
          setStyle(t_title, {
            display: "block",
            margin: "0px 10px 0px 10px",
          });
        } else if (window.matchMedia("(max-width:1199px)").matches) {
          setBefore();
          document.getElementById("bm_ad_category").style.display="none";
        } else {
          setBefore();
        }
      } catch (e) {
      }
    }

    window.addEventListener('resize', function(){
      function setStyle(elms, sObj) {
        try {
          for(var i = 0, j = elms.length; i < j; i++) {
            for(var c in sObj) {
              elms[i].style[c] = sObj[c];
            }
          }
        } catch (e) {
        }
      }
      function setBefore() {
        try {
          document.getElementById("bm_ad_text_sub").style.display="";
          document.getElementsByClassName("bm_ad_text")[0].style.height="64px";
          document.getElementsByClassName("bm_ad_text")[1].style.height="64px";
          document.getElementById("bm_ad_category").style.display="";
          var t_title = document.getElementsByClassName("bm_ad_title_back");
          setStyle(t_title, {
            display: "",
            margin: "0px 0px 0px 10px",
          });
        } catch (e) {
        }
      }

      try {
        if (window.matchMedia("(max-width:767px)").matches) {
          setBefore();
        } else if (window.matchMedia("(max-width:991px)").matches) {
          document.getElementsByClassName("bm_ad_text")[0].style.height="96px";
          document.getElementsByClassName("bm_ad_text")[1].style.height="96px";
          //document.getElementById("bm_ad_subtitle").style.display="none";
          document.getElementById("bm_ad_text_sub").style.display="none";
          document.getElementById("bm_ad_category").style.display="none";
          var t_title = document.getElementsByClassName("bm_ad_title_back");
          setStyle(t_title, {
            display: "block",
            margin: "0px 10px 0px 10px",
          });
        } else if (window.matchMedia("(max-width:1199px)").matches) {
            setBefore();
            document.getElementById("bm_ad_category").style.display="none";
        } else {
            setBefore();
        }
      } catch (e) {
      }
    }, false);
  } catch (e) {
  }
})(this);