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
    Invalid_input=  'Invalid input !!! Please try again'

    while True :
        city = input("Enter the name of the city you want to analyze \ncity names are: \nChicago \nNew York City \nWashington \n").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print(Invalid_input)

    # get user input for month (all, january, february, ... , june)
    while True :
        month = input("Enter the month to filter by, or \"all\" to apply all months filter \nmonths are: \nJanuary\nFebruary\nMarch\nApril\nMay\nJune \n").lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print(Invalid_input)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("\nEnter the day of week to filter by, or \"all\" to apply all days filter\nDays are: \nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday\n").lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print(Invalid_input)
            
          


    print('-'*50)
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
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

#convert Start Time To Datetime formate
    df['Start Time']=pd.to_datetime(df['Start Time'])    
#filtring the Dataframe
# filter by month
    if month != 'all':
        df['month'] = df['Start Time'].dt.month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month]
#filter by day 
    if day != 'all':
        df['day'] = df['Start Time'].dt.day_name()
        df = df.loc[df['day'] == day.title()]
      

    return df


def time_stats(df):
    #Displays statistics on the most frequent times of travel.

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #convert Start Time To Datetime formate
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #Extartct month,day, hour to new columns 
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    df['start_hour']=df['Start Time'].dt.hour
    # most common month
    common_month = df['month'].mode()[0]
    print('The most common month: ',common_month)


    # display the most common day of week
    common_day=df['day'].mode()[0]
    print('The most common day of the week: ',common_day)


    # common start hour
    common_start_hour= df['start_hour'].mode()[0]
    print('The most common start hour: ',common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def station_stats(df):
   # most popular stations and trip

    print('\nCalculating The Most Popular Stations and Trips ...\n')
    start_time = time.time()

    # commonly used start station
    common_s_sattion=df['Start Station'].mode()[0]
    print('The most commonly used start station: ',common_s_sattion)


    # commonly used end station
    common_e_sattion=df['End Station'].mode()[0]
    print('The most commonly used End station: ',common_e_sattion)


    # display most frequent combination of start station and end station trip
    stations = df['Start Station'] + "+" + df['End Station']
    common_station = stations.value_counts().idxmax()
    print('Most frequent used combinations are:\n{} \nto\n{}'.format(common_station.split('+')[0], common_station.split('+')[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    #the total and average trip duration

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    total_in_min=total_travel/60
    print('Total travel time: ',round(total_in_min),'Minutes')

    # display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Mean travel time:' ,round(mean_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    #Displays statistics on bikeshare users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # counts of user types
    user_typs=df['User Type'].value_counts()
    print(user_typs)
    print('')


    # counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
        print('')


    # earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        
        print("Earliest year of birth: " ,earliest)
        print("Most recent year of birth: " ,recent)
        print("Most common year of birth: " ,common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def raw_data(df):
    user_input = input('Would you like to see more raw data? Enter yes or no.\n')
    line = 0

    while True :
        if user_input.lower() != 'no':
            print(df.iloc[line : line + 5])
            line += 5
            user_input = input('Would you like to see more raw data? Enter yes or no.\n')
        else:
            break 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
