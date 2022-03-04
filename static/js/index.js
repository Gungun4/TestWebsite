window.onload = $(function myFun() {
    $.ajax({
        url: "http://192.168.0.80:5000/api/v1/ip",
        type: "get",
        success: function (result) {
            if (100 === result.code) {
                console.log("success");
                html_body = '<select>' +
                    '<option>项目1</option>' +
                    '<option>项目2</option>' +
                    '</select>';
                html_body += '<select>' +
                    '<option>项目1</option>' +
                    '<option>项目2</option>' +
                    '</select>';
                $(".boxb-1").html(html_body);
            }

        }
    })

})

$(document).on("click",".boxc-1",function (){
    html_body = '<h1>项目</h1>';
    console.log("click")
    $(".boxb").html(html_body)
})

// 运行脚本
window.alert = function Alert(str) {
    var msgw, msgh, bordercolor;
    msgw = 350;//提示窗口的宽度
    msgh = 100;//提示窗口的高度
    titleheight = 25 //提示窗口标题高度
    if (str == "执行成功") {
        bordercolor = "#31d71f";//提示窗口的边框颜色
        titlecolor = "#2ecc71";//提示窗口的标题颜色
    } else {
        bordercolor = "#993333";//提示窗口的边框颜色
        titlecolor = "#cc2e40";//提示窗口的标题颜色

    }
    var sWidth, sHeight;
    //获取当前窗口尺寸
    sWidth = document.body.offsetWidth;
    sHeight = document.body.offsetHeight;
//    //背景div
    var bgObj = document.createElement("div");
    bgObj.setAttribute('id', 'alertbgDiv');
    bgObj.style.position = "absolute";
    bgObj.style.top = "0";
    bgObj.style.background = "#E8E8E8";
    bgObj.style.filter = "progid:DXImageTransform.Microsoft.Alpha(style=3,opacity=25,finishOpacity=75";
    bgObj.style.opacity = "0.6";
    bgObj.style.left = "0";
    bgObj.style.width = sWidth + "px";
    bgObj.style.height = sHeight + "px";
    bgObj.style.zIndex = "10000";
    document.body.appendChild(bgObj);
    //创建提示窗口的div
    var msgObj = document.createElement("div")
    msgObj.setAttribute("id", "alertmsgDiv");
    msgObj.setAttribute("align", "center");
    msgObj.style.background = "white";
    msgObj.style.border = "1px solid " + bordercolor;
    msgObj.style.position = "absolute";
    msgObj.style.left = "50%";
    msgObj.style.font = "12px/1.6em Verdana, Geneva, Arial, Helvetica, sans-serif";
    //窗口距离左侧和顶端的距离
    msgObj.style.marginLeft = "-225px";
    //窗口被卷去的高+（屏幕可用工作区高/2）-150
    msgObj.style.top = document.body.scrollTop + (window.screen.availHeight / 2) - 150 + "px";
    msgObj.style.width = msgw + "px";
    msgObj.style.height = msgh + "px";
    msgObj.style.textAlign = "center";
    msgObj.style.lineHeight = "25px";
    msgObj.style.zIndex = "10001";
    document.body.appendChild(msgObj);
    //提示信息标题
    var title = document.createElement("h4");
    title.setAttribute("id", "alertmsgTitle");
    title.setAttribute("align", "left");
    title.style.margin = "0";
    title.style.padding = "3px";
    title.style.background = bordercolor;
    title.style.filter = "progid:DXImageTransform.Microsoft.Alpha(startX=20, startY=20, finishX=100, finishY=100,style=1,opacity=75,finishOpacity=100);";
    title.style.opacity = "0.75";
    title.style.border = "1px solid " + bordercolor;
    title.style.height = "25px";
    title.style.font = "20px Verdana, Geneva, Arial, Helvetica, sans-serif";
    title.style.color = "white";
    title.innerHTML = "提示信息";
    document.getElementById("alertmsgDiv").appendChild(title);
    //提示信息
    var txt = document.createElement("p");
    txt.setAttribute("id", "msgTxt");
    txt.style.margin = "16px 0";
    txt.innerHTML = str;
    document.getElementById("alertmsgDiv").appendChild(txt);
    //设置关闭时间
    window.setTimeout("closewin()", 2000);
}

function closewin() {
    document.body.removeChild(document.getElementById("alertbgDiv"));
    document.getElementById("alertmsgDiv").removeChild(document.getElementById("alertmsgTitle"));
    document.body.removeChild(document.getElementById("alertmsgDiv"));
}

// 运行脚本
// $(document).on("click", ".run",
//     function () {
//         var t = $(this)
//         $.confirm({
//             title: '确认',
//             content: '确认执行?',
//             type: 'green',
//             icon: 'glyphicon glyphicon-question-sign',
//             buttons: {
//                 ok: {
//                     text: '确认',
//                     btnClass: 'btn-primary',
//                     action: function () {
//                         run_script();
//                     }
//                 },
//                 cancel: {
//                     text: '取消',
//                     btnClass: 'btn-primary',
//                 }
//             }
//         })
//
//         function run_script() {
//             var case_name = t.attr("data")
//             var data = {"case_name": case_name}
//             console.log(data)
//             $.ajax({
//                 url: "http://192.168.0.80:5000/api/v1/record",
//                 type: "post",
//                 contentType: 'application/json',
//                 dataType: 'json',
//                 data: JSON.stringify(data),
//                 success: function (result) {
//                     if (result.code === 100) {
//                         alert("执行成功")
//                     } else {
//                         alert("调试文件不可执行", false, false)
//                     }
//                 },
//                 error: function () {
//                     alert("服务器繁忙", "456")
//                 }
//
//             })
//         }
//     })


