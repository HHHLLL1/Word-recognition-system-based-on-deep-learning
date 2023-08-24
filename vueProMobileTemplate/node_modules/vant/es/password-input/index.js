import _mergeJSXProps from "@vue/babel-helper-vue-jsx-merge-props";
// Utils
import { createNamespace, addUnit } from '../utils';
import { emit, inherit } from '../utils/functional';
import { BORDER_LEFT, BORDER_SURROUND } from '../utils/constant'; // Types

var _createNamespace = createNamespace('password-input'),
    createComponent = _createNamespace[0],
    bem = _createNamespace[1];

function PasswordInput(h, props, slots, ctx) {
  var _ref;

  var mask = props.mask,
      value = props.value,
      length = props.length,
      gutter = props.gutter,
      focused = props.focused,
      errorInfo = props.errorInfo;
  var info = errorInfo || props.info;
  var Points = [];

  for (var i = 0; i < length; i++) {
    var _class;

    var _char = value[i];
    var showBorder = i !== 0 && !gutter;
    var showCursor = focused && i === value.length;
    var style = void 0;

    if (i !== 0 && gutter) {
      style = {
        marginLeft: addUnit(gutter)
      };
    }

    Points.push(h("li", {
      "class": (_class = {}, _class[BORDER_LEFT] = showBorder, _class),
      "style": style
    }, [mask ? h("i", {
      "style": {
        visibility: _char ? 'visible' : 'hidden'
      }
    }) : _char, showCursor && h("div", {
      "class": bem('cursor')
    })]));
  }

  return h("div", {
    "class": bem()
  }, [h("ul", _mergeJSXProps([{
    "class": [bem('security'), (_ref = {}, _ref[BORDER_SURROUND] = !gutter, _ref)],
    "on": {
      "touchstart": function touchstart(event) {
        event.stopPropagation();
        emit(ctx, 'focus', event);
      }
    }
  }, inherit(ctx, true)]), [Points]), info && h("div", {
    "class": bem(errorInfo ? 'error-info' : 'info')
  }, [info])]);
}

PasswordInput.props = {
  info: String,
  gutter: [Number, String],
  focused: Boolean,
  errorInfo: String,
  mask: {
    type: Boolean,
    default: true
  },
  value: {
    type: String,
    default: ''
  },
  length: {
    type: [Number, String],
    default: 6
  }
};
export default createComponent(PasswordInput);