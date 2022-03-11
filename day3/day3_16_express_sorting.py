#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_16_express_sorting.py
@time: 2022/3/1  15:40
# @describe: 快递分拣⼩程序
"""

"""
 需求： 
    现有一堆快递地址信息，需对其进行按省分拣，以方便后续投递，最终⽣成的数据格式如下：
    { 
        "北京市":[
             ['王*⻰', '北京市海淀区苏州街⼤恒科技⼤厦南座4层'],
             ['庞*⻜', '北京市昌平区汇德商厦四楼403'],
             ....
             ],
        "⼭东省":[
             ['孙*云', '⼭东省济南市⼭东省济南市历下区祥泰汇东国际，⼀号楼3005室'],
             ['鞠*⻰', '⼭东省潍坊市⽟清街江⼭帝景B区12号楼⼀单元14楼'],
             ['张*', '⼭东省济南市兴港路三庆城市主⼈']
             ....
             ],
        ...
         ..
    }
"""

addres_data = [['王*龙', '北京市 海淀区', '苏州街大恒科技大厦南座4层'], ['庞*飞', '北京市 昌平区', '汇德商厦四楼403'],
               ['顾*锐', '江苏省 扬州市', '三垛镇工业集中区扬州市立华畜禽有限公司'], ['王*飞', '上海市 徐汇区', '上海市徐汇区H88越虹广场B座5E'],
               ['华*升', '北京市 海淀区', '杰睿大厦'], ['朱*锴', '上海市 浦东新区', '川沙新镇华川家园33号楼503'],
               ['陈*盼', '浙江省 杭州市', '闲林街道，西溪华东园，十幢一单元401。'], ['司*鹏', '河南省 鹤壁市', '淇滨大道310号  鹤壁京立医院'],
               ['聂*睿', '河北省 石家庄市', '中山路勒泰中心写字楼b座11层'], ['张*', '辽宁省 本溪市', '明兴丽城九号楼四单元'],
               ['冉*晗', '河北省 石家庄市', '体育南大街385号'], ['高*杰', '北京市 朝阳区', '广渠路42号院3号楼，408'], ['李*国', '安徽省 合肥市', '新站区淮合花园'],
               ['常*源', '江苏省 南京市', '白下路242号，南京市红十字医院，放射科'], ['张*玉', '河北省 沧州市', '新居然家居广场'],
               ['王*川', '上海市 奉贤区', '南桥镇 贝港七区'], ['冀*庆', '河北省 保定市', '河北大学坤兴园生活区'],
               ['胡*晨', '浙江省 宁波市', '浙江省宁波市江东区中山首府A座2004室'], ['尹*婷', '湖北省 武汉市', '武汉大学信息学部'],
               ['李*东', '辽宁省 大连市', '大关一街3号3-3-1'], ['张*', '天津市 河西区', '隆昌路94号（天津科技馆）'], ['刘*', '湖北省 黄冈市', '城关镇'],
               ['阿*亚', '内蒙古 呼和浩特市', '包头东接民望家园1区3号楼2单元1501'], ['孙*云', '山东省 济南市', '山东省济南市历下区祥泰汇东国际，一号楼3005室'],
               ['曹*亮', '黑龙江省 大庆市', '服务外包产业园D1'], ['侯*琦', '上海市 长宁区', '金钟路凌空soho16号楼3楼'],
               ['郭*峰', '河南省 商丘市', '高新技术开发区恒宇食品厂'], ['赵*生', '河北省 唐山市', '朝阳道与学院路路口融通大厦2408室'],
               ['张*', '陕西省 咸阳市', '文汇东路6号西藏民族大学'], ['刘*民', '北京市 大兴区', '南海家园四里7号楼1单元902'], ['郭*兰', '湖北省 武汉市', '湖北省'],
               ['张*强', '河北省', '张家口市经开区钻石南路11号'], ['鞠*龙', '山东省 潍坊市', '玉清街江山帝景B区12号楼一单元14楼'],
               ['李*', '北京市 海淀区', '西二旗智学苑5号楼超市'], ['许*康', '北京市 西城区', '西单北大街甲133号'], ['叶*生', '江苏省 扬州市', '扬子江中路756号'],
               ['赵*兴', '北京市 海淀区', '西二旗上地信息路1号金远见大楼华纬讯301'], ['徐*革', '北京市 海淀区', '闵庄路3号102栋二层206'],
               ['徐*', '安徽省 淮南市', '金荷小区(金格商场旁)'], ['雷*', '北京市 朝阳区', '望京街道望京sohoT1C座1201'], ['庄*', '浙江省 杭州市', '恒生电子大厦'],
               ['蔡*恩', '湖北省 武汉市', '仁和路沙湖港湾B区1103'], ['陈*', '江苏省 苏州市', '巴城镇湖滨北路193号牛吃蟹庄'],
               ['黄*', '北京市 朝阳区', '霄云路26号鹏润大厦A座33层'], ['魏*飞', '河北省 石家庄市', '新石北路与红旗大街交口开元大厦502室'],
               ['张*', '山东省 济南市', '兴港路三庆城市主人'], ['袁*成', '上海市 闵行区', '华翔路2215号魔方公寓A115'], ['陈*雷', '江苏省 南通市', '三和镇三江村11组'],
               ['刘*超', '河南省 鹤壁市', '浚州大道丽景公馆'], ['P*r*t', '江苏省 苏州市', '苏雅路158号华盛广场B座802室'],
               ['唐*亮', '上海市 浦东新区', '金科路2889弄长泰广场A座（1号楼）3层'], ['郑*盛', '湖北省 武汉市', '黄孝河路特1号王府花园D座2803室'],
               ['荆*东', '山东省 青岛市', '新疆路8号中联自由港湾A座4楼'], ['周*', '山东省 聊城市', '兴华东路58号国土资源局'],
               ['郭*坤', '浙江省 金华市', '北苑街道拥军路518号'], ['杨*', '北京市 昌平区', '北京市朝阳区将台路5号院3号楼5门3501号A室'],
               ['漆*平', '浙江省 温州市', '上江路123号金钻家园3-102'], ['任*军', '河北省 张家口市', '乾华购物广场四层乾华影城'],
               ['万*旭', '河北省 邯郸市', '武安市石洞乡赵庄村'], ['赵*', '安徽省 阜阳市', '一道河路39号，阜阳创伤医院6楼网络中心'],
               ['杨*', '北京市 海淀区', '中关村科学院南路2号融科资讯中心C座北楼9层'], ['张*成', '浙江省 杭州市', '杭州市萧山区广元公寓13幢1单元2803室'],
               ['沈*弘', '江苏省 南京市', '明发滨江新城2期281栋2519室'], ['周*', '上海市 浦东新区', '航头镇航都路18号'],
               ['程*', '河南省 洛阳市', '太康路与望春门街交叉口奥林商务'], ['张*凯', '北京市 朝阳区', '朝阳路67号院财满街8-1-801'],
               ['杜*家', '山东省 潍坊市', '健康东街潍坊软件园B座8楼'], ['李*兵', '北京市 东城区', '北京市东城区建国门南大街7号万豪中心A座10层1005'],
               ['牛*雷', '上海市 浦东新区', '东方路1217号 陆家嘴金融服务广场8楼'], ['饶*君', '上海市 杨浦区', '锦建路腾讯众创空间'],
               ['冯*', '陕西省 西安市', '大寨路185号华洲城熙悦都'], ['胡*', '湖北省 十堰市', '明清村盐业附近'], ['吴*', '陕西省 西安市', '含光路华豪丽晶'],
               ['白*', '河南省 南阳市', '麒麟路468号平通小区'], ['李*', '北京市 朝阳区', '高碑店东区D26-9'], ['师*飞', '湖北省 武汉市', '雄楚大道991号礼尚人家小区'],
               ['刘*', '陕西省 商洛市', '铁路小区世纪豪城a座'], ['田*', '北京市 海淀区', '六道口金码大厦B座22层金英杰医学前台'],
               ['刘*晓', '北京市 朝阳区', '建国路甲92号世贸大厦C座13层'], ['张*', '新疆 昌吉州', '玛纳斯镇团结南路280号'],
               ['苏*', '河北省', '石家庄市桥西区建胜路7号3302小区'], ['仝*', '天津市 西青区', '西青开发区 赛达国际工业城 天津威盛电子有限公司'],
               ['丁*凯', '浙江省 宁波市', '周巷镇段头湾转角超市'], ['佟*', '北京市 昌平区', '霍营街道回龙观首立社区'],
               ['陈*言', '北京市 朝阳区', '六里屯街道八里庄北里87爱丽家公寓775'], ['关*', '北京市 海淀区', '永丰路与北清路交汇口东南角 四维图新大厦'],
               ['夏*英', '上海市 嘉定区', '金润路478弄永翔佳苑21号楼601'], ['凌*', '上海市 静安区', '共和新路2301弄23号'],
               ['李*华', '上海市 静安区', '共和新路2301弄23号'], ['马*波', '北京市 海淀区', '西三旗建材城西路北辰机械厂2单选605'],
               ['刘*源', '山东省 潍坊市', '盛景嘉苑小区7号楼2单元202室'], ['李*', '河南省 郑州市', '永平路48号绿业元1号办公楼607室'],
               ['张*', '河南省 郑州市', '英协路7号移动大楼5楼'], ['温*燃', '吉林省 长春市', '营口路77号 孵化基地一号楼 长光华大基因'],
               ['李*亮', '新疆 乌鲁木齐市', '红光山路1966号'], ['张*硕', '北京市 朝阳区', '建国门南大街10号北京高法北门'],
               ['许*', '河北省 廊坊市', '燕郊开发区夏威夷北岸北门'], ['包*', '北京市 朝阳区', '广百西路16号院一号楼二单元602'],
               ['傅*凯', '辽宁省 沈阳市', '上园路39号（新华壹品A区5号楼）342'], ['邢*中', '北京市 海淀区', '西二旗软件园尚东数字山谷A区1号楼2层七号门'],
               ['苏*', '上海市 普陀区', '镇坪路81弄6号门207室'], ['沈*', '北京市', '昌平区回龙观北郊农场家属院5号楼4单元201'],
               ['耀*', '浙江省 杭州市', '常二路中国移动研发部'], ['郑*宾', '河南省 洛阳市', '升龙广场e区一号楼一单元2301'],
               ['彭*', '河南省 郑州市', '刘寨街道南阳路165号心语雅园5号楼2单元302'], ['王*乾', '山东省 济宁市', '新驿镇后寺村'],
               ['夏*', '浙江省 舟山市', '高亭镇大岙文明路7号301栋'], ['王*', '江苏省 常州市', '湖塘镇小庙路江南农村商业银行'], ['刘*', '河南省 许昌市', '湛北乡李庄村'],
               ['魏*浩', '浙江省 宁波市', '解放南路208号建设大厦1911室'], ['余*平', '浙江省 杭州市', '紫荆花路2号，联合大厦B座11楼'],
               ['邓*', '河南省 郑州市', '冬青街95号'], ['龚*', '湖北省 黄冈市', '漕河镇石墩路232号（30号对面）'], ['李*', '浙江省 台州市', '湫水大道金茂大厦A幢'],
               ['杨*伟', '黑龙江省 黑河市', '九三分局 南苑小区 B3 一单元  601'], ['赵*智', '北京市 西城区', '广安门内311号院内1号楼'],
               ['金*山', '北京市', '北京市东城区和平里东街11号楼航星园2号楼–车音网'], ['鲍*亮', '湖北省 武汉市', '珞狮南路196号瑞湖天地1栋2单元1602'],
               ['童*瑞', '安徽省 芜湖市', '汀塘服务中心天门山东路荷塘月色9栋二单元'], ['林*光', '浙江省 杭州市', '浙江杭州余杭区西溪北苑北区90幢402'],
               ['蔡*光', '北京市 大兴区', '大兴区芦花路1号院5号楼302室'], ['段*琪', '山西省 临汾市', '福利路尧乡小区'], ['刘*', '北京市 昌平区', '龙禧三街骊龙园601'],
               ['王*生', '上海市 杨浦区', '邯郸路复旦大学遗传学楼319室'], ['王*君', '江苏省 扬州市', '叶挺路318号建行营业部'],
               ['王*义', '北京市 东城区', '环球贸易中心D座'], ['李*', '陕西省 汉中市', '同沟寺镇晨光村二组'], ['裴*宇', '吉林省 四平市', '岭西新耀豪庭7栋'],
               ['丁*', '山东省 烟台市', '大季家镇芦洋村'], ['刘*铎', '黑龙江省 佳木斯市', '火电小区桥头浴池附近惠惠干洗店'], ['樊*', '浙江省 宁波市', '文苑风荷201-301'],
               ['陈*瑞', '安徽省 宣城市', '安徽省宣城市宣州区薰化路301合肥工业大学宣城校区'], ['崔*峰', '浙江省 台州市', '福溪街道始丰西路43号501室'],
               ['徐*', '湖北省 武汉市', '三金雄楚天地1号楼1210'], ['王*', '浙江省 宁波市', '浙江工商职业技术学院信息中心'],
               ['闫*', '上海市 浦东新区', '蓝天路368弄1号301室'], ['于*泉', '吉林省 四平市', '金星书苑小区8号楼5单元102室'],
               ['刘*萌', '河北省 秦皇岛市', '抚宁镇交通局家属院3-2-201'], ['石*', '安徽省 宣城市', '薰化路301'], ['王*雯', '甘肃省 兰州市', '天水南路222号兰州大学'],
               ['王*朝', '河南省 郑州市', '嵩山南路政通路升龙城六号院'], ['金*晶', '吉林省 延边州', '延吉市新兴街民安委11'], ['蒋*彬', '辽宁省 本溪市', '新城北岸，恒大绿洲'],
               ['牛*鑫', '黑龙江省 鸡西市', '南山路康光二号楼中雅发廊'], ['陈*宏', '山西省 太原市', '太原理工大学'], ['刘*', '山西省 运城市', '卿头镇'],
               ['陈*杰', '浙江省 宁波市', '高新区研发园A5幢7楼多维时空科技有限公司'], ['郝**', '山东省 德州市', '焦庙镇'],
               ['焦*', '山西省 长治市', '太行西街金威超市太西店金威快购办公室'], ['李*旗', '北京市 昌平区', '沙河镇汇德商厦4楼403老男孩教育'],
               ['通*大都', '北京市 丰台区', '万泉寺东路9号院1栋1单1704'], ['孙*川', '浙江省 金华市', '佛堂镇雅西村双溪口便民超市'],
               ['宋*', '安徽省 合肥市', '上派镇滨河家园9栋2102'], ['李*', '陕西省', '安康市汉滨区新城街道南环东路口桃园小区大门口'],
               ['李*连', '北京市 昌平区', '立汤路北七家威尼斯花园2区2-3'], ['籍*旭', '北京市 房山区', '良乡鸿顺园西区20号楼3单元601'],
               ['韩*嵩', '北京市 昌平区', '立汤路威尼斯花园2区2-3'], ['曹*', '北京市 朝阳区', '东三环北路28号博瑞大厦B座'],
               ['贺*', '上海市 徐汇区', '古美路1515号19号楼1101室'], ['关*轩', '山西省 长治市', '石哲镇'], ['罗*', '河北省 廊坊市', '书香苑小区四号楼'],
               ['段**', '北京市 朝阳区', '酒仙桥东路M5世纪互联'], ['杜*伟', '北京市 昌平区', '汇德商厦老男孩教育'], ['王*', '北京市 昌平区', '汇德商厦四楼'],
               ['赵*波', '上海市 闵行区', '上海市闵行区莘庄镇庙泾路水清三村52号32弄402室'], ['许*', '北京市 海淀区', '西北旺镇中海枫涟山庄北门对面中心'],
               ['李*成', '北京市 昌平区', '沙河镇于辛庄村天利合家园'], ['刘*', '江苏省 南京市', '兴智路6号兴智科技园A栋7层'],
               ['张*涛', '安徽省 合肥市', '安徽省合肥市庐阳区寿春路156号古井百花大厦大厦A座2603'], ['高*', '上海市 虹口区', '欧阳路351弄10号楼104室'],
               ['谷*成', '浙江省 杭州市', '城厢街道 下湘湖路1号'], ['王*玉', '上海市 嘉定区', '南翔镇'], ['刘*海', '北京市 海淀区', '玉渊潭南路3号水科院万方城科技楼'],
               ['杨*娟', '安徽省 合肥市', '清源路中铁国际城和畅园'], ['谢*桥', '北京市 海淀区', '丰秀中路3号院9号楼北京数码大方科技股份有限公司'],
               ['张*', '陕西省 咸阳市', '北上召秦楚汽车城别克雪佛兰4s店'], ['邵*龙', '北京市 海淀区', '西北旺镇大牛坊社区四期4号楼1单元301'],
               ['耿*涛', '北京市 朝阳区', '三间房东柳巷甲一号意菲克大厦A座'], ['孙*周', '北京市 东城区', '东花市街道便宜坊写字楼10层，恒信通大厦。就在崇文门地铁站口旁边'],
               ['于*涵', '山东省 济南市', '舜耕路舜耕山庄宿舍'], ['陈*', '上海市 普陀区', '近铁城市广场北座15楼'], ['马*', '北京市', '昌平区沙河镇松兰堡村西口兴业家园6号楼'],
               ['李*宇', '江苏省 苏州市', '工业园区苏雅路158号华盛广场3楼东北证券304室'], ['王*杰', '河北省 邯郸市', '后仓街39号'],
               ['刘*明', '河北省 唐山市', '卫国北路305张家口银行'], ['王*凡', '天津市 南开区', '卫津路92号天津大学鹏翔公寓'],
               ['郭*军', '上海市 浦东新区', '郭守敬路498号浦东软件园16号3楼'], ['宋*东', '北京市 丰台区', '万寿路南口288号华信大厦'],
               ['江*', '安徽省 阜阳市', '临海尚城B区2单元，19号楼'], ['吴*', '河南省 郑州市', '经三路与东风路交汇处金城国际广场6#东单元2403'],
               ['祁*雄', '湖北省 武汉市', '洪山区白沙洲大道武汉科技大学北苑'], ['吕*', '上海市 嘉定区', '上海市嘉定区嘉罗公路2019号'],
               ['黄*', '湖北省 武汉市', '国家光电实验室'], ['常*旗', '山东省 潍坊市', '林海生态博览园'], ['陈*', '上海市 虹口区', '吴淞路218号宝矿大厦2501A'],
               ['郑*琳', '北京市 丰台区', '西马金润家园2区10号楼11单元11-2-1'], ['姚*峰', '江苏省 无锡市', '江苏省无锡市滨湖区龙山龚巷213#'],
               ['徐*', '浙江省 杭州市', '余杭塘路515矩阵国际中心2号楼705'], ['沈*', '上海市 长宁区', '金钟路968号凌空SOHO11号楼506室'],
               ['王*', '上海市 浦东新区', '川沙路1666弄79号803'], ['徐*', '山东省 日照市', '安东卫街道汾水村'],
               ['路*领', '北京市 丰台区', '四方景园一区3号楼1006室'], ['张*巍', '河南省 开封市', '西环路北段青年城8号楼3单元302'],
               ['王*俊', '江苏省 盐城市', '新都路29号紫金大厦19楼'], ['姜*波', '北京市 朝阳区', '北京市朝阳区阜通东大街1号望京soho塔三B座17层1707'],
               ['曹*翎', '江苏省 苏州市', '科教新城太和丽都31-1604'], ['齐*', '江苏省 南京市', '天元东路228号莱茵量子国际'],
               ['高*', '山西省 太原市', '经济技术开发区龙盛街2号国药控股'], ['刘*', '北京市 海淀区', '中关村丹棱街中国电子大厦B座1608'],
               ['陈*山', '安徽省 六安市', '南港镇'], ['赵*', '黑龙江省 哈尔滨市', '锦山路5号，黑龙江省地质科学研究所'], ['伍*', '安徽省 芜湖市', '泉塘镇'],
               ['白*潮', '上海市 浦东新区', '康桥镇环桥路2585弄文怡苑一期27号楼301'], ['黄*曦', '北京市 朝阳区', '西坝河南路3号2层201室 同创双子信息技术股份有限公司'],
               ['牟*强', '山东省 日照市', '山东东路619号 广电网络公司'], ['李*运', '上海市 松江区', '沪亭南路208弄109号801室'],
               ['杨*', '北京市 朝阳区', '安苑路20号世纪兴源大厦304'], ['宋*伟', '河北省 石家庄市', '高头乡西高村'],
               ['任*鹏', '陕西省 西安市', '锦业一路29号 龙旗科技园 6层 西安和利时系统工程有限公司'],
               ['孙*洲', '北京市 东城区', '东花市街道便宜坊写字楼10层，恒信通公司。就在崇文门地铁站旁边'], ['张*义', '上海市 浦东新区', '三舒路181弄2号904'],
               ['门*意', '黑龙江省 哈尔滨市', '文昌街238号联通系统集成有限公司'], ['陈*维', '上海市 虹口区', '欧阳路196号26栋2楼'],
               ['周*涛', '浙江省 嘉兴市', '施家北路陈家浜1号'], ['吴*', '江苏省 苏州市', '工业园区星湖街328号11栋'],
               ['苏*', '河南省 郑州市', '登封路晨光社区14号院绿田野超市'], ['王*', '陕西省 西安市', '雁塔区雁翔路58号西安理工大学曲江校区'],
               ['赵*龙', '河北省 廊坊市', '燕郊经济开发区福成大酒店东福成行政中心三楼信息部'], ['范*勇', '江苏省 苏州市', '苏州市吴中区木渎镇胥口镇621号斯莱克精密设备股份有限公司'],
               ['白*', '北京市 东城区', '安定门外大街10号楼415'], ['刘*', '北京市 昌平区', '回龙观镇二拨子新村东区7号楼1单元402'],
               ['钱*庭', '江苏省', '江苏省泰州市姜堰区南苑新村58号'], ['王*', '北京市 朝阳区', '北京市朝阳区摩托罗拉大厦'], ['杨*', '北京市 朝阳区', '阜荣街10号首开广场5楼'],
               ['姬*飞', '北京市 昌平区', '宏福创业园15号创昱'], ['熊*威', '浙江省 杭州市', '万塘路252号计量大厦10楼'],
               ['薛*', '山东省 济南市', '高新区新泺大街888号福瑞达'], ['贾*凯', '上海市 浦东新区', '鹤永路751弄汇贤雅苑'],
               ['孟*震', '上海市', '宝山区淞南镇祥腾生活广场，8栋816室'], ['刘*', '河南省 洛阳市', '城关镇人民路21号'], ['杨*凯', '湖北省 武汉市', '中国地质大学北区1栋'],
               ['王*', '上海市 浦东新区', '环桥路1137弄秀怡苑31号楼302'], ['夏*', '北京市 朝阳区', '垂杨柳东里11号楼3单元402'],
               ['张*宇', '北京市 海淀区', '中关村南大街6号中电信息大厦1207'], ['蔡*', '陕西省 西安市', '凤城八路天朗御湖一号楼二单元（西门）'],
               ['高*', '新疆 乌鲁木齐市', '民主路99号建行大厦12楼审计室'], ['孙*园', '陕西省 西安市', '丈八沟街道科技五路8号数字大厦'],
               ['王*亚', '北京市 朝阳区', '华盛乐章b座1708'], ['李*博', '山东省 淄博市', '索镇花园小区5#2单元202室'],
               ['方*', '北京市 海淀区', '北洼西里33号清华同方研究院'], ['杨*东', '上海市', '闵行区梅陇镇高兴路高兴花园一街坊14号501'],
               ['袁*', '陕西省 西安市', '高新四路南窑头东区22排11号'], ['王*', '天津市 河北区', '建国道地铁站B口旁青创中心'],
               ['程*磊', '北京市 西城区', '北三环中路27号商房大厦5楼'], ['陈*琦', '安徽省 合肥市', '徽州大道与九华山路交叉口信旺九华国际2419'],
               ['刘*杰', '北京市 大兴区', '亦庄经济开发区地盛北街1号35号楼2栋北京如风达快递有限公司'], ['侯*森', '北京市 朝阳区', '北苑路潮驿178'],
               ['胡*辉', '浙江省 杭州市', '瑞立东方花城2-2-503'], ['杨*平', '北京市 昌平区', '沙河镇于辛庄村赋腾公寓'],
               ['黄*', '浙江省 杭州市', '衢江路耀江福村3单元602'], ['李*', '上海市 黄浦区', '黄浦区北京东路288弄66号甲，后门201室'],
               ['邹*', '安徽省 淮北市', '南坪镇黄沟村邹圩庄'], ['刘*', '北京市 昌平区', '沙河镇赋腾公寓E516'], ['彭*', '北京市', '望京SOHOt3  40层'],
               ['张*乾', '河南省 周口市', '八一路人民路交叉口医药局家属楼'], ['贺*梦', '北京市 通州区', '永顺镇世纪星城92号楼二单元'],
               ['冯*琴', '北京市 海淀区', '金澳国际写字楼1115  中汇'], ['邓*亮', '湖北省 武汉市', '云林街台北一路58号'],
               ['李*沙', '北京市 昌平区', '城南街道北清路珠江摩尔国际大厦五号楼二单元906'], ['徐*瑞', '上海市 徐汇区', '古美路1595号宝石园27号楼2楼D区'],
               ['梁*', '陕西省 西安市', '电子二路18号(西安石油大学)'], ['徐*', '浙江省 衢州市', '西区广电大楼'], ['雷*强', '河南省 信阳市', '汪桥镇街道滨河花园A幢6208'],
               ['张*亮', '天津市 河西区', '郁江道17号陈塘科技328'], ['陈*', '上海市 浦东新区', '东方路1217号陆家嘴金融服务广场15楼'],
               ['郭*', '北京市 昌平区', '北七家镇东三旗365号'], ['李*扬', '上海市', '浦东新区北蔡镇北艾路1500弄6号楼203'],
               ['汝*明', '吉林省 长春市', '长春光机所研究生部D栋'], ['朱*懿', '上海市 静安区', '陕西北路66号科恩国际中心1027室'],
               ['刘*', '上海市 浦东新区', '五莲路 锦河苑'], ['任*荣', '陕西省 西安市', '软件新城软件公寓'], ['王*', '上海市 闵行区', '莲花路2080弄50号C幢3楼'],
               ['崔*斌', '北京市 房山区', '阎村镇焦庄村四里'], ['王*强', '浙江省 杭州市', '物联网街451号芯图大厦17楼'],
               ['姬*玲', '黑龙江省 哈尔滨市', '长江路462号悦山国际c座1单元2501'], ['T*m', '上海市 浦东新区', '浦东大道3040弄丽江锦庭1号楼'],
               ['李*宇', '黑龙江省 绥化市', '十道街升平小区15号楼1单元102室'], ['董*', '河南省 郑州市', '崇高路与嵩山路交叉口北黄河商务酒店'],
               ['杨*辉', '江苏省 镇江市', '江苏大学F 区'], ['韩*鉴', '北京市 门头沟区', '滨河路葡东小区七号楼4层D门'],
               ['罗*若', '陕西省 西安市', '龙首北路宫园一号5号楼4单元'], ['王*', '北京市 海淀区', '上地东路盈创动力大厦e座801c源清慧虹信息科技'],
               ['马*', '湖北省 武汉市', '庙山中路10号名湖豪庭7栋1403'], ['常*峰', '山西省 太原市', '迎新街'], ['侯*', '浙江省 杭州市', '江陵路1541号'],
               ['许*娟', '上海市 宝山区', '殷高西路高境二村177号502'], ['徐*飞', '湖北省 武汉市', '潘塘街喻大村梅家大湾'],
               ['崔*腾', '辽宁省 沈阳市', '虹桥路15号富雅豪临'], ['张*俊', '新疆 巴音郭楞州', '石化大道塔指1区25栋403'],
               ['严*', '北京市 大兴区', '清源北路16号，校长大厦'], ['李*', '北京市 大兴区', '十八里店乡横街子村64号柠檬家园B113'],
               ['于*佳', '北京市 朝阳区', '郎园2号A座2层'], ['张*江', '北京市 海淀区', '海淀区上地三街9号金隅嘉华大厦Ｆ座703室'],
               ['萌*', '北京市 西城区', '金融街邮政集团公司'], ['张*宾', '河南省 郑州市', '文治路泰祥投资集团楼下新锐广告'],
               ['彭*灿', '江苏省 苏州市', '玉山镇印象欧洲17#606'], ['王*亮', '北京市 朝阳区', '双营路11号美立方4号楼4单元602'],
               ['朱*伦', '北京市 海淀区', '西三环中路19号海军大院西门顺丰快递'], ['杜*', '河北省 石家庄市', '河北科技大学新校区26号'],
               ['董*', '北京市 朝阳区', '雅宝路华声国际大厦'], ['朱*', '江苏省 镇江市', '延陵镇'], ['段*', '山东省 临沂市', '银雀山街道万阅城A座1207'],
               ['朱*', '北京市 昌平区', '北京联合大学昌平校区'], ['陈*章', '北京市 昌平区', '沙河镇白沙路汇德商厦老男孩教育'],
               ['肖*雅', '北京市 昌平区', '沙河汇德商厦4楼老男孩儿教育'], ['赵*明', '北京市 昌平区', '沙河顺沙路汇德商厦老男孩教育403'],
               ['邹*', '宁夏 银川市', '上海路福州街口云峰盛大药房'], ['袁*', '辽宁省 锦州市', '辽宁省凌海市国庆路33B号2单元23室'],
               ['陈*', '浙江省 杭州市', '昌化电站里56号骏程瓷砖店'], ['索*辉', '辽宁省 沈阳市', '浑南区创新路117号东软医疗系统有限公司'],
               ['李*', '北京市 大兴区', '天宫院地铁站熙悦春天小区'], ['张*', '陕西省 西安市', '电子城街道高新领域4号楼'], ['王*', '山西省 吕梁市', '一家庄小区三期五号楼'],
               ['钟*', '陕西省 商洛市', '商洛学院'], ['薛*', '江苏省 泰州市', '口岸街道向阳北路94号农商行'],
               ['张*强', '甘肃省 兰州市', '北滨河西路666号（中国移动甘肃分公司）'], ['姚*飞', '上海市 浦东新区', '成山路1728弄88号'],
               ['赵*宁', '浙江省 金华市', '光南路898号金华移动公司'], ['张*昌', '北京市 昌平区', '回龙观东大街 矩阵小区 11楼1单元1102室'],
               ['董*亨', '上海市 嘉定区', '曹安公路4800号同济大学嘉定校区'], ['李*根', '北京市 昌平区', '马连店4号楼2单元'], ['贾*新', '北京市 海淀区', '学院路29号'],
               ['吕*', '浙江省 舟山市', '高亭镇军民路106号'], ['张*东', '河南省 周口市', '西华县基城高中'], ['李*东', '河北省 石家庄市', '新石中路，物联网大厦10层'],
               ['韩*泰', '山东省 青岛市', '青岛农业大学西苑'], ['邵*遥', '浙江省 杭州市', '塘栖镇张家墩路65号博乐展具内'],
               ['李*泽', '河南省 郑州市', '郑东新区龙子湖高校园区郑州信息科技职业学院'], ['沈*蕾', '浙江省 杭州市', '下沙学源街中国计量大学'],
               ['冯*明', '上海市 浦东新区', '张江路华夏中路 虹御公寓'], ['海*', '浙江省 杭州市', '良渚街道大陆村邱家桥桥南3号'],
               ['刘*龙', '北京市', '通州区台湖镇次渠嘉园8区1号楼1705号'], ['王*宇', '河南省 安阳市', '红旗路天宇国际三号楼四单元'],
               ['宋*波', '北京市 海淀区', '龙翔路甲1号泰翔商务楼508'], ['周*萧', '北京市 昌平区', '回龙观镇史各庄村176号'],
               ['梁*升', '吉林省 吉林市', '承德街45号吉林化工学院'], ['陈*龙', '上海市 浦东新区', '郭守敬路498号23号楼23215'],
               ['张*', '上海市 徐汇区', '桂林路402号 诚达创意园76幢407室 银基科技'], ['何*畅', '河南省 周口市', '西华县箕城高中'],
               ['欧*', '北京市 丰台区', '东营里5号院8号楼2单元401'], ['张*', '陕西省 西安市', '陕西西安思源学院'],
               ['曹*', '浙江省 宁波市', '白沙街道新马路61弄江北区农林水利局'], ['陈*刚', '宁夏 银川市', '上海东路银佐家园东区11-1-501'],
               ['喻*明', '湖北省 武汉市', '徐东'], ['陈*余', '北京市 海淀区', '甘家口街道阜成路北二街阜光里小区7号楼二单元102'],
               ['刘*博', '山西省 太原市', '小店区平阳路42号山西省自动化研究所'], ['王*', '北京市 大兴区', '亦庄经济技术开发区大族广场T5，6层洪泰空间c033'],
               ['褚*文', '湖北省 武汉市', '明伦正街明伦生鲜市场9号'], ['乔**', '河北省 衡水市', '香榭丽都2号楼1单元 2603'],
               ['貟*杰', '上海市 宝山区', '上海市宝山区陆翔路678弄62号903'], ['甘*德', '北京市 海淀区', '四季青杏石口路甲18号航天信息园'],
               ['杨*奖', '北京市 东城区', '东单北大街1号国旅大厦502'], ['李*', '北京市 海淀区', '北京市海淀区中关村南大街9号理工科技大厦207'],
               ['刘*', '浙江省 杭州市', '紫荆花路金月巷嘉禾花苑'], ['刘*亮', '北京市', '朝阳门'], ['聂*敏', '上海市', '浦东新区高博路188弄1号楼1903室'],
               ['刘*正', '山东省 青岛市', '流亭街道洼里社区八号楼尚美美发'], ['杨*强', '陕西省 西安市', '枣园路万科金色悦城'], ['聂*', '湖北省 武汉市', '台银大厦1单位1楼'],
               ['刘*', '上海市 闵行区', '闵驰一路29弄3号1101'], ['郭*', '青海省 西宁市', '互助东路12号海亮大都汇'],
               ['芦*坤', '北京市 朝阳区', '北京工人体育场3号看台2号楼1706'], ['晋*林', '上海市 杨浦区', '隆昌路619号城市概念10号b座'],
               ['董*', '浙江省 杭州市', '丰潭路城西银泰E2幢10楼'], ['刘*', '湖北省 武汉市', '中国地质大学（北区）'],
               ['马*', '河北省 保定市', '保定市南市区朝阳南大街哈弗技术中心2076号包裹站'], ['王*超', '黑龙江省 哈尔滨市', '永泰城3号楼1单位1304'],
               ['孙*敏', '北京市 昌平区', '北京市昌平区沙河于辛庄于辛家园1号楼1单元'], ['郑*龙', '河南省 郑州市', '花园路国基路花园SOHO2栋'],
               ['李*', '北京市 昌平区', '流星花园三区11号楼4单元401室'], ['李*', '浙江省 杭州市', '金岸提香3幢1单元1303'], ['庄*峰', '北京市 海淀区', '慧科大厦'],
               ['马*', '北京市 朝阳区', '惠新东街11号紫光发展大厦A座12层'], ['朱*', '北京市 海淀区', '东升镇宝盛东路奥北科技园领智中心Ｂ座5层'],
               ['吴*峰', '湖北省 武汉市', '幸福路鸿福花园1栋3006'], ['付*诚', '北京市 海淀区', '观林园'],
               ['滕*', '江苏省 南京市', '秣周东路11号双子楼9号楼15楼君度科技'], ['石*刚', '辽宁省 大连市', '大连市经济技术开发区福泉北路20号'],
               ['程*', '北京市 昌平区', '沙河兆丰家园'], ['武*', '北京市 昌平区', '回龙观西大街龙腾苑五区16号楼1单元202'],
               ['郭*欣', '北京市 西城区', '阜成门 万通新世界 B座1503'], ['毛*', '陕西省 西安市', '高新六路万象汇B座'],
               ['龙*宇', '山东省 青岛市', '山东省青岛市市南区青岛啤酒大厦403'], ['郅*', '北京市 顺义区', '后沙峪清岚花园西区15号楼一单元502'],
               ['蔡*芝', '江苏省 南京市', '新模范马路五号南京工业大学国家科技园 A2405'], ['王*飞', '江苏省 苏州市', '工业园区雪堂街1号，善行楼17栋'],
               ['葛*光', '北京市 海淀区', '复兴路甲23号华能大厦'], ['胡*鑫', '天津市 和平区', '河南路63号'], ['陶*东', '浙江省 宁波市', '杭州湾新区滨海四路777号b-4'],
               ['王*庆', '上海市 静安区', '万荣路700号A1 SINODIS食品有限公司'], ['刘*闯', '北京市 东城区', '东中街58号美惠大厦B座2单元1层MH-Z-0005'],
               ['李*', '上海市 闵行区', '航北路228弄142号202'], ['林*春', '河南省 郑州市', '河南中医药大学龙子湖校区'],
               ['张*春', '陕西省 延安市', '李渠镇阳山村延安北铁路小区'], ['李*', '浙江省 杭州市', '文三西路52号建投大厦'], ['李*', '河南省 郑州市', '红旗路6号华图教育'],
               ['徐*麒', '河南省 洛阳市', '河南科技大学开元校区'], ['陈*', '江苏省 苏州市', '伟业迎春华府'], ['张*', '北京市', '北京亦庄经济开发区地泽北街1号朗致集团'],
               ['伍*葵', '新疆 阿克苏地区', '红旗坡十一队'], ['王*操', '上海市 浦东新区', '亮秀路72号X座6楼'], ['赵*刚', '山西省 长治市', '长治学院北校区'],
               ['高*峰', '吉林省 四平市', '永乐小区丰沃新农饲料商店'], ['田*瑞', '山东省 淄博市', '索镇中心大街惠仟佳4楼'], ['赵*龙', '北京市 朝阳区', '望京首开广场5层'],
               ['胡*', '上海市 宝山区', '陆翔路龙湖北城天街2号502'], ['刘*悦', '北京市 昌平区', '于辛庄南街家乐家园'], ['贺*旋', '北京市 昌平区', '汇德商厦403'],
               ['李*', '北京市 昌平区', '北京市昌平区顺沙路八号院二区汇德商厦四楼403     小姐姐们，真送的话，我直接去403拿可否？'],
               ['陈*', '北京市 昌平区', '昌平科技园超前路37号北京乐普科技7-1号楼5层'], ['李*', '北京市', '北京市丰台区莲怡园二区六栋405'],
               ['喻*溢', '湖北省 武汉市', '五里墩街道办事处汉阳大道642号金龙花园5-3-302'], ['孙*强', '湖北省 宜昌市', '大学路8号三峡大学'],
               ['王*军', '山东省 临沂市', '九曲街道格瑞斯小镇'], ['郭*', '天津市 西青区', '侯台碧水家园e区'], ['聂*双', '北京市 海淀区', '柳浪家园东里5号楼3单元801室'],
               ['安*', '辽宁省 沈阳市', '青山路亚都名苑3期逸林14号楼1-11-2'], ['戴*', '浙江省 杭州市', '乔司街道花漫里8幢3单元101'],
               ['米*俊', '陕西省 西安市', '太白新苑'], ['周*祺', '河南省 新乡市', '新辉路街道建设西路保温瓶厂家属院向西100米新中批发'],
               ['丁*', '山西省 运城市', '运城宾馆对面北大青鸟'], ['文*宇', '湖北省 宜昌市', '三峡大学欣苑'], ['王*', '北京市 海淀区', '北清路68号用友软件园'],
               ['张*君', '山东省 青岛市', '上清路16号甲，青岛东软载波科技股份有限公司'], ['正*', '山东省 济南市', '经十路20188号'],
               ['李*晓', '北京市 朝阳区', '国际电子城总部360发票A座收发室'], ['丁*涛', '江苏省 苏州市', '子胥路新峰工业小区11栋苏州三川'],
               ['A*yua*', '上海市 浦东新区', '华佗路1号'], ['夏*捷', '陕西省 西安市', '西安邮电大学'], ['郭*坤', '山东省 济宁市', '济宁学院男生宿舍'],
               ['杨*星', '湖北省 武汉市', '江夏大道18号梅兰山居碧水轩'], ['唐*宁', '新疆 乌鲁木齐市', '新疆省乌鲁木齐头屯河区火车西站6街'],
               ['田*', '上海市 黄浦区', '马当路388号SOHO复兴广场E栋2楼R13A'], ['覃*', '湖北省 武汉市', '南李路55号'],
               ['杨*', '北京市 朝阳区', '光华路甲8号和侨大厦B座508'], ['梁*雷', '北京市 海淀区', '王庄路1号，清华同方科技广场B2006'],
               ['李*', '湖北省 武汉市', '东湖高新南湖大道182号'], ['曹*伟', '江苏省 南京市', '安德门大街57号楚翘城1号楼4层'],
               ['郭*铠', '山西省 太原市', '南中环西街万年花城7号楼2单元401'], ['李*生', '江苏省 南京市', '江山路明发3期332栋603室'],
               ['许*辰', '河南省 郑州市', '丰产路111号河南省国家税务局8楼信息中心'], ['姚*超', '北京市 昌平区', 'TBD云集中心1号楼5层'],
               ['张*', '山东省 青岛市', '山东科技大学'], ['高*锐', '山东省 济南市', '经十路万科金域中心a座'],
               ['严*', '安徽省 合肥市', '双凤开发区阜阳北路与魏武路交叉口西南角北部湾小区'], ['李*春', '山东省 德州市', '德州职业技术学院'],
               ['张*豪', '河南省 南阳市', '河南省南阳市宛城区第七小学邮政家属院对面的楼七一搬运站'], ['康*', '北京市 朝阳区', '垡头东里百斯特大厦A663'],
               ['陈*', '江苏省 南京市', '文苑路9号南京邮电大学'], ['柴*虎', '北京市 昌平区', '北七家镇顺玮阁小区'], ['韩*', '辽宁省 葫芦岛市', '小庄子乡宝仓村'],
               ['魏*森', '北京市 昌平区', '于辛庄路，赋腾国创中心，2楼'], ['邓*明', '北京市', '丰台区新华街三里1号楼305'],
               ['赵*', '上海市 宝山区', '宝山区高境镇高境一村11号后3号车库'], ['徐*亮', '北京市 海淀区', '花园东路11号泰兴大厦302'],
               ['张*凡', '北京市 昌平区', '沙河镇松兰堡迎客家园507'], ['赵*', '北京市', '北京市海淀区农大国际创业园b区6065'],
               ['顾*天', '北京市 海淀区', '上地东路1号华控大厦'], ['丁*', '上海市 杨浦区', '安波路533弄硕和商务2号楼1102'],
               ['封*号', '江苏省 苏州市', '陆家镇陆丰东路199号水岸香堤2#2309'], ['王*哲', '上海市 静安区', '曲沃路430弄15号401'],
               ['刘**', '湖北省 武汉市', '左岭镇 武汉华星光电一号门'], ['付*', '安徽省 合肥市', '长江西路305号电信新技术楼'],
               ['鲁*', '湖北省 武汉市', '武大科技园宏业楼C座'], ['张*', '北京市 朝阳区', '小营路13号亚非大厦7层8704室'], ['齐*', '湖北省 武汉市', '珞喻路马家庄'],
               ['王*', '北京市 海淀区', '北坞嘉园北里9号楼三单元D01'], ['陈*龙', '北京市 朝阳区', '北卫新园'], ['曹*生', '江苏省 无锡市', '澄南花苑'],
               ['沈*', '北京市 海淀区', '中关村南大街甲18号北京国际大厦D座7层'], ['续*', '山西省 晋中市', '中都广场12层畅快车贷'],
               ['赵*全', '河北省 唐山市', '李钊庄镇大王庄村'], ['成*', '上海市 虹口区', '东五小区641号楼2007'],
               ['方*', '上海市 闵行区', '联航路1399弄28号1103室'], ['曹*', '上海市 浦东新区', '向城路15号24C'],
               ['韩*德', '北京市 大兴区', '枣园北里小区1号楼8单元202'], ['金*鹏', '浙江省 温州市', '温州职业技术学院生活区快递中心'],
               ['陶*明', '浙江省 嘉兴市', '南溪路桂苑小区23幢603'], ['李*ir', '北京市 丰台区', '南苑乡 德鑫家园9号楼5单元50'],
               ['姜*杰', '山东省 临沂市', '凤凰岭大街惠民早餐'], ['l*xq', '辽宁省 沈阳市', '卫工南街4-4网点2门瀚辰跆拳道'],
               ['赵*', '河北省 邯郸市', '幸福街于联防路交叉口北行幸福馨苑'], ['张*锋', '内蒙古 呼和浩特市', '双河镇莹昱佳苑商铺A段13号（防汛东巷莲爱粮油副食门市）'],
               ['胡*', '北京市 西城区', '鸭子桥路24号'], ['王*鲲', '北京市 延庆区', '东外小区15号楼一单元101'], ['马*闻', '陕西省 西安市', '西安邮电大学东门'],
               ['许*', '安徽省 合肥市', '宿松路紫竹苑B区2栋2单元602室'], ['范*', '浙江省 金华市', '金华职业技术学院'], ['马*铎', '山西省 太原市', '徐沟镇山西警察学院'],
               ['武*文', '上海市 浦东新区', '浦东新区盛夏路738弄樟盛苑32号楼一楼'], ['陈*', '江苏省 徐州市', '苏堤北小区四号楼三单元702室'],
               ['曹*政', '辽宁省 大连市', '大连理工大学软件学院'], ['张*超', '山东省 济南市', '八一立交桥西南角联通公司3号楼'],
               ['唐*生', '山东省 济南市', '工业南路鑫苑国际城市花园'], ['严*鹏', '上海市 杨浦区', '五角场街道 国定路277弄铁村小区13号601'],
               ['张**', '甘肃省 兰州市', '甘肃省兰州市七里河区兰公坪兰州理工大学校本部'], ['麻*肖', '安徽省 宿州市', '香格里拉108幢'],
               ['刘*仪', '河北省 廊坊市', '燕郊经济开发区 华北科技学院'], ['刘*龙', '河南省 洛阳市', '新一中文印室'], ['李*', '陕西省', '西安市临潼区西安科技大学'],
               ['相**', '北京市 昌平区', '天通公园里'], ['康*熙', '山西省 忻州市', '万人商厦对面联想专卖店'], ['张*栋', '山东省 泰安市', '安驾庄镇上前'],
               ['陶*', '安徽省 宣城市', '鳌峰东路180号宣城皖南农商银行413室'], ['艾*麦提江·拜克热', '浙江省 杭州市', '浦沿街道江畔云卢4幢2单元1202'],
               ['王*', '上海市 浦东新区', '福山路455号，全华信息大厦，1楼，平安银行'], ['刘*林', '湖北省 宜昌市', '枝城镇大堰村四组'],
               ['罗*', '河南省 信阳市', '西关黄国新城C6'], ['莫*', '河南省 郑州市', '金水区76号9202'], ['徐*龙', '安徽省 合肥市', '长江西路新加坡花园城4联排'],
               ['杨*杰', '山西省 忻州市', '京原南路雷神网咖'], ['朱*北', '海南省 海口市', '和平北路三亚上二街9号'], ['朱*', '浙江省 杭州市', '龙湖春江郦城'],
               ['常*磊', '北京市', '海淀区学院南路59号'], ['王*阳', '江苏省 南京市', '南京江宁21世纪现代城'], ['谢*星', '甘肃省 酒泉市', '雄关路54号东风物流十号'],
               ['侯*', '河南省 郑州市', '河南省郑州市高新区莲花街牡丹路西雅图荣邦城'], ['孙*康', '江苏省 南京市', '化工园方水东路9号'],
               ['索*华', '北京市 昌平区', '北七家镇东三旗村委会'], ['王*', '陕西省 西安市', '十里铺街长力小区北门对面（王家辣子面）'],
               ['姜*生', '北京市 朝阳区', '东大桥宫宵国际1103'], ['顾*生', '安徽省 阜阳市', '清河西路100号阜阳师范学院'],
               ['申*伟', '上海市 青浦区', '巷佳华苑三期10号楼904室'], ['刘*', '湖北省 武汉市', '左岭新城1社区15栋'], ['单*成', '山东省 日照市', '日照职业技术学院'],
               ['马**', '北京市 丰台区', '德鑫家园9单元502'], ['郑*勇', '山东省 威海市', '顺河街214号'], ['程*', '黑龙江省 佳木斯市', '桦南县第一中学'],
               ['刘*', '北京市 东城区', '永定门外西革新里百荣嘉园3号楼3单元505室'], ['朱*苇', '浙江省 嘉兴市', '京润大厦1718室'],
               ['王*', '北京市 西城区', '百万庄北街6号经易大厦'], ['杜*杰', '河南省 新乡市', '和平大道与南环路交叉口紫锦国际9楼'],
               ['孙*武', '江苏省 苏州市', '唯华路3号君地中心5号楼2单元2013室'], ['杨*', '陕西省 西安市', '高新六路立人科技园'],
               ['夏*', '湖北省 武汉市', '珞狮路122号武汉理工大学马房山校区西院图书馆5楼'], ['张*', '江苏省 苏州市', '科技城昆仑山路58号中移软件园'],
               ['芦*雄', '山西省 太原市', '北张小区11号楼3单元502'], ['张*源', '江苏省 南京市', '丹阳大道东吉大厦C座6楼'],
               ['戴*宇', '江苏省', '南京栖霞区南京工业职业技术学院'], ['陈*俊', '湖北省', '武汉市洪山区民族大道龙安港汇城a栋615'],
               ['张*', '北京市 昌平区', '霍营龙锦苑东四区1号楼3单元302'], ['柯*安', '北京市 海淀区', '北京市海淀区上地信息基地中黎科技园1号楼6层'],
               ['韩*', '湖北省 武汉市', '汉阳四新北路鲤鱼洲家园30栋'], ['金*强', '浙江省 金华市', '兴平东路58号后门'],
               ['1*610794772', '北京市 朝阳区', '物美超市六层达内科技'], ['韦*兵', '江苏省', '苏州工业园区文荟人才公寓'],
               ['白*飞', '河北省 石家庄市', '博雅盛世A区2号楼2单元1703'], ['贾*', '北京市 海淀区', '北四环西路56号辉煌时代大厦9层'],
               ['应*平', '浙江省 杭州市', '梦想小镇仓新街，VR眼见中心 35栋103'], ['陈*', '海南省 三亚市', '解放四路友谊路口阳光翠园'],
               ['方*琼', '浙江省 宁波市', '假山新村11幢48号'], ['杨*永', '河南省 焦作市', '河南理工大学'], ['郑*龙', '安徽省 淮北市', '人民中路淮北市广电中心'],
               ['吴*江', '北京市 昌平区', '回龙观，新龙城23号楼2单元503室'], ['随*亮', '安徽省', '安徽省亳州市蒙城县双涧镇随寨村万庄'],
               ['徐*', '浙江省 衢州市', '东城欣苑12幢'], ['田*阳', '湖北省 武汉市', '青合居天天鲜果店收'], ['刘*', '山东省 青岛市', '港澳新城53号  702'],
               ['许*', '上海市 普陀区', '双山路167弄4号2005室'], ['张*飞', '浙江省 嘉兴市', '富民路106号'],
               ['刘*浩', '上海市 浦东新区', '金海路2360上海第二工业大学'], ['赵*峰', '山西省 太原市', '北营街道太原二中家属楼'],
               ['崔*超', '北京市 海淀区', '上地五街方正大厦副楼四层'], ['许*龙', '北京市', '朝阳区电通创意广场3A'], ['王**', '山东省 济南市', '高新区明湖白鹭郡6号楼803'],
               ['张*恒', '北京市 朝阳区', '惠新西街南口小关东里10号院核工业北京地址研究院南门'], ['卢*飞', '浙江省 杭州市', '东信大道66号东方通信科技园B座'],
               ['黄*祥', '山东省 济南市', '美里湖街道 美里路邹庄新村'], ['钱*旭', '山东省 济南市', '市中区济南大学'],
               ['王*瑞', '山西省 太原市', '高新区 产业路 新岛科技园A座502'], ['伍*愿', '北京市 朝阳区', '鹏润大厦A座30层'], ['何*艳', '湖北省 荆州市', '长江大学西校区'],
               ['霍*', '北京市 朝阳区', '朝阳北路11号首开东都汇B座402室'], ['吴*祖', '浙江省 宁波市', '和邦大厦  A座1509'],
               ['孟*', '浙江省 湖州市', '湖州市红丰西路2198号'], ['朱*生', '浙江省 杭州市', '祥符街道中国智慧信息产业园N幢8楼'],
               ['李*生', '浙江省 杭州市', '古塘路30-4 一单元501'], ['王*', '陕西省 西安市', '御笔华府小区4号楼1单元2308'],
               ['陈*俊', '北京市 海淀区', '花园东路高德大厦3层311'], ['戢*', '北京市 通州区', '运河明珠家园2号楼6单元6161'],
               ['马*', '北京市 朝阳区', '北辰汇欣大厦A座706'], ['邓*', '北京市 昌平区', '霍营华龙苑南里小区36栋8单元402'],
               ['史*鑫', '北京市 朝阳区', '酒仙桥路甲12号电子城科技大厦2层'], ['随*亮', '上海市 杨浦区', '上海理工大学'],
               ['韩*兵', '上海市 普陀区', '祁安路368弄16号301'], ['张*', '浙江省 杭州市', '文一西路522号3幢2单元1楼'],
               ['王*', '安徽省 合肥市', '安徽省合肥市庐阳区春梅路与青松路交叉口东150米万科森林公园御庭3栋2801室'], ['李*熊', '北京市 海淀区', '花园北路，中鑫嘉园二期丰巢'],
               ['梁*龙', '北京市 海淀区', '紫竹桥广源大厦5118室'], ['郭*彦', '河北省 保定市', '裕华路金街a座529'], ['王*健', '北京市 朝阳区', '北京像素北区1号楼632'],
               ['孙*峰', '安徽省 马鞍山市', '西塘路488移动公司'], ['侯*茹', '北京市 东城区', '北京市东城区金城建国5号三层链家地产'],
               ['郑*坤', '北京市 海淀区', '北京市海淀区阜成路6号院海军总医院'], ['刘*超', '天津市 南开区', '芥园西道大园新居21-2007'],
               ['蒋*宇', '宁夏 银川市', '实诚小区11号楼'], ['耿*宏', '山西省 晋中市', '平遥县古陶镇北城村兴德南路东七排59号'],
               ['朱*', '北京市 昌平区', '回龙观新村东区1号楼'], ['刘*莹', '湖北省 武汉市', '流芳大道武汉工程大学流芳校区泰塑公寓'], ['王*阳', '内蒙古 包头市', '北方医院'],
               ['周*军', '安徽省 芜湖市', '伟星时代金融中心j'], ['王*', '湖北省 武汉市', '武汉大学工学部6教'], ['詹*胜', '北京市 丰台区', '花家地30号楼蒙'],
               ['刘*', '北京市 昌平区', '沙河高教园'], ['刘*粮', '北京市 海淀区', '北京市海淀区北京师范大学'], ['詹*龙', '北京市 海淀区', '温泉镇福溪家园'],
               ['李*达', '湖北省 武汉市', '关山大道590号中建康城东区14栋'], ['李*旺', '浙江省 杭州市', '学院路28号德力西大厦3号楼3楼'],
               ['宋*鹏', '浙江省 杭州市', '西溪新座6栋A座3层'], ['杨*鹰', '北京市 海淀区', '方正国际大厦19层'],
               ['司*', '北京市 门头沟区', '北京市门头沟区潭柘寺镇潭柘新区8号院'], ['刘*', '北京市 东城区', '和平里东街11号院4号楼'],
               ['周*伟', '浙江省 杭州市', '笕桥镇同心一区34号'], ['杨*', '江苏省 淮安市', '淮阴工学院'], ['张*', '湖北省 武汉市', '关东园五路荷叶山社区1103'],
               ['张*生', '河北省 廊坊市', '和平路送酒郎'], ['周*', '河南省', '郑州市高新区玉兰街升龙又一城f区'], ['朱*杰', '北京市 朝阳区', '三元桥中电发展大厦A座12层'],
               ['冯*明', '北京市 朝阳区', '定福庄北街瑞和国际6号楼1304'], ['崔*', '天津市 南开区', '华苑产业园区海泰信息广场'],
               ['王*', '天津市 西青区', '华天道海泰信息广场G座506'], ['段*鹏', '天津市 南开区', '海泰信息广场G座506'],
               ['冯*猛', '北京市 朝阳区', '安苑路20号  世纪兴源大厦304'], ['杨*', '江苏省 无锡市', '大成巷8号明珠广场19楼1901室'],
               ['张**', '安徽省 亳州市', '芍花小区'], ['岳*', '北京市 海淀区', '西直门北大街首钢国际A座'], ['李*', '北京市 西城区', '新凤街 天成科技大厦 A座 1006'],
               ['徐*林', '河北省 石家庄市', '大河镇 学府路169号 石家庄工程职业学院'], ['魏*鹏', '宁夏 银川市', '丽景北街康顺家园12号楼702'],
               ['张*', '江苏省 南京市', '花神大道23号10栋1018'], ['何*兵', '江苏省 常州市', '湖塘镇阳湖世纪苑北苑42栋甲单元401'],
               ['王*伟', '上海市 静安区', '延平路121号3楼'], ['周*', '北京市 海淀区', '清河永泰园甲1号401收'], ['韩*', '北京市 朝阳区', '华威西里51号楼1906'],
               ['王*鹏', '河南省 郑州市', '文化路97号郑州大学北校区'], ['曾*旭', '内蒙古 呼伦贝尔市', '呼伦贝尔日报社'], ['王*', '安徽省 阜阳市', '颍上协和医院门诊二楼信息科'],
               ['庞*', '山东省 济南市', '唐冶街道幸福城南门丰巢'], ['a*ex', '北京市 朝阳区', '林萃西里43号楼7楼'], ['丁*江', '浙江省 杭州市', '庆春东路3号'],
               ['常*', '安徽省 淮南市', '田集街道供电局小区'], ['邱*海', '辽宁省 沈阳市', '东北大学浑南校区'], ['李*锋', '江苏省 南京市', '未来小镇2号楼'],
               ['张*', '山东省 枣庄市', '民生路嘉汇大厦7-c-16'], ['舒*士', '北京市', '朝阳区大望路温特莱中心A18'],
               ['王*诚', '北京市 海淀区', '丹棱街18号创富大厦902室'], ['常*鸿', '北京市 朝阳区', '大望路温特莱A座11层'], ['闫*聪', '湖北省 武汉市', '民族大道东林外庐'],
               ['薛*', '河南省 郑州市', '莲花街与红松路交叉口天迈科技'], ['陈*', '天津市', '南开区华苑海泰信息广场G506'],
               ['曹*庆', '湖北省 武汉市', '光谷坐标城D19 1单元 401'], ['白*好', '新疆 乌鲁木齐市', '新市区杭州东路四季风情园北区40-7-401'],
               ['潘*', '天津市 南开区', '海泰信息广场G座506'], ['徐*', '湖北省 武汉市', '佛祖岭街道 关南工业园 t4栋'], ['姜*', '上海市 青浦区', '徐泾镇明珠路1018号'],
               ['王*', '甘肃省 兰州市', '庆阳路348号世纪广场A座2007室'], ['金*洋', '北京市', '朝阳区金泽家园315号楼4单元'],
               ['高*', '北京市 海淀区', '北清路68号用友软件园'], ['曹*衡', '上海市 闵行区', '莘朱路879弄127号502'], ['李*', '河南省 郑州市', '花园路兰德中心1902'],
               ['王*强', '北京市', '北京朝阳区清河营中街2号华贸城8号院5号楼2单元1503'], ['肖*', '上海市 浦东新区', '上海浦东新区川沙南桥459弄桃园公寓19号楼502室'],
               ['韩*红', '上海市 杨浦区', '隆昌路619号10号楼二楼'], ['魏*琪', '北京市 丰台区', '汉威国际广场4区12号楼'],
               ['杨*康', '北京市 丰台区', '丰台科技园汉威广场12栋'], ['钱*超', '北京市 海淀区', '万泉庄路15号创新大厦5层'],
               ['孙**', '江苏省 徐州市', '广场小区2号楼3单元601室'], ['王*斌', '北京市 朝阳区', '单店西路坝鑫家园5号楼4单元803'],
               ['宋*', '山东省 烟台市', '东海旅游度假区海泰居小区'], ['李*下', '河南省 驻马店市', '黄淮学院中区'], ['王**', '天津市 红桥区', '本溪路凤城楼9门503'],
               ['谷*华', '江苏省 南京市', '新城总部大厦21楼'], ['王*良', '河北省 唐山市', '唐山湾生态城渤海大道21号'],
               ['乔*', '河北省 石家庄市', '建设南大街150号国富华庭6号商务公寓1-808、809室'], ['贾*棋', '浙江省 舟山市', '临城新区长峙岛海大南路一号浙江海洋大学'],
               ['李*强', '上海市 浦东新区', '张江高科松涛路647号3号楼2楼'], ['张*', '北京市 海淀区', '中关村大街59号（中国人民大学）理工配楼103B'],
               ['党*', '陕西省 西安市', '曲江圣卡纳1130'], ['陈*', '河北省 保定市', '河北金融学院'], ['董*佩', '山东省 济南市', '齐鲁云商大厦1308'],
               ['石*', '湖北省 黄冈市', '黄冈经济开发区新港二路148号黄冈师范学院南区'], ['贾*霖', '北京市 昌平区', '马池口镇北京吉利大学俊园八号'],
               ['罗*发', '辽宁省 大连市', '大连理工大学软件学院五舍'], ['叶*', '江苏省 南京市', '软件大道50号中兴通讯2区8号楼'],
               ['夏*', '北京市 朝阳区', '朝外大街乙6号 朝外soho D座 0757'], ['朱*', '湖北省 武汉市', '湖北工业大学'], ['涂*', '湖北省 武汉市', '南李路湖北工业大学'],
               ['郭*威', '河南省 漯河市', '医专东门'], ['刘*双', '北京市 海淀区', '神州科技园b座尚学堂2层'], ['丁*冬', '北京市 朝阳区', '光华路9号SOHO二期D座805'],
               ['梁*巧', '河南省 郑州市', '郑州市高新区合欢街新芒果春天南门金梧桐超市附近一号楼'], ['张*厚', '辽宁省 抚顺市', '光明街光明垣小区7号楼2单元'],
               ['陈*胜', '天津市 津南区', '海河教育园区 天津轻工职业技术学院'], ['韩*生', '山西省 长治市', '柏后新区经济适用房小区16号楼'],
               ['郝*锋', '山西省 晋城市', '太原科技大学晋城校区'], ['乔*', '辽宁省 大连市', '大连理工大学开发区校区'],
               ['钟*洋', '山东省 潍坊市', '经济开发区古亭街199号古亭街友谊路交叉口东北角 山东联合阀门集团股份有限公司'], ['吕*军', '北京市 海淀区', '致真大厦c座'],
               ['吕*蓬', '山东省 威海市', '高区火炬路196号庆威大厦东敏捷大楼A栋308'], ['张*', '北京市 丰台区', '木樨园桥西 西罗园南里小区4号楼4单元303'],
               ['周*成', '浙江省 杭州市', '城厢街道休博园三区奥兰多小镇蔬菜水果店'], ['张*东', '上海市 杨浦区', '周家嘴路白洋淀绿苑30号502'],
               ['卢*委', '北京市 朝阳区', '东四环百子湾路大成国际中心A2-1708'], ['钱*宇', '江苏省 无锡市', '安镇街道开普动力有限公司'],
               ['方*韩', '湖北省 黄冈市', '湖北省黄冈市英山县罗非鱼小区'], ['郭*', '陕西省 西安市', '旺座现代城e座2301'],
               ['王*', '北京市 房山区', '长阳镇 书院南街旭辉E天地12号院3号楼A大堂'], ['王*鑫', '北京市 海淀区', '万寿路街道翠微路二号院12号楼五门501'],
               ['马*', '北京市 朝阳区', '阜荣街10号首开广场智联招聘'], ['刘*', '上海市 长宁区', '天山西路450弄48号201（新泾七村）'],
               ['裴*森', '北京市', '北京市丰台区诺德中心11号楼2611'], ['杨*文', '江苏省 南京市', '浦珠南路30号南京工业大学亚青服务柜'],
               ['刘*飞', '北京市 大兴区', '顺益街6号宝隆世纪3楼'], ['孙*高', '上海市 宝山区', '同济支路199号智慧七立方3楼3层'],
               ['潘*涛', '陕西省', '西安市雁塔区高新四路西京医院高新区干部住房'], ['郑*君', '黑龙江省 哈尔滨市', '船舶大厦西区1009A'],
               ['施*', '北京市 昌平区', '东小口镇公园悦府7号楼4单元e栈'], ['朱*喱', '上海市 宝山区', '呼兰路智力产业园4号楼'],
               ['宋*敏', '天津市 河西区', '友谊路58号(新业广场对过)天津津好医院8楼'], ['夏*', '河南省 郑州市', '郑州市科学大道169号  世界工厂网'],
               ['金*姐', '上海市 宝山区', '水产西路859弄24号1101室'], ['张*', '河南省 郑州市', '江山路于庄路西16栋'],
               ['陶*宇', '浙江省 宁波市', '杭州湾新区海南村103号'], ['孔*祯', '山东省 泰安市', '岱庙街道山东科技大学东校区'], ['程*', '湖北省 武汉市', '汪集街孔埠程山村'],
               ['王*超', '北京市 朝阳区', '恒通商务园B4楼301中国网地产'], ['刘*', '河南省 郑州市', '升龙城8号院'],
               ['邢*翔', '河北省 石家庄市', '建民街10号 二单元301'], ['张*', '上海市 闸北区', '万荣路1050弄21栋1301室'],
               ['郑*中', '北京市 朝阳区', '望京东园四区7号楼绿地中心B座9层'], ['张*', '上海市 黄浦区', '北京东路668号G区6楼'],
               ['李*', '北京市 大兴区', '长子营镇李家务村'], ['王*存', '北京市 朝阳区', '北苑路媒体村天畅园4号楼1层卓越游戏'],
               ['朱**', '上海市 闵行区', '浦江镇三达支路537弄38号'], ['王*刚', '北京市 朝阳区', '西坝河英特公寓c2座1503'],
               ['李*', '海南省 三亚市', '吉阳镇育才一号琼州学院'], ['谭*毅', '湖北省 武汉市', '湖北省武昌区白沙洲街道丰收小区8栋2单元504门'],
               ['何*强', '山西省 晋城市', '泽州县金村镇府城村陵沁线666号'], ['许*波', '浙江省 嘉兴市', '许村镇永福村6组52号'],
               ['罗*', '北京市 朝阳区', '南磨房百子湾西里中水电小区431-2-701'], ['马*涛', '北京市 朝阳区', '三元西桥东枫曙光中心3层'],
               ['马*', '北京市 海淀区', '北京市海淀区上地东路5号京蒙高科3层'], ['徐*龙', '浙江省 杭州市', '滨文路66号中国移动'], ['李*强', '江苏省 南京市', '浦珠南路30号'],
               ['杨*波', '北京市 通州区', '经济技术开发区经海三路109号院天骥智谷37号楼'], ['张*', '江苏省 南京市', '江浦街道浦珠南路30号南工大江浦校区亚青丰巢自助服务区'],
               ['白*南', '北京市 海淀区', '北京市海淀区北三环西路43号中航广场A2号楼7层'], ['曹*普', '北京市 朝阳区', '麦子店街道霄云中心A座22层'],
               ['学*成', '北京市 密云区', '花园小区52号楼2单元402'], ['张*环', '北京市 海淀区', '西北旺甲1号百望山庄'], ['徐*涛', '湖北省 黄石市', '太子镇商贸街'],
               ['王*', '北京市 朝阳区', '太阳国际公馆A1-305'], ['杨*东', '河北省 石家庄市', '中华北大街19号'],
               ['蔡*博', '北京市 海淀区', '昆明湖南路52号1号院中烟追溯(北京)科技有限公司'], ['柴*', '浙江省 宁波市', '钱湖南路8号（浙江万里学院）'],
               ['王*', '黑龙江省 鸡西市', '永信小区6号楼2单元101室'], ['赵*', '上海市 黄浦区', '龙华东路647中电科技大厦'],
               ['怀*涛', '北京市 西城区', '西单北大街甲133 中国联通'], ['薛*', '北京市 海淀区', '双榆树北路甲4号楼206'],
               ['孟**', '安徽省', '合肥市蜀山区西湖国际广场A座1103'], ['李*江', '北京市 昌平区', '北京市昌平区马连店家园8号楼一单元2503'],
               ['姜*龙', '北京市 石景山区', '古城现代嘉园68号院3号楼2单元1201'], ['周*', '北京市 东城区', '安定门外大街丁88号江苏大厦8号楼1层医保专委会'],
               ['邓*友', '河北省 廊坊市', '燕郊镇维多利亚D座23层'], ['胡**', '北京市 昌平区', '汇德商厦'],
               ['白**', '浙江省 杭州市', '长河街道白马湖小区孔雀苑29栋1002'], ['李*飞', '北京市 海淀区', '西北旺东路10号院中关村软件园二期E13号楼广联达信息大厦'],
               ['张*科', '浙江省 杭州市', '经济开发区钱江农场13栋3单元202（菜市场后）'], ['陈*', '内蒙古 包头市', '内蒙古科技大学'],
               ['贾*华', '浙江省 杭州市', '金隅田员外17幢901'], ['邹*泺', '湖北省 宜昌市', '东湖三巷13号'],
               ['王*', '上海市 嘉定区', '南翔镇德园南路485弄泰翔嘉苑24号304室'], ['胡*通', '河南省 郑州市', '农业路天明路怡丰新都会8号楼1单元1825'],
               ['许*', '河南省 郑州市', '商城路29号硝滩街海尔售后东，商城建筑安装公司'], ['水*恒', '辽宁省 抚顺市', '滨河路东段一号沈阳工学院'],
               ['程*', '江苏省 无锡市', '滨湖区太湖西大道2188号200室'], ['何*勇', '北京市 昌平区', '沙河汇德商厦403'],
               ['袁**', '北京市 大兴区', '福苑小区，甲6号楼，四单元302'], ['王*', '江苏省 无锡市', '滨湖区仙河苑二期'], ['马*瑞', '天津市 南开区', '金平路3号'],
               ['陈*斐', '山东省 青岛市', '山东省青岛省城阳区明阳路乙安泰居'], ['商*泽', '辽宁省 锦州市', '站前街道中央大街三段52号'],
               ['刘*祥', '浙江省 杭州市', '仓前街道文一西路969号2号邮局'], ['王*', '内蒙古 呼和浩特市', '金桥开发区闻都新苑3号楼4单元401'],
               ['姚*', '内蒙古 呼和浩特市', '蒙鑫国际一号楼四单元'], ['王*海', '山东省 潍坊市', '实验中学高中部北校区'],
               ['杨*', '江苏省 南京市', '软件大道180号大数据产业基地8幢'], ['杨*杰', '天津市 津南区', '天津中德应用技术大学'],
               ['王*', '北京市 海淀区', '海淀北一街2号爱奇艺创新大厦'], ['华*龙', '江苏省 苏州市', '万科魅力花园6-506'],
               ['周*', '浙江省 杭州市', '湖墅南路大塘新村5-3-302'], ['孙*', '浙江省 宁波市', '软件研发B2幢504室'], ['蔡*民', '陕西省 汉中市', '劳动西路石门家属院'],
               ['刘*辉', '河南省 郑州市', '未来路71号未来花园H座1604室'], ['冬*', '上海市 普陀区', '宜川二村104号103室'],
               ['高*', '安徽省 合肥市', '庐州大道与祁门路交口大摩华尔街生活广场4＃1613'], ['原*雄', '北京市 昌平区', '商业街70号'],
               ['焦*波', '河南省 郑州市', '工业示范区朝阳路8号巩义市滤料工业有限公司'], ['戚*正', '安徽省 淮南市', '洞山中路34号电信大楼'],
               ['游*兵', '北京市 海淀区', '北京市海淀区宝盛南路1号院奥北科技园领智中心A座'], ['陈*豪', '浙江省 宁波市', '蝶缘路768号锦悦湾花苑'],
               ['刘*', '浙江省 杭州市', '高科技企业孵化器2幢9楼'], ['许*', '江苏省 南通市', '万寿南路人才公寓'], ['刘*瀚', '辽宁省 沈阳市', '重工街南十西路55号183'],
               ['王*', '北京市 昌平区', '文华西路育荣教育园区'], ['霍*松', '河南省 郑州市', '郑东新区郑州工商学院'], ['沙*', '北京市 西城区', '诚实胡同1号，新华社北京分社'],
               ['袁*飞', '北京市', '朝阳区东三环环球金融中心东塔1510'], ['陈*升', '北京市 昌平区', '史各庄东半壁店村委会门口'],
               ['蔡*银', '北京市 海淀区', '车公庄西路华通大厦B座南塔12楼多汇电子商务有限公司'], ['闻*', '河北省 保定市', '莲池区水晶国际908早稻田教育'],
               ['胡*', '浙江省 杭州市', '留下镇西溪君逸汇'], ['贾*博', '江苏省 扬州市', '南京邮电大学通达学院'], ['高*亭', '新疆 五家渠市', '梧桐东街幸福小区'],
               ['于*洋', '北京市 怀柔区', '莲馨苑3号楼五单元601'], ['鲁*俊', '新疆 伊犁哈萨克自治州', '酒厂拓海乐小区兴旺商店'],
               ['顾*勃', '上海市', '闵行区吴泾镇都会路368号交大其灵自如寓'], ['孙*航', '河南省 洛阳市', '吉庆路玉泉街洛阳师范学院'],
               ['张*', '江苏省 南京市', '栖霞区康桥圣菲3栋北户208'], ['周**', '江苏省 常州市', '常州信息职业技术学院'],
               ['王*凯', '上海市 徐汇区', '柳州路928号百丽国际广场22楼'], ['单*华', '山东省 济南市', '乐梦公馆四号楼1914'],
               ['陈*', '北京市 朝阳区', '傲城融富中心a座1804'], ['王*豪', '江苏省 盐城市', '盐城工业职业技术学院'], ['王*康', '上海市 长宁区', '哈密路398弄2号301'],
               ['刘*', '上海市 松江区', '思贤路3255号正泰生活区'], ['吴*', '浙江省 杭州市', '临江花园29幢2单元'], ['测*', '河北省', '来来来来'],
               ['娜*', '北京市 昌平区', '沙河赋腾玻璃A座'], ['史*文', '上海市 虹口区', '计算机等级简单']]

# 方法一：特殊的省市会有问题
# result = {}
# for item in addres_data:
#     provice = item[1][0:3]
#     if provice in result:
#         result[provice].append(item)
#     else:
#         result[provice] = [item,]
# print(result)

"""
方法二思路：
    数据源为嵌套列表
    结果为字典样式，key为省份，value为嵌套列表
    取前三字符判断是否可行，特殊区域特殊处理
"""

results = {}
others = ['新疆', '宁夏']
for info in addres_data:
    province = info[1][:3]
    if info[1][:2] in others:
        province = info[1][:2]
    if province in results:
        results[province].append(info)
    else:
        results[province] = [info]
print('{')
for province in results:
    print(f"\t'{province}':[")
    for value in results[province]:
        print(f"\t\t{value},")
    print(f"\t],")
print('}')
