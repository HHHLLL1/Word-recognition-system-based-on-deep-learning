import _mergeJSXProps from "@vue/babel-helper-vue-jsx-merge-props";
// Utils
import { createNamespace } from '../../utils';
import { inherit } from '../../utils/functional';
import { BORDER_BOTTOM } from '../../utils/constant'; // Types

var _createNamespace = createNamespace('sku-row'),
    createComponent = _createNamespace[0],
    bem = _createNamespace[1],
    t = _createNamespace[2];

function SkuRow(h, props, slots, ctx) {
  var multipleNode = props.skuRow.is_multiple && h("span", {
    "class": bem('title-multiple')
  }, ["\uFF08", t('multiple'), "\uFF09"]);
  return h("div", _mergeJSXProps([{
    "class": [bem(), BORDER_BOTTOM]
  }, inherit(ctx)]), [h("div", {
    "class": bem('title')
  }, [props.skuRow.k, multipleNode]), slots.default && slots.default()]);
}

SkuRow.props = {
  skuRow: Object
};
export default createComponent(SkuRow);