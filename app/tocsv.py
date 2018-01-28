def text2csv(screenname):
    t=""
    data_file = open("fakenewsFE\data.csv", 'w')
    for s in screenname:
       if(s!=',' and s!='\n'):
           t=t+s
    data_file.write('text, \n'+t+',')
