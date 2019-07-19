import requests
import re
import urllib.request
import urllib.error
#from bs4 import BeautifulSoup
import time
import socket
import googlemaps
gmaps = googlemaps.Client(key = '....') # my key hidden for this public file on GitHub

#for TA: the station_coord I have got after running with GoogleMapAPI is as follows:
#station_coord = {'丰台科技园': [39.82532399999999, 116.296991], '北苑路北': [40.030392, 116.418126], '北新桥': [39.940809, 116.416884], '王府井': [39.90807600000001, 116.41148], '旧宫': [39.806461, 116.459358], '苏州街': [39.9753686, 116.3069314], '景泰': [39.90419989999999, 116.4073963], '西四': [39.924206, 116.373332], '清源路': [39.745129, 116.332359], '方庄': [39.865593, 116.421661], '上地': [40.03298100000001, 116.320205], '亦庄桥': [39.802961, 116.480346], '牡丹园': [39.976336, 116.369938], '慈寿寺': [39.9340783, 116.2954452], '六里桥': [39.8853024, 116.3116869], '安河桥北': [40.012148, 116.26997], '鼓楼大街': [39.948972, 116.393776], '小红门': [39.828041, 116.459195], '苹果园': [39.926261, 116.177864], '大葆台': [39.80751009999999, 116.2909474], '和平里北街': [39.958718, 116.418506], '霍营': [40.073837, 116.362564], '广渠门内': [39.897367, 116.444923], '天宫院': [39.668657, 116.319927], '化工': [39.8881855, 116.5031498], '圆明园': [39.99951, 116.30965], '龙泽': [40.070887, 116.319303], '沙河': [40.148307, 116.288739], '枣园': [39.752716, 116.332237], '长阳': [39.763827, 116.212421], '南邵': [40.207729, 116.286174], '永泰庄': [40.0394108, 116.3651032], '国展': [40.072609, 116.556282], '宋家庄': [39.845851, 116.428395], '大井': [39.83583, 116.25187], '呼家楼': [39.9220119, 116.4610196], '阜成门': [39.92350100000001, 116.356012], '立水桥': [40.042316, 116.414574], '马泉营': [40.0345084, 116.5029933], '俸伯': [40.133274, 116.700989], '丰台南路': [39.840444, 116.296748], '安贞门': [39.977005, 116.405954], '平西府': [40.090615, 116.350587], '五道口': [39.992929, 116.337851], '良乡大学城北': [39.729978, 116.183337], '国贸': [39.909104, 116.461841], '生物医药基地': [39.686616, 116.322244], '北工大西门': [39.90419989999999, 116.4073963], '草房': [39.924541, 116.615334], '宣武门': [39.899723, 116.374314], '什刹海': [39.937563, 116.396247], '前门': [39.90019400000001, 116.397875], '东四': [39.9237466, 116.4180058], '森林公园南门': [40.010234, 116.392764], '东单': [39.908322, 116.417935], '清华东路西口': [40.000659, 116.339068], '柳芳': [39.9581617, 116.432529], '复兴门': [39.907252, 116.357641], '八里桥': [39.905966, 116.618532], '车道沟': [39.947923, 116.293818], '双井': [39.893512, 116.461834], '天安门西': [39.90747200000001, 116.391278], '海淀黄庄': [39.975999, 116.317558], '东夏园': [39.90285, 116.736188], '马家堡': [39.853176, 116.371359], '回龙观东大街': [40.081154, 116.363025], '将台': [39.971315, 116.489861], '平安里': [39.933784, 116.372881], '西直门': [39.94048, 116.355425], '白堆子': [39.9245203, 116.3253359], '管庄': [39.909719, 116.595554], '崔各庄': [40.000061, 116.515561], '生命科学园': [40.094861, 116.294137], '灵境胡同': [39.916134, 116.373742], '万源街': [39.805324, 116.507983], '望京': [39.998741, 116.469783], '花园桥': [39.9324, 116.310713], '郝家府': [39.902402, 116.720442], '磁器口': [39.8934739, 116.4215791], '角门东': [39.845136, 116.385524], '火器营': [39.965938, 116.289058], '长椿街': [39.8946151, 116.3633015], '育新': [40.060384, 116.347271], '健德门': [39.976723, 116.381353], '首经贸': [39.84449, 116.32074], '黄渠': [39.92419400000001, 116.578184], '高米店北': [39.7412236, 116.3325516], '花梨坎': [40.08675, 116.558632], '万寿路': [39.9077482, 116.294875], '北京站': [39.90499399999999, 116.427132], '和平西桥': [39.968416, 116.417975], '后沙峪': [40.114078, 116.564183], '四惠': [39.908785, 116.495516], '科怡路': [39.8318592, 116.2970136], '车公庄': [39.932365, 116.354424], '肖村': [39.834321, 116.448335], '六道口': [39.845851, 116.428395], '巩华城': [40.131089, 116.293905], '通州北苑': [39.901136, 116.638299], '义和庄': [39.712387, 116.319079], '陶然亭': [39.878496, 116.374386], '阜通': [39.99183379999999, 116.4740651], '张自忠路': [39.9332404, 116.4166687], '望京西': [40.0083668, 116.4614997], '金台夕照': [39.91673, 116.46184], '西红门': [39.7898, 116.328689], '军事博物馆': [39.9070944, 116.3220149], '菜市口': [39.8897598, 116.3754684], '丰台站': [39.8476959, 116.3057018], '潘家园': [39.8769858, 116.4603512], '丰台东大街': [39.8583436, 116.2939849], '次渠': [39.803539, 116.591549], '来广营': [40.0197127, 116.4674733], '良乡大学城': [39.723205, 116.176469], '北京西站': [39.894834, 116.32111], '南法信': [40.128411, 116.609416], '南锣鼓巷': [39.9338003, 116.4051186], '沙河高教园': [40.164663, 116.280363], '分钟寺': [39.8525816, 116.4544966], '枣营': [39.944303, 116.474275], '西苑': [39.9996209, 116.2903477], '大瓦窑': [39.8969546, 116.2942767], '同济南路': [39.772913, 116.5398], '林萃桥': [40.021906, 116.372998], '海淀五路居': [39.933022, 116.2778457], '天通苑南': [40.0665093, 116.4127545], '天安门东': [39.90778, 116.401216], '顺义': [40.130005, 116.65844], '知春里': [39.976332, 116.32862], '焦化厂': [39.849969, 116.535819], '潞城': [39.90142, 116.752501], '金台路': [39.9250007, 116.4785133], '虎坊桥': [39.88982, 116.3833539], '石榴庄': [39.8452, 116.4189], '雍和宫': [39.949334, 116.417143], '刘家窑': [39.857495, 116.422117], '湾子': [39.8907994, 116.326489], 'T3航站楼': [40.0526613, 116.615611], '芍药居': [39.977636, 116.435914], '成寿寺': [39.84587399999999, 116.447531], '中关村': [39.98586, 116.329344], '东风北桥': [39.957614, 116.486697], '天通苑北': [40.083617, 116.412973], '和平门': [39.90009, 116.384132], '广阳城': [39.747974, 116.184959], '篱笆房': [39.76493500000001, 116.186371], '北京大学东门': [39.99227399999999, 116.315843], '百子湾': [39.89312899999999, 116.500939], 'T2航站楼': [40.079311, 116.592808], '物资学院路': [39.926854, 116.639264], '西土城': [39.9767521, 116.3529516], '古城': [39.90743399999999, 116.190296], '西小口': [40.046845, 116.351658], '八宝山': [39.90744, 116.235948], '纪家庙': [39.848211, 116.329325], '朝阳门': [39.92384699999999, 116.433593], '永安里': [39.908465, 116.450372], '亦庄文化园': [39.806886, 116.490676], '新街口': [39.9409449, 116.368966], '梨园': [39.883567, 116.668833], '良乡南关': [39.723288, 116.140683], '东四十条': [39.93366899999999, 116.434136], '次渠南': [39.795159, 116.581401], '郭公庄': [39.82608, 116.319158], '育知路': [40.087824, 116.326491], '良乡大学城西': [39.723234, 116.156056], '通州北关': [39.929111, 116.673278], '西单': [39.907422, 116.374253], '苏庄': [39.723289, 116.125085], '双合': [39.8592186, 116.525514], '西局': [39.8648496, 116.3042559], '巴沟': [39.974179, 116.293727], '荣京东街': [39.794857, 116.51413], '高碑店': [39.909475, 116.531679], '惠新西街南口': [39.97701199999999, 116.41752], '北运河西': [39.902761, 116.689938], '传媒大学': [39.90914799999999, 116.554692], '劲松': [39.8847124, 116.4604434], '惠新西街北口': [39.987863, 116.417047], '草桥': [39.845869, 116.351387], '奥林匹克公园': [40.002253, 116.393295], '玉泉路': [39.907414, 116.25299], '关庄': [40.001597, 116.428053], '人民大学': [39.966956, 116.321367], '南礼士路': [39.907234, 116.352583], '公主坟': [39.907447, 116.30992], '十里堡': [39.91554, 116.489848], '回龙观': [40.070794, 116.336275], '七里庄': [39.8664479, 116.2915932], '长春桥': [39.9576776, 116.2957039], '安华桥': [39.96863, 116.394608], '桥湾': [39.892681, 116.408859], '常营': [39.93234899999999, 116.586841], '大郊亭': [39.8939443, 116.4887116], '十里河': [39.8658, 116.459118], '蒲黄榆': [39.8649059, 116.4211872], '泥洼': [39.8594939, 116.3043943], '木樨地': [39.907379, 116.337583], '果园': [39.892844, 116.6497657], '团结湖': [39.933747, 116.461806], '珠市口': [39.8905792, 116.3969225], '大红门': [39.830101, 116.378924], '莲花桥': [39.8973066, 116.3100612], '建国门': [39.908483, 116.435783], '土桥': [39.871981, 116.686439], '北苑': [40.043104, 116.434371], '高米店南': [39.763509, 116.331774], '知春路': [39.9763719, 116.3347996], '大屯路东': [40.0028428, 116.4197348], '西二旗': [40.053062, 116.30601], '北海北': [39.933237, 116.386677], '光熙门': [39.968378, 116.431805], '广安门内': [39.8898174, 116.3571138], '五棵松': [39.907456, 116.273987], '安定门': [39.949179, 116.408228], '三元桥': [39.9619772, 116.4570321], '崇文门': [39.90106100000001, 116.417042], '郭庄子': [39.83583, 116.25187], '垡头': [39.860864, 116.511829], '稻田': [39.794805, 116.218701], '灯市口': [39.91713499999999, 116.417785], '石门': [40.12986799999999, 116.641337], '园博园': [39.861361, 116.201611], '黄村火车站': [39.722966, 116.332611], '北宫门': [40.002374, 116.277583], '九龙山': [39.893212, 116.477516], '荣昌东街': [39.782854, 116.521773], '东湖渠': [40.010225, 116.467364], '达官营': [39.893178, 116.33599], '白石桥南': [39.933022, 116.32568], '天通苑': [40.075255, 116.412795], '立水桥南': [40.041943, 116.414551], '亮马桥': [39.94941000000001, 116.461874], '善各庄': [40.02626, 116.475537], '四惠东': [39.90853370000001, 116.5158243], '褡裢坡': [39.92441000000001, 116.56276], '魏公村': [39.966956, 116.321367], '欢乐谷景区': [39.86854599999999, 116.499906], '北土城': [39.9766591, 116.3953432], '八角游乐园': [39.907442, 116.212684], '孙河': [40.045164, 116.534646], '朱辛庄': [40.104346, 116.313662], '张郭庄': [39.83583, 116.25187], '东大桥': [39.92305899999999, 116.451681], '国家图书馆': [39.943019, 116.323111], '奥体中心': [39.985803, 116.393742], '角门西': [39.846317, 116.371733], '天坛东门': [39.882547, 116.420832], '北沙滩': [40.001523, 116.369041], '安立路': [40.00266999999999, 116.407812], '双桥': [39.910282, 116.576697], '青年路': [39.9226768, 116.5180134], '动物园': [39.938287, 116.339012], '六里桥东': [39.8869627, 116.3144733], '九棵树': [39.890472, 116.657394], '太阳宫': [39.972747, 116.44751], '公益西桥': [39.837022, 116.37082], '积水潭': [39.9499, 116.3795], '广渠门外': [39.893571, 116.449427], '黄村西大街': [39.7310598, 116.3236303], '大钟寺': [39.966674, 116.345092], '大望路': [39.9104386, 116.4776375], '东直门': [39.941098, 116.433552], '望京南': [39.98497589999999, 116.482754], '新宫': [39.81225999999999, 116.365609], '农业展览馆': [39.941341, 116.462114], '临河里': [39.875435, 116.678722], '南楼梓庄': [39.874772, 116.501138], '车公庄西': [39.932466, 116.344082], '西钓鱼台': [39.9218479, 116.2945456], '永定门外': [39.868334, 116.398559], '北京南站': [39.865127, 116.378922], '经海路': [39.784142, 116.563522]}


