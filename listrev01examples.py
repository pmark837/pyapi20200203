#!/usr/bin/python3

def main ():
    ##create an empty list for extend demo
    myemptylist = []

    ##add to out list with a list method
    ##The extend method will add every item to the list
    myemptylist.extend("192.168.102.55")

    print(myemptylist)

    ##create another empty list for append demo
    myotherlist = []
   

    myotherlist.append("192.168.102.55")
    
    print(myotherlist)

    ##
    networklist = ["cisco", "juniper"]
    myemptylist.extend(networklist)
    print(myemptylist)

if __name__=="__main__":
    main()
