import streamlit
import pandas 
import requests
from urllib.error import URLError
import snowflake.connector 
streamlit.title("My Mom's New Healthy Dinner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# data importing
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#reseting index
my_fruit_list.set_index('Fruit',inplace=True)
#selecting items adding into list

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
def get_fruityvice_data(this_fruit_chioce):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
    if not fruit_choice:
        streamlit.error("Please select fruit to get information.")
    else  :
        back_from_function=get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e :
    streamlit.error()


def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
if streamlit.button("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


# def insert_row_snowflake(new_fruit):
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute("insert into fruit_load_list values ('" + new_fruit +  "')")
#         return "Thanks For Adding "+ new_fruit

# add_my_fruit = streamlit.text_input('What fruit would you like to add ?')
# if streamlit.button("Add a fruit to the list"):
#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     back_from_function = insert_row_snowflake(add_my_fruit)
#     streamlit.text(back_from_function)

# if streamlit.button("Get Fruit list"): 
#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     my_data_rows = get_fruit_load_list()
#     my_cnx.close()
#     streamlit.dataframe(my_data_rows)

# # my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# # my_cur = my_cnx.cursor()
# # my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# # my_data_row = my_cur.fetchall()
# # streamlit.header("The Fruit Load List Contains:")
# # streamlit.dataframe(my_data_row)


# add_my_fruit = streamlit.text_input('What fruit would you like to add ?','jackfruit')
# streamlit.write('Thanks for adding ', add_my_fruit)


# my_cur.execute("insert into fruit_load_list values ('" + new_fruit +  "')")


