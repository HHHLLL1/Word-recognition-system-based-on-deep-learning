import _extends from "@babel/runtime/helpers/esm/extends";
import { createNamespace, get } from '../utils';
import { isDate } from '../utils/validate/date';
import { padZero } from '../utils/format/string';
import { getTrueValue, getMonthEndDay } from './utils';
import { sharedProps, TimePickerMixin } from './shared';
var currentYear = new Date().getFullYear();

var _createNamespace = createNamespace('date-picker'),
    createComponent = _createNamespace[0];

export default createComponent({
  mixins: [TimePickerMixin],
  props: _extends(_extends({}, sharedProps), {}, {
    type: {
      type: String,
      default: 'datetime'
    },
    minDate: {
      type: Date,
      default: function _default() {
        return new Date(currentYear - 10, 0, 1);
      },
      validator: isDate
    },
    maxDate: {
      type: Date,
      default: function _default() {
        return new Date(currentYear + 10, 11, 31);
      },
      validator: isDate
    }
  }),
  watch: {
    filter: 'updateInnerValue',
    minDate: 'updateInnerValue',
    maxDate: 'updateInnerValue',
    value: function value(val) {
      val = this.formatValue(val);

      if (val.valueOf() !== this.innerValue.valueOf()) {
        this.innerValue = val;
      }
    }
  },
  computed: {
    ranges: function ranges() {
      var _this$getBoundary = this.getBoundary('max', this.innerValue),
          maxYear = _this$getBoundary.maxYear,
          maxDate = _this$getBoundary.maxDate,
          maxMonth = _this$getBoundary.maxMonth,
          maxHour = _this$getBoundary.maxHour,
          maxMinute = _this$getBoundary.maxMinute;

      var _this$getBoundary2 = this.getBoundary('min', this.innerValue),
          minYear = _this$getBoundary2.minYear,
          minDate = _this$getBoundary2.minDate,
          minMonth = _this$getBoundary2.minMonth,
          minHour = _this$getBoundary2.minHour,
          minMinute = _this$getBoundary2.minMinute;

      var result = [{
        type: 'year',
        range: [minYear, maxYear]
      }, {
        type: 'month',
        range: [minMonth, maxMonth]
      }, {
        type: 'day',
        range: [minDate, maxDate]
      }, {
        type: 'hour',
        range: [minHour, maxHour]
      }, {
        type: 'minute',
        range: [minMinute, maxMinute]
      }];

      if (this.type === 'date') {
        result = result.slice(0, 3);
      }

      if (this.type === 'year-month') {
        result = result.slice(0, 2);
      }

      if (this.type === 'month-day') {
        result = result.slice(1, 3);
      }

      return result;
    }
  },
  methods: {
    formatValue: function formatValue(value) {
      if (!isDate(value)) {
        value = this.minDate;
      }

      value = Math.max(value, this.minDate.getTime());
      value = Math.min(value, this.maxDate.getTime());
      return new Date(value);
    },
    getBoundary: function getBoundary(type, value) {
      var _ref;

      var boundary = this[type + "Date"];
      var year = boundary.getFullYear();
      var month = 1;
      var date = 1;
      var hour = 0;
      var minute = 0;

      if (type === 'max') {
        month = 12;
        date = getMonthEndDay(value.getFullYear(), value.getMonth() + 1);
        hour = 23;
        minute = 59;
      }

      if (value.getFullYear() === year) {
        month = boundary.getMonth() + 1;

        if (value.getMonth() + 1 === month) {
          date = boundary.getDate();

          if (value.getDate() === date) {
            hour = boundary.getHours();

            if (value.getHours() === hour) {
              minute = boundary.getMinutes();
            }
          }
        }
      }

      return _ref = {}, _ref[type + "Year"] = year, _ref[type + "Month"] = month, _ref[type + "Date"] = date, _ref[type + "Hour"] = hour, _ref[type + "Minute"] = minute, _ref;
    },
    updateInnerValue: function updateInnerValue() {
      var _this = this;

      var type = this.type;
      var indexes = this.getPicker().getIndexes();

      var getValue = function getValue(index) {
        var values = _this.originColumns[index].values;
        return getTrueValue(values[indexes[index]]);
      };

      var year;
      var month;
      var day;

      if (type === 'month-day') {
        year = this.innerValue.getFullYear();
        month = getValue(0);
        day = getValue(1);
      } else {
        year = getValue(0);
        month = getValue(1);
        day = type === 'year-month' ? 1 : getValue(2);
      }

      var maxDay = getMonthEndDay(year, month);
      day = day > maxDay ? maxDay : day;
      var hour = 0;
      var minute = 0;

      if (type === 'datetime') {
        hour = getValue(3);
        minute = getValue(4);
      }

      var value = new Date(year, month - 1, day, hour, minute);
      this.innerValue = this.formatValue(value);
    },
    onChange: function onChange(picker) {
      var _this2 = this;

      this.updateInnerValue();
      this.$nextTick(function () {
        _this2.$nextTick(function () {
          _this2.$emit('change', picker);
        });
      });
    },
    updateColumnValue: function updateColumnValue() {
      var _this3 = this;

      var value = this.innerValue;
      var formatter = this.formatter;
      var values = [formatter('year', "" + value.getFullYear()), formatter('month', padZero(value.getMonth() + 1)), formatter('day', padZero(value.getDate()))];

      if (this.type === 'datetime') {
        values.push(formatter('hour', padZero(value.getHours())), formatter('minute', padZero(value.getMinutes())));
      }

      if (this.type === 'year-month') {
        values = values.slice(0, 2);
      }

      if (this.type === 'month-day') {
        values = values.slice(1, 3);
      }

      this.$nextTick(function () {
        _this3.getPicker().setValues(values);
      });
    }
  }
});