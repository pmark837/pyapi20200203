#!/usr/bin/python3
  
def main():
    ##create a list already containing IP addresses
    iplist=['10.0.0.1', '10.0.1.1','10.3.2.1']

    ##create a list of ports
    iplist2=['5060', '80', '22']

    ##display list
    print(iplist)

    ## Use the extend method on iplist, our list object
    ## Append takes whatever it is passed and adds it to the list object (iplist)
    ## This will create a list within a list
    iplist.append(iplist2)

    ## Show how iplist has changed
    print(iplist)

if __name__ == "__main__":
    main()
