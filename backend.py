from pyswip import Prolog
prolog = Prolog()
prolog.consult("movie.pl")

def insert(title, author, year, genre, rate, actor):
    myQuery="test('{0}','{1}',{2},'{3}',{4},'{5}')".format(title,author,year,genre,rate,actor)
    print(myQuery, "<< my insert query")
    prolog.assertz(myQuery)

def view():
    mylist = list(prolog.query("test(Title,Director,Year,Genre,Rate,Actor)"))
    print(mylist, "<- this is my list")
    return mylist

def search(title="", author="", year="",genre="", rate="",actor=""):
    otherdict={}
    myQuery="test("

    if(title==""):
        myQuery += "Title,"
    else:
        myQuery += "'{0}',".format(title)
        otherdict['Title']= title
    if(author==""):
        myQuery += "Director,"
    else:
        myQuery += "'{0}',".format(author)
        otherdict['Director']= author
    if(year==""):
        myQuery += "Year,"
    else:
        myQuery += "{0},".format(year)
        otherdict['Year']= year
    if(genre==""):
        myQuery += "Genre,"
    else:
        myQuery += "{0},".format(genre)
        otherdict['Genre']= genre

    #myQuery += "Genre,"

    if(rate==""):
        myQuery += "Rate,"
    else:
        myQuery += "{0},".format(rate)
        otherdict['Rate']= rate
    if(actor==""):
        myQuery += "Actor"
    else:
        myQuery += "{0}".format(actor)
        otherdict['Actor']= actor

    #myQuery += "Actor)"
    myQuery += ")"


    print(myQuery,"<< My query")
    print(otherdict,"<< My dict")
    mylist = list(prolog.query(myQuery))
    print(mylist, "<- this is my search list")

    for dict in mylist:
        dict.update(otherdict)
    print(mylist,"<< newest list")
    return mylist

def delete(myDict):
    myQuery="test('{0}','{1}',{2},'{3}',{4},'{5}')".format(myDict['Title'],myDict['Director'],myDict['Year'],myDict['Genre'],myDict['Rate'],myDict['Actor'])
    print(myQuery, "<< my delete query")
    prolog.retract(myQuery)

def update(myDict, title, author, year, genre, rate, actor):
    myQuery="test('{0}','{1}',{2},'{3}',{4},'{5}')".format(myDict['Title'],myDict['Director'],myDict['Year'],myDict['Genre'],myDict['Rate'],myDict['Actor'])
    print(myQuery, "<< my update query")
    prolog.retract(myQuery)
    myQuery="test('{0}','{1}',{2},'{3}',{4},'{5}')".format(title,author,year,genre,rate,actor)
    print(myQuery, "<< my insert query")
    prolog.assertz(myQuery)


print(view())
