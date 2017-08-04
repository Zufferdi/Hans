---
layout: page
title: L'itinéraire d'un retour.
permalink: /map/
---

<p> Cette carte illustre le retour de Hans Mayer dans son village d'Oberstdorf, et surtout le parcours accompli à pied. <br>
Pour son établissement, les lieux ont été géolocalisés selon la description du soldat Mayer dans son Journal. Il est clairement impossible de tracer précisément son parcours à pied. Hans donne néanmoins de précieuses indications en énumérant les lieux qu'il a traversé avec ses compagnons.</p>

<div id="mapid" class="mapbig"> </div>

<script>
var mymap = L.map('mapid').setView([48.282094, 13.058854], 7);
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {minZoom: 4, maxZoom: 12, attribution: osmAttrib});
mymap.addLayer(osm);
{% for post in site.posts %}
    {% if post.latitude %}
    L.marker([{{post.latitude}}, {{post.longitude}}]).addTo(mymap).bindPopup("<a href='{{ post.url | prepend: site.baseurl }}'> <strong>{{post.title}}</strong> </a>"); 
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



 