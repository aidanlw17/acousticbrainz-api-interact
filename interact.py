import requests, json, sys, pprint

#baseUrl = 'https://acousticbrainz.org'
#'Authorization': 'Bearer {0}'.format(api_tok)}
baseUrl = 'http://localhost:8080'
head={'Content-Type': 'application/json'}

#Takes a list of MusicBrainz ids, returns their high level json data
def getHLRecordings(mbids):
    urlExt = '/api/v1/high-level?'
    queryStr = 'recording_ids='
    for i in range(len(mbids)):
        if(i==len(mbids)-1):
            queryStr += (mbids[i])
        else:
            queryStr += (mbids[i] + ';')
    print('q string is:')
    print(queryStr)
    urlExt += queryStr
    response=requests.get(baseUrl + urlExt, headers=head)
    response.raise_for_status()
    
    resData = json.loads(response.text)
    print('--------------------------------------')
    print('DATA')
    print('--------------------------------------')
    pprint.pprint(resData)
    print('--------------------------------------')
    return resData

#Gets high level for one recording
def getHLRecording(mbid):
    urlExt = '/api/v1/' + mbid + '/high-level'
    #queryStr = 'recording_id=' + mbid
    #print('q string is:')
    #print(queryStr)
    #urlExt += queryStr
    response=requests.get(baseUrl + urlExt, headers=head)
    response.raise_for_status()
    
    resData = json.loads(response.text)
    print('--------------------------------------')
    print('DATA')
    print('--------------------------------------')
    pprint.pprint(resData)
    print('--------------------------------------')
    return resData

#Gets lower level for multiple recordings
def getLLRecordings(mbids):
    urlExt = '/api/v1/low-level?'
    queryStr = 'recording_ids='
    for i in range(len(mbids)):
        if(i==len(mbids)-1):
            queryStr += (mbids[i])
        else:
            queryStr += (mbids[i] + ';')
    print('q string is:')
    print(queryStr)
    urlExt += queryStr
    response=requests.get(baseUrl + urlExt, headers=head)
    response.raise_for_status()
    
    resData = json.loads(response.text)
    print('--------------------------------------')
    print('DATA')
    print('--------------------------------------')
    pprint.pprint(resData)
    print('--------------------------------------')
    return resData

def getLLRecording(mbid):
    urlExt = '/api/v1/' + mbid + '/low-level'
    #queryStr = 'recording_ids='
    #print('q string is:')
    #print(queryStr)
    #urlExt += queryStr
    response=requests.get(baseUrl + urlExt, headers=head)
    response.raise_for_status()
    
    resData = json.loads(response.text)
    print('--------------------------------------')
    print('DATA')
    print('--------------------------------------')
    pprint.pprint(resData)
    print('--------------------------------------')
    return resData



ids=['5fdad79b-8cc8-418f-8eed-1407f233566d','3a08c860-28a3-4962-a883-bb767abc0582']
#ids=['4ad72fb1-c0f2-405d-b218-c98727a206f5','be541ac5-23f8-44f3-901c-e501306aee1b']
mb='61e7c4f0-9e4a-4e7a-bc47-75eca3700403'

#getHLRecordings(ids)
#getHLRecording(mb)
#getLLRecordings(ids)
getLLRecording(mb)







