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
    print('Hi! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    x=True
    while x:
      city = input("\nChoose a city : \nchicago\nnew york city \nwashington\n").lower()
      if city not in ('chicago', 'new york city', 'washington'):
        print("Choose a right city")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while x:
      month = input("\nChoose a month:  \nall \njanuary \nfebruary \nmarch \napril \nmay \njune\n").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Choose a right month")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while x:
      day = input("\nChoose a day \nall  \nmonday \ntuesday \nwednesday \nthursday \nfriday \nsaturday \nsunday\n ").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'fiday', 'saturday', 'all'):
        print("Choose a right day")
        continue
      else:
        break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is :', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is :', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station is:', Start_station)

    # TO DO: display most commonly used end station
    End_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station is:', End_station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nmost frequent combination of start station is:',Start_station,'\nmost frequent combination of end station is:',  End_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = sum(df['Trip Duration'])
    print('Total travel time is:', Total_travel_time)

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time is:', Mean_Travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_types = df['User Type'].value_counts()
    print('User types:\n', User_types)

    # TO DO: Display counts of gender
    try:
      Gender_types = df['Gender'].value_counts()
      print('\nGender types:\n', Gender_types)
    except KeyError:
      print("\nthere is no gender")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nthere is no earliest year")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\n there is no most recent year")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\n there is no most common year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual    trip data? Enter yes or no?")
    start_loc = 0
    while (view_data.lower() != 'no' ):
      print(df.iloc[start_loc:start_loc+4])
      start_loc += 5
      view_data = input("Do you wish to continue?: ").lower()
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to start again? Enter yes or no.\n')
        if restart.lower() == 'no':
            break
   print ("Have a nice day!")


if __name__ == "__main__":
	main()
