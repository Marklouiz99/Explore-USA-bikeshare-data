import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Please! input the city name you want see its data from the following list [chicago,new york city,washington]:  ')
        city=city.strip().lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Please! input city name from the previous list only')
    print('Thank you for your entery.')        

    # TO DO: get user input for month (all, january, february, ... , june)
    try:
        chosen_filter=int(input('DO you want to filter data on base of month, day , both or none ? answer 1 for month , 2 for day , 3 for both and 4 for none: '))
    except ValueError:
        print('Please! Enter only numbers')
        chosen_filter=int(input('DO you want to filter data on base of month, day , both or none ? answer 1 for month , 2 for day , 3 for both and 4 for none: '))
    half_year_months=['january','february','march','april','may','june']
    weekdays=['saturday','sunday','monday','tuseday','wednesday','thursday','friday']
    if chosen_filter==1:
        day='all'
        print('Thank you for your pervious selection')
        while True:
            month=input(' Now! Please! Enter a month from the first six months of the year: ')
            month=month.strip().lower()
            if month in half_year_months:
                break
            else:
                print('Please! Enter from the first six months of the year')
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif chosen_filter==2:
        month='all'
        print('Thank you for your pervious selection')
        while True:
            day=input(' Now! Please! Enter a day: ')
            day=day.strip().lower()
            if day in weekdays:
                break
            else:
                print('Please! Enter valid day ')
     
    elif chosen_filter==3:
        print('Thank you for your pervious selection')
        while True:
            month=input('Now! Please! Enter a month from the first six months of the year: ')
            month=month.strip().lower() 
            if month in half_year_months:
                break
            else:
                print('Please! Enter from the first six months')
        while True:
            day=input(' Now! Please! Enter a day: ')
            day=day.strip().lower()
            if day in weekdays:
                break
            else:
                print('Please! Enter valid day ')
    elif chosen_filter==4:
        print("Thank you for your previous selection \n You didn't choose any filter base.")
        month='all'
        day='all'
    while True:
        if chosen_filter==1 or chosen_filter==2 or chosen_filter==3 or chosen_filter==4:
            break
        else:
            print('Please! Enter one of the four numbers 1,2,3 or 4 to choose your filter base')
            chosen_filter=int(input('DO you want to filter data on base of month, day , both or none ? answer 1 for month , 2 for day , 3 for both and 4 for no none: '))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Load the city chosen data into pands dataframe
    df=pd.read_csv(CITY_DATA[city])
    #convert Start Time column to datetime forum
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extract the month , week day and hour from datetime
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    # filter base on chosen month if the user choose this option
    if month != 'all':
        #converting the month to its nummerical value
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #adding month to dataframe
        df = df[df['month'] == month]
    if day != 'all':
        #adding day to the dataframe
        df = df[df['day_of_week'] == day.title()]    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    '''arg: data frame of the chosen city , month and day if applicable '''
    '''output: most common month , day and start hour'''

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print('The most common month: ', most_common_month)
    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print('The most common month: ', most_common_day)
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]       
    print('The rush hour: ',most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    '''arg: data frame of the chosen city , month and day if applicable '''
    '''output: the most common start station , end station and trip from start station and end station'''

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('The most popular start station: ',popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('The most Popular end station: ',popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['station']=df['Start Station'] + '  ' + df['End Station']
    popular_trip=df['station'].mode()[0]
    print('The popular trip: ',popular_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    ''' arg: data frame of the chosen city , month and day if applicable '''
    ''' output: total travel time and mean travel time'''
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_sum = df['Trip Duration'].sum()
    print('The total travel time is: ',trip_sum)
    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('Mean travel time is: ',average_trip_duration) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    '''arg: data frame of the chosen city , month and day if applicable '''
    '''output user type , gender and birth year the last two if applicable'''
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print(user_types_counts)
    # TO DO: Display counts of gender
    if 'Gender' in df.keys() and 'Birth Year' in df.keys():
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
        # TO DO: Display earliest, most recent, and most common year of birth
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        the_most_common_birth_year = df['Birth Year'].mode()[0]
        print('The earlist year of birth is: ',oldest)
        print('The most recent year of birth is: ',youngest)
        print('The most Common year of birth is: ',the_most_common_birth_year)
    
    else:
        print('This data has no gender or birth year column')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city):
    print('\n Raw Data is available to check...\n')
    start_time = time.time()
    display_raw_data = input ('Do you want to see  five lines of data ?, Please! answer yes or no.: ')
    display_raw_data = display_raw_data.strip().lower()
    if display_raw_data == 'yes':
        for line in pd.read_csv(CITY_DATA[city] , chunksize=5):
            print(line)
            while True:
                display_raw = input('\n Would you like to see another 5 rows of the raw data? Please! answer yes or no: ')
                display_raw = display_raw.strip().lower()
                if display_raw== 'yes':
                    for line in pd.read_csv(CITY_DATA[city] , chunksize=5):
                        print(line)
                        break
                else:
                    print('Thank You')
                    break 
            break
                   
    elif display_raw_data == 'no':
        print('Thank you for your choose')
    else:
        print('Please! answer with yea or no only')
                    
    print("\nThis took %s seconds." % (time.time() - start_time))        
    print('-'*40)

                 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
