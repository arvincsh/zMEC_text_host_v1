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
app.listen("3000",function () {
    console.log("3000端�~O��~\~M�~J��~P��~J���~Z")
});
//�~K��~H�请��~B
app.post("/image",function (req,res) {
    var form = new formidable.IncomingForm();
    var returnData = "";
    //form.encoding = 'utf-8';
    form.uploadDir = path.join(__dirname + "/page/upload");
    form.keepExtensions = true;//��~]�~U~Y�~P~N��~@
    form.maxFieldsSize = 2 * 1024 * 1024;
    //��~D�~P~F�~[��~I~G
    form.parse(req, function (err, fields, files){

        var date = new Date();
        var time = date.getFullYear() + "_" + date.getMonth() + "_" + date.getDay() + "_" +
                                 date.getHours() + "_" + date.getMinutes() + "_" + date.getMilliseconds();
        var avatarName = time + '.png';
        fs.renameSync(files.upload.path, __dirname+"/page/upload/"+avatarName);

                returnData = child_process.execSync('python3 Identification.py '+ __dirname+"/page/upload/"+avatarName);
                //console.log(""+returnData);
                res.send(""+returnData);
        })

})