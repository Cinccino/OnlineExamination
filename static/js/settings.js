

$("#dialogsubmit").click(function () {

    var subjectid = $("#subjectid").val();//document.getElementById("inputusername");
    var name = $("#inputname").val();


    if (subjectid && name)
        {
            $.post("/btnaddsubjectrequest/",  
            {  
            subjectid:subjectid, 
            name:name,

            },
            function(data)
                { 
                // var dialog=document.getElementById("modal-add")
                // dialog.close();
                //$("#modal-add").hide();
                alert( data );
                }
            )
        }
    else
        {
            alert("error!"); 
        }

});

// $('#modaledit').on('shown.bs.modal', function () {
    
//     var result = $('#tb_departments').bootstrapTable('getSelections');  
//     var ids = [];
//     for (var i = 0; i < result.length; i++) {
//         var item = result[i];
//         ids.push(item.username);
//     }
//     if (ids.length < 1) {
//         alert("请选中一行");
//         return;
//     }

// })

$("#btneditrequest").click(function () {

   
    // var result = $('#tb').bootstrapTable('getSelections');  
    // var ids = [];
    // for (var i = 0; i < result.length; i++) {
    //     var item = result[i];
    //     ids.push(item.username);
    // }
    // if (ids.length != 1) {
    //     alert("请选中一行");
    //     return;
    // }
    $('#modaledit').appendTo("body").modal('show');
    // $('#modaledit').modal('show');

    // $('#modal-edit').modal({  
    //     keyboard: false ,
    //     show: true,
    // })  
    // $('#modal-edit').modal('show')=true;

    // $.post("/btneditrequest/",  
    //     {
    //         usersets:ids,
    //         form: "student",
    //     },
    //     function (data) {
    //         // var dialog=document.getElementById("modal-add")
    //         // dialog.close();
    //         //$("#modal-add").hide();
    //         alert(data);
    //     }
    // )



    // var username = $("#inputusername").val();
    // var name = $("#inputname").val();
    // var pwd = $("#inputpwd").val();
    // var email = $("#inputemail").val();
    // var major = $("#inputmajor").val();

    // if(email.indexOf("@") == -1){  
              
    //         alert("请输入正确的email地址");
    //         inputemail.focus();
    //         return; 
    // }
    // else if (username && name && pwd && email && major)
    //     {
    //         $.post("/btneditsaverequest/",  
    //         {  
    //         username:username, 
    //         name:name,
    //         pwd:pwd,
    //         email:email,
    //         major:major,
    //         form:"student",
    //         },
    //         function(data)
    //             { 
    //             // var dialog=document.getElementById("modal-add")
    //             // dialog.close();
    //             //$("#modal-add").hide();
    //             alert( data );
    //             }
    //         )
    //     }
    // else
    //     {
    //         alert("error!"); 
    //     }

});


$(function () {
    //1.初始化Table
    // alert("www")
    var oTable = new TableInit();
    oTable.Init();

    //2.初始化Button的点击事件
    var oButtonInit = new ButtonInit();
    oButtonInit.Init();

});


var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb').bootstrapTable({
            url: "/asset_show_table_subject",         //请求后台的URL（*）
            method: 'get',                      //请求方式（*）
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
            pagination: true,                   //是否显示分页（*）
            sortable: true,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: oTableInit.queryParams,//传递参数（*）
            sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber:1,                       //初始化加载第一页，默认第一页
            pageSize: 10,                       //每页的记录行数（*）
            pageList: [10, 25, 50, 100],        //可供选择的每页的行数（*）
            search: true,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大
            strictSearch: true,
            showColumns: true,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行
            height: 500,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId: "ID",                     //每一行的唯一标识，一般为主键列
            showToggle:true,                    //是否显示详细视图和列表视图的切换按钮
            cardView: false,                    //是否显示详细视图
            detailView: false,                   //是否显示父子表
            // editable:true,
            // showExport: true,  //是否显示导出按钮  
            // buttonsAlign:"right",  //按钮位置  
            // exportTypes:['excel'],  //导出文件类型  
            // Icons:'glyphicon-export',  
            columns: [{
                checkbox: true
            }, {
                field: 'subjectid',
                title: '科目编号',
                sortable: true,
                
            }, {
                field: 'name',
                title: '科目'
            }, {
                field: 'flag',
                title: '状态'
            },
         ]
        });
    };

    //得到查询的参数
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset,  //页码
            username: $("#txt_search_departmentname").val(),
            search:params.search,
            order: params.order,
            ordername: params.sort,
        };
        return temp;
    };
    return oTableInit;
};


var ButtonInit = function () {
    var oInit = new Object();
    var postdata = {};

    oInit.Init = function () {
        //初始化页面上面的按钮事件
        $("#btn_delete").click(function () {
                var result = $('#tb').bootstrapTable('getSelections');  
    
                var ids = [];  
                for (var i = 0; i < result.length; i++) {  
                    var item = result[i];  
                    ids.push(item.subjectid);  
                }  

                if (ids.length <1 ) {
                    alert("未选中行!");
                    return; 
                }
                //alert(ids)
                $.post("/btndeletesubjectrequest/",  
                {  
                subjectsets:ids, 

                },  
                function(data){  
                alert( data );  
                });

            });     

            
    };

    return oInit;
};


