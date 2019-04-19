import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = {'All': 0, 'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6}
weekdays = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

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
        try:
            city = str(input('Please choose a city: Chicago, New York City, Washington: ')).lower()
        except ValueError:
            continue
        if city in CITY_DATA:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('you can choose a month: All, January, February, March, April, May, June:')).title()
        except ValueError:
            continue
        if month in months:
            break
        else:
            month = 'All'
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Please choose a day of week: All, Monday, Tuesday, ... Sunday:')).title()
        except ValueError:
            continue
        if day.title() in weekdays:
            break
        else:
            day = 'All'
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


    df['start_time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['start_time'].dt.month
    df['day_of_week'] = df['start_time'].dt.weekday_name


    if month != 'All':
        df = df[(df.month == months[month])]

    if day != 'All':
        df = df[(df.day_of_week == day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    most_month_name = most_month;


    print('The most common month is {}.'.format(most_month_name))



    most_day = df['day_of_week'].mode()[0]
    print('The most common day is {}.'.format(most_day))


    # TO DO: display the most common start hour
    df['hour'] = df['start_time'].dt.hour


    most_hour = df['hour'].mode()[0]
    print('The most common hour is {}.'.format(most_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_most = df['Start Station'].mode()[0]
    print('The most common start station is {}.'.format(start_station_most))

    # TO DO: display most commonly used end station
    end_station_most = df['End Station'].mode()[0]
    print('The most common end station is {}.'.format(end_station_most))


    # TO DO: display most frequent combination of start station and end station trip
    df['StartToEnd'] = df['Start Station'].map(str) + ' > ' + df['End Station'].map(str)
    most_combination = df['StartToEnd'].mode()[0]
    print('The most frequent combination of stations is {}.'.format(most_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} sec.'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {} sec.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types')
    print(df['User Type'].value_counts())
    print('\n')

    # TO DO: Display counts of gender
    print('Counts of  gender')
    print(df['Gender'].value_counts())
    print('\n')


    print('Earliest Year of Birth: ', int(df['Birth Year'].min()))
    print('Most recent Year of Birth: ', int(df['Birth Year'].max()))
    print('Most common Year of Birth: ', int(df['Birth Year'].mode()[0]))

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
