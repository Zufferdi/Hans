---
layout: page
title: Le parcours
permalink: /map/
---



    
<div id="mapid" class="mapbig"> </div>

<script>
var mymap = L.map('mapid').setView([48.282094, 13.058854], 7);
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {minZoom: 4, maxZoom: 12, attribution: osmAttrib});
mymap.addLayer(osm);
{% for post in site.posts %}
    {% if post.latitude %}
    L.marker([{{post.latitude}}, {{post.longitude}}]).addTo(mymap).bindPopup("<a href='{{ site.url }}/Hans{{ page.url }}'> <strong>{{post.title}}</strong> </a>"); 
    {% endif %}
{% endfor %}
var latlngs = [
{% for post in site.posts %}
    {% if post.latitude %}
        [{{post.latitude}}, {{post.longitude}}]
            {% if forloop.last == false %}
            ,
        {% endif %}
   {% endif %}
{% endfor %}
]
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(mymap);
</script>



 