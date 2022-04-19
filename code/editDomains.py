# Import and set parameters 
import arcpy
import pandas 
arcpy.env.workspace = 'C:/Temp/domainEdit'  # PATH 
db = 'Current.gdb'                          # DB   
addTable = 'ucuDomains_add.csv'             # table of values to add
delTable = 'ucuDomains_del.csv'             # table of values to delele

# ADD 
print("\n   ADDING VALUES")
add = pandas.read_csv(addTable)
domains = add.columns
for i in domains:
    arcpy.TableToDomain_management(addTable, i, i, db, i,"APPEND")
    print (i)

# DELETE
print ("\n   DELETING VALUES")
delete = pandas.read_csv(delTable)
cols = delete.columns
for d in cols:
    print (d)
    dVals = list((delete[d]).dropna()) # drop nas and coerce to list 
    print(dVals)
    arcpy.DeleteCodedValueFromDomain_management(db, d , dVals)

# SORT
print ("\n   SORTING")
for i in domains:   # modify if add != del domains
    arcpy.SortCodedValueDomain_management(db, i, "CODE", "ASCENDING")
    print (i)

print ("\n   DONE!")






