# -*- coding: utf-8 -*-

socket.setdefaulttimeout(20)

## step 1. get lines
url = 'http://bj.bendibao.com/ditie/'

response = requests.get(url)

what_we_want = r'<strong><a href=\"(/ditie/xl_\d{3}.shtml)\" target=\"_blank\">([0-9\u4e00-\u9fa5\(M1\)\(L1\)]*)</a></strong>'

pattern = re.compile(what_we_want)

lines = pattern.findall(response.text)

## step 2. get stations for each line

station_per_line = dict()  #what to get from the for loop
stations = set()  # a SET containing all stations in Beijing metro system. what to get from the for loop

for line in lines:

    line_name = line[1]

    station_in_order = set()

    url_line = 'http://bj.bendibao.com'+line[0]

    response_line = requests.get(url_line)

    station_wt_w_change = r'(<a class=\"link\" href=\"/ditie/\w+\.shtml\">|<a href=\"/ditie/\w+\.shtml\" class=\"link\" target=\"_blank\">|<a class=\"link\" href=\"/ditie/\w+\.shtml\">)([A-Z0-9\u4e00-\u9fa5]*)'

    pattern_line = re.compile(station_wt_w_change)

    station_in_order = pattern_line.findall(response_line.text)
    stations_temporary = []
    for station in station_in_order:
        stations_temporary.append(station[1])

    stations.update(stations_temporary)

    station_per_line[line_name] = stations_temporary