//打开报告文件
$(document).on("click", ".report",
    function () {
        var file_name = $(this).text()
        console.log(file_name)
        window.open("../static/report/" + file_name)
    })

$(document).on({
    mouseover:
        function (e) {
            var y = $(this).offset().top - 75;
            var x = $(this).offset().left + 170;
            $("body").append("<div class='tip bottom' style=\"top:" + y + "px;left:" + x + "px;position: absolute\">点击打开报告文件</div>");
        },
    mouseout:
        function () {
            $(".tip").remove();
        },
}, ".report")

// 上传
$(document).on("click", ".upload", function () {
    $(".el-wrapper").css({"display": "flex"});
    var html_form = '';
    console.log("click-upload");
    $.ajax({
        url: 'http://192.168.0.80:5000/api/v1/get_pm',
        type: 'get',
        success: function (result) {
            if (result.code === 100) {
                let data = result.data;
                html_form += '文件名:<input type="text" name="file_name" id="file_name">\n'
                html_form += '选择模块:'
                html_form += '<select name="module">\n';
                for (i in data) {
                    console.log("i=" + i)
                    html_form += '<optgroup label="' + i + '">\n'
                    for (j in data[i]) {
                        html_form += '<option value="' + Object.keys(data[i][j]) + '">' + Object.values(data[i][j]) + '</option>\n';
                    }
                    html_form += '</optgroup>\n'
                }
                html_form += '</select>\n';
                html_form += '<input type="file" id="myfile" name="file">\n</br>' +
                    '<label><input type="radio" name="type" value="0" checked>用例</label><label><input type="radio" name="type" value="1">脚本</label></br>' +
                    '<button id="confirm-upload" type="submit" style="margin-left: 130px" >确定</button>\n' +
                    '<button id="form-close" type="button" name="取消">取消</button>';
                $('#upload').html(html_form);
            } else {
                alert("操作失败");
            }
        }
    })
})

// 获取上传的文件名赋值
$(document).on("change", "#myfile", function () {
    file = $(this).val();
    file_name = file.split("\\").pop();
    file_name = file_name.substring(0, file_name.lastIndexOf("."));
    console.log(file_name)
    $("#file_name").val(file_name)
})

// 确认提交
$(document).on("click", "#confirm-upload", function () {
    $(".el-wrapper").css({"display": "none"})
})

// 关闭弹窗
$(document).on("click", "#form-close", function () {
    $(".el-wrapper").css({"display": "none"})
})

// 模块选择
$(document).on("click", ".boxc-2", function () {
    $(".boxc-2").css("background", "");
    $(this).css("background", "black");
    var name = $(this).attr("name")
    var html_body = ""
    if (name === "0") {
        html_body += "<table class=\"hovertable\">\n" +
            "        <thead>\n" +
            "        <tr>\n" +
            "            <th style=\"width: 5%\">序号</th>\n" +
            "            <th style=\"width: 15%\">项目</th>\n" +
            "            <th style=\"width: 15%\">模块</th>\n" +
            "            <th style=\"width: 30%\">时间</th>\n" +
            "            <th style=\"width: 30%\">文件</th>\n" +
            "            <th>操作</th>\n" +
            "        </tr>\n" +
            "        </thead>\n" +
            "    </table>\n"
    } else {
        html_body += "<table class=\"hovertable\">\n" +
            "        <thead>\n" +
            "        <tr>\n" +
            "            <th style=\"width: 5%\">序号</th>\n" +
            "            <th style=\"width: 15%\">项目</th>\n" +
            "            <th style=\"width: 15%\">模块</th>\n" +
            "            <th style=\"width: 30%\">脚本文件</th>\n" +
            "            <th style=\"width: 30%\">报告文件</th>\n" +
            "            <th>操作</th>\n" +
            "        </tr>\n" +
            "        </thead>\n" +
            "    </table>\n"
    }

    $.ajax({
        url: "/api/v1/get_list?name=" + name,
        type: 'get',
        success: function (result) {
            if (result.code === 100) {
                let data = result.data
                html_body += "<div style=\"height: 91%;overflow: auto;box-sizing: border-box\">\n";
                html_body += "<table class=\"hovertable\">\n";
                html_body += "<tbody>\n";
                console.log(data);
                let n = 0
                for (i in data) {
                    console.log("i=" + i)
                    for (j in data[i]) {
                        n += 1
                        html_body += "<tr>\n" +
                            "<td style=\"width: 5%\">" + n + "</td>\n" +
                            "<td style=\"width: 15%\">" + data[i][j][0] + "</td>\n" +
                            "<td style=\"width: 15%\">" + i + "</td>\n" +
                            "<td style=\"width: 30%\">" + data[i][j][1] + "</td>\n" +
                            "<td class=\"report\" style=\"width: 30%\">" + data[i][j][2] + "</td>\n" +
                            "<td class=\"download\" style='width:5%' data=\"" + data[i][j][4] + "\">" + data[i][j][3] + "</td>\n" +
                            "</tr>\n";
                    }
                }
                html_body += "</tbody>";
                html_body += "</table>";
                html_body += "</div>";
                $(".boxb").html(html_body);
            }
        },
    })
})

// 下载文件
$(document).on("click", ".download", function () {
    fid = $(this).attr("data");
    console.log(fid)
    window.open("http://192.168.0.80:5000/api/v1/download/" + fid)
})
