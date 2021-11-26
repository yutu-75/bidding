
	var type=$.getUrlParam("type");//信息类型
	var gongShiType=$.getUrlParam("gongShiType");//信息类型
	var otherFlag=$.getUrlParam("otherFlag");
	function initSearch(){

		if(otherFlag == "9999"){
			$(".JiaoYiTypeClass").show();
			$(".GongChengLeiXingClass").show();
			$(".GongChengLeiBieClass").show();
		}
		if(type == "10"){ //工程建设
			$(".GongChengLeiXingClass").show();
			$(".GongChengLeiBieClass").show();
			$(".bdmc").remove();
			$(".bdbh").remove();
			$(".gcmc").show();
			$(".gcbh").show();
		}else if(type == "20"){ //政府采购
			$(".GongChengLeiXingClass").show();
			$(".bdbh").remove();
			$(".bdbh_td").remove();
		}

		if(gongShiType==40 || gongShiType==60 ){//控制价 ，业绩公示 不需要选择工程类型下拉选择
			$(".teshu2").remove();
			$(".teshu3").remove();
		}
		if(gongShiType==90){//合同公示
			$("#type").val(20);

			$(".teshu1").remove();
			$(".teshu3").remove();
			$(".gongcheng_op").remove();
			$(".zhengfu_op").show();
		}

	}

	//加载数据
	function loadData(){

		initSearch();

		if(gongShiType==null){
			if(type==10){
				gongShiType=10;
			}
			if(type==20){
				gongShiType=70;
			}
			if(type==30){
				gongShiType=190;
			}
			if(type==40){
				gongShiType=190;
			}
			if(type==50){
				gongShiType=110;
			}
			if(type==60){
				gongShiType=150;
			}
		}
		var app=angular.module('app',['services']);
		app.controller ( 'xinXiGongShiController' , [ '$scope' , '$http' , 'Paginator' ,function ($scope , $http , Paginator) {
				var  fetchFunction = function(currentPage,pageSize,callback){
					var url="/jiaoyixinxi/queryJiaoYiXinXiPagination.do";
					var bianHao=$("#biaoHao").val();
					var title=$("#title").val();
					/*添加2个参数  */
					var gongChengType = $("#gongChengType").val();
					var gongChengLeiBie = $("#gongChengLeiBie").val();
					var typeTmp = type;
					if(isNotBlank($("#type").val())){
						typeTmp = $("#type").val();
					}
					/*对参数进行转码，避免测试或正式环境，因为查询条件是中文导致无法查询数据问题；jiezc 2017-03-21 begin*/
					bianHao = encodeURIComponent(bianHao);
					title = encodeURIComponent(title);
					/*对参数进行转码，避免测试或正式环境，因为查询条件是中文导致无法查询数据问题；jiezc 2017-03-21 end*/
					/*结束添加  */
					$http.get(url,{params :{ title:title, bianHao:bianHao, type:typeTmp, gongShiType:gongShiType, gongChengType:gongChengType, gongChengLeiBie:gongChengLeiBie, page:currentPage, rows:pageSize}}).success(callback);
				};

				$scope.afterLoad=function(){//加载完回调事件
					//parent.$("#right_iframe").height( 900);
					parent.resizeHeight();
				}

				//查询数据
				$scope.queryData=function(){
					$scope.listPaginator = Paginator(fetchFunction, 15 ,$scope.afterLoad);
				}


				$scope.viewDetail=function(guid, yxtid, fromType, douDiFlag,cgptflag){//查看详情方法
					var url = "/jiaoyixinxi/jiaoyixinxi_view.html?guid="+guid+"&yxtid="+yxtid+"&type="+type;
					if(fromType == 2){ //建设工程
						if(gongShiType == 10){
							var url = "/jiaoyixingxi/zbgg_view.html?guid="+yxtid;
						}else if(gongShiType == 170){
							var url = "/jiaoyixingxi/bggs_view.html?guid="+yxtid;
						}else if(gongShiType == 'kzj'){
							var url = "/jiaoyixingxi/kzjgs_view.html?guid="+yxtid;
						}else if(gongShiType == 180){
							var url = "/jiaoyixingxi/pbjg_view.html?guid="+yxtid;
						}else if(gongShiType == 50){
							var url = "/jiaoyixingxi/zbgs_view.html?guid="+yxtid;
						/*   if(douDiFlag){
							  var url = "/jiaoyixingxi/zbgsdd_view.html?guid="+yxtid;
						  }else{
							  var url = "/jiaoyixingxi/zbgs_view.html?guid="+yxtid;
						  }  */
						}else if (gongShiType==130){
							var url = "/jiaoyixingxi/ycxx_view.html?guid="+yxtid;
						}else{
							var url = "/jiaoyixingxi/zbsb_view.html?guid="+yxtid;
						}


					/* 	if(gongShiType == 10){
						 	if(douDiFlag == "1"){
								url = "/jiaoyijsgc/zbggdd_view.html?guid="+yxtid;
							}else{
								url = "/jiaoyijsgc/zbgg_view.html?guid="+yxtid;
							}
						}else if(gongShiType == 20){
							url = "/jiaoyijsgc/zbwj_view.html?guid="+yxtid;
						}else if(gongShiType == 30){
							url = "/jiaoyijsgc/bggs_view.html?guid="+yxtid;
						}else if(gongShiType == 40){
							url = "/jiaoyijsgc/kzjgs_view.html?guid="+yxtid;
						}else if(gongShiType == 50){
							if(douDiFlag == "1"){
							//	var url = "/jiaoyijsgc/zbgsdd_view.html?guid="+guid;
								var url = "/jiaoyijsgc/zbgsdd_view.html?guid="+yxtid;
							}else{
								url = "/jiaoyijsgc/zbgs_view.html?guid="+yxtid;
							}


						}else if(gongShiType == 60){
							if(douDiFlag=="1"){
							    var url = "/jiaoyijsgc/yjgsdd_view.html?guid="+yxtid;
							}else{
								var url = "/jiaoyijsgc/yjgs_view.html?guid="+yxtid;
							}

						} */
					}else if(fromType == 3){ //政府采购
						debugger;
						console.log("11111");
						console.log("11111"+cgptflag+"11111");
						if(gongShiType == 70){
							if(isNotBlank(cgptflag)&&cgptflag!="0"){
								if(cgptflag=="1"){
									var url = "http://www.ezggzy.cn/zcsc/wssc/caiGouXinXi/toJingJiaBulletenDetail.html?guid="+yxtid;
								}else if(cgptflag=="2"){
									var url = "http://www.ezggzy.cn/zcsc/wssc/caiGouXinXi/toZhiGouBulletenDetail.html?guid="+yxtid;
								}
							}else{
								var url = "/jiaoyizfcg/zbgg_view.html?guid="+yxtid;
							}
						}else if(gongShiType == 170){
							if(isNotBlank(cgptflag)&&cgptflag!="0"){
								if(cgptflag=="5"){
									var url = "http://www.ezggzy.cn/zcsc/wssc/caiGouXinXi/toBuYiBulletenDetail.html?guid="+yxtid;
								}
							}else{
								var url = "/jiaoyizfcg/bggs_view.html?guid="+yxtid;
							}
						}else if(gongShiType == 50){
							if(isNotBlank(cgptflag)&&cgptflag!="0"){
								if(cgptflag=="3"){
									var url = "http://www.ezggzy.cn/zcsc/wssc/caiGouXinXi/toJingJiaResultDetail.html?guid="+yxtid;
								}else if(cgptflag=="4"){
									var url = "http://www.ezggzy.cn/zcsc/wssc/caiGouXinXi/toZhiGouResultDetail.html?guid="+yxtid;
								}
							}else{
								var url = "/jiaoyizfcg/zbgs_view.html?guid="+yxtid;
							}
							/* if(douDiFlag){
								var url = "/jiaoyizfcg/zbgsdd_view.html?guid="+yxtid;
							}else{
								var url = "/jiaoyizfcg/zbgs_view.html?guid="+yxtid;
							}  */
						}else if (gongShiType== 130){
							var url = "/jiaoyizfcg/ycxx_view.html?guid="+yxtid;
						}

						/* if(gongShiType == 70){
							if(douDiFlag == "1"){
								url = "/jiaoyixingxi/zbggdd_view.html?guid="+yxtid;
							}else{
								url = "/jiaoyixingxi/zbgg_view.html?guid="+yxtid;
							}
					   }else if(gongShiType == 30){
						   url = "/jiaoyixingxi/bggs_view.html?guid="+yxtid;
					   }else if(gongShiType == 80){
						  if(douDiFlag == "1"){
							  var url = "/jiaoyixingxi/zbgsdd_view.html?guid="+yxtid;
						  }else{
							  var url = "/jiaoyixingxi/zbgs_view.html?guid="+yxtid;
						  }
					   }else if(gongShiType == 'hy'){
						      var url = "/jiaoyixingxi/hygs_view.html?guid="+guid;
					   }*/
					}
				    window.open(url);
			    }

				$scope.query=function(){//查询
					$scope.queryData();
			    }

				//查询数据
				$scope.queryData();
		}]);

		angular.module('app').filter('cut', function () {
			  return function (value, wordwise, max, tail) {
			    if (!value) return '';

			    max = parseInt(max, 10);
			    if (!max) return value;
			    if (value.length <= max) return value;

			    value = value.substr(0, max);
			    if (wordwise) {
			      var lastspace = value.lastIndexOf(' ');
			      if (lastspace != -1) {
			        value = value.substr(0, lastspace);
			      }
			    }

			    return value + (tail || ' …');
			  };
		});


		angular.module('app').filter('dealType', function () {
			return function(value){
				if (!value) return '';
				return JiaoYiLeiXingType[value];
			}

			});

		angular.module('app').filter('dealCongChengType', function () {
			return function(value){
				if (!value) return '';
				return GongChengType[value];
			}
		});
	}
