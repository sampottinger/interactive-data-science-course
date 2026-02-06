# {{ name }}

{{ header | striptags }}

## Contents

{% for section in sections %}
- [{{ section.short }}](#{{ section.name }})
{% endfor %}

{% for section in sections %}
## {{ section.short }}

{{ section.body | striptags }}

{% endfor %}

{% if citations %}
## Citations

{% for citation in citations %}
- {{ citation | striptags }}
{% endfor %}
{% endif %}
