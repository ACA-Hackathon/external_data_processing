obtain_agreste_2010_2024:
	echo Obtaining agreste data ">= 2010"...
	mkdir -p src
	curl -k -o src/agreste_saa.zip https://agreste.agriculture.gouv.fr/agreste-web/download/publication/publie/SAA-SeriesLongues/SAA_2010-2024-d%C3%A9finitives_donnees-DepartementalesetRegionales.zip
	#unzip src/agreste_saa.zip -d src
	python zipper.py
	rm src/agreste_saa.zip
	python agreste_2010_2024_transform.py
	echo agreste data ">= 2010" obtained and saved in src/ directory!
