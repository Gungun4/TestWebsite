// window.onload = $(function myFun() {
//     $.ajax({
//         url: "http://192.168.0.80:5000/api/v1/get_report",
//         type: "post",
//         success: function (result) {
//             if (100 == result.code) {
//                 console.log(result)
//                 window.localStorage.setItem("data", result.data);
//             }
//
//         }
//     })
// })
// 运行脚本
$(document).on("click", ".run",
    function () {
           var bool = $.confirm({
                title: '确认',
                content: '确认执行?',
                type: 'green',
                icon: 'glyphicon glyphicon-question-sign',
                buttons: {
                    ok: {
                        text: '确认',
                        btnClass: 'btn-primary',
                        action:function (){
                            run_script();
                        }
                    },
                    cancel: {
                        text: '取消',
                        btnClass: 'btn-primary',
                    }
                }
            })
        function run_script() {
            var data = $(this).attr("data")
            console.log(data)
            $.ajax({
                url: "http://192.168.0.80:5000/api/v1/record/" + data,
                type: "post",
                success: function (result) {
                    if (result.code === 100) {
                        alert("执行成功")
                    }
                },
                error: function () {
                    alert("执行失败")
                }

            })
        }
    })

$(document).on("click", ".report",
    function () {
        window.open("../static/report/report.html")
    })