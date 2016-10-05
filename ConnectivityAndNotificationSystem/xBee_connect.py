    import json

    #simulate reception from XBEE
    RcvData= '{"Arduino1":[{"temperature":"32","humidity":"80"}]}'

    #extract data

    XData= json.loads(RcvData)

    #get Arduino ID

    KeyName = XData.keys()[0].encode('ascii')
    if not (KeyName == None):
       ArduinoSplit = KeyName.split('Arduino')
       if len(ArduinoSplit) == 2:
        print('test')

       else:
           print('Unable to decode json')