station_per_line['北京地铁10号线'].append('巴沟')  #line 10 is a loop. This is to manually close the loop stations

print(station_per_line)

# step 3. get station_coord.

station_coord = {}

for station in stations:
    geocode_result= gmaps.geocode(station+"地铁站\,北京\,中国")
    station_coord[station] = list(geocode_result[0]['geometry']['location'].values())

# step 4. draw the map.

import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'

import networkx as nx
station_graph = nx.Graph()
station_graph.add_nodes_from(list(station_coord.keys()))
%matplotlib inline
import matplotlib.pyplot as plt
nx.draw(station_graph, station_coord, with_labels=True, node_size=30)

# step 5. connect stations to create a network

from collections import defaultdict
station_connection = defaultdict(set)
for key in station_per_line.keys():
    stations_in_key = station_per_line[key]
    for x in range(0,len(stations_in_key)-1):
        if x == 0:
            station_connection[stations_in_key[x]].add(stations_in_key[x + 1])
        elif x == len(stations_in_key):
            station_connection[stations_in_key[x]].add(stations_in_key[x - 1])
        else:
            station_connection[stations_in_key[x]].add(stations_in_key[x - 1])
            station_connection[stations_in_key[x]].add(stations_in_key[x + 1])

# draw lines to connect stations
nx.draw(nx.Graph(station_connection), station_coord, with_labels=True, node_size=30)

# step 6. build the search agent
def search(start, destination, connection_grpah, sort_candidate):
    paths = [[start]]
    visitied = set()
    while paths:  # if we find existing paths
        path = paths.pop(0)  # list.pop(i) removes the item at the given position and returns it
        frontier = path[-1]
        if frontier in visitied: continue
        successors = connection_grpah[frontier]
        for city in successors:
            if city in path: continue  # eliminate loop
            new_path = path + [city]
            paths.append(new_path)
            if city == destination: return new_path
        visitied.add(frontier)
        paths = sort_candidate(paths)  # 我们可以加一个排序函数 对我们的搜索策略进行控制

def transfer_stations_first(paths):
    return sorted(paths, key=len)
def transfer_as_much_possible(paths):
    return sorted(paths, key=len, reverse=True)
def pretty_print(cities):
    print('🚗->'.join(cities))


pretty_print(search('慈寿寺','军事博物馆', station_connection,transfer_as_much_possible))
pretty_print(search('慈寿寺','军事博物馆', station_connection,transfer_stations_first))

##疑问：搜索结果不完全准确，有时会出现error，有时可以返回正确结果，有时返回不正确的结果（比如transfer_as_much_possible时给出的路线并不是中转最多的）


