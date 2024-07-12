import pandas as pd
import streamlit as sl

sl.title('Inflation Calculator')

form = sl.form('calculator_form')
initial_amount = form.number_input('Enter initial amount', value=10000)
inflation_rate = form.number_input('Annual inflation rate (%)', value=7.0)
years = form.number_input('Number of years', value=10)
submit = form.form_submit_button('Calculate')


def calculate_inflation(initial_amount, inflation_rate, years):
    return initial_amount * (1 + inflation_rate / 100) ** years


if submit:
    future_value = calculate_inflation(initial_amount, inflation_rate, years)
    sl.write("Future value: ", future_value)

    year_range = range(0, years + 1)
    future_values = [calculate_inflation(
        initial_amount, inflation_rate, year) for year in year_range]

    data = pd.DataFrame({
        'Year': year_range,
        'Future Value': future_values
    })

    sl.line_chart(data.set_index('Year'))
