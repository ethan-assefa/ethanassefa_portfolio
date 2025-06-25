---
title: '{{ replace .Name "-" " " | title }}'
date: {{ .Date }}
image: "/images/publications/{{ .Name }}.jpg"
cover: "/images/publications/{{ .File.BaseFileName }}/cover.jpg"

# New image‐path params:
flowchart: "/images/publications/{{ .File.BaseFileName }}/purpose-chart.svg"
# Optional interactive embed
flowchartEmbed: <iframe width="100%" frameborder="0" src=""> </iframe>
methodsGraphic: "/images/publications/{{ .File.BaseFileName }}/methods-graphic.svg"
resultsGraph: "/images/publications/{{ .File.BaseFileName }}/results-plot.svg"

purpose: ""
methods: ""
findings: ""
skills:
  - ""
pdf: "/pdfs/{{ .File.BaseFileName }}.pdf"
link: ""
---
