class updateExam:
    part2 = ""
    part2_1 = ""
    part2_3 = ""
    part1 = """

    (function () {
        require.config({
            paths: {
    			echarts: "echarts",
    		},
        });

        require(
        [
            "echarts",
            "echarts/chart/main",
    		"echarts/chart/map",	
        ],
        function (echarts, BMapExtension) {
            $('#main').css({
                height:$('body').height(),
                width:$('body').width()
            });

            // 初始化地图
            var BMapExt = new BMapExtension($('#main')[0], BMap, echarts,{
                enableMapClick: false
            });
            var map = BMapExt.getMap();
            var container = BMapExt.getEchartsContainer();

            var startPoint = {
                x: 116.328755, //天河城 
                y: 39.95588
            };

            var point = new BMap.Point(startPoint.x, startPoint.y);
            map.centerAndZoom(point, 17);
            map.enableScrollWheelZoom(true);
            // 地图自定义样式
            map.setMapStyle({
               styleJson: [
              {
                        'featureType': 'land',     //调整土地颜色
                        'elementType': 'geometry',
                        'stylers': {
                                  'color': '#081734'
                        }
              },
              {
                        'featureType': 'building',   //调整建筑物颜色
                        'elementType': 'geometry',
                        'stylers': {
                                  'color': '#04406F'
                        }
              },
             {
                        'featureType': 'building',   //调整建筑物标签是否可视
                        'elementType': 'labels',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'highway',     //调整高速道路颜色
                        'elementType': 'geometry',
                        'stylers': {
                        'color': '#015B99'
                        }
              },
              {
                        'featureType': 'highway',    //调整高速名字是否可视
                        'elementType': 'labels',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'arterial',   //调整一些干道颜色
                        'elementType': 'geometry',
                        'stylers': {
                        'color':'#003051'
                        }
              },
              {
                        'featureType': 'arterial',
                        'elementType': 'labels',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'green',
                        'elementType': 'geometry',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'water',
                        'elementType': 'geometry',
                        'stylers': {
                                  'color': '#044161'
                        }
              },
              {
                        'featureType': 'subway',    //调整地铁颜色
                        'elementType': 'geometry.stroke',
                        'stylers': {
                        'color': '#003051'
                        }
              },
              {
                        'featureType': 'subway',
                        'elementType': 'labels',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'railway',
                        'elementType': 'geometry',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'railway',
                        'elementType': 'labels',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'all',     //调整所有的标签的边缘颜色
                        'elementType': 'labels.text.stroke',
                        'stylers': {
                                  'color': '#313131'
                        }
              },
              {
                        'featureType': 'all',     //调整所有标签的填充颜色
                        'elementType': 'labels.text.fill',
                        'stylers': {
                                  'color': '#FFFFFF'
                        }
              },
              {
                        'featureType': 'manmade',   
                        'elementType': 'geometry',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'manmade',
                        'elementType': 'labels',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'local',
                        'elementType': 'geometry',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'local',
                        'elementType': 'labels',
                        'stylers': {
                        'visibility': 'off'
                        }
              },
              {
                        'featureType': 'subway',
                        'elementType': 'geometry',
                        'stylers': {
                                  'lightness': -65
                        }
              },
              {
                        'featureType': 'railway',
                        'elementType': 'all',
                        'stylers': {
                                  'lightness': -40
                        }
              },
              {
                        'featureType': 'boundary',
                        'elementType': 'geometry',
                        'stylers': {
                                  'color': '#8b8787',
                                  'weight': '1',
                                  'lightness': -29
                        }
              }
        ]
            });

    option = {

        color: ['gold','aqua','lime'],
        title : {
            text: '',
            subtext: '',
            x:'center',
            textStyle : {
                color: '#fff',
    			fontSize:20,
    			fontWeight:'bold',
            }
        },
        tooltip : {
            show: true,
    		trigger:'item',
    		hideDelay:4000,
            formatter: function(d) {
    			var jw= '经度：'+d.value[0]+'<br/>'
    			    jw += '纬度：'+d.value[1]
    			return jw       
            }
    	},
    	color:['gold','red'],

      series : [
    {
    	  name:'上班轨迹(甲)',
          type:'map',
          mapType: 'none',
          data:[],

          markLine : {
          Symbol:['none', 'arrow'],
          symbolSize:['0', '0.1'],
          smooth:true,
          smooth:0,
          effect : {
              show: true,
              scaleSize: 1,
              period: 30,
              color: '#fff',
              shadowBlur: 10
          },
          itemStyle : {
              color: 'red',
              normal: {
                  color:function(param){
                  return(param.data[0].value.colorValue);
                  },
                  borderWidth:3,
                  lineStyle: {
                      type: 'solid',
                      width: 3,
                      shadowBlur: 10
                  },
                  label:{show:false,value:'天河城'}
            }
          },

        data : [
        """
    part2_2 ="""



    		]
    		},
    	  markPoint:{
    			symbol:'image://./image/location.svg',
    			symbolSize:function(v){
    				return v/5
    			},
    			effect:{
    			    show:true,
                    type:'bounce',
                    period:3,				
    			},
    			itemStyle:{
    				normal:{
    					label:{
    						show:false,
    					},
    				},
    				emphasis:{
    					label:{
    						show:false,
    					},
    				},
    			},
    			data:[
    			   {name:'p1',value:50,
    			       tooltip:{
    					   formatter:'时间:8:30am<br/>出发地:中海锦城南苑'
    				   },
    			   },
    			   """
    part2_4="""
    			       tooltip:{
    					   formatter:'天河城<br/>经度:112.328755<br/>纬度:23.137588'  
    				   },
    			   },

    			],
    		},
          geoCoord:{
    """

    part3 = """
    }
    },


        ]
    };


    var myChart = BMapExt.initECharts(container);
    window.onresize = myChart.onresize;
    BMapExt.setOption(option);
                    }
                    );
                    })();


    """

    def upexams(tupleList,file):
        lens = len(tupleList)
        print("begin")
        data = []
        for i in tupleList:
            newTuple = (i[0],i[1])
            data.append(newTuple)
        for i in range(lens):
            tamp = lens-1
            j = i+1;
            t1 = "'p"+str(j)+"':["+data[i][0]+","+data[i][1]+"]"
            if i==tamp:
                t1+"\n"
            else:
                t1+=",\n"
            updateExam.part2+=t1
        # all=updateExam.part1+updateExam.part2+updateExam.part3
        #
        # with open("F:\\dataset\\demo个人轨迹\\js\\example1.js", 'w') as f:
        #     f.write(all)
        #     f.close()
        # print("done")


        # str = """ """
        # for i in range(1,lens):
        #     j = i+1
        #     t1 = "[{name:'p"+str(i)+"'}, {name:'p"+str(j)+"',value:{colorValue:'gold'}}]"
        #     if i+1 == lens :
        #         t1 = "[{name:'p" + str(i) + "'}, {name:'p" + str(i) + "',value:{colorValue:'gold'}}]"
        #         t1 += "\n"
        #     else:
        #         t1 += ",\n"
        for i in range(1, lens):
            j = i + 1
            t1 = "[{name:'p" + str(i) + "'}, {name:'p" + str(j) + "',value:{colorValue:'gold'}}]"
            if j <= lens:
                # t1 = "[{name:'p" + str(i) + "'}, {name:'p" + str(i) + "',value:{colorValue:'gold'}}]"
                t1 += ",\n"
            else:
                t1 += "\n"



            updateExam.part2_1 += t1

            strss = ""
            strss+="{name:'p"+str(lens)+"',value:70,"
            strss+="\n"
            updateExam.part2_3 = strss

            all=updateExam.part1+updateExam.part2_1+updateExam.part2_2+updateExam.part2_3+updateExam.part2_4+updateExam.part2+updateExam.part3


            fileName = "F:\\dataset\\demo个人轨迹\\js\\example"+str(file)+".js"
            with open(fileName, 'w') as f:
                f.write(all)
                f.close()
            # print("done")
        updateExam.part2 = ""
        updateExam.part2_1 = ""
        updateExam.part2_3 = ""




