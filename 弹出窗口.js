<!DOCTYPE html>
<html>
<head>
  <title>弹出窗口示例</title>
  <script>
    function openPopup() {
      // 打开一个新的弹出窗口
      var popup = window.open("popup.html", "弹出窗口", "width=400,height=400");
    }
  </script>
</head>
<body>

<button onclick="openPopup()">打开弹出窗口</button>

</body>
</html>
