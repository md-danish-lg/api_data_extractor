import requests as rt
import pandas as pd



r = rt.get('https://jsonplaceholder.typicode.com/users')
if (r.status_code == 200):
    print("Fetched data Successfully")
    data = r.json()
    request_data =[]


    for i in range(len(data)):
        request_data.append({"id": data[i]["id"],
                            "name": data[i]["username"],
                            "email": data[i]["email"],
                            "city": data[i]["address"]["city"],
                            "company": data[i]["company"]["name"]})


    final_data = pd.DataFrame(request_data)
    

    try:

        final_data.to_csv("users.csv")
        final_data.to_excel("users.xlsx", index=False)
        print("Files Saved Sucessfully")
    except:
        print("Failed to save the Files!")

else:
    print("Error getting data")
