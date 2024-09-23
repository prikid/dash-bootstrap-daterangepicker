from dash import html, dcc

import dash_bootstrap_daterangepicker
import dash
from dash.dependencies import Input, Output, State
from datetime import date, timedelta
from dateutil.parser import parse

app = dash.Dash(
    __name__,
    external_stylesheets=['node_modules\\bootstrap\\dist\\css\\bootstrap.min.css']
)

server = app.server

t = date.today()
d = lambda v: v.strftime("%m/%d/%Y")
st = d(t)

first_day_of_this_month = t.replace(day=1)
last_day_of_prev_month = first_day_of_this_month - timedelta(days=1)
start_day_of_prev_month = first_day_of_this_month - timedelta(days=last_day_of_prev_month.day)

ranges = {
    'Last 3 days': [d(t - timedelta(days=2)), st],
    'Last 7 days': [d(t - timedelta(days=6)), st],
    'Last 14 days': [d(t - timedelta(days=13)), st],
    'Last 30 days': [d(t - timedelta(days=29)), st],
    'This month': [d(first_day_of_this_month), st],
    'Last month': [d(start_day_of_prev_month), d(last_day_of_prev_month)],
}

app.layout = html.Div([
    dash_bootstrap_daterangepicker.DashBootstrapDaterangepicker(
        id='date_picker',
        initialSettings={
            'startDate': '12/08/2001',
            'endDate': '12/09/2003',
            'autoApply': True,
            'showDropdowns': True,
            'linkedCalendars': True,
            'ranges': ranges,
            'alwaysShowCalendars': True,
            'showCustomRangeLabel': False
        },
        className='DateRangePickerInput DateRangePickerInput__withBorder',
        innerClassName='DateInput_input'
    ),
    html.Div(id='output'),
    html.Br(),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        start_date=date(2016, 8, 25),
        end_date=date(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-range')
])


@app.callback(
    Output('date_picker', 'start_date'),
    Output('date_picker', 'end_date'),
    # Output('date_picker', 'initialSettings'),

    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),

    State('date_picker', 'initialSettings'),
    prevent_initall_call=True
)
def on_dates_change(start_date, end_date, settings):
    # settings['startDate'] = parse(start_date).strftime("%m/%d/%Y")
    # settings['endDate'] = parse(end_date).strftime("%m/%d/%Y")
    # return settings
    return parse(start_date).strftime("%m/%d/%Y"), parse(end_date).strftime("%m/%d/%Y")


@app.callback(
    Output('output', 'children'),
    Input('date_picker', 'start_date'),
    Input('date_picker', 'end_date'),
    # prevent_initall_call=True
)
def display_output(start_date, end_date):
    print(start_date, end_date)

    string_prefix = 'You have selected: '

    if start_date is not None:
        start_date_object = parse(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix += 'Start Date: ' + start_date_string + ' | '

    if end_date is not None:
        end_date_object = parse(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix += 'End Date: ' + end_date_string

    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix


@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_output(start_date, end_date):
    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix


if __name__ == '__main__':
    app.run_server(debug=True)
