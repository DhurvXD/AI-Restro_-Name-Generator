from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from Secret_key import groq_api_key

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=groq_api_key
)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    name_prompt = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Return only the name, nothing else."
    )

    # Chain 2: Menu Items
    items_prompt = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as a comma separated string only, nothing else."
    )

    parser = StrOutputParser()

    # Modern chain using | operator
    name_chain = name_prompt | llm | parser
    items_chain = items_prompt | llm | parser

    # Run chain 1
    restaurant_name = name_chain.invoke({"cuisine": cuisine})

    # Run chain 2
    menu_items = items_chain.invoke({"restaurant_name": restaurant_name})

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }

if __name__ == "__main__":
    response = generate_restaurant_name_and_items("Italian")
    print("Restaurant Name:", response['restaurant_name'])
    print("Menu Items:", response['menu_items'])