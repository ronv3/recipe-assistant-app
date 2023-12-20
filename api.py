!pip install googletrans==4.0.0rc1
import googletrans

apikey= "8afdf27f0d56409c8720c7b36a541831"



def makeRequest(ingredientsList,apikey):
  if len(ingredientsList)!=0:
    ingredients=ingredientsList[0]
    for i in range(1,len(ingredientsList)):
      ingredients+=f",+{ingredientsList[i]}"

    url="https://api.spoonacular.com/recipes/findByIngredients"

    query_params="apiKey=" + apikey + "&ingredients=" + ingredients+ "&number=3"

    query=url+"?"+query_params

    spoontacular_response=requests.get(query)

    return spoontacular_response
  else:
    print("You have no ingredients in the list.")
    return None



def recipeURL(recipeID,apikey):
  url= f"https://api.spoonacular.com/recipes/{recipeID}/information"

  query_params="apiKey=" + apikey

  query=url+"?"+query_params
  spoontacular_response=requests.get(query)
  
  return spoontacular_response



def desc(ingredients):
  spoontacular_response = makeRequest(ingredients,apikey)
  if spoontacular_response == None:
    return False
  else:
    jäson = spoontacular_response.json()
    print("Computer:")
    for el in jäson:
      recipe= recipeURL(el['id'],apikey).json()
      print(" Recipe: " + el['title']+ " -> "+ recipe["sourceUrl"])
      if len(el['missedIngredients'])!=0:
        missing = el['missedIngredients']
        print(" The following ingredients are missing from this recipe:")
        for ing in missing:
          print("   "+ing['original'])
      else:
        print("You have everything to start cooking! Enjoy!")
    return True




print("Computer: Hello! Please add a picture of the foods to your Google Drive Colab Notebooks folder and enter the name of the picture file. If you have already added a picture, that's great and simply enter a name!")
while True:

    human = input("User: ")
    if human == "bye":
        print("Computer: Bye!")
        break
      
    elif ".jpeg" in human.lower() or  ".jpg" in human.lower() or ".png" in human.lower() or  ".HEIC" in human.lower():
      failinimi = leiaFail(human)
      print(f"Processing picture: {failinimi}")
      ingredients=getIngredients(failinimi)
      #Remove duplicatees
      ingredients = list(dict.fromkeys(ingredients))
      if len(ingredients)!=0:
        print("Computer: I recognized the following ingredients from your picture:")
        for el in ingredients:
          print("• " + el)
      else:
        print("I did not recognize any ingredients from the picture, the list is empty.")
      print("Computer: Would like to add any other ingredients to the list?")

    elif re.search(r"\bno\b", human.lower()):
      par = desc(ingredients)
      if par==False:
        while par==False:
          ingredients+=addMore()
          par=desc(ingredients)

    elif re.search(r"\byes\b", human.lower()):
      par=False
      while par==False:
        ingredients+=addMore()
        par=desc(ingredients)
    else:
      print("Computer: Something went wrong, try again!")