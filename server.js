var path = require("path");
var fs = require("fs");
var express =require("./node_modules/express");
var app=express();
var bodyParser = require('./node_modules/body-parser');
var formidable = require('./node_modules/formidable');
const child_process = require('child_process');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/page"));
app.listen("80",function () {
    console.log("80端口服务启动：")
});
//拦截请求
app.post("/image",function (req,res) {
    var form = new formidable.IncomingForm();
    var returnData = "";
    //form.encoding = 'utf-8';
    form.uploadDir = path.join(__dirname + "/page/upload");
    form.keepExtensions = true;//保留后缀
    form.maxFieldsSize = 2 * 1024 * 1024;
    //处理图片
    form.parse(req, function (err, fields, files){

        var date = new Date();
        var time = date.getFullYear() + "_" + date.getMonth() + "_" + date.getDay() + "_" +
        			 date.getHours() + "_" + date.getMinutes() + "_" + date.getMilliseconds();
        var avatarName = time + '.png';
        fs.renameSync(files.upload.path, __dirname+"/page/upload/"+avatarName);

		returnData = child_process.execSync('python Identification.py '+ __dirname+"/page/upload/"+avatarName);
		//console.log(""+returnData);
		res.send(""+returnData);
	})

})
