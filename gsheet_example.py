print("Bot starting up...")
import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
# discord related things
token = this_is_where_you_will_put_your_discord_token
client = discord.Client()
 
# google sheets related things
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("the_name_of_your_google_json_file_goes_here.json", scope)
google_client = gspread.authorize(credentials)
 
# I called my sheet "Test Sheet" so you might need to change the name
sheet = google_client.open("Test Sheet").sheet1
 
 
@client.event
async def on_ready():
    print("Bot ready!")
 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    # this is your !time command
    if message.content.lower() == "!time":
        text = ""
 
        cell_list = sheet.range("A1:B25")
        for cell in cell_list:
            text += cell.value
            text += ", "
 
        await message.channel.send(text)
 
    # this is an alternative time command where the output reads one column first, then the other
    if message.content.lower() == "!time2":
        text = ""
 
        cell_list = sheet.range("A1:A25")
        for cell in cell_list:
            text += cell.value
            text += ", "
 
        cell_list = sheet.range("B1:B25")
        for cell in cell_list:
            text += cell.value
            text += ", "
 
        await message.channel.send(text)
 
    # this is the !kc command
    if message.content.lower() == "!kc":
        # the normal outputs of these are lists
        column_c_list = sheet.col_values(3)
        column_d_list = sheet.col_values(4)
 
        # now we need to turn the lists into a single string respectively
        column_c_string = ' '.join(column_c_list)
        column_d_string = ' '.join(column_d_list)
 
        text_to_send = column_c_string + " " + column_d_string
 
        await message.channel.send(text_to_send)
 
 
# token goes here
client.run(token)