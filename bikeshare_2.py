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
    # get user input for city (Chicago, New York City, Washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city == 'chicago':
            print('Looks like you want to hear about Chicago! If this is not true, restart the program now!')
            break
        elif city == 'new york city':
            print('Looks like you want to hear about New York City! If this is not true, restart the program now!')
            break
        elif city == 'washington':
            print('Looks like you want to hear about Washington! If this is not true, restart the program now!')
            break
        else:
            print('Please enter a valid input')

    # get user input for month (all, January, February, ... , June)
    while True:
        prompt = input('Would you like to filter the data by month? Please enter "yes" or "no" \n').lower()
        if prompt == 'yes':
            while True:
                month = input('Which month? January, February, March, April, May, or June?\n').lower()
                if month == 'january':
                    break
                elif month == 'february':
                    break
                elif month == 'march':
                    break
                elif month == 'april':
                    break
                elif month == 'may':
                    break
                elif month == 'june':
                    break
                else:
                    print('Pleae enter a valid month \n')
            break
        elif prompt == 'no':
            month = 'all'
            break
        else:
            print('Please enter either yes or no \n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        prompt = input('Would you like to filter the data by day? Please enter "yes" or "no" \n').lower()
        if prompt == 'yes':
            while True:
                day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n').lower()
                if day == 'monday':
                    break
                elif day == 'tuesday':
                    break
                elif day == 'wednesday':
                    break
                elif day == 'thursday':
                    break
                elif day == 'friday':
                    break
                elif day == 'saturday':
                    break
                elif day == 'sunday':
                    break
                else:
                    print('Please enter a valid day of the week \n')
            break
        elif prompt == 'no':
            day = 'all'
            break
        else:
            print('Please enter either yes or no \n')


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[(df['month'] == month)]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[(df['day_of_week'] == day)]

    # ask user if they want to see 5 lines of raw data
    row = 0
    while True:
        raw_data = input('Would you like to see 5 lines of raw data? Please enter "yes" or "no"\n').lower()
        if raw_data == 'yes':
            print(df.iloc[row:row + 5])
            # continue to show a new 5 rows of data when the user says yes
            row += 5
        elif raw_data == 'no':
            break
        else:
            print('Please enter a valid response - "yes" or "no"\n')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Common Month:', months[popular_month - 1])

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Common Day:', days[popular_day])

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start  Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end)

    # display most frequent combination of start station and end station trip
    popular_start_end = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most Frequent Combination of Start & End Station:', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print('Travel Time Total', travel_time_total)

    # display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print('Travel Time Mean', travel_time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types \n', user_types)

    # Display counts of gender
    if not 'Gender' in df.columns:
        print('No gender data to share')
    else:
        gender_counts = df['Gender'].value_counts()
        print('Gender Counts\n', gender_counts)


    # Display earliest, most recent, and most common year of birth
    if not 'Birth Year' in df.columns:
        print('No birth year data to share')
    else:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year', earliest_birth_year)

        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year', recent_birth_year)

        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year', common_birth_year)


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
