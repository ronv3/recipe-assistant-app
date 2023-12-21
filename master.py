from pip._vendor import requests
apikey= "8afdf27f0d56409c8720c7b36a541831"

def addIngr():
  print("Please enter the missing ingredient names one by one, if you are finished simply press enter with empty field!")
  templist=[]
  print("\n")
  while True:
    human = input("User: ")
    if human=="":
      break
    templist.append(human.strip())
  if len(templist)!=0:
    print("Computer: I have added the following ingredients to the list: ", end='')
    for el in templist:
      print(el, end=' ')
    print()
  return templist

def rmIngr():
  print("Your list of ingredients consists of:")
  for el in ingredients:
    print("• " + el)
  print("Please enter the ingredient names you want to remove one by one, \nif you are finished simply press enter with empty field!")
  templist=[]
  print("\n")
  while True:
    human = input("User: ")
    if human=="":
      break
    if human.lower() not in ingredients:
        print("There's no such ingredient in your list.")
        continue
    templist.append(human.strip())
    for el in ingredients:
      if el == human.lower():
        ingredients.remove(el)
  if len(templist)!=0:
    print("Computer: I have removed the following ingredients to the list:")
    for el in templist:
      print("• " + el)
  return

def makeRequest(ingredientsList,apikey):
  pass
  if len(ingredientsList)!=0:
    ingredients=ingredientsList[0]
    for i in range(1,len(ingredientsList)):
      ingredients+=f",+{ingredientsList[i]}"

    url="https://api.spoonacular.com/recipes/findByIngredients"
    query_params="apiKey=" + apikey + "&ingredients=" + ingredients+ "&number=100" + "&ranking=21" + "&ignorePantry=True"
    query=url+"?"+query_params

    spoonacular_response=requests.get(query)

    return spoonacular_response
 
  else:
    print("You have no ingredients in the list.")
    return None


def recipeURL(recipeID,apikey):
  pass
  url= f"https://api.spoonacular.com/recipes/{recipeID}/information"

  query_params="apiKey=" + apikey
  query=url+"?"+query_params
  spoonacular_response=requests.get(query)
  
  return spoonacular_response

def desc(ingredients):
  spoonacular_response = makeRequest(ingredients,apikey)
  if spoonacular_response == None:
    return False
  else:
    jsnRecipes = spoonacular_response.json()
    print("Computer:")
    counter = 0
    for el in jsnRecipes:
      if len(el['missedIngredients']) > 3:
        continue
      counter += 1
      if counter == 5:
        break
      recipe= recipeURL(el['id'],apikey).json()
      print(" Recipe: " + el['title']+ " -> "+ recipe["sourceUrl"])
      if len(el['missedIngredients'])!=0:
        missing = el['missedIngredients']
        print(" The following ingredients are missing from this recipe:")
        for ing in missing:
          print("   "+ing['original'])
        print("\n")
      else:
        print("You have everything to start cooking! Enjoy!")
        print("\n")
    return True


with open("ingredients.txt", 'r+', encoding="utf-8") as f:
  ingredients = f.read()
  if ingredients != '':
    ingredients = ingredients[:-1].strip().split(';')
  else:
    ingredients = []

print("\n\n\n\nComputer: Hello. I am your personal food assistant. Here to help you with recipes.\n")
if ingredients == []:
  print("Your list of ingredients is currently empty.\n")
else:
  print(f"Your current list of ingredients consists of ", end="")
  print(*ingredients, sep=", ", end=".\n\n")
print('\tTo add ingredients to your list, type "add".')
print('\tTo add ingredients to your list, type "remove".')
print('\tTo get recipes from your ingredients, type "recipes"')
print('\tTo shut down the program, type "bye"\n')

while True:
  human = input("User: ")
  if human == "bye":
    print("Computer: Bye!")
    with open("ingredients.txt", 'w', encoding="utf-8") as f:
      rowIngr = ''
      for x in range(len(ingredients)):
        if ingredients[x] != '':
          rowIngr += f'{ingredients[x]};'
      f.write(rowIngr)
    break
  
  elif human.lower() == "recipes":
    status = desc(ingredients)
    if status==False:
      while status==False:
        ingredients+=addIngr()
        if makeRequest(ingredients, apikey) != None:
          status=True
        else:
          print("You have no ingredients in the list.")
          ingredients+=addIngr()

  elif human.lower() == "add":
    status=False
    while status==False:
      ingredients+=addIngr()
      print("Your list of ingredients now consists of:")
      for el in ingredients:
        print("• " + el)
      print()
      if makeRequest(ingredients, apikey) != None:
        status=True
  
  elif human.lower() == "remove":
    status=False
    while status==False:
      rmIngr()
      print("Your list of ingredients now consists of:")
      for el in ingredients:
        print("• " + el)
      print()
      status = True
      if makeRequest(ingredients, apikey) != None:
        status=True
  else:
    print("Something went wrong, try again.")

    