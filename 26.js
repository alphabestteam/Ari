const papuchasJason = {"firstname": "Jason", 
                    "lastname" : "Todd", 
                    "age" : 30,
                    "codenames": 
                     [ 
                        "Robin",
                        "Nightwing", 
                        "Hush" 
                    ]
                }
const jasonObject = JSON.parse(papuchasJason);
const firstCodename = jasonObject.codenames[0];
print(firstCodename)
