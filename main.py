from query import *
from load import *
from extract import *

run = True
while(run):
    print("1. Fetch Securities")
    print("2. Fetch Today's Bhavcopy")
    print("3. Fetch Bhavcopy for 30 days")
    print("4. Load Securities")
    print("5. Load Bhavcopy")
    print("6. Get top 25 gainers for today")
    print("7. Get top 25 gainers day wise")
    print("8. Extract and Load All")
    print("9. Get top 25 historical gainers")
    print("10. Exit")
    print("ENTER CHOICE: ")
    
    try: 
        choice = int(input())

        if(choice == 1):
            get_securities()
    
        elif(choice == 2):
            get_latest_bhavcopy()
    
        elif(choice == 3):
            get_monthly_bhavcopy()
    
        elif(choice == 4):
            load_securities()
    
        elif(choice == 5):
            load_bhavcopy()
    
        elif(choice == 6):
            top_25_gainers_for((datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d'))
    
        elif(choice == 7):
            for i in range(1, 31):
                top_25_gainers_for((datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d'))
        
        elif(choice == 8):
            get_securities()
            get_monthly_bhavcopy()
            load_securities()
            load_bhavcopy()

        elif(choice == 9):
            top_25_historical_gainers()

        elif(choice == 10):
            run = False

        else:
            print("Invalid input!")
    except:
        print("An exception occurred!")
