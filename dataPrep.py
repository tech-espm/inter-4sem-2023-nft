def prep(data):
    for collection in data:
        if collection['volumeChange'] == None:
            collection['volumeChange'] = 0
        
        collection['volumeChange'] = round(collection['volumeChange'], 2)
    
    return data