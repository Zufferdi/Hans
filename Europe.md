---
layout: page
title: Hans et ses déplacements dans la 337e ID.
permalink: /europe/
---

<p> Cette carte pointe les différents lieux visités par Hans Mayer jusqu'en mai 1945. Elle illustre clairment la grande mobilité et l'impressionnante logistique mise en place par la Wehrmacht pour assurer son rôle de troupe d'occupation (en France et au Benelux notamment), mais aussi de troupe de conquête (front Est).</p>

<div id="mapid" class="mapbig"> </div>

<script>
var mymap = L.map('mapid').setView([50.066826, 14.465596], 4);
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {minZoom: 4, maxZoom: 12, attribution: osmAttrib});
mymap.addLayer(osm);
{% for post in site.posts %}
    {% if post.WW2_lat %}
    L.marker([{{post.WW2_lat}}, {{post.WW2_long}}]).addTo(mymap).bindPopup("<a href='{{ post.url | prepend: site.baseurl }}'> <strong>{{post.title}}</strong> </a>"); 
    {% endif %}
{% endfor %}
var latlngs = [
{% for post in site.posts %}
    {% if post.WW2_lat %}
        [{{post.WW2_lat}}, {{post.WW2_long}}]
            {% if forloop.last == false %}
            ,
        {% endif %}
   {% endif %}
{% endfor %}
]

</script>



 