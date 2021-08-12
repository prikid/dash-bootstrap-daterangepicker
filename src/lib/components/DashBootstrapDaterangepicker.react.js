import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {DateRangePicker} from 'react-bootstrap-daterangepicker';
// you will need the css that comes with bootstrap@3. if you are using
// a tool like webpack, you can do the following:
// import './bootstrap.min.css';
// you will also need the css that comes with bootstrap-daterangepicker
import './daterangepicker.css';
import moment from 'moment'


/**
 * DashBootstrapDaterangepicker component based on react-bootstrap-daterangepicker
 */
export default class DashBootstrapDaterangepicker extends Component {
    constructor(props) {
        super(props);

        // this.props.start_date = moment(this.props.initialSettings.startDate)
        // this.props.end_date = moment(this.props.initialSettings.endDate)

        this.props.setProps(
            {
                start_date: moment(this.props.initialSettings.startDate).format("M/D/YYYY"),
                end_date: moment(this.props.initialSettings.endDate).format("M/D/YYYY")
            }
        )
    }

    render() {
        const {id, initialSettings, setProps, className, innerClassName} = this.props;

        return (
            <div id={id} className={className}>
                <DateRangePicker
                    initialSettings={initialSettings}
                    onCallback={(start, end) => {
                        console.log(start)
                        console.log(this)
                        // thrown when the start/end dates change
                        setProps({start_date: start.format("M/D/YYYY"), end_date: end.format("M/D/YYYY")})
                    }}

                    // onShow={} callback(event, picker) //thrown when the widget is shown
                    // onHide: callback(event, picker) thrown when the widget is hidden
                    // onShowCalendar: callback(event, picker) thrown when the calendar is shown
                    // onHideCalendar: callback(event, picker) thrown when the calendar is hidden
                    // onApply: callback(event, picker) thrown when the apply button is clicked
                    // onCancel: callback(event, picker) thrown when the cancel button is clicked
                    // onEvent: callback(event, picker) thrown when any of the 6 events above are triggered
                >
                    <input type="text" className={innerClassName}/>
                </DateRangePicker>
            </div>
        );
    }
}

DashBootstrapDaterangepicker.defaultProps = {};

DashBootstrapDaterangepicker.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,


    /**
     * You can pass all the settings from the original plugin (http://www.daterangepicker.com/)
     * to the initialSettings prop:
     *
     * <input>, alwaysShowCalendars, applyButtonClasses, applyClass, autoApply, autoUpdateInput, buttonClasses,
     * cancelButtonClasses, cancelClass, dateLimit, drops, endDate, isCustomDate, isInvalidDate, linkedCalendars,
     * locale, maxDate, maxSpan, maxYear, minDate, minYear, moment, opens, parentEl, ranges, showCustomRangeLabel,
     * showDropdowns, showISOWeekNumbers, showWeekNumbers, singleDatePicker, startDate, template, timePicker,
     * timePicker24Hour, timePickerIncrement, timePickerSeconds
     */
    initialSettings: PropTypes.object,

    /**
     * start_date
     */
    start_date: PropTypes.string,

    /**
     * end_date
     */
    end_date: PropTypes.string,

    /**
     * Class of the input component.
     */
    className: PropTypes.string,


    /**
     * Class of the input.
     */
    innerClassName: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
