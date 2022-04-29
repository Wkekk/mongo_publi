###############################################		TODO	#################################################
#	Q1 : Compter le nombre de documents de la collection publis : done 										#
#	Q2 : Lister tous les livres (type “Book”) : done 														#
#	Q3 : Lister les livres depuis 2014 : done 																#
#	Q4 : Lister les publications de l’auteur “Toru Ishida” : done 											#
#	Q5 : Lister tous les auteurs distincts : done 															#
#	Q6 : Trier les publications de “Toru Ishida” par titre de livre : done 									#
#	Q7 : Compter le nombre de ses publications : done 														#
#	Q8 : Compter le nombre de publications depuis 2011 et par type : done 									#
#	Q9 : Compter le nombre de publications par auteur et trier le résultat par ordre croissant : done 		#
#############################################################################################################


from pymongo import MongoClient
from pprint import pprint

####################### CONNECTION ##########################

connectionString = "mongodb://admin:admin@127.0.0.1:27017"
client = MongoClient(connectionString)
db=client.DBLP
publis=db.publis

###################### QUESTION 1 ###########################

Q1_nb_doc = publis.count_documents({})

print('======================\n')
print("il y a ", Q1_nb_doc, "document(s) dans la base\n")
print('----------------------\n')

###################### QUESTION 2 ###########################

Q2_livres = publis.find({"type" : 'Book'})

###################### QUESTION 3 ###########################

Q3_livres_depuis_2014 = publis.find({"type" : 'Book', "year": {"$gte": 2014}})

###################### QUESTION 4 ###########################


Q4_publi_toru_ishida = publis.find({"authors" : 'Toru Ishida'})

###################### QUESTION 5 ###########################

Q5_auteurs = publis.distinct("authors")

###################### QUESTION 6 ###########################

Q6_publi_toru_ishida_ord = publis.find({"authors" : 'Toru Ishida'}).sort("title")

###################### QUESTION 7 ###########################

Q7_nb_doc_toru = publis.count_documents({"authors" : 'Toru Ishida'})
print('Toru Ishida a publié ', Q7_nb_doc_toru, 'document(s)\n')

###################### QUESTION 8 ###########################

Q8_pipeline=[
	{
		"$match":
		{
			"year" : {"$gte" : 2011}
		}
	},
	{
		"$group":
		{
			"_id":"$type",
			"total" : { "$sum" : 1}
		}
	}
]


Q8_results = publis.aggregate(Q8_pipeline)

###################### QUESTION 9 ###########################

Q9_pipeline=[
	{ 
		"$unwind" : "$authors"
	},
	{ 
		"$group" : 
		{
			"_id" : "$authors", 
			"number" : { "$sum" : 1 } 
		}
	},
	{
		"$sort" : {"number" : 1}
	}
]


Q9_results = publis.aggregate(Q9_pipeline)


#########################  AFFICHAGE  #####################################

### REMPLACE LE CURSEUR DE LA BOUCLE FOR PAR CELUI DE LA REPONSE A LA QUESTON VOULUE
## Q1 et Q7 affcihées séparément car elles ne prennent pas de place

#Q2_livres, Q3_livres_depuis_2014, Q4_publi_toru_ishida, Q5_auteurs, 
#Q6_publi_toru_ishida_ord, Q8_results, Q9_results


for documents in Q4_publi_toru_ishida:
	print('++++++++++++++++++++++++++++++++++++++\n')
	pprint(documents)

print('\n======================')
