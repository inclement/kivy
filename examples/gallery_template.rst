
Kivy Gallery
============

Documentation for the examples in kivy's examples folder.

{% for key, value in headings.iteritems() %}

{{ key }}
{% for i in key %}-{% endfor %}

{% for filen, image_filen, exists in value %}
{{ filen.split('/')[-1] }}
{% for i in filen.split('/')[-1] %}~{% endfor %}

Source is at `<https://github.com/kivy/kivy/tree/master/examples/{{ filen }}>`__.

Image filen would be {{ image_filen }}. It {% if exists %}exists{% else %}doesn't exist{% endif %}.

{% if exists %}.. image:: {{ image_filen }}
    :width: 300px
    :alt: Image of the running example {{ filen.split('/')[-1] }}
    :align: center
{% endif %}

{% endfor %}

{% endfor %}
