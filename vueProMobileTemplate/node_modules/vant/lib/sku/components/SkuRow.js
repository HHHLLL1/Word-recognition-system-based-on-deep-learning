"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");

exports.__esModule = true;
exports.default = void 0;

var _babelHelperVueJsxMergeProps = _interopRequireDefault(require("@vue/babel-helper-vue-jsx-merge-props"));

var _utils = require("../../utils");

var _functional = require("../../utils/functional");

var _constant = require("../../utils/constant");

// Utils
var _createNamespace = (0, _utils.createNamespace)('sku-row'),
    createComponent = _createNamespace[0],
    bem = _createNamespace[1],
    t = _createNamespace[2];

function SkuRow(h, props, slots, ctx) {
  var multipleNode = props.skuRow.is_multiple && h("span", {
    "class": bem('title-multiple')
  }, ["\uFF08", t('multiple'), "\uFF09"]);
  return h("div", (0, _babelHelperVueJsxMergeProps.default)([{
    "class": [bem(), _constant.BORDER_BOTTOM]
  }, (0, _functional.inherit)(ctx)]), [h("div", {
    "class": bem('title')
  }, [props.skuRow.k, multipleNode]), slots.default && slots.default()]);
}

SkuRow.props = {
  skuRow: Object
};

var _default = createComponent(SkuRow);

exports.default = _default;