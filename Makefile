all: diversity.pdf tutorial.html

diversity.pdf: diversity.tex diversity.bib
	pdflatex diversity.tex
	bibtex diversity
	pdflatex diversity.tex
	pdflatex diversity.tex

tutorial.html: tutorial.rst
	rst2html.py tutorial.rst tutorial.html

clean:
	rm *.aux *.bbl *.blg *.log *.pdf
