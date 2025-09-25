serve:
	mkdocs serve

html:
	mkdocs build

pdf:
	python merge-md.py --fmt=pdf
	pandoc index.md \
	-o 癸酉本石头记后28回.pdf \
	--toc -V toc-title="目录" \
	--include-before-body=cover.tex \
	--pdf-engine=xelatex

epub:
	python merge-md.py --fmt=epub
	pandoc index.md \
	-o 癸酉本石头记后28回.epub \
	--epub-title-page=false \
	--epub-cover-image=docs/assets/cover.jpg \
	--toc -V toc-title="目录"

all: html pdf epub
