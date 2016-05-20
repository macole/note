var spawn = require('child_process').spawn;

var cmd = "top -l1|grep usage|cut -d' ' -f3|tr -d '%'|tr -d '\n'";
//console.log("cmd = "+cmd);
 
function shspawn(command) {
  return spawn('sh', ['-c', command]);
}

var child = shspawn(cmd);
var buf="";

child.stdout.on('data',function(data){
  buf=buf+data;
});
child.stderr.on('data',function (data){
  console.log('exec error: '+data);
});

child.on('close',function(code) {
  // コマンド実行後の処理
  // codeでコマンドの実行の成否が確認できる。
  // この時点でbufに正常時はコマンドの出力結果が入っている。

});
}