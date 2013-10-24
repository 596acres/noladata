all: download_data process_addresses process_buildings process_boundary process_parcels

clean: clean_db clean_processed

prepare_processed:
	mkdir -p processed
	mkdir -p processed/addresses
	mkdir -p processed/buildings
	mkdir -p processed/boundary
	mkdir -p processed/parcels
	mkdir -p processed/nora/uncommitted_properties

clean_processed:
	rm -rf processed

clean_db:
	-psql -q -c "DROP TABLE addresses" -d nola
	-psql -q -c "DROP TABLE buildings" -d nola
	-psql -q -c "DROP TABLE boundary" -d nola
	-psql -q -c "DROP TABLE parcels" -d nola

clean_data:
	rm -rf raw

download_data:
	mkdir -p raw
	curl -L "https://data.nola.gov/download/div8-5v7i/application/zip" -o raw/NOLA_Addresses_20130913.zip
	unzip raw/NOLA_Addresses_20130913.zip -d raw/NOLA_Addresses_20130913
	curl -L "https://data.nola.gov/download/t3vb-bbwe/application/zip" -o raw/BuildingOutlines2013.zip
	unzip raw/BuildingOutlines2013.zip -d raw/BuildingOutlines2013
	curl -L "https://data.nola.gov/api/geospatial/2b2j-u6kh?method=export&format=Shapefile" -o raw/NOLA_Boundary.zip
	unzip raw/NOLA_Boundary.zip -d raw/NOLA_Boundary
	curl -L "https://data.nola.gov/download/xy5r-5rjk/application/zip" -o raw/NOLA_Parcels_20130913.zip
	unzip raw/NOLA_Parcels_20130913.zip -d raw/NOLA_Parcels_20130913

process_addresses: prepare_processed
	ogr2ogr -t_srs EPSG:4326 -overwrite processed/addresses/addresses.shp raw/NOLA_Addresses_20130913/NOLA_Addresses_20130913.shp

import_addresses:
	shp2pgsql -D -c -I processed/addresses/addresses.shp addresses | psql -d nola

process_buildings: prepare_processed
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/buildings/buildings.shp raw/BuildingOutlines2013/BuildingOutlines2013.shp

import_buildings:
	shp2pgsql -D -c -I processed/buildings/buildings.shp buildings | psql -d nola

process_boundary: prepare_processed
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/boundary/boundary.shp raw/NOLA_Boundary/NOLA_Boundary.shp

import_boundary:
	shp2pgsql -D -c -I processed/boundary/boundary.shp boundary | psql -d nola

process_parcels: prepare_processed
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite processed/parcels/parcels.shp raw/NOLA_Parcels_20130913/NOLA_Parcels_20130913.shp

import_parcels:
	shp2pgsql -D -c -I processed/parcels/parcels.shp parcels | psql -d nola
	psql -c "ALTER TABLE parcels ADD COLUMN full_address VARCHAR(100);" -d nola
	psql -c "UPDATE parcels SET full_address = situs_numb || ' ' || situs_stre || ' ' || situs_type WHERE situs_dir IS NULL;" -d nola
	psql -c "UPDATE parcels SET full_address = situs_numb || ' ' || situs_dir || ' ' || situs_stre || ' ' || situs_type WHERE situs_dir IS NOT NULL;" -d nola

download_nora_uncommitted:
	curl -L "https://data.nola.gov/api/views/5ktx-e9wc/rows.csv?accessType=DOWNLOAD" -o raw/NORA_Uncommitted_Properties.csv

# Break Property Address cells into multiple cells by newline
# Break address cells into multiple cells by comma and "LA "
# Break coordinates into multiple cells by comma
# Remove parentheses from coordinates
process_nora_uncommitted:
	sed -e '/^ORL/ { N;N;s/\n/","/g; }' \
		-e '1,/Address/ s/Address/Address,City,State,Zip,Y,X/' \
		-e 's/, /","/g' \
		-e 's/(//' -e 's/)//' \
		-e 's/LA /LA","/g' \
		< raw/NORA_Uncommitted_Properties.csv > processed/nora/uncommitted_properties/uncommitted_properties.csv
