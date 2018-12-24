class updateExam:
    part2 = ""
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
    	          [{name:'p1'}, {name:'p2',value:{colorValue:'gold'}}],
                [{name:'p2'}, {name:'p3',value:{colorValue:'gold'}}],
                [{name:'p3'}, {name:'p4',value:{colorValue:'gold'}}],
				[{name:'p4'}, {name:'p5',value:{colorValue:'gold'}}],
				[{name:'p5'}, {name:'p6',value:{colorValue:'gold'}}],
				[{name:'p6'}, {name:'p7',value:{colorValue:'gold'}}],
				[{name:'p7'}, {name:'p8',value:{colorValue:'gold'}}],
				[{name:'p8'}, {name:'p9',value:{colorValue:'gold'}}],
				[{name:'p9'}, {name:'p10',value:{colorValue:'gold'}}],
				[{name:'p10'}, {name:'p11',value:{colorValue:'gold'}}],
				[{name:'p11'}, {name:'p12',value:{colorValue:'gold'}}],
				[{name:'p12'}, {name:'p13',value:{colorValue:'gold'}}],
				[{name:'p13'}, {name:'p14',value:{colorValue:'gold'}}],
				[{name:'p14'}, {name:'p15',value:{colorValue:'gold'}}],
				[{name:'p15'}, {name:'p16',value:{colorValue:'gold'}}],
				[{name:'p16'}, {name:'p17',value:{colorValue:'gold'}}],
				[{name:'p17'}, {name:'p18',value:{colorValue:'gold'}}],
				[{name:'p18'}, {name:'p19',value:{colorValue:'gold'}}],
				[{name:'p19'}, {name:'p20',value:{colorValue:'gold'}}],
				[{name:'p20'}, {name:'p21',value:{colorValue:'gold'}}],
				[{name:'p21'}, {name:'p22',value:{colorValue:'gold'}}],
				[{name:'p22'}, {name:'p23',value:{colorValue:'gold'}}],
				[{name:'p23'}, {name:'p24',value:{colorValue:'gold'}}],
				[{name:'p24'}, {name:'p25',value:{colorValue:'gold'}}],
				[{name:'p25'}, {name:'p26',value:{colorValue:'gold'}}],
				[{name:'p26'}, {name:'p27',value:{colorValue:'gold'}}],
				[{name:'p27'}, {name:'p28',value:{colorValue:'gold'}}],
				[{name:'p28'}, {name:'p29',value:{colorValue:'gold'}}],
				[{name:'p29'}, {name:'p30',value:{colorValue:'gold'}}],
				[{name:'p30'}, {name:'p31',value:{colorValue:'gold'}}],
				[{name:'p31'}, {name:'p32',value:{colorValue:'gold'}}],
				[{name:'p32'}, {name:'p33',value:{colorValue:'gold'}}],
				[{name:'p33'}, {name:'p34',value:{colorValue:'gold'}}],
				[{name:'p34'}, {name:'p35',value:{colorValue:'gold'}}],
				[{name:'p35'}, {name:'p36',value:{colorValue:'gold'}}],
				[{name:'p36'}, {name:'p37',value:{colorValue:'gold'}}],
				[{name:'p37'}, {name:'p38',value:{colorValue:'gold'}}],
				[{name:'p38'}, {name:'p39',value:{colorValue:'gold'}}],
				[{name:'p39'}, {name:'p40',value:{colorValue:'gold'}}],
				[{name:'p40'}, {name:'p41',value:{colorValue:'gold'}}],
				[{name:'p41'}, {name:'p42',value:{colorValue:'gold'}}],
				[{name:'p42'}, {name:'p43',value:{colorValue:'gold'}}],
				[{name:'p43'}, {name:'p44',value:{colorValue:'gold'}}],
				[{name:'p44'}, {name:'p45',value:{colorValue:'gold'}}],
				[{name:'p45'}, {name:'p46',value:{colorValue:'gold'}}],
				[{name:'p46'}, {name:'p47',value:{colorValue:'gold'}}],
				[{name:'p47'}, {name:'p48',value:{colorValue:'gold'}}],
				[{name:'p48'}, {name:'p49',value:{colorValue:'gold'}}],
				[{name:'p49'}, {name:'p50',value:{colorValue:'gold'}}],
				[{name:'p50'}, {name:'p51',value:{colorValue:'gold'}}],
				[{name:'p51'}, {name:'p52',value:{colorValue:'gold'}}],
				[{name:'p52'}, {name:'p53',value:{colorValue:'gold'}}],
				[{name:'p53'}, {name:'p54',value:{colorValue:'gold'}}],
				[{name:'p54'}, {name:'p55',value:{colorValue:'gold'}}],
				[{name:'p55'}, {name:'p56',value:{colorValue:'gold'}}],
				[{name:'p56'}, {name:'p57',value:{colorValue:'gold'}}],
				[{name:'p57'}, {name:'p58',value:{colorValue:'gold'}}],
				[{name:'p58'}, {name:'p59',value:{colorValue:'gold'}}],
				[{name:'p59'}, {name:'p60',value:{colorValue:'gold'}}],
				[{name:'p60'}, {name:'p61',value:{colorValue:'gold'}}],
				[{name:'p61'}, {name:'p62',value:{colorValue:'gold'}}],
				[{name:'p62'}, {name:'p63',value:{colorValue:'gold'}}],
				[{name:'p63'}, {name:'p64',value:{colorValue:'gold'}}],
				[{name:'p64'}, {name:'p65',value:{colorValue:'gold'}}],
				[{name:'p65'}, {name:'p65',value:{colorValue:'gold'}}]



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
    			   {name:'p66',value:70,
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

    def upexams(tupleList):
        print("begin")
        data = []
        for i in tupleList:
            newTuple = (i[0],i[1])
            data.append(newTuple)
        for i in range(66):
            j = i+1;
            t1 = "'p"+str(j)+"':["+data[i][0]+","+data[i][1]+"]"
            if i==65:
                t1+"\n"
            else:
                t1+=",\n"
            updateExam.part2+=t1
        all=updateExam.part1+updateExam.part2+updateExam.part3

        with open("F:\\dataset\\demo个人轨迹\\js\\example1.js", 'w') as f:
            f.write(all)
            f.close()
        print("done")







