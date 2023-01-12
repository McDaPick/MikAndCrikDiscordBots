
# gets the users in a voice chat channel and returns them in a list
# needs the channel object as a parameter
def checkVoiceChannelforUsers(channel):
    members = channel.members  # finds members connected to the text_channel

    memnames = []  # (list)
    for member in members:
        memnames.append(member.name)

    # print members to terminal
    #print(memnames)

    return memnames