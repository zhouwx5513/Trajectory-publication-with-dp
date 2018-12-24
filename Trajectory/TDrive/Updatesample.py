class updateSample:
    part2 = ""
    part1 = """

    <!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title></title>

    <style type="text/css">
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }

        #map {
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>

    <div id="map"></div>
    <canvas id="canvas"></canvas>

    <script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=1XjLLEhZhQNUzd93EjU5nOGQ"></script>
    <script type="text/javascript" src="../build/mapv.js"></script>

    <script type="text/javascript">

        // 百度地图API功能
        var map = new BMap.Map("map", {
            enableMapClick: false
        });    // 创建Map实例
        map.centerAndZoom(new BMap.Point(105.403119, 38.028658), 5);  // 初始化地图,设置中心点坐标和地图级别
        map.enableScrollWheelZoom(true); // 开启鼠标滚轮缩放

        map.setMapStyle({
            style: 'light'
        });
        
        """

    part3 = """
    
     var data = [];
//var citys = ["北京","天津","上海","重庆","石家庄","太原","呼和浩特","哈尔滨","长春","沈阳","济南","南京","合肥","杭州","南昌","福州","郑州","武汉","长沙","广州","南宁","西安","银川","兰州","西宁","乌鲁木齐","成都","贵阳","昆明","拉萨","海口"];

        // 构造数据
        while (Count--) {
         //   var cityCenter = mapv.utilCityCenter.getCenterByCityName(citys[parseInt(Math.random() * citys.length)]);
            data.push({
                geometry: {
                    type: 'Point',
					coordinates: [das[Count][0], das[Count][1]]
                },
                count: 30 * Math.random()
            });
        }

		//alert(mapv.utilCityCenter.getCenterByCityName(citys[10]).lng)
		
        var dataSet = new mapv.DataSet(data);

        var options = {
            fillStyle: 'rgba(255, 50, 50, 0.6)',
            shadowColor: 'rgba(255, 50, 50, 1)',
            shadowBlur: 30,
            globalCompositeOperation: 'lighter',
            methods: {
                click: function (item) {
                    console.log(item);
                }
            },
            size: 2,
            draw: 'simple'
        }

        var mapvLayer = new mapv.baiduMapLayer(map, dataSet, options);

        // dataSet.set(data); // 修改数据

        // mapvLayer.show(); // 显示图层
        // mapvLayer.hide(); // 删除图层
    </script>
	
</body>
</html>


    """

    def upexams(tupleList):
        print("begin")
        # data = []
        t1 = "var das = ["
        for i in tupleList:
            # newTuple = (i[0],i[1])
            # data.append(newTuple)
            t1+="["+i[0]+","+i[1]+"],\n"
        t1+="]\n"
        t1=t1+"var Count  = "+str(len(tupleList))

        updateSample.part2+=t1

        print(updateSample.part2)

        all=updateSample.part1+updateSample.part2+updateSample.part3

        with open("F:\\dataset\\mapv-2.0.12\\examples\\baidu-map-point-simple.html", 'w') as f:
            f.write(all)
            f.close()
        print("done")







