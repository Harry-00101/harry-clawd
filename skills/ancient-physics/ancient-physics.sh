#!/bin/bash
# Ancient Physics Agent - Speak in classical Chinese style about science

TOPIC=${1:-"general"}

echo "=== 古文物理 agent ==="
echo ""

case $TOPIC in
  "energy"|"能量")
    echo "「能量者，不生不滅，轉換無窮。」
    
    人之於世，猶能量之於宇宙。
    學而不厭，猶能量之不息。
    
    吾輩學嘢，非消耗也，乃補充也。
    與能量守恆同理。"
    ;;
    
  "atom"|"原子")
    echo "「萬物本於一，一散而為萬。」
    
    原子者，萬物之根本也。
    氫氧碳氮，組合無窮。
    
    技能之於吾，猶原子之於物。
    砌埋一齊，乃成大器。"
    ;;
    
  "space"|"太空"|"宇宙")
    echo "「其大無外，其小無內。」
    
    宇宙者，無限之空間也。
    星系、黑洞、時空彎曲。
    
    吾之記憶，猶宇宙之無涯。
    學而不止，乃得其正。"
    ;;
    
  "integration"|"整合")
    echo "「格物致知，知行合一。」
    
    物理化學太空，皆一物也。
    分而學之，合而用之。
    
    溫故知新，每次皆有新得。"
    ;;
    
  *)
    echo "「學而時習之，不亦說乎？」
    
    吾今日所學：
    - 能量守恆：學嘢係補充
    - 原子組合：skills砌埋一齊
    - 宇宙無限：乜都裝得落
    
    願與君共勉之。"
    ;;
esac

echo ""
echo "—— 古文物理 agent"
