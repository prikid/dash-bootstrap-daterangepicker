# AUTO GENERATED FILE - DO NOT EDIT

export dashbootstrapdaterangepicker

"""
    dashbootstrapdaterangepicker(;kwargs...)

A DashBootstrapDaterangepicker component.
DashBootstrapDaterangepicker component based on react-bootstrap-daterangepicker
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Class of the input component.
- `end_date` (String; optional): end_date
- `initialSettings` (Dict; optional): You can pass all the settings from the original plugin (http://www.daterangepicker.com/)
to the initialSettings prop:

<input>, alwaysShowCalendars, applyButtonClasses, applyClass, autoApply, autoUpdateInput, buttonClasses,
cancelButtonClasses, cancelClass, dateLimit, drops, endDate, isCustomDate, isInvalidDate, linkedCalendars,
locale, maxDate, maxSpan, maxYear, minDate, minYear, moment, opens, parentEl, ranges, showCustomRangeLabel,
showDropdowns, showISOWeekNumbers, showWeekNumbers, singleDatePicker, startDate, template, timePicker,
timePicker24Hour, timePickerIncrement, timePickerSeconds
- `innerClassName` (String; optional): Class of the input.
- `start_date` (String; optional): start_date
"""
function dashbootstrapdaterangepicker(; kwargs...)
        available_props = Symbol[:id, :className, :end_date, :initialSettings, :innerClassName, :start_date]
        wild_props = Symbol[]
        return Component("dashbootstrapdaterangepicker", "DashBootstrapDaterangepicker", "dash_bootstrap_daterangepicker", available_props, wild_props; kwargs...)
end

