"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _utils = require("../../utils");

var _email = require("../../utils/validate/email");

var _number = require("../../utils/validate/number");

var _cell = _interopRequireDefault(require("../../cell"));

var _field = _interopRequireDefault(require("../../field"));

var _SkuImgUploader = _interopRequireDefault(require("./SkuImgUploader"));

// Utils
// Components
var _createNamespace = (0, _utils.createNamespace)('sku-messages'),
    createComponent = _createNamespace[0],
    bem = _createNamespace[1],
    t = _createNamespace[2];

var _default2 = createComponent({
  props: {
    messageConfig: Object,
    goodsId: [Number, String],
    messages: {
      type: Array,
      default: function _default() {
        return [];
      }
    }
  },
  data: function data() {
    return {
      messageValues: this.resetMessageValues(this.messages)
    };
  },
  watch: {
    messages: function messages(val) {
      this.messageValues = this.resetMessageValues(val);
    }
  },
  methods: {
    resetMessageValues: function resetMessageValues(messages) {
      var messageConfig = this.messageConfig;
      var _messageConfig$initia = messageConfig.initialMessages,
          initialMessages = _messageConfig$initia === void 0 ? {} : _messageConfig$initia;
      return (messages || []).map(function (message) {
        return {
          value: initialMessages[message.name] || ''
        };
      });
    },
    getType: function getType(message) {
      if (+message.multiple === 1) {
        return 'textarea';
      }

      if (message.type === 'id_no') {
        return 'text';
      }

      return message.datetime > 0 ? 'datetime-local' : message.type;
    },
    getMessages: function getMessages() {
      var _this = this;

      var messages = {};
      this.messageValues.forEach(function (item, index) {
        var value = item.value;

        if (_this.messages[index].datetime > 0) {
          value = value.replace(/T/g, ' ');
        }

        messages["message_" + index] = value;
      });
      return messages;
    },
    getCartMessages: function getCartMessages() {
      var _this2 = this;

      var messages = {};
      this.messageValues.forEach(function (item, index) {
        var value = item.value;
        var message = _this2.messages[index];

        if (message.datetime > 0) {
          value = value.replace(/T/g, ' ');
        }

        messages[message.name] = value;
      });
      return messages;
    },
    getPlaceholder: function getPlaceholder(message) {
      var type = +message.multiple === 1 ? 'textarea' : message.type;
      var map = this.messageConfig.placeholderMap || {};
      return message.placeholder || map[type] || t("placeholder." + type);
    },
    validateMessages: function validateMessages() {
      var values = this.messageValues;

      for (var i = 0; i < values.length; i++) {
        var value = values[i].value;
        var message = this.messages[i];

        if (value === '') {
          // 必填字段的校验
          if (String(message.required) === '1') {
            var textType = t(message.type === 'image' ? 'upload' : 'fill');
            return textType + message.name;
          }
        } else {
          if (message.type === 'tel' && !(0, _number.isNumeric)(value)) {
            return t('invalid.tel');
          }

          if (message.type === 'mobile' && !/^\d{6,20}$/.test(value)) {
            return t('invalid.mobile');
          }

          if (message.type === 'email' && !(0, _email.isEmail)(value)) {
            return t('invalid.email');
          }

          if (message.type === 'id_no' && (value.length < 15 || value.length > 18)) {
            return t('invalid.id_no');
          }
        }
      }
    },
    genMessage: function genMessage(message, index) {
      var _this3 = this;

      var h = this.$createElement;

      if (message.type === 'image') {
        return h(_cell.default, {
          "key": this.goodsId + "-" + index,
          "attrs": {
            "title": message.name,
            "label": t('imageLabel'),
            "required": String(message.required) === '1',
            "valueClass": bem('image-cell-value')
          },
          "class": bem('image-cell')
        }, [h(_SkuImgUploader.default, {
          "attrs": {
            "maxSize": this.messageConfig.uploadMaxSize,
            "uploadImg": this.messageConfig.uploadImg
          },
          "model": {
            value: _this3.messageValues[index].value,
            callback: function callback($$v) {
              _this3.$set(_this3.messageValues[index], "value", $$v);
            }
          }
        })]);
      }

      return h(_field.default, {
        "attrs": {
          "maxlength": "200",
          "label": message.name,
          "required": String(message.required) === '1',
          "placeholder": this.getPlaceholder(message),
          "type": this.getType(message)
        },
        "key": this.goodsId + "-" + index,
        "model": {
          value: _this3.messageValues[index].value,
          callback: function callback($$v) {
            _this3.$set(_this3.messageValues[index], "value", $$v);
          }
        }
      });
    }
  },
  render: function render() {
    var h = arguments[0];
    return h("div", {
      "class": bem()
    }, [this.messages.map(this.genMessage)]);
  }
});

exports.default = _default2;