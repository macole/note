$(document).ready(function(){
    // 一覧取得
    $('#get_entries').click(function(event){
      // jQueryのajax()関数で /entries からGET
      $.ajax({
        url: '/entries',
        type: 'GET',
        cache: false,
        dataType: 'json'
      })
      .done(function(data, textStatus, jqXHR) {
        // 成功したら一覧を更新
        $('#ul_entreis').empty();
        for(var i in data){
          $('#ul_entreis').append('<li>' + data[i].id + ', ' + data[i].start_time + ', ' + data[i].file_name + '</li>');
        }
      })
      .fail(function(jqXHR, textStatus, errorThrown){
        alert('fail');
      })
    });
    // エントリー更新
    $('#post_entry').click(function(event){
      // フォームから情報を取得
      var entry = {};
      entry['id'] = $('#entry_id').val();
      entry['file_name'] = $('#file_name').val();
      var start_time = $('#start_time_hh').val() + ':' + $('#start_time_mm').val()
      entry['start_time'] = $('#start_date').val().replace(new RegExp('/', 'g'), '-') + ' ' + start_time;
      // jQueryのajax()関数で /entry/id へPOST
      $.ajax({
        'url': '/entry/' + entry['id'],
        'type': 'POST',
        'cache': false,
        'contentType': 'application/json; charset=utf-8',
        'dataType': 'json',
        'data': JSON.stringify(entry)
      })
      .done(function(data, textStatus, jqXHR) {
        // 成功したら一覧を更新
        $('#ul_entreis').empty();
        for(var i in data){
          $('#ul_entreis').append('<li>' + data[i].id + ', ' + data[i].start_time + ', ' + data[i].file_name + '</li>');
        }
      })
      .fail(function(jqXHR, textStatus, errorThrown){
        alert('fail');
      })
    });

    // 初期化処理
    // 必要な時刻情報の取得
    date = new Date();
    var YYYY = date.getFullYear();
    var MM = ('0' + (date.getMonth() + 1)).slice(-2);
    var DD = ('0' + date.getDate()).slice(-2);
    var hh = ('0' + date.getHours()).slice(-2);
    var mm = '00'
    var date_str = YYYY + '/' + MM + '/' + DD;
    // 年月日指定用部品
    $('#start_date').datepicker({
      dateFormat: 'yy/mm/dd',
      yearSuffix: '年',
      showMonthAfterYear: true,
      monthNames: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
      minDate: date
    });
    $('#start_date').datepicker('setDate', date_str);
    // 時間指定用部品
    for(var i = 0 ; i<24 ; i++) { 
      var cnt = ('0' + i).slice(-2);
      $('#start_time_hh').append('<option value="' + cnt + '">' + cnt + '</option>');
    }
    $('#start_time_hh').val(hh);
    // 分指定用部品
    for(var i = 0 ; i<60 ; i = i + 5) { 
      var cnt = ('0' + i).slice(-2);
      $('#start_time_mm').append('<option value="' + cnt + '">' + cnt + '</option>');
    }
    $('#start_time_mm').val(mm);
});

