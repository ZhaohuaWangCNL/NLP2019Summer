import requests
import re
import urllib.request
import urllib.error
#from bs4 import BeautifulSoup
import time
import socket
import googlemaps
gmaps = googlemaps.Client(key = 'AIzaSyDzjzVn_WCGPY0VUuAY1KNZV0bLCUw6ono')
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


