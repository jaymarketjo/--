// 1. 安装Express框架
// 在命令行中运行以下命令：
// npm install express

// 2. 创建一个新的Node.js文件（例如app.js），并编写以下代码：

const express = require('express');
const app = express();

// 模拟汽车数据库
const carDatabase = {
    "bmw": "宝马是一家德国汽车制造商，以生产高档汽车而闻名。",
    "tesla": "特斯拉是一家美国电动汽车制造商，专注于电动汽车和可再生能源解决方案。"
    // 其他汽车信息
};

// 处理汽车信息查询请求
app.get('/searchCar', (req, res) => {
    const carInput = req.query.carInput.toLowerCase();
    const result = carDatabase[carInput] || "抱歉，找不到关于该汽车的信息。";
    res.send(result);
});

// 启动服务器
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`服务器运行在 http://localhost:${PORT}`);
});