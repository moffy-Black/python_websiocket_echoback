# study websocket in python

### server function
simple echo back

### What's socket?
SNSの登場によって,リアルタイムなやり取りができることが求められた.

リアルタイムなやり取りを実現するには,サーバ上の更新が行われたらクライアントの画面を更新する必要がある.

HTTPでは実現することが難しいので,Webにおいて双方向通信を低コストで行うための仕組みとしてwebSocketが生まれた.もちろんプロトコルの一種.

通信の仕組みは2ステップ！

1. ハンドシェイク
- コネクションの確立はHTTP通信によって行われる.その後HTTPのUpgradeヘッダを変更し,プロトコルの変更を行う.ステータスコード101[Switching Protocols]がレスポンスとして返る.

2. 双方向通信
- websocketプロトコルで双方向通信を行う.送信データはフレーム単位.
### what's pythons with?
通信処理やファイル処理、データベース操作等の,開始と終了を必要とする処理で利用する.

detail: https://techacademy.jp/magazine/15823
### reference web
https://docs.python.org/ja/3.6/library/socket.html

https://docs.python.org/ja/3.6/library/socket.html#example

https://kazuhira-r.hatenablog.com/entry/2019/05/04/221923

https://qiita.com/chihiro/items/9d280704c6eff8603389