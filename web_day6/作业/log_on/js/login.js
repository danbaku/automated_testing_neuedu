window.onload = function () {
  $("#login")[0].onclick = function () {
	  // alert("1")
    $.getJSON('./json/manager.json', function (data) {
		
      var $jsontip = $("#jsonTip");
      var strHtml = "读取的数据：<br/>"; //存储数据的变量
      $jsontip.empty(); //清空内容
      var name = $("#name").val();
      var pass = $("#pass").val();
      $.each(data, function (haha, info) {
        if (name == info["admin"] && pass == info["passwd"]) {
          strHtml = 1;
          return false;
        } else {
          strHtml = 0;
        }
      });
      if (strHtml == 1) {
        alert("登录成功");
      } else {
        alert("登录失败");
        $(".form_link")[0].innerText="忘记密码？进行找回！"
      }
      //显示处理后的数据
      console.log(strHtml);
    });
  };
  $("#on")[0].onclick = function () {
    console.log(this)
  };
};
