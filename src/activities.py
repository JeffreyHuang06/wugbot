from discord import Game, Activity, ActivityType as AT
listening = AT.listening
streaming = AT.streaming
watching = AT.watching
competing = AT.competing

activities = [
    Game(name="Reconstructing Altaic"),
    Game(name="Reconstructing Nostratic"),
    Activity(name="Retroflex Consonants", type=listening),
    Activity(name="Unstressed ɛ", type=listening),
    Game(name="Summer Tournament of Fun"),
    Game(name="Conlanging"),
    Activity(name="Noam Chompsky", type=watching)
]