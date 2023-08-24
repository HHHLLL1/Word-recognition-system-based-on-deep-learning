import { createNamespace } from '../../utils';
import { t, bem } from '../utils';

var _createNamespace = createNamespace('calendar-header'),
    createComponent = _createNamespace[0];

export default createComponent({
  props: {
    title: String,
    subtitle: String,
    showTitle: Boolean,
    showSubtitle: Boolean
  },
  methods: {
    genTitle: function genTitle() {
      var h = this.$createElement;

      if (this.showTitle) {
        var title = this.slots('title') || this.title || t('title');
        return h("div", {
          "class": bem('header-title')
        }, [title]);
      }
    },
    genSubtitle: function genSubtitle() {
      var h = this.$createElement;

      if (this.showSubtitle) {
        return h("div", {
          "class": bem('header-subtitle')
        }, [this.subtitle]);
      }
    },
    genWeekDays: function genWeekDays() {
      var h = this.$createElement;
      var weekdays = t('weekdays');
      return h("div", {
        "class": bem('weekdays')
      }, [weekdays.map(function (item) {
        return h("span", {
          "class": bem('weekday')
        }, [item]);
      })]);
    }
  },
  render: function render() {
    var h = arguments[0];
    return h("div", {
      "class": bem('header')
    }, [this.genTitle(), this.genSubtitle(), this.genWeekDays()]);
  }
});