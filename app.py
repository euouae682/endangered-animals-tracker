import asyncio
from EdgeGPT import Chatbot, ConversationStyle
import json
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import regex as re

app = Flask(__name__)
api = Api(app)
CORS(app)

async def main():
    bot = Chatbot(cookiePath='cookies.json')
    x = """
    Tell me information without including any other irrelevant text for the Pacific Sleeper Shark in the following format. For the habitats choose them from these categories only: ([Forest, Savanna, Shrubland, Grassland, Wetlands, Rocky Areas (e.g., inland cliffs, mountain peaks), Caves & Subterranean Habitats (non-aquatic), Desert, Marine Neritic, Marine Oceanic, Marine Deep Ocean Floor (Benthic and Demersal), Marine Intertidal, Marine Coastal/Supratidal, Artificial-Terrestrial, Artificial-Aquatic, Unknown]) 

    Format:
    Animal Name:
    Scientific Name:
    Conservation Status:
    Habitats:
    Continents:
    Countries:
    Summary:
    """
    answer = (await bot.ask(prompt=x, conversation_style=ConversationStyle.precise))['item']['messages'][1]['text']
    y = answer.split("\n")
    list = []
    for item in y:
        list.append(re.sub("^.*: ",'',item))
    jason = {"Animal Name:":list[0],"Scientific Name":list[1],"Conservation Status":list[2],"Habitats":list[3],"Continents":list[4],"Countries":list[5],"Summary":list[6]}
    print(jason)
    return jason
    


class Animal(Resource):

    """
    Creating Animal Resource
    """

    # Send Back Recipe Response
    def post(self, animalname):
        return asyncio.run(main(()))
    
    


# Add Resource To Path
api.add_resource(Animal, "/recipe/<string:animalname>")

if __name__ == "__main__":
    #app.run(debug=True)
    asyncio.run(main())

    