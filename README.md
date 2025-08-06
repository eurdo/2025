# python實現雙向循環鏈表基本結構及其基本方法

11224215 顏玉棠

雙向循環鏈表是在雙向鏈表的基礎上發展的，雙向鏈表的最後一個節點指向起始節點，起始節點的上一個節點指向最後一個節點，就得到雙向循環鏈表。

雙向循環鏈表比雙向鏈表具有更多的優勢，節點的增加和刪除有很多優化的地方，從起點開始不必循環完整個鏈表就可以增加或刪除節點。

首先定義雙向鏈表的基本類和節點的基本類：<img width="848" height="537" alt="螢幕擷取畫面 2025-08-07 001249" src="https://github.com/user-attachments/assets/35751c05-50e6-48c6-bbe1-d295e94de108" />
<img width="432" height="336" alt="C1" src="https://github.com/user-attachments/assets/5ff4368b-943c-4ff5-90a4-1f615e0f155f" />

下面我們添加基本屬性方法的邏輯，注意判斷是否為最後一個節點的方式是：最後一個節點的下一個節點是否指向頭部指向的節點。
<img width="398" height="672" alt="C2" src="https://github.com/user-attachments/assets/a585cf91-2570-4810-9b43-0a0bc5d6d167" />

<img width="376" height="343" alt="C3" src="https://github.com/user-attachments/assets/fe9040f7-8073-4e4f-a43b-f5ea0a0aa67a" />


鏈表類的操作有幾個核心的地方，第一個是判斷是否為最後一個節點，通過鏈表的相關特性，如單向鏈表最後一個節點的 next 屬性為 None、單向循環鏈表的最後一個節點的 next 屬性等於頭部節點；第二個是使用游標來替代節點指向，這在操作節點時，有時需要兩個游標，但對於雙向節點而言只需要一個游標，因為透過當前節點的屬性可以找到上下節點。
繼續給對象添加方法：頭部插入節點、尾部添加節點、任意位置插入節點。

<img width="405" height="822" alt="C4" src="https://github.com/user-attachments/assets/86e68801-c015-4e40-9a48-50a0952cdfcc" />/n

<img width="397" height="567" alt="C5" src="https://github.com/user-attachments/assets/c6780776-9ecd-4145-a613-648a6ef6e66d" />


接著實現判斷節點是否存在以及刪除指定節點的方法：

<img width="431" height="432" alt="C6" src="https://github.com/user-attachments/assets/20821649-c8f3-40dc-b1bd-1acb26199372" />/n
<img width="563" height="552" alt="C7" src="https://github.com/user-attachments/assets/0018fb8d-e1ff-4656-98f4-3d8510b66b4b" />

只以基本的思路實現基本的方法，對於雙向循環鏈表而言還有很多可以優化的地方，正向遍歷和逆向遍歷獲得結果的時間是不一樣的。
<img width="750" height="203" alt="P1" src="https://github.com/user-attachments/assets/93a6c54c-c70e-48b4-8098-1ecb93483204" />

