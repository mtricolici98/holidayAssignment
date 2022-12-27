# Explanation

## RO

Packageul `data` contine 2 package-uri `data_access` si `data_storage`.

### Data Storage
Package-ul `data_storage` este destinat pentru a lucra cu fisierele si faciliteaza salvarea/citirea fisierelor cu date pentru programul nostru.

Nu modificati `data_storage`, intrucat acolo toata logica este deja scrisa si testata.


### Data Access
Package-ul `data_access`este destinat pentru toate metodele de manipulare a datelor noastre, exemplu (find_car_by_vin, save_car, etc...)
 
Modificati modulele in `data_access` si implementati metodele necesare pentru a modifica datele, etc.


## ENG

The `data` package contains 2 packages `data_access` and `data_storage`.

### Data Storage

The data storage package has been created to handle file I/O so the programmer can save/read data from the files.

There is no need to modify anything in the `data_storage` package.

**!!!Warning!!!** The methods to save data will overwrite any existing data

### Data Access

The `data_access` package conains all the files that will be used to access and modify our data, for example: get_car_by_vin or save_car, etc. 

You have to implement everything yourself.