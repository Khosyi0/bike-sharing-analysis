import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    data = pd.read_csv("dashboard/main_data.csv")
    return data

def show_total_count_chart(data):
    total_count = data.groupby('yr')['cnt'].sum().reset_index()

    st.subheader('Bike Sharing Total Count by Year')
    fig, ax = plt.subplots()
    sns.barplot(x='yr', y='cnt', data=total_count, ax=ax)
    st.pyplot(fig)

    st.write("First, let's look at a comparison graph between the total number of bicycles borrowed between 2011 and 2012. It can be seen that in 2011 the number of bicycles borrowed was less than in 2012.")

def shot_total_count_by_season(data):
    season_year_groups = data.groupby(['season', 'yr']).agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    })

    st.subheader('Bike Sharing Total Count by Year Season')

    st.subheader('Year 2011')
    st.write(season_year_groups.loc[(slice(None), 2011), :])

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=season_year_groups.loc[(slice(None), 2011), :], x='season', y='casual', marker='o', label='Casual', ax=ax)
    sns.lineplot(data=season_year_groups.loc[(slice(None), 2011), :], x='season', y='registered', marker='o', label='Registered', ax=ax)
    sns.lineplot(data=season_year_groups.loc[(slice(None), 2011), :], x='season', y='cnt', marker='o', label='Count', ax=ax)
    plt.title('Year 2011')
    plt.xlabel('Season')
    plt.ylabel('Total')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader('Year 2012')
    st.write(season_year_groups.loc[(slice(None), 2012), :])

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=season_year_groups.loc[(slice(None), 2012), :], x='season', y='casual', marker='o', label='Casual', ax=ax)
    sns.lineplot(data=season_year_groups.loc[(slice(None), 2012), :], x='season', y='registered', marker='o', label='Registered', ax=ax)
    sns.lineplot(data=season_year_groups.loc[(slice(None), 2012), :], x='season', y='cnt', marker='o', label='Count', ax=ax)
    plt.title('Year 2012')
    plt.xlabel('Season')
    plt.ylabel('Total')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.write("Furthermore, in the second and third graph, it can be seen that the Fall season is the peak of the number of bicycle borrowings that occur. Then the least amount of bicycles being borrowed is in the spring.")

def show_weather_count_chart(data):
    weather_count = data.groupby(['weathersit', 'yr']).agg({'cnt': 'sum'}).reset_index()

    st.subheader('Count by Weather Situation and Year')

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', hue='yr', data=weather_count, palette='coolwarm', ax=ax)
    plt.xlabel('Weather Situation')
    plt.ylabel('Count')
    plt.title('Count by Weather Situation and Year')
    plt.legend(title='Year', loc='upper right')
    st.pyplot(fig)

    st.write("There is a correlation between weather conditions, temperature and humidity and the number of bicycle rentals that occur. In the first graph, it is clear that in both 2011 and 2012 there were a lot of bicycles borrowed when the weather was sunny, very few bicycles were borrowed when the weather was snowy and there were no bicycles borrowed when the weather was heavy rain.")

def show_humidity_count_chart(data):
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
    labels = ['0 ≤ x < 20', '20 ≤ x < 40', '40 ≤ x < 60', '60 ≤ x < 80', '80 ≤ x ≤ 100']
    data['hum_interval'] = pd.cut(data['hum'], bins=bins, labels=labels, include_lowest=True)

    hum_count = data.groupby(['hum_interval', 'yr']).agg({'cnt': 'sum'}).reset_index()

    st.subheader('Count by Humidity Interval and Year')
    fig, ax = plt.subplots()
    sns.barplot(x='hum_interval', y='cnt', hue='yr', data=hum_count, ax=ax)
    st.pyplot(fig)

def show_temperature_count_chart(data):
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
    labels = ['0≤x<8.2', '8.2≤x<16.4', '16.4≤x<24.6', '24.6≤x<32.8', '32.8≤x≤41']
    data['temp_interval'] = pd.cut(data['temp'], bins=bins, labels=labels, include_lowest=True)

    hum_count = data.groupby(['temp_interval', 'yr']).agg({'cnt': 'sum'}).reset_index()

    st.subheader('Count by Temperature Interval and Year')
    fig, ax = plt.subplots()
    sns.barplot(x='temp_interval', y='cnt', hue='yr', data=hum_count, ax=ax)
    st.pyplot(fig)

    st.write("It can be seen from the fifth and sixth graphs that the graph will appear to increase as temperature and humidity increase. The temperatre is in celcius.")

def main():
    st.title('Bike Sharing Data Dashboard')

    data = load_data()

    selected_chart = st.sidebar.radio("Select Chart", ["All Chart", "Total Count by Year", "Total Count by Season", "Weather Count", "Humidity Count", "Temperature Count"])

    if selected_chart == "All Chart":
        show_total_count_chart(data)
        shot_total_count_by_season(data)
        show_weather_count_chart(data)
        show_humidity_count_chart(data)
        show_temperature_count_chart(data)
    elif selected_chart == "Total Count by Year":
        show_total_count_chart(data)
    elif selected_chart == "Total Count by Season":
        shot_total_count_by_season(data)
    elif selected_chart == "Weather Count":
        show_weather_count_chart(data)
    elif selected_chart == "Humidity Count":
        show_humidity_count_chart(data)
    elif selected_chart == "Temperature Count":
        show_temperature_count_chart(data)

if __name__ == '__main__':
    main()
