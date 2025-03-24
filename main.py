from BoudreauxClients import Clients
from linkedlist import Linkedlist

boudreaux_Clients = Linkedlist()

def addClient():
    clientName = input("Provide the client's name: ")
    phoneNumber = input("Provide the client's phone number: ")
    dob = input("Provide the client's D.O.B. in MMDDYYYY: ")
    client  = Clients(clientName, phoneNumber, dob)
    boudreaux_Clients.append(client)
    print("You've added a new client!")

def displayClients():
        print("List of Boudreaux Clients")
        print(boudreaux_Clients)

def searchClient():
    clientName = input("Provide the client's name to search: ")
    
    if clientName in boudreaux_Clients:
        client, client_id = boudreaux_Clients.access(clientName)
        print("client found!")
        print("Client ID(System): "+str(client_id))
        print(client)
    else:
        print("Could not find the client " + clientName)

def deleteClient():
    clientName = input("Provide the client's name to delete: ")
    if clientName in boudreaux_Clients:
        client, client_id = boudreaux_Clients.access(clientName)
        boudreaux_Clients.delete(client_id)
        print("Successfully deleted client: ")
        print(client)
    else:
        print("Could not find the client "+ clientName)

def mainMenu():
    print("Type the number for the action you wish to perform and then hit Enter.")
    print("1. Add a new client")
    print("2. Display a list of all current clients")
    print("3. Search for a client")
    print("4. Delete a client")
    print("5. Quit")
    try:
        cmd = int(input("What do you want to do? "))
    except:
        print("Please enter a numerical value.")
        mainMenu()

    while cmd < 1 or cmd > 5:
        print("I'm sorry, that is not an allowed action.")
        print("\n")
        mainMenu()
    
    if cmd == 1:
        addClient()
        print("\n")
        mainMenu()
    elif cmd == 2:
        displayClients()
        print("\n")
        mainMenu()
    elif cmd == 3:
        searchClient()
        print("\n")
        mainMenu()
    elif cmd == 4:
        deleteClient()
        print("\n")
        mainMenu()
    elif cmd == 5:
        exit()
    

def main():
    print("Boudreaux's Barbershop")
    mainMenu()

if __name__ == "__main__":
    main()