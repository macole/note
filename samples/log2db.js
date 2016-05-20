

var fs = require('fs');
var byline = require('byline');

// ログの行データをデータベースに登録する
var insertLogToDb = function (lineno, knex, ip, accessed, method, url, status, osize, callback) {
    if (osize == "-") {
        osize = 0;
    }

    knex("tomcat_access_logs")
    .insert({
        ip: ip,
        accessed: accessed,
        method: method,
        url: url,
        status: status,
        osize: osize
    }).then(function () {
            //登録に成功したらcallbackを呼び出す。
            console.log("line:" + lineno);
        callback(null);
    }).catch(function (error) {
            //登録に失敗した場合もメッセージを表示してcallbackを呼び出す。
        console.log("error: " + lineno + "::" + [ip, accessed, method, url, status, osize].join(":"));
            console.log(error);
        callback(error);
    });
};

// ログファイルを行単位で読み込んでデータベースに登録する
var importLog = function (dbConfig, targetPath, logPattern) {

    //ファイルストリームを開く
    var rs = fs.createReadStream(targetPath, {encoding: "utf-8"});

    // DB接続
    var knex = require('knex')(dbConfig);

    // 開いたファイルストリームをbylineストリームに繋げる
    var stream = byline.createStream(rs);

    var lineno = 1;
    // 行を読み込んだ時のイベント定義
    stream.on("data", function (line) {
        //行データを分割
        var match = logPattern.exec(line);
        if (match != null) {
            var ip = match[1];
            var accessed = match[2];
            var method = match[3];
            var url = match[4];
            var status = match[5];
            var osize = match[6];

            //ストリームの読み込みを一時停止
            stream.pause();
            //行データをデータベースに登録
            insertLogToDb(lineno, knex, ip, accessed, method, url, status, osize, function (err) {
                //コールバックされたらストリームを再開
                stream.resume();
            });
        } else {
            console.log("no match:" + lineno);
        }
        lineno = lineno + 1;
    });

    //ファイル読み込みが完了した時のイベント定義
    stream.on("end", function () {
        //DB接続を閉じる
        knex.destroy();
        console.log("end");
    });

};

// 読み込むファイルのパス
var targetPath = "C:/Users/test/log2db/localhost_access_log.2016-05-15.txt";

// ログ分割の正規表現パターン
var logPattern = /^(\S+) \- \- \[([^\]]+)\] "(\S+) (\S+) [^"]+" (\S+) (.+)$/;

// DB接続情報
var dbConfig = {
    client: "pg",
    connection: {
        host: "＜DBホスト名＞",
        user: "＜DBユーザー名＞",
        password: "＜DBパスワード＞",
        database: "＜DB名＞",
        port: "＜DBポート番号＞"
    }
};

// メイン関数を呼び出し
importLog(dbConfig, targetPath, logPattern);