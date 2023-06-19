def prep(data):
    for collection in data:
        if collection['volumeChange'] == None:
            collection['volumeChange'] = 0
        if collection['image'] == None:
            collection['image'] = 'https://i.imgur.com/2j5ZQ9V.png'
        collection['volumeChange'] = round(collection['volumeChange'], 2)
    
    return data