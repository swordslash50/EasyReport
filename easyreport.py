import whoisit
import webbrowser
def main():
    print(r""" 
  ______           _______     __  _____  ______ _____   ____  _____ _______ 
 |  ____|   /\    / ____\ \   / / |  __ \|  ____|  __ \ / __ \|  __ \__   __|
 | |__     /  \  | (___  \ \_/ /  | |__) | |__  | |__) | |  | | |__) | | |   
 |  __|   / /\ \  \___ \  \   /   |  _  /|  __| |  ___/| |  | |  _  /  | |   
 | |____ / ____ \ ____) |  | |    | | \ \| |____| |    | |__| | | \ \  | |   
 |______/_/    \_\_____/   |_|    |_|  \_\______|_|     \____/|_|  \_\ |_|   
                                                                                                                                                       
""")
    print(' A program used to make it easy to research and report websites')
    print('1. Lookup Name Servers')
    decision = int(input('Number: '))
    if decision == 1:
            website = input('WEBSITE URL: ')
            whoisit.bootstrap()
            results = whoisit.domain(website)
            print('-------------- Results --------------')
            print('NAME:', results['name'])
            print('NAMESERVERS:', results['nameservers'])
            print('REGISTRATIONDATE:', results['registration_date'])
            print('ENTITY INFO:', results['entities'])
            print('')
            print('')
            print('')

    elif decision == 2:
        print('')
    
        
main()
input('Press Enter to Close')
