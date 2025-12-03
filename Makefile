obtain_agreste_2010_2024:
	echo Obtaining agreste data ">= 2010"
	mkdir -p src
	curl -k -o src/agreste_saa.zip https://agreste.agriculture.gouv.fr/agreste-web/download/publication/publie/SAA-SeriesLongues/SAA_2010-2024-d%C3%A9finitives_donnees-DepartementalesetRegionales.zip
	python zipper.py -f src/agreste_saa.zip -o src/
	rm src/agreste_saa.zip
	python agreste_2010_2024_transform.py
	echo agreste data ">= 2010" obtained and saved in data/ directory!


# For this period ze don't retain all the files for practical reasons
obtain_agreste_2000_2010:
	echo Obtaining agreste data "2000-2009"
	mkdir -p src
# 	curl -o src/agreste_2000_2009.zip #link_here#
	python zipper.py -f src/agreste_2000_2009.zip -o src/agreste_2000_2009/
	rm src/agreste_2000_2009.zip


obtain_BDGSF:
	echo Obtaining BDGSF v.3.2.8.0
	mkdir -p src
# 	TODO: This have to be manual download from: https://recherche.data.gouv.fr/fr/jeu-de-donnee/base-de-donnees-geographique-des-sols-de-france-a-11-000-000-1 
#   for the moment, the link below doesn't work it is an api call that needs to be set up properly.
# 	curl -o src/BDGSF.zip https://entrepot.recherche.data.gouv.fr/api/access/datafiles?gbrecs=true&format=original
	python zipper.py -f src/BDGSF.zip -o src/soils/
	rm src/BDGSF.zip
	python zipper.py -f src/soils/30169_L93.zip -o src/soils/shapes/
	rm src/soils/30169_L93.zip
	python soils_transform.py
	echo BDGSF obtained and saved in data/ directory!