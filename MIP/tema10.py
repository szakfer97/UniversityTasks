import pymongo

cluster = pymongo.MongoClient("mongodb+srv://Adam:Adam@cluster0.74w1f.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["sample"]

post1 = {"_id":0,"Nume":"Adam","Facultatea":"Informatica","Anul":"III","Materia":"Medii si instrumente de programare"}
post2 = {"_id":1,"Nume":"Szakacsi Ferenc-Adam","Facultatea":"Informatica","Anul":"III","Materia":"Medii si instrumente de programare"}

collection.insert_one(post2)